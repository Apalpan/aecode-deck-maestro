# Deck Maestro AECODE Startup · v4 "Enfoque Final 10/10"

Presentación autocontenida (un solo `index.html`, sin build ni dependencias) que sirve como
**file completo de entendimiento avanzado** de AECODE como startup. Posicionamiento:
**plataforma de adopción tecnológica para construcción** — *aprende, aplica, construye mejor*.
Cubre problema, dolor por cliente, solución/producto, categoría, diferenciación, mercado,
modelo de 3 motores (Live valida · B2B ancla · On-demand AI escala), **finanzas** (ventas por
año, mix por modelo, márgenes de contribución), NSM dual, growth, moat, ask e impacto del capital.

**Live:** https://apalpan.github.io/aecode-deck-maestro/

## Diseño

Usa el **design system oficial de AECODE** (`brand/DESIGN.md`): **Manrope**, navy `#0E1121`,
violeta `#4A3AC1`, verde `#17B14E`, azul `#4465EE`, lavanda `#A6A7FF`. Logos reales en portada,
cierre e isotipo por slide + Aecodito. Ritmo **light + dark combinado** por capítulo, con toggle global.
Gráficas: barras, **barras apiladas** (mix de ingresos), TAM/SAM/SOM concéntrico, donut de fondos,
mapa competitivo 2×2, flywheel y diagramas de flujo.

Esquemas y gráficas incluidas: barras animadas, TAM/SAM/SOM concéntrico, pirámide de 3 capas
(Wedge/Engine/Moat), driver tree de la NSM, gauge de North Star, funnels B2C/B2B,
mapa competitivo 2×2, donut de uso de fondos, flywheel, timeline de roadmap y diagramas de flujo.

## Cómo usar

- **Abrir**: doble clic en `index.html` (cualquier navegador) o desde Obsidian.
- **Navegar**: `←` / `→` o barra espaciadora · rueda del mouse · clic en los bordes · swipe en móvil.
- **Barra de capítulos** (arriba): clic en cualquier segmento salta a ese capítulo; muestra el avance.
- **Índice**: tecla `O` o el botón ☰.
- **Auto-play**: tecla `P` o el botón ▶ (avanza cada 7 s; cualquier acción lo pausa).
- **Tema**: tecla `T` o el botón ◐ — cicla **mix (combinado) → todo oscuro → todo claro**.
- **Pantalla completa**: tecla `F`.
- **Responsive**: en escritorio escala 16:9; en móvil/vertical el contenido **reflowea** (columnas se apilan,
  tablas con scroll, diagramas reescalados) — completo y legible en cualquier pantalla.

## Cómo iterar

Todo el contenido vive en la lista `SLIDES` de `build_deck.py`. Edita y regenera:

```bash
python build_deck.py
```

Layouts: `cover`, `statement`, `divider`, `split`, `chart`, `cards`, `table`, `flow`,
`tss`, `pyramid`, `nsm`, `funnel`, `map`, `timeline`, `ask`, `close`.
Gráficas: `barchart()`, `tamsamsom()`, `pyramid()`, `tree()`, `donut()`, `map2x2()`, `flow()`.

## Fuentes (vault AP_Knowledge_OS)

`.codex/G+ Startup/AECODE Startup/` (master report, dossier estratégico/operativo, design system del site)
· `02_EMPRESAS/AECODE/01_AECODE-Startup-Base/*` · `03_AECODE-Estrategia/AECODE-Tesis-de-Mercado-v1`
· `05_AECODE-Growth/AECODE-Dashboard-Metricas` + `Growth-Playbook` · `02_AECODE-Producto/Arquitectura`.

> Corte: junio 2026. Varias cifras (TAM/SAM/SOM, unit economics por motor, ask, pricing USD,
> tracción aportada para pitch) están marcadas en fuente como **ASUMIDO · VALIDAR** y deben
> conciliarse con contabilidad/analytics/CRM antes de un data room externo.
