# AECODE Design System — Referencia compacta

> Dark-first. Navy profundo + violeta/índigo como marca. Verde para comunidad y acción positiva. Fuente: `Manrope`. Bordes redondeados, cards elevadas, pill nav, CTAs con gradiente.

**Principio rector:** ingeniería moderna + energía de comunidad + IA aplicada al AEC.

---

## 1. Assets

| Asset | Ruta |
|---|---|
| Isotipo AECODE fondo morado | `./assets/logos/aecode-isotipo-fondo-morado.jpg` |
| Isotipo Principal AECODE | `./assets/logos/aecode-isotipo-principal.png` |
| Logo Principal AECODE | `./assets/logos/aecode-isotipo-principal.png` |
| Logo Principal Fondo Oscuro AECODE | `./assets/logos/aecode-logo-principal-fondo-oscuro.png` |
| Logo Principal Fondo Blanco AECODE | `./assets/logos/aecode-logo-principal-fondo-blanco.png` |
| Aecodito (home) | `./assets/reference/aecodito-home.png` |
| Aecodito (footer) | `./assets/reference/aecodito-footer.png` |
| Community mascot | `./assets/reference/community-mascot.png` |
| Training hero | `./assets/reference/training-hero.png` |

---

## 2. Tokens de color

### 2.1 Paleta dark / light

| Token | Dark | Light | Uso |
|---|---|---|---|
| `--ae-bg` | `#0E1121` | `#F5F5F6` | Fondo principal |
| `--ae-bg-deep` | `#0D0F1F` | `#EEF3F8` | Navbar, sidebar, overlays |
| `--ae-surface` | `#13172F` | `#FFFFFF` | Cards, containers |
| `--ae-surface-raised` | `#1B1E3C` | `#F8F9FC` | Cards elevadas, popups |
| `--ae-surface-soft` | `#222341` | `#EDEBF9` | Inputs, bloques secundarios |
| `--ae-border` | `#7C7EDF66` | `#C7C2EC` | Borde default |
| `--ae-border-muted` | `#0C0F29` | `#EDEBF9` | Separadores sutiles |
| `--ae-text` | `#EEF3F8` | `#202231` | Texto principal |
| `--ae-text-muted` | `#A2B4CB` | `#3A4065` | Texto secundario |
| `--ae-text-soft` | `#8C97DC` | `#6D61CD` | Links, nav muted |
| `--ae-primary` | `#4A3AC1` | `#4A3AC1` | Acción primaria |
| `--ae-primary-hover` | `#4646B5` | `#4235B0` | Hover primario |
| `--ae-lavender` | `#A6A7FF` | `#A6A7FF` | Focus ring, íconos IA |
| `--ae-green` | `#17B14E` | `#17B14E` | Éxito, comunidad, WhatsApp |
| `--ae-danger` | `#E26A62` | `#E26A62` | Error, destructivo |

### 2.2 Gradientes

```css
--ae-gradient-primary:  linear-gradient(90deg, #4465EE, #6D12E3);
--ae-gradient-brand:    linear-gradient(90deg, #0B8CCD, #6A1FDF 50%, #0B8CCD);
--ae-gradient-success:  linear-gradient(90deg, #19C356, #493AC1);
--ae-glow-primary:      0 0 24px rgba(84, 80, 217, 0.55);
--ae-glow-green:        0 12px 28px rgba(25, 195, 86, 0.24);
```

---

## 3. Tipografía

**Fuentes:** `Manrope` (display + UI) · `Plus Jakarta Sans` (fallback/captions).

| Token | Size / LH | Weight | Uso |
|---|---|---|---|
| `display-1` | 64 / 72 | 700 | Hero desktop |
| `display-2` | 48 / 56 | 700 | Hero compacto |
| `h1` | 40 / 48 | 700 | Título de página |
| `h2` | 32 / 40 | 600 | Secciones |
| `h3` | 24 / 32 | 600 | Cards destacadas |
| `body-lg` | 16 / 24 | 400 | Párrafos, botones L |
| `body-md` | 14 / 22 | 400 | UI estándar |
| `body-sm` | 12 / 18 | 400 | Captions, labels, badges |

---

## 4. Espaciado, radios y sombras

