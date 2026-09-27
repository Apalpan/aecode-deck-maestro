---
format: 1920x1080
duration: 75s
message: "Claude dejó de ser un chat que responde: ahora es un colega que ejecuta trabajo real, y tu ventaja está en qué le delegas."
arc: listicle
audience: "Profesionales AEC y comunidad AECODE en LATAM"
mode: autonomous
music: calm confident minimal tech underscore, soft synth pads, light pulse, no vocals
---

## Video direction

- **Palette system (frame.md):** ground `canvas` + dual radial swell + faint blueprint grid on every frame; type `text` / `text-muted`; brand ink `primary` / `primary-bright`; AI accents and kickers `lavender`; `green` ONLY for completed/delivered states (checks, "listo"); ONE `gradient-primary` stroke per frame (underline, connector, progress bar or CTA pill).
- **Persistent chrome:** brand-bug top-left ("AECODE · LO ÚLTIMO DE CLAUDE") on frames 1–8; index-counter top-right ("01 / 05" … "05 / 05") on frames 3–7; date chip + source rail on every fact frame (3–7). Chrome enters once, quietly, in the first ~0.4s and then holds still.
- **Stage for the listicle run (frames 3–7):** the same composition every time — LEFT text column (~42% width: kicker → headline → date chip, stacked, left-anchored at the upper third) + RIGHT visual stage (~52% width) holding the invented diagram; source rail bottom-left above the caption band. The seam between them is always `push-slide LEFT`, so the five items read as one continuous film.
- **Motion grammar:** long-tail eases (power3.out default, power2.inOut for camera); smooth over bouncy; spring overshoot only on numerals landing. Every frame follows the **VO-paced reveal model**: at t=0 only what the narration is saying enters; each further piece reveals when the VO names it (cue times below are real word timings from `audio_meta.json`); after the last reveal the frame holds a still read (subtle jitter at most). No lazy breathing, no drifting cards.
- **Rhythm / held frames:** frame 2 (tesis) and frame 9 (cierre) end on deliberate held reads (~1.2–2s of stillness); frames 3–7 are the energetic listicle run; frame 8 slows into a calm flow diagram.
- **Negative list:** no Anthropic logos/colors/type (write "Claude" as plain Manrope text); no third-party brand logos (tools are generic line icons); no floating bokeh or purple "AI" blobs; no neon; no emoji; no copied real browser chrome (UI mocks are generic, AECODE-styled); no invented numbers (only figures listed in frame.md → Numerals); nothing important in the bottom 17% caption band. Both motion failure modes are banned: **slideshow** (front-load everything, then freeze) and **screensaver** (elements floating independently forever).

## Frame 1 — Hook

- scene: Una pregunta tipográfica gigante "¿Solo preguntas?" sobre el suelo blueprint; se tacha con el trazo de gradiente y "Eso cambió." aterriza con un chip de fecha.
- voiceover: "¿Todavía usas la inteligencia artificial solo para hacer preguntas? En septiembre, eso cambió."
- duration: 5.94s
- transition_in: cut
- status: outline
- src: compositions/frames/01-hook.html
- type: hook
- persuasion: Rhetorical question + direct address
- beat: Recognition + intrigue
- blueprint: kinetic-type-beats (Adapt)
- focal: la pregunta tipográfica "¿Solo preguntas?" y su remate "Eso cambió."
- roles: ground grid + swell = background · kicker "LA IA EN TU TRABAJO" = supporting · pregunta "¿Solo preguntas?" = foreground subject · trazo de tachado (gradient-stroke) + chip "SEP · 2026" = supporting · brand-bug = chrome
- sfx: click-soft

narrativeRole: Abre la brecha: el espectador se reconoce usando la IA como buscador y siente que se quedó atrás.
keyMessage: Usar la IA solo para preguntar ya es la forma vieja.

Adapt: keep the statement-builds-across-beats signature; the payoff is a strike-through + a slam of the answer line instead of a logo pop.
Scene 1 (0.0–1.4s): ground + brand-bug settle; a `kicker` "LA IA EN TU TRABAJO" in `lavender` fades up at the upper-left third on "¿Todavía usas la inteligencia artificial" — only the kicker, the frame stays quiet while the question is being asked.
Scene 2 (1.4–3.6s): the hero question "¿Solo preguntas?" builds word-by-word at `display-hero` scale, left-anchored, ~65% of the frame width: "¿Solo" on "solo" @2.2, "preguntas?" on "preguntas" @3.2 (lands in `lavender`). Generous silence to the right.
Scene 3 (3.9–4.4s): on "En septiembre" a `gradient-stroke` draws left→right straight through "¿Solo preguntas?" (SVG stroke self-draw) and the question dims to `text-muted` ~40%; a `chip-date` "SEP · 2026" pops at the stroke's end with a smooth settle.
Scene 4 (4.3–5.94s): "Eso cambió." slams in beneath at `display-hero` scale (kinetic beat-slam → `kinetic-beat-slam`), `text` color with an `ai-glow` bloom behind it; hold still to the end.

