# Prompt maestro — "Cómo presento Claude" (video HyperFrames)

Este es el prompt que originó el video. Úsalo tal cual en Claude Code (con HyperFrames instalado)
para regenerarlo, o cambia los bloques marcados `[EDITABLE]` para la próxima edición.

## 1. Setup (una sola vez por carpeta)

```bash
npx hyperframes skills update      # instala las skills core de HyperFrames
npx hyperframes doctor             # verifica Node 22+, FFmpeg y Chrome headless
```

## 2. El prompt

```text
Usando /hyperframes (workflow faceless-explainer, modo autónomo), crea un video de 75 s en
español, 1920x1080, titulado "Lo último de Claude".

QUIÉN PRESENTA: Alejandro Palpan, AECODE. Tono de estratega que enseña: directo, sin hype,
cada dato con fuente oficial visible en pantalla.

AUDIENCIA [EDITABLE]: profesionales AEC (arquitectura, ingeniería, construcción) y la
comunidad AECODE en LATAM. Conocen ChatGPT/Claude como chat; no conocen los agentes.

MENSAJE ÚNICO: "Claude dejó de ser un chat que responde: ahora es un colega que ejecuta
trabajo real, y tu ventaja está en qué le delegas."

ESTRUCTURA (listicle, 9 escenas):
1. Hook: "¿Todavía usas la IA solo para preguntar?" (dirección al espectador)
2. Tesis: de chat a colega → investiga · construye · entrega
3. Opus 5.5 (22-sep): nivel Fable 5.1 en la mayoría de tareas, −40 % costo, +30 % velocidad vs Opus 5
4. 1 millón de tokens (~555 mil palabras): el expediente técnico completo en una conversación
5. Un solo Claude (16-sep): sigue trabajando con la laptop cerrada; Docs y Slides → PowerPoint/PDF
6. Claude en Chrome (26-ago): navega, hace clic y llena formularios con control de seguridad
7. Marketplace (23-sep): 2.000+ conectores y plugins para tus herramientas
8. Qué significa para AEC: expediente → Claude → informe listo (marcado como ejemplo, no anuncio)
9. Cierre: "La pregunta ya no es qué le preguntas a Claude. Es qué trabajo le delegas." + AECODE

HECHOS [EDITABLE — actualizar en cada edición]: usa SOLO los de
capture/extracted/visible-text.txt. Nada de cifras inventadas: si una cifra no tiene fuente,
va como texto sin número.

MARCA: sistema AECODE (brand/DESIGN.md): fondo navy #0E1121, violeta #4A3AC1, lavanda #A6A7FF,
verde #17B14E, tipografía Manrope. Sin logos ni estética de Anthropic: es contenido editorial.

VOZ [EDITABLE]: voz masculina en español. Ideal: la voz real de Alejandro o un clon HeyGen /
ElevenLabs. Fallback local: Kokoro em_alex.

ENTREGA: renders/video.mp4 + contact sheet + lista de escenas con sus ids para iterar una a una.
```

## 3. Cómo iterar sin rehacer todo

- Cambiar un dato: edita la escena en `compositions/frames/NN-*.html` y vuelve a renderizar.
- Cambiar la narración: edita `SCRIPT.md` y regenera el audio con el paso 3.1 del workflow.
- Cambiar la voz por la tuya: graba cada línea de `SCRIPT.md` como `audio/NN.wav`, reemplaza
  los archivos y ejecuta `audio.mjs sync-durations`; el video se reajusta a tus tiempos.
- Versión vertical (Reels/Shorts): pide "misma historia, 1080x1920" y el workflow re-maqueta.

## 4. Por qué este enfoque (lógica de posicionamiento)

1. **No se presenta Claude como producto, sino como cambio de categoría** (de chat a colega):
   eso es lo que el público AEC no ha entendido todavía y es donde AECODE aporta criterio.
2. **Cada claim con fuente y fecha**: protege la autoridad de AECODE frente a contenido con hype.
3. **Termina en una pregunta de decisión** ("qué le delegas"): convierte el video en puerta de
   entrada a formación aplicada, no en una noticia más.