| Token | Valor | Token | Valor |
|---|---|---|---|
| `space-2` | 8px | `radius-sm` | 8px |
| `space-3` | 12px | `radius-md` | 12px |
| `space-4` | 16px | `radius-lg` | 16px |
| `space-6` | 24px | `radius-xl` | 24px |
| `space-8` | 32px | `radius-pill` | 999px |
| `space-12` | 48px | `shadow-card` | `0 18px 50px rgba(0,0,0,.28)` |
| — | — | `shadow-light` | `0 12px 36px rgba(32,34,49,.10)` |

---

## 5. Layout

| Breakpoint | Container | Cols | Gutter |
|---|---|---|---|
| Mobile | 100% | 4 | 16px |
| Tablet | 720px | 8 | 20px |
| Desktop | 1180px | 12 | 24px |
| Wide | 1320px | 12 | 32px |

**Zonas de página:** header pill flotante → hero (gradiente + mascota + CTAs) → cards ecosistema (2–3 col) → social proof → FAQ/formulario → footer dark.

**Densidad:** landing `64–96px` entre secciones · app `24–32px` · tablas `12–16px`.

---

## 6. Componentes

### 6.1 Botones

**Tipos**

| Tipo | Dark | Light |
|---|---|---|
| Primary | Gradiente `#4465EE→#6D12E3` | `#4A3AC1` sólido |
| Secondary | Transparente, border `#EEF3F8` | Bg `#EDEBF9`, texto `#4A3AC1` |
| Success | `#17B14E` | `#17B14E` |
| Ghost | Transparente, texto `#A2B4CB` | Transparente, texto `#6D61CD` |
| Destructive | `#E26A62` | `#E26A62` |

**Tamaños**

| Tamaño | Font | Height | Padding H | Radius |
|---|---|---|---|---|
| Large | 16px | 48px | 24px | 999px |
| Medium | 14px | 40px | 20px | 12px |
| Small | 12px | 32px | 14px | 8–999px |

**Estados:** Default · Hover (glow `--ae-glow-primary`, `translateY(-1px)`) · Pressed (`#342989`, `scale(.98)`) · Disabled (opacity `.45`, cursor `not-allowed`) · Selected (border `#7C7EDF`) · Focus (ring `2px #A6A7FF`, offset 2px — obligatorio).

### 6.2 Navegación

**Top nav (pill):** items `border: 0.5px solid #0C0F29`; hover `border-color: #7C7EDF61`; active bg `#4A3AC1`; padding `15px 7.5px`; radius `25px`. Mobile: bottom nav icono + label 12px.

**Sidebar app**

| Estado | Dark | Light |
|---|---|---|
| Fondo | `#0D0F1F` | `#FFFFFF` |
| Item default | Texto `#A2B4CB` | Texto `#3A4065` |
| Item hover | Bg `rgba(124,126,223,.12)` | Bg `#EDEBF9` |
| Item active | Bg `#4A3AC1`, texto `#EEF3F8` | Bg `#EDEBF9`, texto `#4A3AC1`, border `#4A3AC1` |

Máximo 7 ítems primarios; agrupar si hay más.

### 6.3 Cards

| Propiedad | Dark | Light |
|---|---|---|
| Background | `#13172F` / `#1B1E3C` | `#FFFFFF` |
| Border | `1px solid #7C7EDF33` | `1px solid #EDEBF9` |
| Radius | 16–24px | 16–24px |
| Padding | 20–24px | 20–24px |

**Variantes:** Course card (img 16:9 + badge + metadata + CTA) · Ticket card (precio tachado + beneficios + CTA full) · Speaker card (avatar + nombre + badge) · Member card (avatar circular + país + rol).

### 6.4 Formularios

**Tamaños:** Large `48px / 0 16px` · Medium `40px / 0 14px` · Small `32px / 0 12px`.

| Estado | Cambio visual |
|---|---|
| Default | Dark: bg `#1B1E3C`, border `#7C7EDF33` · Light: bg `#fff`, border `#C7C2EC` |
| Focus | Border `#A6A7FF` + ring `rgba(166,167,255,.24)` |
| Error | Border `#E26A62` + mensaje 12px específico |
| Disabled | Opacity `.55` |

Placeholder: `#8C97DC` dark · `#9CA3AF` light. Checkbox/radio checked `#4A3AC1`. Switch on: gradiente primario.

### 6.5 Overlays y feedback

**Badges / chips**

| Variante | Dark | Light |
|---|---|---|
| Info | Bg `#6D70F94D` | Bg `#EDEBF9`, texto `#4A3AC1` |
| Success | Bg `#17B14E` | Bg `#17B14E` |
| Premium | Gradiente primario | Gradiente primario |
| Muted | Border `#7C7EDF66` | Border `#C7C2EC` |

