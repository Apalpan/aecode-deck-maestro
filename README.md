# Deck Maestro AECODE Startup · 50 slides

Presentación autocontenida (un solo `index.html`, sin build ni dependencias) que sirve como
**file completo de entendimiento avanzado** de AECODE como startup: oportunidad, problema,
producto, mercado, modelo, tracción, métricas, moat, competencia, roadmap, equipo y ask.

**Live:** https://apalpan.github.io/aecode-deck-maestro/

## Diseño (v2)

Usa el **design system oficial de AECODE**: violeta `#4a3ac1` (primario) + verde `#26b96f` +
azul `#4465ee` sobre lavanda claro `#f7f8fe` y navy `#0c0f29`. Tipografía Inter.
Ritmo **light + dark combinado** por capítulo, con toggle global.

Esquemas y gráficas incluidas: barras animadas, TAM/SAM/SOM concéntrico, pirámide de 3 capas
(Wedge/Engine/Moat), driver tree de la NSM, gauge de North Star, funnels B2C/B2B,
mapa competitivo 2×2, donut de uso de fondos, flywheel, timeline de roadmap y diagramas de flujo.

## Cómo usar

- **Abrir**: doble clic en `index.html` (cualquier navegador) o desde Obsidian.
- **Navegar**: `←` / `→` o barra espaciadora · clic en los bordes · swipe en móvil.
- **Índice**: tecla `O` o el botón ☰.
- **Tema**: tecla `T` o el botón ◐ — cicla **mix (combinado) → todo oscuro → todo claro**.
- **Pantalla completa**: tecla `F`.

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
