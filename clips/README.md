# Fábrica de clips AECODE · «Historias de la IA»

Clips verticales (9:16) con la marca AECODE, generados con **MoneyPrinterTurbo** (`../MoneyPrinterTurbo`)
como motor de voz, subtítulos y montaje, más una capa de diseño propia.

| Ep | Clip | Duración |
|---|---|---|
| 01 | [El verano que inventó la IA](output/ep01-el-verano-que-invento-la-ia.mp4) | ~49 s |
| 02 | [La jugada 37](output/ep02-la-jugada-37.mp4) | ~45 s |
| 03 | [La canción detrás de ChatGPT](output/ep03-la-cancion-detras-de-chatgpt.mp4) | ~47 s |

Textos para publicar, hashtags y fuentes: [`output/PUBLICAR.md`](output/PUBLICAR.md).

## Cómo funciona

```
episodes.py ──► MPT voice.tts (piper:, offline) ──► voz + tiempos por cláusula
                         │
                         ├─► MPT create_subtitle ─────────────► subtitle.srt
                         ├─► engine/stage.html (Playwright) ──► escenas sincronizadas (visual.mp4)
                         └─► music.py ────────────────────────► música original + ducking (bed.wav)
                                                   │
                      MPT video.generate_video ◄───┘  subtítulos Manrope + mezcla
                                   │
                         master −14 LUFS ──► output/*.mp4 + portada
```

- **Guion**: `episodes.py`. Cada escena = lo que dice la voz (`say`) + una plantilla visual (`type`).
  Para que un elemento aparezca justo cuando la voz lo dice, se usa `c<n>` (cláusula n de la escena).
- **Voz**: proveedor `piper:` que se añadió a MoneyPrinterTurbo (Piper vía `sherpa-onnx`). Corre en CPU,
  sin API keys ni internet. `LEXICON` en `episodes.py` corrige pronunciaciones solo en el audio.
- **Escenas**: `engine/stage.html` es una línea de tiempo determinista: Python llama `seek(t)` por cada
  fotograma y hace captura. Plantillas disponibles: `hook`, `rewind`, `people`, `stats`, `quote`,
  `statement`, `curves`, `versus`, `goboard`, `dots`, `timer`, `score`, `lesson`, `acronym`, `paper`,
  `morph`, `attention`, `race`, `news`, `cta`.
- **Música**: sintetizada en `music.py` (sin licencias de terceros), con whoosh en cada corte y ducking
  bajo la voz.
- **Montaje**: `generate_video` de MoneyPrinterTurbo quema los subtítulos (Manrope ExtraBold sobre
  píldora violeta `#4A3AC1`) y mezcla voz + música.

## Uso

```bash
bash clips/setup.sh                                  # venv + dependencias + voz Piper (una vez)
.venv-clips/bin/python clips/factory.py              # los 3 episodios (~10 min en 4 núcleos)
.venv-clips/bin/python clips/factory.py --only 2     # un episodio
.venv-clips/bin/python clips/factory.py --preview    # fotogramas de control en clips/.work/
```

Variables: `AECODE_VOICE` (por defecto `piper:es_MX-claude-high`), `AECODE_VOICE_RATE` (1.1),
`AECODE_CHROMIUM` (ruta a Chromium si Playwright no lo encuentra).

## Nuevo episodio

1. Añade un `dict` a `EPISODES` en `episodes.py` reutilizando plantillas.
2. `--preview` para revisar el diseño; ajusta textos y tiempos (`c<n>`).
3. Render completo.

## Con API keys (modo MoneyPrinterTurbo clásico)

Si configuras `MoneyPrinterTurbo/config.toml` con un LLM y Pexels/Pixabay, MPT puede generar guion y
video de stock por sí solo (`cd MoneyPrinterTurbo && sh webui.sh`). Para contenido de marca AECODE
recomendamos este flujo: guion curado + escenas de marca, porque el stock genérico no transmite la
identidad visual.
