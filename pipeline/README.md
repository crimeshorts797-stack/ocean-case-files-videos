# Ocean Case Files – production pipeline

Own scripts used to produce the channel's Shorts (1080x1920, 63 s).

- `make_vo.py` – narration with the free local Kokoro voice (kokoro-onnx, voice `am_michael`), fitted to ~61 s.
- `make_music.py` – synthesizes an original music bed and sound effects from an events file.
- `scenelib.py` + `examples/build_scene_*.py` – build the scene JSON for each video.
- `render_vertical.mjs` – renders a scene in 9:16. Needs the KazChart engine, which is NOT in this repository (licensed separately, see its rights notice). Set `KZ_ENGINE` to its `engine/index.html`.
- `finalize.sh` / `render_queue.sh` – join halves, mix voice and music, normalise loudness, trim to 63 s.

Kokoro model files: https://github.com/thewh1teagle/kokoro-onnx/releases (model-files-v1.0).
