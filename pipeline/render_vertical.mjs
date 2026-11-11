#!/usr/bin/env node
// Vertical 9:16 driver for the KazChart engine (engine itself is untouched).
// The engine world is 1920x1080; here the SVG is sliced so the centre 607x1080 fills 1080x1920.
//   node render_vertical.mjs scene.json out.mp4 [--from s] [--to s]
//   node render_vertical.mjs scene.json outdir --stills 1.5,8,20
import { createRequire } from 'node:module';
import { spawn } from 'node:child_process';
import fs from 'node:fs'; import path from 'node:path'; import { pathToFileURL } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), '/opt/npm-tools/node_modules', ...(process.env.NODE_PATH || '').split(':').filter(Boolean)] }));
const ENGINE = process.env.KZ_ENGINE || '/home/claude/kaz_extract/kazchart-skill/engine/index.html';
const args = process.argv.slice(2);
const flag = (n, d) => { const i = args.indexOf('--' + n); return i < 0 ? d : args[i + 1]; };
const [specPath, outPath] = args;
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const W = 1080, H = 1920, fps = 30; spec.width = W; spec.height = H;
const total = spec.shots.at(-1).end;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H } });
await page.goto(pathToFileURL(ENGINE).href);
await page.evaluate(() => document.fonts.ready);
const shoot = async t => {
  await page.evaluate(([s, t]) => { window.KZ.render(s, t); document.querySelector('#stage svg').setAttribute('preserveAspectRatio', 'xMidYMid slice'); }, [spec, t]);
  return page.screenshot({ type: 'jpeg', quality: 92 });
};
const stills = flag('stills');
if (stills) {
  fs.mkdirSync(outPath, { recursive: true });
  for (const t of stills.split(',').map(Number)) fs.writeFileSync(path.join(outPath, `t${t.toFixed(1).padStart(5, '0')}.jpg`), await shoot(t));
} else {
  const from = +flag('from', 0), to = Math.min(+flag('to', total), total), frames = Math.round((to - from) * fps);
  const tmp = outPath.replace(/\.mp4$/, '.part.mp4');
  await new Promise((res, rej) => {
    const p = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
    p.on('close', c => c ? rej(new Error('ffmpeg ' + c)) : res());
    (async () => { for (let f = 0; f < frames; f++) { const b = await shoot(from + f / fps); if (!p.stdin.write(b)) await new Promise(r => p.stdin.once('drain', r)); } p.stdin.end(); })();
  });
  fs.renameSync(tmp, outPath);
}
await browser.close(); console.log('wrote', outPath);
