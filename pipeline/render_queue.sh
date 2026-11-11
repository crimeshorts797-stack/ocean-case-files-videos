#!/usr/bin/env bash
# render_queue.sh v4 v5 ... : renders each video (two halves in parallel) and finalizes it
for v in "$@"; do
  d=/home/claude/out/$v; cd $d || continue
  while [ ! -f timings.json ] || [ ! -f scene.json ] || [ ! -f music.wav ]; do sleep 5; done
  rm -f part_a.mp4 part_b.mp4
  node /home/claude/pipeline/render_vertical.mjs scene.json part_a.mp4 --from 0 --to 31.5 > ra.log 2>&1 &
  node /home/claude/pipeline/render_vertical.mjs scene.json part_b.mp4 --from 31.5 --to 63 > rb.log 2>&1
  wait
  /home/claude/pipeline/finalize.sh $d final_$v.mp4 > fin.log 2>&1 && echo "$v done" || echo "$v FAILED"
done