## Frame 2 — De chat a colega

- scene: Una burbuja de chat ("responde") se encoge a un lado y de ella crece una tarjeta "Un colega"; tres verbos se encienden en fila: Investiga · Construye · Entrega.
- voiceover: "Claude dejó de ser un chat que responde. Ahora es un colega que investiga, construye y entrega trabajo real."
- duration: 7.4s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/02-tesis.html
- type: product_intro
- persuasion: Before/after + rule of three
- beat: Clarity + anticipation
- blueprint: kinetic-type-beats (Adapt)
- focal: la tarjeta "Un colega" con sus tres verbos
- roles: ground = background · burbuja de chat "ANTES" = supporting (se atenúa) · tarjeta "AHORA · Un colega" = foreground subject · tres chips de verbo con icono lineal = supporting · subrayado de gradiente bajo "trabajo real" = accent
- sfx: whoosh-short, pop

narrativeRole: Nombra la idea protagonista (de chat a colega) y fija la tesis antes de la evidencia.
keyMessage: Claude pasó de responder a ejecutar trabajo.

Adapt: keep the in-place swap signature (the chat bubble IS replaced by the colleague card at the same anchor), then a rule-of-three chip row.
Scene 1 (0.0–1.6s): center-left, a chat-bubble `card` (rounded, tail bottom-left) with kicker "ANTES" and three typing dots that resolve into the word "responde"; small caption "Claude, un chat" above it. ~35% of frame.
Scene 2 (1.6–2.5s): the bubble scales down and slides to the far left, dimming to ~40% (scale-swap handoff).
Scene 3 (2.5–3.6s): on "Ahora es un colega" a larger `card` morphs out from the bubble's position to center (card morph-anchor → `card-morph-anchor`): kicker "AHORA" in `lavender`, `display` headline "Un colega" — the card fills ~50% of the frame, `ai-glow` behind it.
Scene 4 (3.7–5.4s): inside the card, a row of three `chip`s with 2px line icons reveals on each spoken verb: "Investiga" (lupa) @3.7 · "Construye" (bloques/grúa) @4.3 · "Entrega" (check en `green`) @4.9 (per-item spring pop, triptych row).
Scene 5 (5.5–7.4s): "trabajo real" appears as a `body-lede` line under the chips and a `gradient-stroke` underline draws beneath it @5.5–6.1; then a deliberate held read — everything still.

## Frame 3 — Opus 5.5

- scene: Escalera de modelos (Haiku 4.5 · Sonnet 5 · Opus 5.5 · Fable 5.1) con Opus 5.5 subiendo al nivel de Fable 5.1; dos tarjetas de cifras verificadas (−40 % costo, +30 % velocidad) cuentan hacia su valor.
- voiceover: "Primero: Opus cinco punto cinco. Rinde al nivel de Fable cinco punto uno en la mayoría de tareas, cuesta cuarenta por ciento menos y es treinta por ciento más rápido que Opus cinco."
- duration: 11.046s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/03-opus.html
- type: feature_showcase
- persuasion: Numbered enumeration + statistical proof
- beat: Momentum + conviction
- blueprint: dataviz-countup (Adapt)
- focal: la pastilla "Opus 5.5" elevándose al nivel de "Fable 5.1", luego las dos cifras
- roles: ground = background · columna izquierda (kicker "NOVEDAD 01 · MODELOS", headline "Opus 5.5", chip-date "22-SEP-2026") = foreground text · escalera de 4 pastillas de modelo = foreground subject (right stage) · 2 tarjetas de stat = supporting → focal on their cue · source-rail = chrome
- sfx: whoosh-short, ping

narrativeRole: Primera novedad: el motor es más capaz y más barato, lo que hace viable delegar más.
keyMessage: Opus 5.5 da rendimiento de gama alta a menor costo y más rápido.