**Tabs / filtros:** pill container · selected: gradiente `#4465EE→#4235B0`, texto blanco · hover: bg `rgba(124,126,223,.10)`.

**Tooltip:** 12px, padding `8px 10px`, radius 8px, max-width 260px · dark: bg `#1B1E3C` · light: bg `#202231` blanco · delay 300ms hover.

**Modal:** overlay `rgba(5,7,24,.72)` blur 4px · panel radius 24px · dark `#10152F→#050718` · light `#FFFFFF` · width 480–960px.

**Toasts:** border-left 4px · radius 12px · duración 4–6s.

| Tipo | Color |
|---|---|
| Success | `#17B14E` |
| Warning | `#F59E0B` |
| Error | `#E26A62` |
| Info | `#4465EE` |

**Skeleton:** dark `#222341→#3A4065` · light `#EDEBF9→#F8F9FC`.

**Íconos:** lineal/rounded 1.5–2px stroke · IA: gradiente `#A6A7FF→#7853E5` · comunidad/WA: verde · tallas 16/20/24px. Aecodito para soporte, empty states y onboarding.

---

## 7. Dark / Light — reglas de adaptación

| Elemento | Dark | Light |
|---|---|---|
| Body | `#0E1121` | `#F5F5F6` |
| Hero | Navy + gradiente radial | Blanco + shape violeta |
| Cards | Superficie navy | Blanco + border suave |
| Texto | `#EEF3F8` | `#202231` |
| CTA | Gradiente | `#4A3AC1` sólido |
| Footer | Siempre dark | Mantener dark por identidad |

> El modo light no es "quitar colores". Es mover el contraste. Los acentos de marca no cambian.

---

## 8. Accesibilidad

- Contraste mínimo 4.5:1 (texto normal), 3:1 (texto grande).
- Focus ring `2px #A6A7FF` obligatorio en todo elemento interactivo.
- No depender solo del color para estado (selected / error / success).
- Área táctil mínima 40px; ideal 44–48px.
- `prefers-reduced-motion` en todas las animaciones.
- Label real + `aria-describedby` para ayuda/error en formularios.

---

## 9. Implementación CSS

```css
:root {
  color-scheme: dark;
  --ae-bg: #0E1121;
  --ae-bg-deep: #0D0F1F;
  --ae-surface: #13172F;
  --ae-surface-raised: #1B1E3C;
  --ae-surface-soft: #222341;
  --ae-border: #7C7EDF66;
  --ae-text: #EEF3F8;
  --ae-text-muted: #A2B4CB;
  --ae-primary: #4A3AC1;
  --ae-primary-hover: #4646B5;
  --ae-lavender: #A6A7FF;
  --ae-green: #17B14E;
  --ae-danger: #E26A62;
  --ae-gradient-primary: linear-gradient(90deg, #4465EE, #6D12E3);
  --ae-gradient-success: linear-gradient(90deg, #19C356, #493AC1);
}

[data-theme="light"] {
  color-scheme: light;
  --ae-bg: #F5F5F6;
  --ae-bg-deep: #EEF3F8;
  --ae-surface: #FFFFFF;
  --ae-surface-raised: #F8F9FC;
  --ae-border: #C7C2EC;
  --ae-text: #202231;
  --ae-text-muted: #3A4065;
  --ae-primary: #4A3AC1;
  --ae-primary-hover: #4235B0;
}

body {
  background: var(--ae-bg);
  color: var(--ae-text);
  font-family: 'Manrope', 'Plus Jakarta Sans', sans-serif;
}
```

## 10. Tailwind theme

```ts
export const aecodeTheme = {
  colors: {
    ae: {
      bg: '#0E1121',        bgDeep: '#0D0F1F',
      surface: '#13172F',   surfaceRaised: '#1B1E3C',
      border: '#7C7EDF66',  text: '#EEF3F8',
      muted: '#A2B4CB',     primary: '#4A3AC1',
      blue: '#4465EE',      violet: '#6D70F9',
      lavender: '#A6A7FF',  green: '#17B14E',
      danger: '#E26A62',
    },
  },
  borderRadius: {
    aeSm: '8px', aeMd: '12px', aeLg: '16px', aeXl: '24px', aePill: '999px',
  },
  fontFamily: {
    display: ['Manrope', 'Plus Jakarta Sans', 'sans-serif'],
    sans: ['Manrope', 'Plus Jakarta Sans', 'sans-serif'],
  },
};
```
