#!/usr/bin/env python3
"""Voice-over builder: segments JSON -> wav + timings JSON (free local Kokoro voice).
usage: make_vo.py segments.json out.wav timings.json [--voice am_michael] [--target 61.5]
segments.json: [{"id":"s1","text":"...","pause":0.35}, ...]"""
import sys, json, argparse, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
ap = argparse.ArgumentParser(); ap.add_argument("seg"); ap.add_argument("wav"); ap.add_argument("timings")
ap.add_argument("--voice", default="am_michael"); ap.add_argument("--target", type=float, default=61.5)
ap.add_argument("--lead", type=float, default=0.15); a = ap.parse_args()
segs = json.load(open(a.seg))
k = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
lang = "en-gb" if a.voice.startswith("b") else "en-us"
def trim(x, sr, thr=0.004):
    idx = np.where(np.abs(x) > thr)[0]
    return x if len(idx) == 0 else x[max(0, idx[0]-int(.02*sr)): idx[-1]+int(.06*sr)]
def build(speed):
    out, tim, t, sr = [], [], a.lead, 24000
    out.append(np.zeros(int(a.lead*sr), dtype=np.float32))
    for s in segs:
        x, sr = k.create(s["text"], voice=a.voice, speed=speed*s.get("speed", 1.0), lang=lang)
        x = trim(x.astype(np.float32), sr)
        tim.append({"id": s["id"], "text": s["text"], "start": round(t, 3), "end": round(t+len(x)/sr, 3)})
        out.append(x); t += len(x)/sr
        p = s.get("pause", 0.3); out.append(np.zeros(int(p*sr), dtype=np.float32)); t += p
    return np.concatenate(out), sr, tim
speed = 1.0
for it in range(4):
    y, sr, tim = build(speed); end = tim[-1]["end"]
    print(f"speed {speed:.3f} -> voice ends {end:.2f}s", flush=True)
    if abs(end - a.target) < 0.5: break
    speed = float(np.clip(speed * end / a.target, 0.8, 1.25))
y = y / max(1e-6, np.max(np.abs(y))) * 0.89
sf.write(a.wav, y, sr); json.dump({"speed": speed, "voice": a.voice, "segments": tim}, open(a.timings, "w"), indent=1)