Adapt: keep the count-up signature on the two stats; the "trend chart" becomes a 4-step model ladder (ascending bar heights, labeled pills) where Opus rises to Fable's height.
Scene 1 (0.0–1.6s): listicle stage. Left column: kicker "NOVEDAD 01 · MODELOS", index-counter "01 / 05" top-right, then `display` headline "Opus 5.5" per-word on "Opus cinco punto cinco" (0.5–1.6); `chip-date` "22-SEP-2026" slides up under it.
Scene 2 (2.4–5.4s): right stage upper half: four model columns assemble left→right as rounded bars with name pills (Haiku 4.5 · Sonnet 5 · Opus 5.5 · Fable 5.1), heights ascending, Opus bar in `primary-bright`, others `surface-raised` (stat-bars-and-fills → `stat-bars-and-fills`) on "Rinde" @2.4; on "Fable cinco punto uno" @3.4 the Fable pill outlines in `lavender` and the Opus bar grows up to Fable's height while a dashed `lavender` level line connects them with the tag "≈ nivel Fable 5.1"; on "en la mayoría de tareas" @4.9 a small `body` note "*en la mayoría de tareas" fades in beneath.
Scene 3 (5.9–7.6s): right stage lower half, card 1: "−40 %" counts up (value-scaled counter → `counting-dynamic-scale`) on "cuesta cuarenta por ciento menos", label "costo vs Opus 5".
Scene 4 (7.8–9.6s): card 2 beside it: "+30 %" counts up on "treinta por ciento más rápido", label "más rápido que Opus 5"; `gradient-stroke` progress bar under card 2 fills.
Scene 5 (9.6–11.05s): source-rail "Fuente: anthropic.com/news/claude-opus-5-5 · 22-sep-2026" is visible (entered with chrome); everything holds still.

## Frame 4 — Un millón de tokens

- scene: Un contador sube hasta 1.000.000 mientras seis documentos de proyecto (Planos, Especificaciones, Contratos, RFIs, Presupuesto, Cronograma) caen dentro de una sola ventana de conversación.
- voiceover: "Segundo: un millón de tokens de contexto. Más de quinientas mil palabras: tu expediente técnico completo, en una sola conversación."
- duration: 8.123s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/04-contexto.html
- type: feature_showcase
- persuasion: Concretization (abstract → tangible object) + anchoring on a familiar referent
- beat: Fascination
- blueprint: dataviz-countup (Adapt)
- focal: el numeral "1.000.000" y, luego, la ventana de conversación llenándose
- roles: ground = background · columna izquierda (kicker "NOVEDAD 02 · CONTEXTO", numeral count-up, label "tokens de contexto", línea "≈ 555.000 palabras", chip "FABLE 5.1 · OPUS 5.5 · SONNET 5") = foreground · ventana de conversación (card) = foreground subject right · 6 tarjetas-documento con icono lineal = supporting · source-rail = chrome
- sfx: whoosh-short, sparkle

narrativeRole: Traduce "un millón de tokens" a algo que un profesional AEC visualiza: su expediente completo.
keyMessage: Cabe todo tu proyecto en una conversación.

Adapt: keep the hero count-up signature; the push-through becomes documents dropping into one window.
Scene 1 (0.0–0.5s): listicle stage; kicker "NOVEDAD 02 · CONTEXTO", index-counter "02 / 05".
Scene 2 (0.5–2.4s): left column: `numeral` counts 0 → "1.000.000" on "un millón" (value-scaled counter → `counting-dynamic-scale`, tabular-nums, Spanish thousands dots), landing with a small spring; label "tokens de contexto" reveals on "tokens de contexto" @1.2–1.7; chip "FABLE 5.1 · OPUS 5.5 · SONNET 5" beneath.
Scene 3 (2.5–4.3s): on "Más de quinientas mil palabras" the line "≈ 555.000 palabras" reveals under the numeral in `text-muted` `body-lede`.
Scene 4 (4.4–6.2s): right stage: a conversation-window `card` (header "Conversación", composer bar at its foot) fades up on "tu expediente"; six document tiles (Planos · Especificaciones · Contratos · RFIs · Presupuesto · Cronograma, each a small card with a 2px line icon) cascade in from above and settle as a neat 3×2 grid inside the window, staggered across "expediente técnico completo" (grid-card-assemble cascade → `dynamic-content-sequencing`).
Scene 5 (6.3–8.12s): on "una sola conversación" the window's border brightens to `lavender` with an `ai-glow` bloom and a small chip "1 conversación" pops at the window header; hold still. Source-rail: "Fuente: platform.claude.com/docs · modelos".

