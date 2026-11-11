#!/usr/bin/env bash
# finalize.sh <dir> <outname.mp4> : join halves, mix voice+music, compress, normalise loudness, trim to 63 s
set -e; cd "$1"
ffmpeg -y -v error -i vo.wav -i music.wav -filter_complex "[0:a]aresample=44100,apad=whole_dur=63,pan=stereo|c0=c0|c1=c0,asplit=2[vo][vok];[1:a]volume=0.42[mu];[mu][vok]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=350[duck];[duck][vo]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=9,aresample=44100,atrim=0:63[a]" -map "[a]" -c:a aac -b:a 192k mix.m4a
printf "file 'part_a.mp4'\nfile 'part_b.mp4'\n" > list.txt
ffmpeg -y -v error -f concat -safe 0 -i list.txt -i mix.m4a -map 0:v -map 1:a -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -c:a copy -movflags +faststart -t 63 final.part.mp4
mv final.part.mp4 "$2"; ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$2"
ffmpeg -i "$2" -af volumedetect -vn -f null - 2>&1 | grep -E "mean_volume|max_volume"
