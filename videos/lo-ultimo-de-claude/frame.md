---
version: alpha
name: AECODE Dark — Frame (video / frame layer)
description: >
  Video-first companion to AECODE's design system (brand/DESIGN.md). The unit is the frame
  (1920×1080). Atoms are identical and sacred — dark-first deep navy ground, violet/indigo as the
  brand ink, lavender for AI accents, green for positive action, Manrope 400–800 as the single
  typeface family + JetBrains Mono for data chrome, rounded elevated cards (16–24px radius),
  pill chips, the primary gradient (#4465EE → #6D12E3) used scarcely on CTAs and one hero stroke.
  Composition, frame scale, and motion-readiness rewritten for the frame.
unit: the frame — 1920×1080 primary
principle: atoms are sacred · composition is free · numbers come from the script

colors:
  canvas: "#0E1121"
  canvas-deep: "#0D0F1F"
  surface: "#13172F"
  surface-raised: "#1B1E3C"
  surface-soft: "#222341"
  border: "rgba(124,126,223,0.40)"
  border-muted: "rgba(124,126,223,0.20)"
  text: "#EEF3F8"
  text-muted: "#A2B4CB"
  text-soft: "#8C97DC"
  primary: "#4A3AC1"
  primary-bright: "#6D5CF0"
  lavender: "#A6A7FF"
  green: "#17B14E"
  blue: "#4465EE"
  danger: "#E26A62"
  gradient-primary: "linear-gradient(90deg, #4465EE, #6D12E3)"
  gradient-ai: "linear-gradient(90deg, #A6A7FF, #7853E5)"
  glow-primary: "0 0 48px rgba(84,80,217,0.55)"
  grid-line: "rgba(166,167,255,0.07)"

typography:
  # — reading ramp —
  body:         { fontFamily: "Manrope", cqw: 1.25, weight: 500, lineHeight: 1.45 }
  body-lede:    { fontFamily: "Manrope", cqw: 1.6, weight: 500, lineHeight: 1.4 }
  label:        { fontFamily: "Manrope", cqw: 0.95, weight: 700, tracking: "0.14em", upper: true }
  mono-tag:     { fontFamily: "JetBrains Mono", cqw: 0.9, weight: 500, tracking: "0.04em" }
  mono-source:  { fontFamily: "JetBrains Mono", cqw: 0.78, weight: 400, tracking: "0.02em" }
  # — display ramp (Manrope 700–800, tight tracking) —
  card-title:   { fontFamily: "Manrope", cqw: 2.1, weight: 700, lineHeight: 1.15 }
  headline:     { fontFamily: "Manrope", cqw: 3.6, weight: 800, lineHeight: 1.05, tracking: "-0.02em" }
  display:      { fontFamily: "Manrope", cqw: 5.4, weight: 800, lineHeight: 1.0, tracking: "-0.03em" }
  display-hero: { fontFamily: "Manrope", cqw: 7.6, weight: 800, lineHeight: 0.95, tracking: "-0.035em" }
  numeral:      { fontFamily: "Manrope", cqw: 11.5, weight: 800, lineHeight: 0.9, tracking: "-0.04em" }

fonts:
  - { family: "Manrope", weight: 400, src: "assets/fonts/Manrope-400.woff2" }
  - { family: "Manrope", weight: 500, src: "assets/fonts/Manrope-500.woff2" }
  - { family: "Manrope", weight: 600, src: "assets/fonts/Manrope-600.woff2" }
  - { family: "Manrope", weight: 700, src: "assets/fonts/Manrope-700.woff2" }
  - { family: "Manrope", weight: 800, src: "assets/fonts/Manrope-800.woff2" }
  - { family: "JetBrains Mono", weight: 400, src: "assets/fonts/JetBrainsMono-400.woff2" }
  - { family: "JetBrains Mono", weight: 500, src: "assets/fonts/JetBrainsMono-500.woff2" }

spacing:
  edge: "4.2cqw"
  pad-top: "6cqw"
  gap-sm: "0.8cqw"
  gap-md: "1.6cqw"
  gap-lg: "3cqw"

components:
  ground:
    background: "{colors.canvas} + a dual radial swell (violet 18% top-left, blue 10% bottom-right) + faint 3cqw blueprint grid in {colors.grid-line}"
    placement: "full-bleed class=clip layer behind EVERY frame"
    description: "Dark engineering-blueprint ground — the AEC nod. Never flat black, never a purple 'AI bokeh'."
  card:
    background: "{colors.surface} → {colors.surface-raised}"
    border: "1px solid {colors.border}"
    radius: "1.2cqw (≈24px)"
    shadow: "0 18px 50px rgba(0,0,0,.28)"
    description: "Elevated content card for items, stats, UI mocks."
  chip:
    background: "rgba(109,112,249,0.30)"
    border: "1px solid {colors.border}"
    radius: "999px"
    typography: "{typography.label}"
    description: "Pill tag: dates, model names, categories."
  chip-date:
    background: "transparent"
    border: "1px solid {colors.lavender}"
    color: "{colors.lavender}"
    typography: "{typography.mono-tag}"
    description: "Date stamp on every news item (e.g. 22-SEP-2026)."
  source-rail:
    typography: "{typography.mono-source}"
    color: "{colors.text-soft}"
    placement: "bottom-left, just above the caption band (y ≈ 80% of height), inset {spacing.edge}"
    description: "'Fuente: anthropic.com · 22-sep-2026' — on every frame that states a fact."
  kicker:
    typography: "{typography.label}"
    color: "{colors.lavender}"
    description: "Small uppercase lead line above a headline ('NOVEDAD 01 · MODELOS')."
  index-counter:
    typography: "{typography.mono-tag}"
    color: "{colors.text-soft}"
    placement: "top-right, inset {spacing.edge}: '01 / 05'"
    description: "Listicle position for the 5 news items."
  brand-bug:
    asset: "assets/brand/aecode-isotipo.png"
    size: "2.6cqw tall"
    placement: "top-left, inset {spacing.edge}, opacity 0.9, next to 'AECODE · LO ÚLTIMO DE CLAUDE' in {typography.label}"
    description: "Persistent small identity chrome on every frame except the close."
  gradient-stroke:
    background: "{colors.gradient-primary}"
    description: "The ONE hero accent: an underline, a progress bar, a connector line, or a CTA pill. Max one per frame."
  ai-glow:
    shadow: "{colors.glow-primary}"
    description: "Soft violet glow behind the focal element on reveal (bloom, then hold)."
---

# AECODE Dark — Frame (video / frame layer)

## Overview

AECODE at frame scale is a **dark engineering studio at night**: deep navy ground with a faint
blueprint grid, violet as the brand ink, lavender for anything "AI", green only for positive
outcomes (done, delivered, check). One typeface family — **Manrope** — carries everything from the
hero numeral to the body; **JetBrains Mono** carries data chrome (dates, sources, counters).
The feel is *ingeniería moderna + energía de comunidad + IA aplicada al AEC*: precise, confident,
warm — never neon, never sci-fi.

**Key characteristics at frame scale:**

- **Dark-first** navy ground `#0E1121` + dual radial swell + faint blueprint grid on every frame.
- **Manrope 800** for display with tight negative tracking; hierarchy by size AND weight contrast (800 vs 500).
- **Violet/lavender** carries brand and AI; **green** is reserved for "done / delivered / yes".
- **Rounded elevated cards** (≈24px radius, soft shadow, 1px violet border) hold items and stats.
- **Pill chips** for dates and model names; the **date chip** is the news signature.
- **Source rail** in mono on every fact frame — credibility is part of the brand.

## The Frame

### Frame Craft Bar

- **Squint** — one element dominates at 3–5× its nearest neighbor (display-hero / numeral vs body).
- **Silence** — statement frames (hook, thesis, close) keep ~45–55% of the frame as ground.
- **Restraint** — max one gradient-stroke per frame; green only for completion; no rainbow.
- **Reference** — aim at a **Linear / Vercel keynote slide in a dark BIM studio**; failure looks like a
  **generic purple AI template with floating bokeh**.

- **Primary:** 1920×1080 (16:9). Author in `cqw`/`cqh` against a `container-type: size` ground.
- **Safe area:** `edge` (4.2cqw) inset. **Caption band:** bottom ~17% reserved — content caps above y ≈ 83%.
- **Chrome:** brand-bug top-left, index-counter top-right (listicle frames), source-rail bottom-left above the band.

## Colors

`{colors.canvas}` is the ground; `{colors.text}` is primary type; `{colors.text-muted}` secondary.
`{colors.primary}` / `{colors.primary-bright}` = brand ink (card borders, active states, key word
highlight). `{colors.lavender}` = AI accents, kickers, date chips. `{colors.green}` = success only.
`{colors.gradient-primary}` = the single hero stroke / CTA per frame. Never pure `#000` or `#fff`.

## Typography

Fonts ship as files — declare `@font-face` for each family/weight you use, pointing at the `src`
paths in the frontmatter (resolve relative to your composition file, e.g. from
`compositions/frames/` use `../../assets/fonts/Manrope-800.woff2`).

- **Legibility floor:** any load-bearing line ≥ 1.25cqw (≈24px); mono chrome ≥ 0.78cqw.
- **Fit-to-measure:** ≤3 words → `display-hero`/`numeral`; 4–7 words → `display`; 8+ → `headline`. Cap text blocks at ≤ 70cqw.
- Spanish copy: keep accents (á é í ó ú ñ ¿ ¡); use `tabular-nums` on counters; thousands separator `.` (1.000.000) and decimal `,`.

## Depth & Surface

Three layers per frame: ground (grid + swell) → cards/diagram (midground, soft shadow) →
focal type/number (foreground, optional ai-glow). Blur is allowed only for depth-of-field on
off-focus items. No glassmorphism stacks, no heavy bevels.

## Shapes

Radius 1.2cqw on cards, 0.6cqw on small tiles, 999px on chips/pills. Lines 2px, rounded caps.
Icons: linear, rounded, 2px stroke, drawn as inline SVG (no emoji, no icon fonts).

## Frame Treatments

1. **Statement (hook / thesis / close)** — centered or left-anchored display-hero on the ground; one
   lavender kicker; one gradient-stroke underline on the key word. Sparse.
2. **News item (listicle 01–05)** — kicker `NOVEDAD 0N · CATEGORÍA` + date chip + headline on the left
   (≈45%); the invented visual (diagram / numeral / UI mock card) on the right (≈55%); source rail.
3. **Data hit** — a numeral count-up dominates (≥40% of width) with a one-line label beneath;
   comparison chips alongside.
4. **Flow diagram** — 3 nodes (cards) connected by gradient-stroke connectors that draw on, left→right.
5. **Close** — AECODE wordmark (`assets/brand/aecode-logo-principal-fondo-oscuro.png`) centered,
   thesis line above, presenter line "Alejandro Palpan · AECODE" below.

## Composition Rules

### Do
- Keep ground grid + swell on every frame; brand-bug top-left except on the close.
- Put a date chip + source rail on every news frame.
- Reveal pieces as the narration names them.
- Use green only when something is completed/delivered.

### Don't
- Don't use Anthropic's logo, colors or type — this is AECODE editorial content about Claude.
- Don't invent numbers; every figure traces to `capture/extracted/visible-text.txt`.
- Don't stack more than one gradient accent per frame; no floating bokeh, no neon.
- Don't place content in the bottom 17% caption band.

## Numerals & Claims (hard rule)

Allowed figures (verbatim from sources): `1.000.000 tokens`, `~555.000 palabras`, `−40 %` (costo vs
Opus 5), `+30 %` (velocidad vs Opus 5), `66,4 %` (Terminal-Bench 4.0), `2.000+` (conectores y
plugins), dates `26-ago-2026`, `16-sep-2026`, `22-sep-2026`, `23-sep-2026`. Anything else → words, not numbers.

## Pre-Render Self-Audit

- Squint: one dominant element. Silence on statement frames. One gradient accent max.
- Ground grid + swell present; brand-bug present (not on close); caption band clear.
- Every fact frame has date chip + source rail. Fonts declared via `@font-face` to shipped files.