## Frame 5 — Un solo Claude

- scene: Una laptop se cierra; la tarjeta de progreso sigue trabajando ("Investigando → Redactando → Armando slides") y entrega archivos que se marcan en verde: Documento, Presentación → PowerPoint, PDF.
- voiceover: "Tercero: un solo Claude. Sigue trabajando aunque cierres la laptop, y te entrega documentos y presentaciones que exportas a PowerPoint o PDF."
- duration: 9.254s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/05-un-solo-claude.html
- type: feature_showcase
- persuasion: Demonstration (show the mechanism running)
- beat: Surprise + delight
- blueprint: agent-progress-theater (Adapt)
- focal: la tarjeta de progreso que sigue avanzando con la laptop cerrada, y su recibo de archivos
- roles: ground = background · columna izquierda (kicker "NOVEDAD 03 · PRODUCTO", headline "Un solo Claude", chip-date "16-SEP-2026", nota "Beta · llegando a Pro y Max") = foreground text · laptop (SVG lineal) = supporting · tarjeta de progreso + lista de entregables = foreground subject · source-rail = chrome
- sfx: whoosh-short, chime

narrativeRole: Muestra el cambio de categoría: trabajo asíncrono con entregables, no respuestas.
keyMessage: Claude trabaja sin ti delante y te entrega archivos listos.

Adapt: keep the working-state theater → receipt cascade that CHECKS OFF; the trigger beat is the laptop lid closing.
Scene 1 (0.0–1.7s): listicle stage; kicker "NOVEDAD 03 · PRODUCTO", index-counter "03 / 05"; `display` headline "Un solo Claude" per-word on "un solo Claude" (0.5–1.3); `chip-date` "16-SEP-2026" under it.
Scene 2 (1.8–4.0s): right stage: a line-drawn laptop (SVG, 2px `text-muted` strokes) sits left of a progress `card`; on "Sigue trabajando" the card's status phrase starts swapping ("Investigando…") with a `gradient-stroke` progress bar filling; on "cierres la laptop" @3.0–3.5 the laptop lid rotates closed (3D hinge, power3) — and the progress bar KEEPS filling while the status swaps to "Redactando…".
Scene 3 (4.3–6.8s): the receipt cascades under the status line: row "Documento" appears on "documentos" @5.0 and its badge flips to a `green` check; row "Presentación" on "presentaciones" @5.9 flips to check; status reads "Listo" in `green`.
Scene 4 (7.0–8.6s): two export `chip`s pop at the right of the Presentación row on their cues: "PowerPoint" @7.7 and "PDF" @8.4 (spring-pop entrance).
Scene 5 (8.6–9.25s): left column shows the small note "Beta · llegando a Pro y Max" (entered at Scene 1 in `text-soft`); source-rail "Fuente: claude.com/blog/cowork-is-now-claude · 16-sep-2026"; hold.

## Frame 6 — Claude en Chrome

- scene: Una ventana de navegador genérica estilo AECODE donde un cursor navega, hace clic y llena un formulario de proveedor; cada acción recibe un escudo de verificación.
- voiceover: "Cuarto: Claude en Chrome. Navega, hace clic y llena formularios por ti, con un filtro de seguridad que revisa cada acción."
- duration: 7.739s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/06-chrome.html
- type: feature_showcase
- persuasion: Demonstration + signposting
- beat: Comprehension + confidence
- blueprint: cursor-ui-demo (Adapt)
- focal: la ventana de navegador con el formulario llenándose y los escudos de verificación
- roles: ground = background · columna izquierda (kicker "NOVEDAD 04 · NAVEGADOR", headline "Claude en Chrome", chip-date "26-AGO-2026") = foreground text · ventana de navegador genérica (card con barra de URL "portal-proveedor.com") = foreground subject · cursor personalizado + ripple = supporting · log de acciones con escudos = supporting · source-rail = chrome
- sfx: whoosh-short, click

narrativeRole: Lleva el agente a la web real (portales, formularios) y responde la objeción de seguridad.
keyMessage: Claude opera la web por ti, con control en cada paso.

Adapt: keep the cursor-driven UI state changes on a locked stage; add a shield-check log rail as the payoff instead of a camera chase.
Scene 1 (0.0–1.6s): listicle stage; kicker "NOVEDAD 04 · NAVEGADOR", index-counter "04 / 05"; `display` headline "Claude en Chrome" per-word (0.4–1.3); `chip-date` "26-AGO-2026".
Scene 2 (1.7–2.5s): right stage: a generic browser `card` (three dots, URL pill "portal-proveedor.com", no real product chrome) with a supplier page skeleton; a custom lavender cursor glides to the "Cotizar" tab on "Navega".
Scene 3 (2.5–3.9s): click ripple on "clic" @2.5 (cursor click + ripple → `cursor-click-ripple`), the page swaps to a form; on "llena formularios" the three fields type in (type-on with caret → `discrete-text-sequence`): "Proyecto: Edificio Los Álamos" · "Partida: Acero corrugado" · "Entrega: Obra, Lima".
Scene 4 (4.2–6.8s): on "filtro de seguridad" a narrow action-log rail slides in at the window's right edge; three rows ("Navegar", "Clic", "Formulario") each get a shield icon that flips from `lavender` outline to a `green` check on "revisa cada acción" (staggered @5.8–6.8).
Scene 5 (6.8–7.74s): hold still; source-rail "Fuente: claude.com/blog · 26-ago-2026".

## Frame 7 — 2.000+ conectores

- scene: Un hub central "Claude" con ocho nodos de herramientas genéricas que se encienden en anillo y un contador que llega a 2.000+.
- voiceover: "Quinto: más de dos mil conectores y plugins. Claude se conecta a las herramientas que tu equipo ya usa."
- duration: 6.424s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/07-conectores.html
- type: feature_showcase
- persuasion: Frame-then-fill + statistical proof
- beat: Breadth + momentum
- blueprint: constellation-hub (Adapt)
- focal: el numeral "2.000+" y luego el hub con su anillo de nodos conectados
- roles: ground = background · columna izquierda (kicker "NOVEDAD 05 · ECOSISTEMA", numeral "2.000+", label "conectores y plugins", chip-date "23-SEP-2026") = foreground · hub central (card circular "Claude") = foreground subject right · 8 nodos con iconos lineales (correo, calendario, carpeta, documento, hoja de cálculo, chat de equipo, tablero de proyecto, CRM) = supporting · conectores (líneas) = supporting · source-rail = chrome
- sfx: whoosh-short, sparkle

narrativeRole: Cierra el listado mostrando que Claude vive dentro del stack del equipo, no aparte.
keyMessage: Claude se integra a tus herramientas actuales.

Adapt: keep the ring-springs-around-center signature resolving on the hub (held hub mark); the count-up guest-stars on the left.
Scene 1 (0.0–0.8s): listicle stage; kicker "NOVEDAD 05 · ECOSISTEMA", index-counter "05 / 05"; `chip-date` "23-SEP-2026".
Scene 2 (0.8–2.4s): left column: `numeral` counts up to "2.000+" on "dos mil" (value-scaled counter), label "conectores y plugins" reveals on "conectores y plugins" @1.2–2.1.
Scene 3 (2.8–3.6s): right stage: the central hub (circular `card`, "Claude" in Manrope 800, `ai-glow`) spring-pops on "Claude se conecta"; connector lines draw outward (SVG self-draw) toward eight empty node positions on an ellipse.
Scene 4 (3.7–5.5s): the eight tool nodes (rounded tiles with 2px line icons, no brand logos) spring into the ring staggered across "las herramientas que tu equipo ya usa" (logo/avatar ring + connectors → `avatar-cloud-network`); each connector brightens from `border-muted` to `primary-bright` as its node lands.
Scene 5 (5.5–6.42s): held hub mark — ring complete and still (at most a subtle jitter); source-rail "Fuente: claude.com/blog/claude-marketplace · 23-sep-2026".

## Frame 8 — Qué significa para AEC

- scene: Diagrama de flujo en tres nodos que se dibuja de izquierda a derecha: Expediente → Claude (lee · revisa portal) → Informe listo (check verde).
- voiceover: "¿Y qué significa para AEC? Imagina: Claude lee tu expediente, revisa el portal del proveedor y te entrega el informe listo para la reunión."
- duration: 9.035s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/08-aec.html
- type: benefit_highlight
- persuasion: Causal chain (A → B → C) + worked example
- beat: Foresight + "aha"
- blueprint: compose
- focal: el flujo de tres nodos, aterrizando en "Informe listo"
- roles: ground = background · headline "Para AEC" + chip "EJEMPLO" = foreground text (top) · 3 nodos (cards) = foreground subject · conectores con gradient-stroke = supporting · sub-pasos ("lee", "revisa portal del proveedor") = supporting
- sfx: whoosh-short, chime

narrativeRole: Conecta las cinco novedades en un caso AEC concreto (marcado como ejemplo, no anuncio).
keyMessage: Juntas, estas piezas convierten un día de trabajo en una delegación.

Compose: a full-width strip flow diagram, built left→right on the VO's causal chain.
Scene 1 (0.0–1.7s): `display-hero` headline "Para AEC" centered in the upper-middle, per-word reveal on "para AEC" @0.9–1.3; "AEC" in `lavender`.
Scene 2 (1.7–2.7s): on "Imagina" the headline eases up to the top third and shrinks to `headline` scale; a `chip` "EJEMPLO" appears beside it (marks this as a scenario, not a launch).
Scene 3 (2.7–4.0s): full-width strip, three node positions at left / center / right (~28% width each). Node 1 `card` "Expediente" (folder + plan-sheet line icon, sub-label "planos · specs · contratos") fades up on "tu expediente" @3.2; a connector draws to node 2 `card` "Claude" (center, `ai-glow`) whose first sub-step "lee" ticks in @3.0–3.4.
Scene 4 (4.0–5.6s): under the Claude node, sub-step 2 "revisa el portal del proveedor" reveals on "revisa el portal" @4.0–5.1 (small globe icon).
Scene 5 (5.7–7.9s): the `gradient-stroke` connector draws from node 2 to node 3 on "te entrega" @5.7–6.4; node 3 `card` "Informe listo" lands and its badge flips to a `green` check on "informe listo" @6.5–7.0; sub-label "para la reunión" reveals @7.3–7.9.
Scene 6 (7.9–9.04s): hold still — the whole chain reads.

## Frame 9 — Cierre AECODE

- scene: "Preguntar" se tacha y "Delegar" aterriza subrayado por el gradiente (callback al hook); luego "Aprende · Aplica · Construye mejor" y el wordmark AECODE con la firma del presentador.
- voiceover: "La pregunta ya no es qué le preguntas a Claude. Es qué trabajo le delegas. Aprende, aplica, construye mejor: esto es AECODE."
- duration: 9.568s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/09-cierre.html
- type: branding
- persuasion: Callback (returns to the hook's question) + distillation
- beat: Resolve + inspiration
- blueprint: logo-assemble-lockup (Adapt)
- focal: la palabra "Delegar" y después el wordmark AECODE
- roles: ground = background · palabra "Preguntar" tachada (text-muted) = supporting · palabra "Delegar" (display-hero) = foreground subject · subrayado gradient bajo "Delegar" = accent · tagline de tres palabras = supporting · wordmark AECODE (assets/brand/aecode-logo-principal-fondo-oscuro.png) + "Presenta: Alejandro Palpan" = foreground lockup
- sfx: riser, impact-bass-1

narrativeRole: Devuelve la pregunta del hook reformulada como decisión y firma con la marca AECODE.
keyMessage: Tu ventaja es decidir qué le delegas a Claude.

Adapt: keep the lockup-resolves-centered signature; the lockup is preceded by the thesis typing in and a three-word tagline relay. No brand-bug on this frame.
Scene 1 (0.0–2.4s): centered, the word "Preguntar" builds at `display` scale in `text-muted` on "La pregunta ya no es qué le preguntas" (@0.2–1.4); on "a Claude" @1.9 a thin `text-muted` strike line draws through it (callback to the hook's strike).
Scene 2 (2.6–4.1s): beneath it, "Delegar" lands at `display-hero` scale in `text` on "Es qué trabajo le delegas" (@2.6–3.5); on "delegas" @3.5 a `gradient-stroke` underline draws under it and an `ai-glow` blooms.
Scene 3 (4.2–6.2s): both words ease upward and scale down ~25%; a centered row of three `label`-style words reveals on its cues, separated by lavender dots: "Aprende" @4.2 · "Aplica" @4.8 · "Construye mejor" @5.4.
Scene 4 (6.3–7.6s): on "esto es AECODE" the AECODE wordmark image assembles at center (scales up from 0.92 with blur→sharp and an `ai-glow` bloom — logo lockup → `spring-pop-entrance` with smooth settle), ~34% of the frame width; "Presenta: Alejandro Palpan" in `label` `text-soft` reveals beneath @7.0.
Scene 5 (7.6–9.568s): held lockup, completely still; the final ~0.6s fades the whole frame to `canvas` (the video's only real exit).
