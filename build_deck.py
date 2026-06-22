# -*- coding: utf-8 -*-
"""
Generador del Deck Maestro AECODE Startup — 50 slides · v2
Paleta OFICIAL AECODE (violeta #4a3ac1 + verde #26b96f + azul #4465ee · navy #0c0f29),
ritmo light+dark combinado, esquemas y gráficas (TAM/SAM/SOM, pirámide 3 capas, driver
tree, barras, mapa 2x2, donut, flywheel, funnel, timeline). Autocontenido: un index.html.
Ejecutar:  python build_deck.py
"""
import html, datetime, pathlib

def esc(s): return html.escape(str(s))

# ---------- helpers de contenido ----------
def chip(t):
    return f'<span class="chip reveal">{t}</span>'
def kicker(t):
    return f'<div class="kicker reveal">{esc(t)}</div>'
def title(t):
    return f'<h2 class="s-title reveal">{t}</h2>'
def lead(t):
    return f'<p class="lead reveal">{t}</p>'
def src(t):
    return f'<div class="source reveal">Fuente vault: {esc(t)}</div>'
def note(t):
    return f'<div class="vnote reveal">{t}</div>'

def _isnum(v):
    s=str(v).replace(",","").replace(".","").replace("-","")
    return s.isdigit()
def stat(value, label, sub="", suffix="", prefix="", tone="violet"):
    cnt=f'data-count="{value}"' if _isnum(value) else ""
    sub_h=f'<div class="stat-sub">{esc(sub)}</div>' if sub else ""
    return (f'<div class="stat reveal stat-{tone}"><div class="stat-num">'
            f'<span class="stat-pre">{esc(prefix)}</span>'
            f'<span class="stat-val" {cnt}>{esc(value)}</span>'
            f'<span class="stat-suf">{esc(suffix)}</span></div>'
            f'<div class="stat-label">{esc(label)}</div>{sub_h}</div>')

def card(head, body, num="", tag="", tone="violet"):
    num_h=f'<div class="card-num">{esc(num)}</div>' if num else ""
    tag_h=f'<div class="card-tag">{esc(tag)}</div>' if tag else ""
    return (f'<div class="card reveal card-{tone}">{num_h}{tag_h}'
            f'<div class="card-head">{head}</div><div class="card-body">{body}</div></div>')

def bullets(items):
    return '<ul class="bullets">'+"".join(f'<li class="reveal">{b}</li>' for b in items)+'</ul>'
def grid(items, cols=3, extra=""):
    return f'<div class="grid grid-{cols} {extra}">{"".join(items)}</div>'
def table(headers, rows, hi=None):
    hi=hi or []
    th="".join(f"<th>{h}</th>" for h in headers)
    body=""
    for r in rows:
        tds="".join(f'<td class="{("cell-hi" if j in hi else "")}">{c}</td>' for j,c in enumerate(r))
        body+=f'<tr class="reveal">{tds}</tr>'
    return f'<div class="table-wrap reveal"><table class="dt"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'
def quote(t):
    return f'<blockquote class="bigquote reveal">{t}</blockquote>'

# ---------- gráficas ----------
def barchart(rows):
    # rows: (label, pct0-100, display, tone)
    out='<div class="barchart reveal">'
    for r in rows:
        label,pct,disp=r[0],r[1],r[2]; tone=r[3] if len(r)>3 else "violet"
        out+=(f'<div class="bar bar-{tone}"><div class="bar-top"><span>{label}</span>'
              f'<b>{disp}</b></div><div class="bar-track"><i style="--w:{pct:.1f}%"></i></div></div>')
    return out+'</div>'

def tamsamsom(items):
    # items: [(label, value, desc)] big->small
    legend="".join(
        f'<div class="tss-leg reveal"><span class="dot d{i}"></span><div><b>{l}</b> · {v}<small>{d}</small></div></div>'
        for i,(l,v,d) in enumerate(items))
    return f'''<div class="tss reveal">
      <div class="tss-rings">
        <div class="ring r0"><span>TAM</span></div>
        <div class="ring r1"><span>SAM</span></div>
        <div class="ring r2"><span>SOM</span></div>
      </div>
      <div class="tss-legend">{legend}</div>
    </div>'''

def pyramid(layers):
    # layers top->bottom: (name, desc, tone)
    rows=""
    widths=["58%","78%","100%"]
    for i,(n,d,t) in enumerate(layers):
        rows+=(f'<div class="pyr-row reveal" style="--w:{widths[i]}"><div class="pyr-band band-{t}">'
               f'<b>{n}</b><span>{d}</span></div></div>')
    return f'<div class="pyramid">{rows}</div>'

def flow(steps):
    # steps: list of (text, kind)  kind: '', 'hot', 'win'
    out='<div class="flow reveal">'
    for i,(t,k) in enumerate(steps):
        out+=f'<div class="flow-step {k}">{t}</div>'
        if i<len(steps)-1: out+='<i class="flow-arr">→</i>'
    return out+'</div>'

def tree(root, drivers):
    items="".join(f'<div class="tree-node reveal">{d}</div>' for d in drivers)
    return f'''<div class="tree reveal">
      <div class="tree-root">{root}</div>
      <div class="tree-line"></div>
      <div class="tree-branches">{items}</div>
    </div>'''

def donut(segs):
    # segs: [(label, pct, color)]
    stops=[]; acc=0
    for l,p,c in segs:
        stops.append(f"{c} {acc}% {acc+p}%"); acc+=p
    grad=",".join(stops)
    legend="".join(
        f'<div class="dn-leg reveal"><span style="background:{c}"></span><b>{p}%</b> {l}</div>'
        for l,p,c in segs)
    return f'''<div class="donut-wrap reveal">
      <div class="donut" style="background:conic-gradient({grad})"><div class="donut-hole"></div></div>
      <div class="donut-legend">{legend}</div></div>'''

def map2x2(points, xlab, ylab):
    # points: (left%, top%, label, tone, big)
    dots=""
    for x,y,l,t,big in points:
        dots+=(f'<div class="mp-dot {"mp-big" if big else ""} mp-{t} reveal" '
               f'style="left:{x}%;top:{y}%"><span>{l}</span></div>')
    return f'''<div class="map2x2 reveal">
      <div class="mp-axis-y">{ylab[0]}<i></i>{ylab[1]}</div>
      <div class="mp-plane">{dots}
        <div class="mp-grid"></div></div>
      <div class="mp-axis-x">{xlab[0]}<i></i>{xlab[1]}</div>
    </div>'''

# ---------- definición de slides ----------
SLIDES=[]
def S(theme, chapter, layout, content):
    SLIDES.append(dict(theme=theme, chapter=chapter, layout=layout, content=content))

# 01 PORTADA
S("dark","AECODE","cover",f"""
  <div class="cover-logo reveal"><img class="logo-dark" src="brand/assets/logos/aecode-logo-principal-fondo-oscuro.png" alt="AECODE"><img class="logo-light" src="brand/assets/logos/aecode-logo-principal-fondo-blanco.png" alt="AECODE"></div>
  <img class="aecodito reveal" src="brand/assets/reference/aecodito-home.png" alt="">
  <h1 class="cover-title reveal">La <span class="grad">capa de capacidad</span><br>para la transformación<br>digital de la construcción</h1>
  <p class="cover-sub reveal">Convierte conocimiento técnico AEC en capacidad real de ejecución, validada con evidencia. <b>Aprende · Aplica · Demuestra.</b></p>
  <div class="cover-meta reveal"><span>Deck maestro de startup</span><span class="dot">·</span><span>file de entendimiento avanzado</span><span class="dot">·</span><span>{datetime.date.today().strftime('%b %Y')}</span></div>
  <div class="cover-hint reveal">← → navegar · <b>T</b> tema · <b>F</b> pantalla completa · <b>O</b> índice</div>
""")

# 02 HOOK
S("dark","Apertura","split",f"""
  {kicker("El hook")}
  {title('La IA hizo <span class="grad">abundante el conocimiento</span>.<br>Lo escaso es demostrar capacidad.')}
  <div class="split">
   <div class="split-l">
     {stat("85","De empleadores dice contratar por skills, no por títulos","HBS + Burning Glass", suffix="%")}
     {stat("0.14","De contrataciones realmente ocurrió sin exigir título","la paradoja de la verificación", suffix="%", tone="green")}
   </div>
   <div class="split-r">
     {lead('En construcción, <b>saber nunca fue saber hacer</b>. Lo verdaderamente escaso es demostrar que alguien puede aplicar BIM, IA, automatización y datos en trabajo real.')}
     {barchart([("Intención: contratar por skill",100,"85%","violet"),("Realidad: lo logran",2,"0.14%","green")])}
     {chip("El contenido se comoditiza · la evidencia se vuelve el activo escaso")}
   </div>
  </div>
""")

# 03 TESIS
S("dark","Apertura","statement",f"""
  {kicker("La tesis en una frase")}
  {quote('AECODE es la <span class="grad">capa de capacidad</span> para la transformación digital del sector AEC: un sistema que convierte conocimiento técnico en <span class="grad">capacidad real de ejecución</span>, demostrada con evidencia.')}
  {flow([("Aprende",""),("Aplica","hot"),("Demuestra","win")])}
  {lead('La unidad de valor no es el curso ni el certificado de asistencia: es la <b>skill verificable</b> — una capacidad concreta demostrada con una evidencia técnica que un empleador puede comprobar.')}
""")

# 04 DIVIDER I
S("light","I · Oportunidad","divider",f"""
  <div class="div-index reveal">01</div>
  <h2 class="div-title reveal">La oportunidad<br>y el <span class="grad">por qué ahora</span></h2>
  <p class="div-sub reveal">Un sector gigante y subdigitalizado entra a su mayor disrupción justo cuando le falta el talento para aprovecharla.</p>
""")

# 05 OPORTUNIDAD
S("light","I · Oportunidad","chart",f"""
  {kicker("La oportunidad")}
  {title('El sector <span class="grad">más grande del planeta</span>, el peor digitalizado')}
  <div class="split">
   <div class="split-l">
     {barchart([
       ("Sector AEC global · TAM macro",100,"US$16.3 T","violet"),
       ("Software AEC 2033 (desde $11.3B '25)",60,"US$32.1 B","blue"),
       ("EdTech LatAm 2033 (CAGR 12.4%)",48,"US$50.4 B","green"),
       ("Inversión histórica en tech (de ingresos)",6,"<1%","ink"),
     ])}
   </div>
   <div class="split-r">
     {bullets([
       '~13% del PIB mundial · <b>200M+</b> empleos.',
       'Productividad <b>plana 20 años</b> mientras el resto de industrias se multiplicaba.',
       'McKinsey: lo digital puede subir productividad <b>15–20% inmediato</b>, 50–60% con 7 palancas.',
       'US$50,000M de VC/PE a tech AEC 2020–2022 (<b>+85%</b>).',
     ])}
   </div>
  </div>
  {src("AECODE-Tesis-de-Mercado-v1 · McKinsey · IMARC · Mordor")}
""")

# 06 POR QUÉ AHORA
S("light","I · Oportunidad","chart",f"""
  {kicker("Por qué ahora")}
  {title('El sector <span class="grad">dice usar IA</span>, pero casi nadie la ejecuta')}
  <div class="split">
   <div class="split-l">
     {barchart([
       ("Firmas AEC que “usan IA”",75,"75%","violet"),
       ("La usa de forma regular",12,"12%","blue"),
       ("Confía en su propia data",29,"29%","green"),
       ("Planea aumentar inversión en IA",94,"94%","violet"),
     ])}
   </div>
   <div class="split-r">
     {lead('La brecha no es de <i>tecnología</i> — es de <b>adopción y capacidad operativa</b>. Las empresas compran herramientas que sus equipos aún no pueden ejecutar en proyectos reales.')}
     {card("Tres condiciones recién alineadas", bullets(["Madurez de datos (década de BIM/ERP/sensores)","Presión operativa (sobrecostos → predicción)","Capital selectivo: 77% del contech fue a IA en 2025"]), tag="Inflexión", tone="green")}
   </div>
  </div>
  {note('Datos del vault 2025–2026 · refrescar contra fuente oficial antes de un pitch público.')}
""")

# 07 5 VECTORES
S("light","I · Oportunidad","table",f"""
  {kicker("La tesis estructural")}
  {title('Los <span class="grad">5 vectores</span> que abren la ventana')}
  {table(["#","Vector","Evidencia clave"],[
   ["1","<b>Mercado AEC gigante y subdigitalizado</b>","US$16.3T · &lt;1% en tech · productividad plana 20 años"],
   ["2","<b>Brecha de talento crítica</b>","499k faltantes (EE.UU. 2026) · 62% sin candidatos con skills"],
   ["3","<b>Inflexión de IA 2025–2026</b>","77% del capital contech fue a IA · de asistente a agente"],
   ["4","<b>Skills sin verificación</b>","85% contrata por skills · solo 0.14% lo logra"],
   ["5","<b>LATAM + Perú = apalancamiento</b>","EdTech LatAm ×3 a 2033 · Plan BIM Perú = mandato estatal"],
  ], hi=[1])}
""")

# 08 TAM/SAM/SOM
S("light","I · Oportunidad","tss",f"""
  {kicker("Mercado · dimensionamiento")}
  {title('TAM / SAM / SOM — <span class="grad">dos marcos internos</span>')}
  <div class="split">
    <div class="split-l">{tamsamsom([
      ("TAM","US$2.5 B","Upskilling AEC LATAM"),
      ("SAM","US$600–800 M","Hispanohablante"),
      ("SOM","US$3–5 M","Capturable a 3 años"),
    ])}</div>
    <div class="split-r">
      {card("Marco operativo bottom-up", table(["","Valor"],[["TAM","US$360 M"],["SAM","US$87.5 M"],["SOM 3 años","US$2.5 M"]]), tag="Alternativa", tone="blue")}
      {note('Ambos marcos están <b>ASUMIDO · VALIDAR</b>. Antes de un pitch externo hay que elegir una metodología y dejar los supuestos explícitos.')}
    </div>
  </div>
""")

# 09 BRECHA TALENTO
S("light","I · Oportunidad","chart",f"""
  {kicker("El cuello de botella")}
  {title('La brecha de talento es <span class="grad">digital y estructural</span>')}
  <div class="split">
   <div class="split-l">
     {stat("499","Trabajadores AEC faltantes en EE.UU. (2026)","Deloitte", suffix="K")}
     {stat("124","En valor en riesgo si la brecha persiste","US$ mil millones · Deloitte", prefix="US$", suffix="B", tone="green")}
   </div>
   <div class="split-r">
     {barchart([
       ("Empresas con dificultad para cubrir vacantes",92,"92%","violet"),
       ("Proyectos con retrasos reportados",80,"80%","blue"),
       ("Empresas sin candidatos con skills",62,"62%","violet"),
       ("Fuerza laboral sin formación formal",50,">50%","green"),
       ("Trabajadores 55+ sin relevo",20,">20%","ink"),
     ])}
   </div>
  </div>
  {lead('Coordinador VDC, modelador BIM, especialista en automatización: <b>roles de ruta crítica que hace una década no existían</b> y hoy nadie forma a escala.')}
""")

# 10 INFLEXIÓN IA
S("light","I · Oportunidad","split",f"""
  {kicker("Inflexión de IA · 2025–2026")}
  {title('El capital ya votó: <span class="grad">la IA es la apuesta</span>')}
  <div class="split">
   <div class="split-l">
     {stat("77","Del capital contech fue a IA en 2025","vs. 35% en 2024 — Cemex Ventures", suffix="%")}
     {stat("30","Mercado IA generativa en construcción 2034","desde US$3.64B (2025), CAGR 26.6%", prefix="US$", suffix="B+", tone="green")}
   </div>
   <div class="split-r">
     {bullets([
       'Early adopters: <b>68% ahorró &gt;US$50,000/año</b>.',
       '<b>46% ahorró 500–1,000 horas</b> al año.',
       'La IA pasó de <i>asistente</i> a <i>agente</i> — cambia qué skills se necesitan.',
       'Cuanto más rápido avanza la IA, <b>más urgente reconvertir</b> al profesional AEC.',
     ])}
     {chip("AECODE es la capa de reconversión de ese talento")}
   </div>
  </div>
""")

# 11 ECONOMÍA SIN VERIFICACIÓN
S("light","I · Oportunidad","split",f"""
  {kicker("La paradoja de verificación")}
  {title('Todos quieren contratar por skills.<br><span class="grad">Nadie sabe probarlas.</span>')}
  <div class="split">
   <div class="split-l">
     {table(["Señal de mercado","Dato"],[
       ["Empleadores que dicen contratar por habilidades","<b>85%</b>"],
       ["Empresas que eliminaron el requisito de título","<b>53%</b>"],
       ["Contrataciones reales sin título","<b>0.14%</b>"],
       ["RR.HH. para quien validar skills es el reto #1","<b>62%</b>"],
       ["Credenciales en circulación EE.UU.","<b>1.8M</b>"],
     ], hi=[1])}
   </div>
   <div class="split-r">
     {lead('La intención existe; la <b>infraestructura de verificación no</b>. Open Badges 3.0 (sobre W3C Verifiable Credentials) recién se estandarizó en 2023.')}
     {quote('La Estrella Polar de AECODE —<b>skills verificadas con evidencia / usuario activo</b>— es la respuesta exacta a ese vacío.')}
   </div>
  </div>
""")

# 12 LATAM + PERÚ
S("light","I · Oportunidad","split",f"""
  {kicker("Máximo apalancamiento")}
  {title('Perú tiene un <span class="grad">viento regulatorio</span> único: Plan BIM')}
  <div class="split">
   <div class="split-l">
     {bullets([
       '<b>Mandato del MEF</b>: BIM progresivo y obligatorio en inversión pública.',
       'Hitos: 2025 → <b>agosto 2026</b> (clave) → 2030 (tres niveles de gobierno).',
       '<b>50+ entidades</b> ya iniciaron: PRONIS, PROVIAS, PRONIED, Vivienda.',
       'El Estado nombró las brechas: formación desigual, falta de talento, certificadoras.',
     ])}
   </div>
   <div class="split-r">
     {stat("2300","Obras públicas paralizadas en Perú","errores técnicos / gestión — lo que BIM previene", suffix="+", tone="green")}
     {stat("26.9","Valor paralizado","miles de millones de soles", prefix="S/", suffix="MM", tone="green")}
   </div>
  </div>
  {lead('El Estado <b>genera la demanda</b> de talento verificado que AECODE forma: un mercado con comprador estructural.')}
""")

# 13 VALIDACIÓN MERCADO
S("light","I · Oportunidad","cards",f"""
  {kicker("Validación clara de mercado")}
  {title('La demanda no es hipótesis: está <span class="grad">documentada</span>')}
  {grid([
   card('<span class="card-big">39%</span> de skills se transforman hacia 2030; 63% ve la brecha como barrera #1.',"", tag="WEF 2025"),
   card('<span class="card-big">46%</span> de líderes pone skills de IA como prioridad de contratación.',"", tag="Autodesk 2025"),
   card('<span class="card-big">96%</span> de empleadores: las microcredenciales fortalecen una postulación.',"", tag="Coursera 2025", tone="green"),
   card('<span class="card-big">56%</span> de premium salarial para quien tiene skills de IA.',"", tag="PwC 2025"),
   card('<span class="card-big">78%</span> de organizaciones ya usó IA en 2024.',"", tag="Stanford HAI", tone="blue"),
   card('<span class="card-big">56%</span> de inversionistas asignará más fondos a IA en construcción.',"", tag="RICS 2025"),
  ], 3, "cards-sm")}
""")

# 14 DIVIDER II
S("dark","II · El Problema","divider",f"""
  <div class="div-index reveal">02</div>
  <h2 class="div-title reveal">El problema<br>que <span class="grad">sí duele</span></h2>
  <p class="div-sub reveal">No es falta de cursos. Es falta de un sistema que conecte aprendizaje, evidencia y ejecución real.</p>
""")

# 15 PROBLEMA CENTRAL
S("dark","II · El Problema","split",f"""
  {kicker("Problema central")}
  {title('Dos lados del mismo <span class="grad">vacío</span>')}
  <div class="split">
   <div class="split-l">
     {card("El profesional", 'Invierte tiempo y dinero en cursos <b>sin ruta clara</b> conectada a roles reales: aprendizaje desordenado, certificados débiles y nada que demuestre capacidad.', num="◐", tag="Lado oferta")}
   </div>
   <div class="split-r">
     {card("La empresa", 'No tiene sistema confiable para <b>diagnosticar brechas, formar equipos y verificar</b> quién puede ejecutar habilidades digitales críticas. Compra tech que el equipo no sabe usar.', num="◑", tag="Lado demanda", tone="green")}
   </div>
  </div>
  {quote('La hipótesis: la brecha crítica no es falta de tecnología — es falta de <span class="grad">adopción y capacidad operativa</span>.')}
""")

# 16 DOLOR ESPECÍFICO
S("dark","II · El Problema","cards",f"""
  {kicker("Dolor específico")}
  {title('Tres actores, <span class="grad">tres dolores</span>')}
  {grid([
   card("Profesional", bullets(["No sabe qué aprender primero","Tiene certificados, no evidencia","Quiere diferenciarse para empleo/ascenso","Necesita resultados en días, no diplomas en meses"]), num="01"),
   card("Empresa AEC", bullets(["Compra capacitación sin progreso medible","No sabe si el equipo puede aplicar BIM/IA","Necesita reducir retrabajo","Debe justificar la inversión en upskilling"]), num="02", tone="green"),
   card("Instructor / experto", bullets(["Tiene expertise pero no escala","Necesita CMS y plantillas","Quiere revenue share","Necesita analítica de su contenido"]), num="03", tone="blue"),
  ], 3)}
""")

# 17 SEGMENTOS
S("dark","II · El Problema","table",f"""
  {kicker("Segmentos prioritarios")}
  {title('A quién <span class="grad">resolvemos</span> y quién paga')}
  {table(["Segmento","Dolor","Oferta AECODE"],[
   ["<b>Junior</b> (0–3 años)","Diferenciación, CV, portafolio","Beca AI Talent, rutas starter, certificados"],
   ["<b>Intermedio</b> (3–8)","Subir de rol, automatizar","Rutas premium, IA aplicada, BIM/VDC"],
   ["<b>Coordinador BIM/VDC</b>","Estandarizar y demostrar impacto","Rutas avanzadas, BEP/ISO, automatización"],
   ["<b>Empresa AEC</b> (B2B)","Upskilling rápido, adopción","Licencias, in-house, dashboard de brechas"],
   ["<b>Experto / instructor</b>","Monetizar conocimiento","Marketplace, revenue share, CMS"],
  ], hi=[0])}
""")

# 18 DIVIDER III
S("light","III · Solución","divider",f"""
  <div class="div-index reveal">03</div>
  <h2 class="div-title reveal">La solución<br>y el <span class="grad">producto</span></h2>
  <p class="div-sub reveal">Un Learning OS que cierra el loop que nadie más cierra: práctica aplicada, evidencia y validación.</p>
""")

# 19 SOLUCIÓN APRENDE/APLICA/DEMUESTRA
S("light","III · Solución","cards",f"""
  {kicker("La solución")}
  {title('Una plataforma de <span class="grad">capacidad</span>, no de cursos')}
  {grid([
   card("Aprende","Rutas por rol, cápsulas de microlearning (5–12 min) y diagnóstico inteligente que ordena el camino.", num="01"),
   card("Aplica","Sandbox activo: el usuario ejecuta flujos reales —no consume teoría— y produce un entregable.", num="02", tone="blue"),
   card("Demuestra","Evidencia + rúbrica 1–4 + validación → badge y Evidence Wallet verificable.", num="03", tone="green"),
  ], 3)}
  {quote('La tecnología no transforma. Tu gente sí. <span class="grad">AECODE convierte conocimiento técnico en capacidad real de ejecución.</span>')}
""")

# 20 LOOP / LEARNING OS
S("light","III · Solución","flow",f"""
  {kicker("El núcleo · Learning OS")}
  {title('El loop que <span class="grad">nadie más cierra</span>')}
  {flow([("Diagnóstico",""),("Ruta por rol",""),("Skill",""),("Sandbox · práctica","hot"),("Evidencia","hot"),("Validación","hot"),("Skill Passport","win")])}
  {lead('La diferencia está en los pasos antes del resultado: <b>práctica aplicada → evidencia → validación</b>. Eso no lo hacen Udemy, YouTube ni cursos grabados — requiere sandbox, rúbrica, feedback y verificación.')}
  {grid([
   card("Diagnóstico de brechas","Rol, experiencia, objetivo, herramienta y urgencia.", num="◆"),
   card("Sandbox activo","Entorno donde se ejecutan flujos reales.", num="◆", tone="blue"),
   card("Evidence Wallet","Portafolio verificable de competencias técnicas.", num="◆", tone="green"),
  ], 3, "cards-sm")}
""")

# 21 MODELO 3 CAPAS
S("light","III · Solución","pyramid",f"""
  {kicker("Modelo de 3 capas")}
  {title('Wedge → Engine → <span class="grad">Moat</span>')}
  <div class="split">
   <div class="split-l">{pyramid([
     ("Wedge","El profesional entra por productividad y relevancia","violet"),
     ("Engine","La empresa paga por transformación y capacidad de equipo","blue"),
     ("Moat","Ecosistema de talento, evidencia y datos AEC","green"),
   ])}</div>
   <div class="split-r">
     {lead('El profesional es la <b>cuña</b> de entrada (CAC bajo vía comunidad); la empresa es el <b>motor</b> de revenue; los datos de evidencia son el <b>foso</b> que se acumula con cada vuelta.')}
     {chip("“Demuestra” empieza como evidencia accionable para empresas, no como credencial masiva")}
   </div>
  </div>
""")

# 22 UNIDAD CENTRAL SKILL
S("light","III · Solución","cards",f"""
  {kicker("Arquitectura de producto")}
  {title('La unidad central es la <span class="grad">Skill</span>, no el video')}
  {lead('Una skill es una <b>capacidad demostrable</b>. Cada una contiene:')}
  {grid([
   card("Objetivo observable","Qué puede <i>hacer</i> el usuario al terminar.", num="01"),
   card("Cápsulas","Microcontenidos de teoría y demo.", num="02"),
   card("Práctica","Ejercicio aplicado en sandbox.", num="03", tone="blue"),
   card("Evidencia","Entregable verificable: reporte, modelo, script, dashboard.", num="04", tone="green"),
   card("Rúbrica","Criterios de evaluación 1–4.", num="05"),
   card("Feedback","Comentario humano / IA.", num="06"),
   card("Certificación","Badge / microcredencial con QR.", num="07", tone="green"),
   card("Datos","Eventos que alimentan recomendación.", num="08", tone="blue"),
  ], 4, "cards-xs")}
""")

# 23 JERARQUÍA
S("light","III · Solución","table",f"""
  {kicker("Jerarquía del producto")}
  {title('De la <span class="grad">ruta</span> a la <span class="grad">evidencia</span>')}
  {flow([("Route",""),("Cluster",""),("Skill","hot"),("Capsule",""),("Practice",""),("Evidence","win"),("Certificate","win")])}
  {table(["Nivel","Definición","Ejemplo"],[
   ["<b>Ruta</b>","Secuencia orientada a rol o resultado","Automation BIM Starter"],
   ["<b>Skill</b>","Capacidad demostrable con evidencia","Automatizar parámetros en Revit"],
   ["<b>Cápsula</b>","Microcontenido de concepto","Nodos básicos de selección"],
   ["<b>Evidencia</b>","Entrega verificable","Archivo .dyn + capturas antes/después"],
  ], hi=[0])}
""")

# 24 SANDBOX + EVIDENCE WALLET
S("light","III · Solución","flow",f"""
  {kicker("Learning OS · lo nuevo")}
  {title('Sandbox Activo + <span class="grad">Evidence Wallet</span>')}
  {flow([("Diagnóstico de brechas",""),("Rutas guiadas por rol",""),("Sandbox Activo","hot"),("Evidence Wallet","win")])}
  <div class="split">
   <div class="split-l">{card("Sandbox Activo", 'Entorno donde el usuario <b>ejecuta flujos reales</b> de ingeniería, no solo consume teoría. La práctica produce el entregable que se valida.', tag="Aplicar", tone="blue")}</div>
   <div class="split-r">{card("Evidence Wallet", 'Portafolio verificable de competencias técnicas — útil para el <b>profesional</b> (carrera) y para el <b>reclutador corporativo</b> (decisión de equipo).', tag="Demostrar", tone="green")}</div>
  </div>
  {note('AI Coach sectorial y capacidades avanzadas: <b>ASUMIDO · VALIDAR</b> en el dossier operativo.')}
""")

# 25 SKILL PILOTO
S("light","III · Solución","split",f"""
  {kicker("Skill piloto · cuña de validación")}
  {title('“Generar un <span class="grad">reporte técnico de obra</span> asistido por IA”')}
  <div class="split">
   <div class="split-l">
     {bullets([
       'Dolor frecuente y transversal: supervisor, residente, oficina técnica, PM.',
       'Resultado visible en <b>≤ 90 min</b> o menos de 7 días.',
       'Evidencia clara: el reporte técnico final.',
       'Usa IA sin prometer automatización excesiva.',
     ])}
     {chip("TTFP — Time to First Practice como métrica de activación")}
   </div>
   <div class="split-r">
     {card("Rúbrica mínima (1–4)", table(["Criterio","Nivel aceptable"],[
       ["Claridad","Situación, ubicación, fecha, contexto"],
       ["Evidencia","Observaciones / fotos referenciadas"],
       ["Análisis","Distingue hallazgo, impacto y riesgo"],
       ["Accionabilidad","Responsable, fecha, siguiente acción"],
     ]), tag="Validación", tone="green")}
   </div>
  </div>
""")

# 26 UX
S("light","III · Solución","cards",f"""
  {kicker("Experiencia de usuario")}
  {title('Tres superficies que el usuario <span class="grad">vive cada día</span>')}
  {grid([
   card("Dashboard", bullets(["Qué skill toca hoy","Progreso por ruta","Créditos y evidencias pendientes"]), num="01"),
   card("Skill Page", bullets(["Cápsulas → práctica → evidencia","Rúbrica y feedback","Foro, recursos y badge"]), num="02", tone="blue"),
   card("Skill Passport", bullets(["Skills + evidencias","Certificados con QR verificable","CV y LinkedIn listos"]), num="03", tone="green"),
  ], 3)}
""")

# 27 MÓDULOS
S("light","III · Solución","table",f"""
  {kicker("Módulos de plataforma")}
  {title('Un sistema completo, no una <span class="grad">colección de videos</span>')}
  {table(["Módulo","Función"],[
   ["<b>Onboarding inteligente</b>","Perfil, rol, objetivo, software, urgencia"],
   ["<b>AI Coach</b>","Recomendación, feedback preliminar, nudges"],
   ["<b>Evidence Engine</b>","Evidencia como unidad de validación, no quiz"],
   ["<b>Skill Passport</b>","Portafolio verificable de skills y certificados"],
   ["<b>CMS Instructor + Marketplace</b>","Crear, publicar, revenue share, reputación"],
   ["<b>B2B Dashboard</b>","Matriz de brechas, progreso y evidencia por equipo"],
   ["<b>AI Hub</b>","+100 bots verticales AEC, normativa y software"],
  ], hi=[0])}
""")

# 28 ARQUITECTURA front/back/AI
S("dark","III · Solución","cards",f"""
  {kicker("Arquitectura del producto")}
  {title('Frontstage · Backstage · <span class="grad">IA</span>')}
  {grid([
   card("Frontstage", bullets(["Landing → diagnóstico","Dashboard personal","Skill Page + Evidence Upload","Feedback → Badge → Passport"]), num="◐"),
   card("Backstage", bullets(["CMS de skills + rúbricas","Cola de revisión humana","Admin analytics","B2B dashboard + performance"]), num="◑", tone="blue"),
   card("Capa de IA", bullets(["Diagnóstico + recomendación","Feedback preliminar (RAG)","Detección de errores","Nudges de abandono"]), num="◓", tone="green"),
  ], 3)}
  {lead('Regla de oro del producto: <b>medir habilidad demostrada, no consumo de contenido</b>. El control humano valida las skills críticas.')}
""")

# 29 INNOVACIÓN
S("dark","III · Solución","cards",f"""
  {kicker("Innovación tecnológica")}
  {title('Cinco activos que <span class="grad">se acumulan</span>')}
  {grid([
   card("Skill Graph AEC","Taxonomía propia de roles, skills, rutas y evidencias.", num="01"),
   card("Evidence Engine","La evidencia es la unidad de validación, no un quiz.", num="02", tone="green"),
   card("AI Coach","Diagnóstico, RAG, feedback preliminar y nudges.", num="03", tone="blue"),
   card("Skill Passport","Perfil verificable de skills y certificados.", num="04"),
   card("Live-to-platform","Cada curso live → cápsulas, rúbricas, evidencias y datos.", num="05", tone="green"),
   card("B2B talent intelligence","Matriz de brechas y evidencia por equipo.", num="06", tone="blue"),
  ], 3, "cards-sm")}
  {chip("Más usuarios → más datos → mejores rutas y evaluación · sin escalar horas humanas")}
""")

# 30 STACK
S("dark","III · Solución","table",f"""
  {kicker("Stack tecnológico")}
  {title('Infraestructura para <span class="grad">escalar sin colapsar</span>')}
  <div class="split">
   <div class="split-l">{table(["Capa","Recomendación"],[
     ["Frontend","Next.js · React · TypeScript"],
     ["UI","Tailwind · componentes reutilizables"],
     ["Auth / Data","Supabase (V1) o mock para demo"],
     ["Evidencias","Supabase Storage / S3"],
     ["AI Coach","RAG sobre base AECODE + eval. preliminar"],
     ["Analytics","Eventos del funnel desde día 1"],
   ], hi=[0])}</div>
   <div class="split-r">
     {card("Eventos mínimos del funnel", '<code>landing_view · cta_clicked · signup_completed · onboarding_completed · route_accepted · skill_started · evidence_uploaded · skill_verified · payment_completed</code>', tag="Analytics", tone="blue")}
     {note('Infra de soporte: AgentFlow (n8n privado + Redis + Cloudflare) · VisionPro (computer vision de obra). No escalar usuarios sin base estable.')}
   </div>
  </div>
""")

# 31 MODELO DE NEGOCIO
S("dark","IV · Negocio","cards",f"""
  {kicker("Modelo de negocio")}
  {title('Cuatro motores, <span class="grad">un solo flywheel</span>')}
  {grid([
   card("1 · Live Training B2C","Caja, comunidad y validación. Motor de hoy.", num="◆"),
   card("2 · B2B institucional","Contratos de mayor valor, recurrencia, brechas.", num="◆", tone="green"),
   card("3 · On-demand + IA","Margen SaaS y escala (microlearning).", num="◆", tone="blue"),
   card("4 · B2B2C","Empresa paga o impulsa; profesional aprende; evidencia valida.", num="◆", tone="violet"),
  ], 4, "cards-sm")}
  {lead('Líneas escalables: <b>freemium · créditos · premium · rutas certificadas · certificaciones · B2B team · corporate academy · marketplace · Summit/sponsors</b>.')}
""")

# 32 B2B2C
S("dark","IV · Negocio","flow",f"""
  {kicker("Modelo B2B2C")}
  {title('La comunidad es el <span class="grad">canal</span>; la empresa, el <span class="grad">ticket</span>')}
  {flow([("Profesional aprende y valida",""),("Comparte evidencia","hot"),("Empresa ve el valor","hot"),("Compra rutas para el equipo","win"),("Data mejora el producto","")])}
  {lead('El mismo motor de contenido sirve al profesional (<b>B2C</b>) y a la empresa que necesita upskilling medible (<b>B2B</b>). La comunidad orgánica baja el CAC; la empresa sube el ticket y la recurrencia. Patrón <b>BuildWitt</b> aplicado a LATAM: medios propios → audiencia → conversión barata.')}
""")

# 33 PRICING
S("dark","IV · Negocio","table",f"""
  {kicker("Pricing")}
  {title('Una escalera del <span class="grad">free al enterprise</span>')}
  <div class="split">
   <div class="split-l">{table(["Oferta","Rango","Objetivo"],[
     ["<b>Free</b>","S/ 0","Adquisición"],
     ["<b>Starter créditos</b>","S/ 49–99","Primer pago"],
     ["<b>Premium individual</b>","S/ 59–129/mes","Recurrencia B2C"],
     ["<b>Ruta certificada</b>","S/ 199–699","Ticket medio"],
     ["<b>B2B Team</b>","S/ 80–180 usuario/mes","Recurrencia B2B"],
     ["<b>Training in-house</b>","S/ 8,000–60,000","Ticket alto"],
   ], hi=[0,1])}</div>
   <div class="split-r">{card("Pricing canónico en USD", table(["Oferta","Rango"],[
     ["Workshop live B2C","US$40–60"],
     ["Programa / cohorte","US$120–250"],
     ["B2B Starter (≤15)","~US$3,000"],
     ["B2B Growth (≤40)","~US$8,000"],
     ["On-demand","US$19/mes · US$180/año"],
     ["Teams B2B2C","US$12–15 usuario/mes"],
   ]), tag="ASUMIDO · VALIDAR", tone="blue")}</div>
  </div>
""")

# 34 ACTUAL VS FUTURO
S("dark","IV · Negocio","table",f"""
  {kicker("Modelo actual vs. futuro")}
  {title('De <span class="grad">servicios</span> a plataforma <span class="grad">recurrente</span>')}
  {table(["Etapa","Modelo","Estado","Riesgo"],[
   ["<b>Actual</b>","Live training, diplomados, talleres","Activo","Depende de horas y ventas one-time"],
   ["<b>Transición</b>","Microlearning, retos, 1ª skill verificable","En validación","Debe probar evidencia y retención"],
   ["<b>Plataforma</b>","Freemium, créditos, premium, certificados","Futuro cercano","Requiere MRR real"],
   ["<b>B2B</b>","Licencias, corporate academy, dashboard","Early","Falta cuantificar pilotos"],
   ["<b>Marketplace</b>","Instructores, revenue share","Posterior","Riesgo de calidad → curaduría"],
  ], hi=[0])}
  {lead('Cada venta live <b>alimenta la plataforma</b>: el curso se convierte en cápsulas, skills, rúbricas, evidencias y datos.')}
""")

# 35 UNIT ECONOMICS + por motor
S("dark","IV · Negocio","chart",f"""
  {kicker("Unit economics")}
  {title('La unidad económica <span class="grad">ya cierra</span>')}
  <div class="statrow">
    {stat("35","CAC blended","8× mejor que benchmark EdTech", prefix="$", tone="green")}
    {stat("3.1","LTV : CAC","gate de inversión: &gt;3× ✓", suffix="×", tone="green")}
    {stat("74","Gross margin plataforma","cockpit · cercano a SaaS", suffix="%", tone="green")}
    {stat("7","Payback","meses · benchmark Kaman &lt;12", suffix=" m")}
  </div>
  <div class="split">
   <div class="split-l">{barchart([
     ("B2C Live · LTV:CAC ≈ 4.5×",45,"GM 50%","violet"),
     ("B2B · LTV:CAC ≈ 30×",100,"GM 62%","green"),
     ("On-demand · LTV:CAC ≈ 12×",78,"GM 82%","blue"),
   ])}</div>
   <div class="split-r">{note('Unit economics por motor: <b>ASUMIDO · VALIDAR</b> (B2C $100/CAC $20 · B2B $5,000/CAC $400 · On-demand $19mes/CAC $15). Churn mensual ~8% (borde alto) y MRR real a separar del one-time.')}</div>
  </div>
""")

# 36 FUNNEL
S("dark","IV · Negocio","funnel",f"""
  {kicker("Funnel comercial")}
  {title('B2C y B2B con <span class="grad">gates de validación</span>')}
  <div class="split">
   <div class="split-l">
     <div class="funnel reveal">
       <div class="fn" style="--w:100%"><span>Lead · diagnóstico</span><b>conv &gt;15%</b></div>
       <div class="fn" style="--w:82%"><span>Reto / taller</span><b>registro &gt;75%</b></div>
       <div class="fn" style="--w:64%"><span>1ª evidencia</span><b>skill start &gt;40%</b></div>
       <div class="fn hot" style="--w:46%"><span>Skill verificada</span><b>&gt;70% · NSM</b></div>
       <div class="fn win" style="--w:30%"><span>Premium / 2ª skill</span><b>free→paid &gt;10%</b></div>
     </div>
     <div class="fn-cap">B2C</div>
   </div>
   <div class="split-r">
     <div class="funnel reveal">
       <div class="fn" style="--w:100%"><span>Contacto empresa</span><b></b></div>
       <div class="fn" style="--w:80%"><span>Diagnóstico de brechas</span><b></b></div>
       <div class="fn hot" style="--w:60%"><span>Piloto 30 días + dashboard</span><b></b></div>
       <div class="fn" style="--w:44%"><span>Reporte ROI</span><b></b></div>
       <div class="fn win" style="--w:30%"><span>Contrato team</span><b>ACV · NRR</b></div>
     </div>
     <div class="fn-cap">B2B</div>
   </div>
  </div>
""")

# 37 NSM DRIVER TREE + GAUGE
S("light","V · Métricas","nsm",f"""
  {kicker("North Star Metric")}
  {title('Skills verificadas con evidencia <span class="grad">/ usuario activo</span>')}
  <div class="nsm reveal">
    <div class="nsm-gauge">
      <div class="nsm-now"><span class="nsm-val" data-count="0.17">0.17</span><small>hoy</small></div>
      <div class="nsm-track"><div class="nsm-fill"></div><div class="nsm-target">0.40</div></div>
      <div class="nsm-goal"><span class="nsm-val">0.40+</span><small>target</small></div>
    </div>
  </div>
  {tree("NSM", ["usuarios activos","onboarding completado","ruta aceptada","skill start","cápsulas","evidencia subida","evidencia aprobada","2ª skill iniciada"])}
  {lead('Una sola palanca mueve 4 streams: empleabilidad → recomienda (baja CAC) → empresas pagan por el Skill Graph → las credenciales valen. <b>No se infla con marketing: o verificas la skill, o no.</b>')}
""")

# 38 TRACCIÓN
S("light","V · Métricas","chart",f"""
  {kicker("Tracción · snapshot")}
  {title('Demanda validada <span class="grad">antes de terminar el producto</span>')}
  <div class="statrow">
    {stat("130","Ventas acumuladas","US$ · x3 crecimiento 2024→2025", prefix="US$", suffix="K+", tone="green")}
    {stat("300","Clientes activos (90 días)","tracción reciente", tone="violet")}
    {stat("95","Alcance de comunidad","8k WhatsApp activo", suffix="K+", tone="blue")}
    {stat("14","Países con presencia","+100 alianzas · +200 expertos", tone="violet")}
  </div>
  <div class="split">
   <div class="split-l">{barchart([
     ("Ventas 2024",33,"×1","violet"),
     ("Ventas 2025",100,"×3","green"),
     ("Run-rate 2026",98,"≈US$118K","blue"),
   ])}</div>
   <div class="split-r">{note('Cifras aportadas por Alejandro para pitch · <b>pendiente conciliación</b> con contabilidad, analytics y CRM antes de due diligence. ProInnóvate Hito 1 aprobado.')}</div>
  </div>
""")

# 39 RETENCIÓN & NPS
S("light","V · Métricas","chart",f"""
  {kicker("Retención & NPS")}
  {title('Retiene <span class="grad">mejor que la media</span> — aún sin terminar')}
  <div class="split">
   <div class="split-l">{barchart([
     ("NPS de cohortes",78,"66–78","green"),
     ("Completion de cohortes",85,"71–85%","blue"),
     ("Retención W4 / M1",38,"38%","violet"),
     ("Evidence upload rate",42,"42%","green"),
   ])}</div>
   <div class="split-r">
     {lead('El loop de <b>evidencia + validación</b> es el antídoto estructural a la deserción de EdTech: el progreso profesional se <i>siente</i> real. La retención W4 (38%) ya supera el benchmark B2C (25–35%).')}
     {table(["Gap a instrumentar","Estado"],[
       ["M3 / M6 retention por cohorte","🟠 urgente"],
       ["TTFSV / TTFP en días","🟠 urgente"],
       ["Re-compra por cohortes","🟡 medir"],
     ])}
   </div>
  </div>
""")

# 40 REVENUE QUALITY
S("light","V · Métricas","split",f"""
  {kicker("Honestidad métrica")}
  {title('Lo que un analista <span class="grad">atacaría primero</span>')}
  <div class="split">
   <div class="split-l">
     {card("El problema", 'Gran parte del revenue es <b>one-time</b> (programas live). El “MRR” de $5,150 es <i>Monthly Revenue</i>, no <i>Recurring</i>. Churn ~8% en el borde alto.', tag="Revenue quality", tone="green")}
     {card("Por qué importa", 'Una empresa con MRR real vale 5–10× ese MRR; un negocio de servicios one-time, mucho menos. Diferencia de 3–7× sobre el mismo ingreso.', tag="Valuación")}
   </div>
   <div class="split-r">
     {card("El plan", bullets(["Separar y medir MRR real vs. one-time","Proyectar el bridge a suscripción","Comunicar en dos fases: live (caja) → plataforma (escala)","No reportar caja de cohortes como MRR"]), tag="Acción", tone="blue")}
   </div>
  </div>
  {quote('Mostrar el gap <span class="grad">nosotros mismos</span>, con plan, construye más confianza que esconderlo.')}
""")

# 41 COMUNIDAD & FLYWHEEL
S("light","V · Métricas","flywheel",f"""
  {kicker("Comunidad & flywheel")}
  {title('El volante: cada vuelta <span class="grad">cuesta menos y empuja más</span>')}
  <div class="fly reveal">
    <div class="fly-ring">
      <div class="fly-node n1">Contenido gratuito atrae AEC</div>
      <div class="fly-node n2">Comunidad capta leads y confianza</div>
      <div class="fly-node n3">Programas live → caja + contenido</div>
      <div class="fly-node n4">Se vuelve cápsulas, skills, evidencias</div>
      <div class="fly-node n5">Data alimenta rutas y demanda B2B</div>
      <div class="fly-node n6">Summit trae sponsors y autoridad</div>
      <div class="fly-core">AECODE<br><small>95k · 14 países</small></div>
    </div>
  </div>
  {lead('La comunidad es <b>canal, producto y moat</b>. Cada evento produce: grabación, cápsula, resumen, post, base de Q&A para el AI Hub y un CTA a diagnóstico. Ecosistema: GEN+ (ticket alto), THESIA (I+D), VisionPro (datos de obra), Summit (autoridad).')}
""")

# 42 DIFERENCIACIÓN
S("dark","VI · Defensibilidad","table",f"""
  {kicker("Diferenciación")}
  {title('Las academias certifican asistencia.<br>AECODE <span class="grad">valida capacidad</span>.')}
  {table(["Dimensión","Cursos tradicionales","AECODE"],[
   ["Unidad de valor","Curso o certificado","<b>Skill verificable</b>"],
   ["Progreso","Clases vistas","<b>Evidencia aprobada</b>"],
   ["Personalización","Temario fijo","<b>Ruta por rol + diagnóstico</b>"],
   ["Evaluación","Quiz o examen","<b>Rúbrica + entregable real</b>"],
   ["Resultado","Constancia","<b>Skill Passport</b>"],
   ["B2B","Capacitación genérica","<b>Dashboard de brechas</b>"],
  ], hi=[2])}
""")

# 43 MOAT
S("dark","VI · Defensibilidad","cards",f"""
  {kicker("Moat compuesto")}
  {title('El contenido se copia. <span class="grad">El moat, no.</span>')}
  {grid([
   card("Comunidad vertical AEC","65–95k de alcance → CAC $35 vs. $100–300.", num="01"),
   card("Skill Graph AEC","Taxonomía propietaria de roles y skills.", num="02", tone="blue"),
   card("Datos de evidencia","Grafo de habilidades reales de la región.", num="03", tone="green"),
   card("Rúbricas + feedback","Estándar de validación que se calibra.", num="04"),
   card("AI Coach contextual","Personalización sin escalar horas humanas.", num="05", tone="blue"),
   card("Ecosistema GEN+/THESIA","Casos reales que alimentan el producto.", num="06", tone="green"),
  ], 3, "cards-sm")}
  {lead('Más: <b>Summit y autoridad</b>, <b>B2B talent intelligence</b>, <b>alianzas institucionales</b> y <b>mandato Plan BIM Perú</b>. El moat está en datos, comunidad, evidencia, certificación y distribución.')}
""")

# 44 COMPETENCIA + 2x2
S("dark","VI · Defensibilidad","map",f"""
  {kicker("Panorama competitivo")}
  {title('Ser <span class="grad">profundo</span> donde todos son <span class="grad">anchos</span>')}
  <div class="split">
   <div class="split-l">{map2x2([
     (78,18,"AECODE","green",True),
     (18,72,"Coursera / Udemy","ink",False),
     (32,58,"Platzi / Crehana","ink",False),
     (60,60,"Autodesk Learning","ink",False),
     (70,74,"BIM local","ink",False),
     (14,86,"YouTube / IA","ink",False),
   ], ("Horizontal","Vertical AEC"), ("Evidencia verificable","Sin evidencia"))}</div>
   <div class="split-r">{table(["Competidor","Límite frente a AECODE"],[
     ["Coursera / Udemy","Horizontal, poca evidencia AEC"],
     ["Platzi / Crehana","Sin foco profundo AEC ni evidencia"],
     ["Maven","Sin Skill Passport AEC ni comunidad propia"],
     ["Autodesk / Procore","Vendor-specific, no ruta por rol"],
     ["BIM local","Artesanal, poca escala y data"],
   ])}</div>
  </div>
  {chip("Profundidad AEC + evidencia verificable + comunidad LATAM + IA contextualizada")}
""")

# 45 GTM
S("light","VII · Crecimiento","split",f"""
  {kicker("Go-to-Market")}
  {title('Distribución <span class="grad">antes</span> que perfección')}
  {flow([("Contenido técnico",""),("Diagnóstico gratis",""),("Reto 7 días","hot"),("1ª evidencia","hot"),("Premium",""),("B2B / equipo","win")])}
  <div class="split">
   <div class="split-l">{card("Motor orgánico (B2C)", bullets(["WhatsApp + LinkedIn (canal dominante)","Webinars y retos de 7 días","AI Construction Summit","Embajadores y referidos"]), tag="CAC bajo", tone="violet")}</div>
   <div class="split-r">{card("Expansión (B2B / B2G)", bullets(["Pilotos B2B de 30 días ligados a outcome","Training in-house + dashboards","Canal B2G vía Plan BIM Perú","Partners, gremios, universidades"]), tag="Ticket alto", tone="green")}</div>
  </div>
  {note('No escalar adquisición paga antes de mejorar activación, evidencia y retención.')}
""")

# 46 ROADMAP
S("light","VII · Crecimiento","timeline",f"""
  {kicker("Roadmap · escalabilidad · milestones")}
  {title('De cerrar el loop a <span class="grad">estándar regional</span>')}
  <div class="tl reveal">
    <div class="tl-item"><div class="tl-dot"></div><div class="tl-when">0–90 días</div><div class="tl-what">Landing skill piloto · instrumentar eventos · <b>TTFSV</b> · piloto B2B 30 días · separar MRR real.</div></div>
    <div class="tl-item"><div class="tl-dot"></div><div class="tl-when">3–6 meses</div><div class="tl-what"><b>3 rutas</b> · 30–50 cápsulas · Evidence Engine v1 · AI Coach básico · 10 instructores.</div></div>
    <div class="tl-item"><div class="tl-dot"></div><div class="tl-when">6–8 meses</div><div class="tl-what"><b>1,000+ usuarios</b> · 500+ skills con evidencia · 200+ certificados · 3+ pilotos B2B · MRR S/15k+.</div></div>
    <div class="tl-item win"><div class="tl-dot"></div><div class="tl-when">2027–2030</div><div class="tl-what">Expansión LATAM (México/Colombia) · B2B robusto · B2G · <b>referencia regional</b>.</div></div>
  </div>
  {lead('Escalar = que cada unidad vendida fortalezca margen, retención y capacidad operativa — no solo sume complejidad (principio Kaman).')}
""")

# 47 RIESGOS
S("light","VII · Crecimiento","split",f"""
  {kicker("Riesgos & mitigación")}
  {title('Los riesgos están <span class="grad">nombrados y cubiertos</span>')}
  <div class="split">
   <div class="split-l">{table(["Riesgo","Mitigación"],[
     ["Parecer academia online","Skill verificable como unidad central"],
     ["MRR inflado con one-time","Separar revenue, MRR real y cohortes"],
     ["IA sin data propia","Capturar perfiles, evidencias, rúbricas, outcomes"],
     ["Certificado débil","QR + evidencia + rúbrica + respaldo institucional"],
     ["CAC alto al escalar","Comunidad, referidos, SEO, partners antes de paid"],
     ["Sobreconstrucción","Solo features que mueven el loop F3"],
   ], hi=[0])}</div>
   <div class="split-r">{card("La herida central", 'La tesis se vuelve defendible cuando <b>una empresa usa evidencia AECODE para tomar una decisión real</b>: asignar proyecto, promover, contratar o cerrar una brecha. Hasta ese caso, la capa de evidencia es una hipótesis fuerte.', tag="El riesgo que decide", tone="green")}</div>
  </div>
""")

# 48 EQUIPO
S("dark","VIII · Cierre","cards",f"""
  {kicker("Equipo")}
  {title('Núcleo complementario con <span class="grad">ejecución técnica y comercial</span>')}
  {grid([
   card("Alejandro Palpan","CEO & Fundador. Visión, estrategia, producto, mercado y fundraising. Lidera AECODE + GEN+.", tag="Estrategia / Producto", tone="violet"),
   card("Anggie","Growth, narrativa y educación. Diseño instruccional y experiencia académica.", tag="Growth / Educación", tone="green"),
   card("Fabrizio","Producto y startup. Desarrollo web, plataforma e integraciones.", tag="Producto / Plataforma", tone="blue"),
   card("Yudely / Daniela","Tecnología y operaciones digitales · operación comercial (según fuente).", tag="Tech / Ops", tone="violet"),
  ], 4, "cards-sm")}
  {note('Equipo extendido + red de expertos AEC (BIM, IA, VDC, estructuras, datos). <b>VACÍO:</b> cap table, equity y roles legales definitivos.')}
""")

# 49 ASK
S("dark","VIII · Cierre","ask",f"""
  {kicker("El Ask")}
  {title('US$125K SAFE para cerrar la brecha <span class="grad">0.17 → 0.40</span>')}
  <div class="ask-grid reveal">
    <div class="ask-left">
      {donut([("Producto e IA",60,"#6f63e6"),("Expansión MX/CO",30,"#43d98f"),("Microlearning",10,"#6f8cff")])}
    </div>
    <div class="ask-right">
      {bullets([
        '<b>60%</b> producto / IA — AI Coach multi-agente, motor on-demand y evidence layer.',
        '<b>30%</b> expansión — entrada a México y Colombia.',
        '<b>10%</b> contenido — convertir live en microlearning reutilizable.',
      ])}
      {note('SAFE post-money · cap ~US$1.5M (rango 1.2–2.0M) · dilución 7–9%. Alternativas por audiencia: ProInnóvate (S/200k), Platanus (US$200K). <b>ASUMIDO · VALIDAR</b> con abogado y cap table.')}
    </div>
  </div>
""")

# 50 CIERRE
S("dark","VIII · Cierre","close",f"""
  <div class="cover-logo reveal"><img class="logo-dark" src="brand/assets/logos/aecode-logo-principal-fondo-oscuro.png" alt="AECODE"><img class="logo-light" src="brand/assets/logos/aecode-logo-principal-fondo-blanco.png" alt="AECODE"></div>
  {quote('No buscamos que más profesionales vean más clases.<br>Buscamos que la construcción pueda <span class="grad">saber quién sabe hacer qué</span>, con qué evidencia y con qué nivel de confianza.')}
  <div class="close-cols reveal">
    <div class="close-c"><div class="close-h">Data room</div>{bullets(["Pitch deck · one-pager · demo F3","Métricas con fuente + conciliación","Evidencias de aprendizaje + casos","Cap table · contratos · roadmap"])}</div>
    <div class="close-c"><div class="close-h">Q&amp;A rápidas</div>{bullets(["NSM 0.17 → meta 0.40","Tracción: US$130K+, ×3, 300 clientes, 14 países","Ask: US$125K SAFE → producto","Moat: vertical + evidencia + comunidad + IA"])}</div>
  </div>
  <div class="close-cta reveal">apalpan@genplusdesign.com · AECODE × GEN+ · La capa de capacidad para AEC</div>
""")

# ---------- render ----------
def render_slide(i,s):
    return (f'<section class="slide" data-base="{s["theme"]}" data-idx="{i}">'
            f'<div class="slide-inner layout-{s["layout"]}">{s["content"]}</div>'
            f'<img class="slide-mark" src="brand/assets/logos/aecode_isotipo_principal.png" alt="">'
            f'<div class="slide-foot"><span class="foot-ch">{esc(s["chapter"])}</span>'
            f'<span class="foot-n">{i+1:02d}<i>/</i>{len(SLIDES):02d}</span></div></section>')
slides_html="\n".join(render_slide(i,s) for i,s in enumerate(SLIDES))
total=len(SLIDES)
toc_items="".join(
   f'<button class="toc-item" data-go="{i}"><span class="toc-n">{i+1:02d}</span>'
   f'<span class="toc-t">{esc(s["chapter"])}</span></button>' for i,s in enumerate(SLIDES))

CSS = r"""
:root{
  --violet:#4A3AC1; --blue:#4465EE; --violet2:#6D70F9; --green:#17B14E; --lavender:#A6A7FF;
  --ease:cubic-bezier(.22,.61,.36,1); --ease-out:cubic-bezier(.16,1,.3,1);
}
.is-light{
  --bg:#F5F5F6; --bg2:#EDEBF9; --surface:#FFFFFF; --fg:#202231; --muted:#3A4065;
  --line:#C7C2EC; --card:#FFFFFF; --card-line:#E3E0F5;
  --accent:#4A3AC1; --accent2:#4465EE; --accent3:#17B14E; --ink-soft:#4A3AC1;
  --grad:linear-gradient(100deg,#4465EE,#6D12E3);
  --grad3:linear-gradient(100deg,#17B14E,#4A3AC1);
  --mesh-a:rgba(74,58,193,.10); --mesh-b:rgba(23,177,78,.10);
  --chip-bg:#EDEBF9;
}
.is-dark{
  --bg:#0E1121; --bg2:#1B1E3C; --surface:#13172F; --fg:#EEF3F8; --muted:#A2B4CB;
  --line:rgba(124,126,223,.24); --card:rgba(27,30,60,.72); --card-line:rgba(124,126,223,.32);
  --accent:#A6A7FF; --accent2:#7E97FF; --accent3:#2FD06E; --ink-soft:#C9D0F5;
  --grad:linear-gradient(100deg,#7E97FF,#9A5CFF);
  --grad3:linear-gradient(100deg,#2FD06E,#8C97DC);
  --mesh-a:rgba(74,58,193,.46); --mesh-b:rgba(23,177,78,.20);
  --chip-bg:rgba(124,126,223,.16);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:#05060f;color:#fff;overflow:hidden;font-family:Manrope,"Plus Jakarta Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.deck{position:fixed;inset:0;display:grid;place-items:center}
.stage{width:1280px;height:720px;position:relative;transform-origin:center}
.slide{position:absolute;inset:0;display:grid;place-items:center;background:var(--bg);color:var(--fg);
  opacity:0;visibility:hidden;pointer-events:none;transition:opacity .5s var(--ease);overflow:hidden}
.slide::before{content:"";position:absolute;inset:-12%;z-index:0;
  background:radial-gradient(38% 50% at 14% 12%,var(--mesh-a),transparent 70%),
             radial-gradient(44% 52% at 88% 90%,var(--mesh-b),transparent 72%)}
.slide.active{opacity:1;visibility:visible;pointer-events:auto}
.slide-inner{position:relative;z-index:2;width:100%;height:100%;padding:58px 72px 66px;
  display:flex;flex-direction:column;justify-content:center;gap:16px}
.slide-foot{position:absolute;z-index:3;left:72px;right:72px;bottom:24px;display:flex;
  justify-content:space-between;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.foot-ch{font-weight:700} .foot-n{font-variant-numeric:tabular-nums;font-weight:700}
.foot-n i{opacity:.4;font-style:normal;margin:0 3px}
.reveal{opacity:0;transform:translateY(16px);transition:opacity .55s var(--ease-out),transform .55s var(--ease-out)}
.slide.active .reveal{opacity:1;transform:none}
/* typo */
.kicker{font-weight:800;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);
  display:flex;align-items:center;gap:11px}
.kicker::before{content:"";width:30px;height:3px;border-radius:3px;background:var(--grad)}
.s-title{font-weight:800;font-size:clamp(30px,3.9vw,48px);line-height:1.03;letter-spacing:-.02em;
  text-wrap:balance;max-width:21ch}
.lead{font-size:clamp(16px,1.45vw,20px);line-height:1.5;color:var(--muted);max-width:64ch}
.lead b{color:var(--fg);font-weight:700} .lead i{font-style:italic;color:var(--accent)}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.chip{display:inline-flex;align-items:center;gap:9px;align-self:flex-start;font-size:14px;font-weight:700;
  padding:9px 17px;border-radius:100px;border:1px solid var(--card-line);background:var(--chip-bg);color:var(--fg)}
.chip::before{content:"◆";color:var(--accent3);font-size:10px}
.source{font-size:12.5px;color:var(--muted);font-style:italic;margin-top:2px}
.vnote{font-size:13.5px;line-height:1.45;color:var(--muted);padding:12px 16px;border-radius:12px;
  background:var(--bg2);border:1px dashed var(--card-line)}
.vnote b{color:var(--accent)}
/* cover */
.layout-cover,.layout-close{align-items:flex-start;justify-content:center;gap:20px}
.cover-logo img{height:52px;width:auto;display:block}
.logo-light{display:none}
.slide.is-light .logo-light{display:block} .slide.is-light .logo-dark{display:none}
.layout-close .cover-logo img{height:44px}
.slide-mark{position:absolute;top:30px;right:34px;height:30px;width:auto;z-index:3;opacity:.92;pointer-events:none}
.layout-cover .slide-mark,.layout-close .slide-mark,.layout-divider .slide-mark{display:none}
.layout-cover{padding-right:336px}
.aecodito{position:absolute;right:52px;bottom:60px;width:248px;height:auto;z-index:1;
  filter:drop-shadow(0 22px 44px rgba(74,58,193,.42));animation:float 6s var(--ease) infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-13px)}}
@media (prefers-reduced-motion:reduce){.aecodito{animation:none}}
.cover-title{font-weight:800;font-size:clamp(38px,5.4vw,70px);line-height:1.0;letter-spacing:-.03em;text-wrap:balance}
.cover-sub{font-size:clamp(16px,1.55vw,21px);color:var(--muted);max-width:60ch;line-height:1.45}
.cover-sub b{color:var(--fg)}
.cover-meta{display:flex;gap:13px;align-items:center;flex-wrap:wrap;font-size:14.5px;color:var(--fg);margin-top:4px}
.cover-meta .dot{color:var(--accent3)}
.cover-hint{font-size:13px;color:var(--muted);margin-top:8px} .cover-hint b{color:var(--accent)}
/* statement */
.layout-statement,.layout-divider{gap:24px}
.bigquote{font-weight:800;line-height:1.16;letter-spacing:-.02em;font-size:clamp(25px,3.1vw,40px);
  text-wrap:balance;max-width:26ch;border-left:4px solid var(--accent3);padding-left:28px}
.div-index{font-weight:800;font-size:clamp(58px,9vw,118px);line-height:1;color:transparent;-webkit-text-stroke:2px var(--accent);opacity:.5}
.div-title{font-weight:800;font-size:clamp(38px,5.2vw,64px);line-height:1.02;letter-spacing:-.025em}
.div-sub{font-size:clamp(16px,1.55vw,20px);color:var(--muted);max-width:56ch;line-height:1.45}
/* split */
.split{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:start;margin-top:2px}
.split-l,.split-r{display:flex;flex-direction:column;gap:14px}
/* stat */
.statrow{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
.layout-chart .statrow{margin-bottom:4px}
.stat{display:flex;flex-direction:column;gap:3px;padding:16px 18px;border-radius:15px;background:var(--card);
  border:1px solid var(--card-line)}
.stat-num{font-weight:800;line-height:1;font-size:clamp(28px,3.4vw,44px);letter-spacing:-.02em;
  font-variant-numeric:tabular-nums;display:flex;align-items:baseline;gap:1px;color:var(--accent)}
.stat-green .stat-num{color:var(--accent3)} .stat-blue .stat-num{color:var(--accent2)}
.stat-pre,.stat-suf{font-size:.5em;font-weight:700}
.stat-label{font-size:14.5px;font-weight:700;color:var(--fg);line-height:1.25}
.stat-sub{font-size:13px;color:var(--muted);line-height:1.3}
/* cards */
.grid{display:grid;gap:14px}
.grid-3{grid-template-columns:repeat(3,1fr)} .grid-4{grid-template-columns:repeat(4,1fr)}
.card{position:relative;padding:18px 18px 16px;border-radius:15px;background:var(--card);border:1px solid var(--card-line);
  display:flex;flex-direction:column;gap:8px;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;width:100%;height:3px;background:var(--accent)}
.card-green::before{background:var(--accent3)} .card-blue::before{background:var(--accent2)}
.card-num{font-weight:800;font-size:21px;color:var(--accent)}
.card-tag{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.card-green .card-tag,.card-green .card-num{color:var(--accent3)}
.card-blue .card-tag,.card-blue .card-num{color:var(--accent2)}
.card-head{font-weight:800;font-size:18px;line-height:1.2;color:var(--fg)}
.card-body{font-size:14.5px;line-height:1.45;color:var(--muted)}
.card-body b{color:var(--fg)} .card-body i{font-style:normal;color:var(--accent)}
.card-big{font-weight:800;font-size:30px;color:var(--accent);display:block;margin-bottom:1px}
.card-green .card-big{color:var(--accent3)} .card-blue .card-big{color:var(--accent2)}
.cards-sm .card-head{font-size:16.5px} .cards-sm .card-body{font-size:13.5px}
.cards-xs{gap:11px}.cards-xs .card{padding:13px 14px;gap:4px}
.cards-xs .card-head{font-size:14px}.cards-xs .card-body{font-size:12.5px}.cards-xs .card-num{font-size:16px}
.card code{font-family:ui-monospace,monospace;font-size:.86em;color:var(--accent2);line-height:1.7}
/* bullets */
.bullets{list-style:none;display:flex;flex-direction:column;gap:8px}
.bullets li{position:relative;padding-left:22px;font-size:15px;line-height:1.4;color:var(--muted)}
.bullets li b{color:var(--fg);font-weight:700} .bullets li i{font-style:normal;color:var(--accent)}
.bullets li::before{content:"";position:absolute;left:2px;top:7px;width:8px;height:8px;border-radius:2px;background:var(--accent3);transform:rotate(45deg)}
.card .bullets li{font-size:13.5px}
/* table */
.table-wrap{width:100%;border-radius:13px;border:1px solid var(--card-line);overflow:hidden}
.dt{width:100%;border-collapse:collapse;font-size:14.5px;background:var(--card)}
.dt th{font-weight:800;text-align:left;padding:11px 16px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--accent);background:var(--bg2);border-bottom:1px solid var(--card-line)}
.dt td{padding:10px 16px;border-bottom:1px solid var(--line);color:var(--muted);line-height:1.35;vertical-align:top}
.dt td b{color:var(--fg)} .dt tr:last-child td{border-bottom:none}
.dt .cell-hi{color:var(--fg);font-weight:700}
.card .dt{font-size:13px;background:transparent} .card .table-wrap{border:none}
.card .dt th{background:transparent;padding:4px 0;border:none}
.card .dt td{padding:5px 0;border-color:var(--line)}
/* barchart */
.barchart{display:flex;flex-direction:column;gap:12px;width:100%}
.bar-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5px;font-size:14px}
.bar-top span{color:var(--fg);font-weight:600} .bar-top b{color:var(--accent);font-weight:800;font-variant-numeric:tabular-nums}
.bar-track{height:11px;border-radius:100px;background:var(--bg2);overflow:hidden;border:1px solid var(--card-line)}
.bar-track i{display:block;height:100%;width:var(--w);border-radius:100px;background:var(--grad);transform:scaleX(0);transform-origin:left;transition:transform .9s var(--ease-out)}
.slide.active .bar-track i{transform:scaleX(1)}
.bar-green .bar-top b{color:var(--accent3)} .bar-green .bar-track i{background:linear-gradient(100deg,var(--green),#43d98f)}
.bar-blue .bar-top b{color:var(--accent2)} .bar-blue .bar-track i{background:linear-gradient(100deg,var(--blue),#6f8cff)}
.bar-ink .bar-top b{color:var(--muted)} .bar-ink .bar-track i{background:var(--muted);opacity:.7}
/* tss concentric */
.tss{display:flex;gap:26px;align-items:center}
.tss-rings{position:relative;width:230px;height:230px;flex:none}
.ring{position:absolute;border-radius:50%;display:grid;place-items:start center;padding-top:10px;
  font-weight:800;font-size:13px;left:50%;top:50%;transform:translate(-50%,-50%)}
.ring span{color:#fff;letter-spacing:.1em}
.ring.r0{width:230px;height:230px;background:rgba(74,58,193,.20);border:1px solid var(--violet)}
.ring.r1{width:158px;height:158px;background:rgba(68,101,238,.28);border:1px solid var(--blue)}
.ring.r2{width:88px;height:88px;background:var(--green);border:1px solid var(--green);place-items:center;padding:0}
.is-light .ring.r0 span,.is-light .ring.r1 span{color:#2a2470}
.tss-legend{display:flex;flex-direction:column;gap:12px}
.tss-leg{display:flex;gap:11px;align-items:flex-start;font-size:14px}
.tss-leg .dot{width:14px;height:14px;border-radius:4px;margin-top:3px;flex:none}
.tss-leg .d0{background:var(--violet)} .tss-leg .d1{background:var(--blue)} .tss-leg .d2{background:var(--green)}
.tss-leg b{color:var(--fg);font-weight:800} .tss-leg small{display:block;color:var(--muted);font-size:12.5px}
/* pyramid */
.pyramid{display:flex;flex-direction:column;gap:9px;align-items:center;width:100%}
.pyr-row{width:var(--w);transition:width .7s var(--ease-out)}
.pyr-band{padding:15px 20px;border-radius:12px;color:#fff;text-align:center}
.pyr-band b{display:block;font-weight:800;font-size:18px;letter-spacing:.02em}
.pyr-band span{font-size:13px;opacity:.92;line-height:1.3}
.band-violet{background:linear-gradient(100deg,#5a4ad0,#4a3ac1)}
.band-blue{background:linear-gradient(100deg,#4465ee,#3f7be0)}
.band-green{background:linear-gradient(100deg,#26b96f,#1fa9a0)}
/* flow */
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.flow-step{font-weight:700;font-size:15px;padding:11px 16px;border-radius:11px;background:var(--card);border:1px solid var(--card-line);color:var(--fg)}
.flow-step.hot{border-color:var(--accent2);color:var(--accent2);box-shadow:0 0 22px rgba(68,101,238,.18)}
.flow-step.win{background:var(--grad3);color:#fff;border:none}
.flow-arr{color:var(--accent);font-weight:800;font-size:18px;font-style:normal}
/* funnel */
.funnel{display:flex;flex-direction:column;gap:6px;align-items:center;width:100%}
.fn{width:var(--w);min-width:170px;display:flex;justify-content:space-between;align-items:center;gap:10px;
  padding:10px 18px;border-radius:9px;background:var(--card);border:1px solid var(--card-line);transition:width .7s var(--ease-out)}
.fn span{font-weight:700;font-size:14px;color:var(--fg)} .fn b{font-size:12px;color:var(--muted)}
.fn.hot{border-color:var(--accent2);background:rgba(68,101,238,.12)} .fn.hot span{color:var(--accent2)}
.fn.win{background:var(--grad3);border:none} .fn.win span,.fn.win b{color:#fff}
.fn-cap{font-weight:800;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);text-align:center;margin-top:6px}
/* nsm */
.nsm{display:flex;justify-content:center;margin:6px 0}
.nsm-gauge{display:flex;align-items:center;gap:20px;width:100%;max-width:760px}
.nsm-now,.nsm-goal{text-align:center}
.nsm-val{font-weight:800;font-size:40px;color:var(--accent);font-variant-numeric:tabular-nums;display:block}
.nsm-goal .nsm-val{color:var(--accent3)}
.nsm-now small,.nsm-goal small{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.nsm-track{flex:1;height:15px;border-radius:100px;background:var(--bg2);position:relative;overflow:hidden;border:1px solid var(--card-line)}
.nsm-fill{position:absolute;left:0;top:0;height:100%;width:0;background:var(--grad);border-radius:100px;transition:width 1.1s var(--ease-out)}
.slide.active .nsm-fill{width:42.5%}
.nsm-target{position:absolute;right:0;top:50%;transform:translateY(-50%);width:3px;height:24px;background:var(--accent3)}
/* tree */
.tree{display:flex;flex-direction:column;align-items:center;gap:0;width:100%}
.tree-root{font-weight:800;font-size:17px;color:#fff;background:var(--grad);padding:9px 26px;border-radius:10px}
.tree-line{width:2px;height:16px;background:var(--card-line)}
.tree-branches{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;border-top:2px solid var(--card-line);padding-top:14px}
.tree-node{font-size:13px;font-weight:600;color:var(--fg);background:var(--card);border:1px solid var(--card-line);padding:8px 13px;border-radius:9px;position:relative}
.tree-node::before{content:"";position:absolute;top:-14px;left:50%;width:2px;height:12px;background:var(--card-line)}
/* donut */
.donut-wrap{display:flex;align-items:center;gap:24px}
.donut{width:180px;height:180px;border-radius:50%;position:relative;flex:none}
.donut-hole{position:absolute;inset:30px;border-radius:50%;background:var(--bg)}
.donut-legend{display:flex;flex-direction:column;gap:11px}
.dn-leg{display:flex;align-items:center;gap:9px;font-size:14.5px;color:var(--muted)}
.dn-leg span{width:13px;height:13px;border-radius:4px;flex:none} .dn-leg b{color:var(--fg);font-weight:800}
/* map2x2 */
.map2x2{display:grid;grid-template-columns:18px 1fr;grid-template-rows:1fr 18px;gap:6px;width:100%;height:286px}
.mp-axis-y{grid-column:1;grid-row:1;writing-mode:vertical-rl;transform:rotate(180deg);display:flex;justify-content:space-between;align-items:center;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.mp-axis-y i{flex:1}
.mp-axis-x{grid-column:2;grid-row:2;display:flex;justify-content:space-between;align-items:center;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.mp-axis-x i{flex:1}
.mp-plane{grid-column:2;grid-row:1;position:relative;border-left:2px solid var(--card-line);border-bottom:2px solid var(--card-line);background:
  linear-gradient(var(--card-line) 1px,transparent 1px) 0 0/100% 25%,
  linear-gradient(90deg,var(--card-line) 1px,transparent 1px) 0 0/25% 100%;background-color:var(--bg2)}
.mp-dot{position:absolute;transform:translate(-50%,-50%);width:13px;height:13px;border-radius:50%;background:var(--muted)}
.mp-dot span{position:absolute;left:50%;top:130%;transform:translateX(-50%);white-space:nowrap;font-size:12px;font-weight:700;color:var(--fg)}
.mp-green{background:var(--green);box-shadow:0 0 0 6px rgba(38,185,111,.2)}
.mp-big{width:20px;height:20px} .mp-big span{font-size:13px;color:var(--accent3);font-weight:800;top:120%}
/* timeline */
.tl{display:grid;grid-template-columns:repeat(4,1fr);position:relative;margin:10px 0}
.tl::before{content:"";position:absolute;left:6%;right:6%;top:9px;height:2px;background:var(--line)}
.tl-item{position:relative;padding:0 13px;display:flex;flex-direction:column;gap:7px}
.tl-dot{width:18px;height:18px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 5px var(--bg),0 0 18px rgba(74,58,193,.4);z-index:2}
.tl-item.win .tl-dot{background:var(--accent3);box-shadow:0 0 0 5px var(--bg),0 0 18px rgba(38,185,111,.45)}
.tl-when{font-weight:800;font-size:16px;color:var(--accent)} .tl-item.win .tl-when{color:var(--accent3)}
.tl-what{font-size:13.5px;line-height:1.4;color:var(--muted)} .tl-what b{color:var(--fg)}
/* ask */
.layout-ask{gap:16px}
.ask-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:34px;align-items:center;margin-top:4px}
.ask-left{display:flex;justify-content:center}
.ask-right{display:flex;flex-direction:column;gap:14px}
.layout-ask .s-title{max-width:30ch}
/* close */
.layout-close{justify-content:center;gap:18px}
.close-cols{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:4px}
.close-h{font-weight:800;font-size:15px;color:var(--accent);letter-spacing:.04em;margin-bottom:9px;text-transform:uppercase}
.close-cta{font-weight:700;font-size:16px;color:var(--fg);margin-top:6px;padding-top:14px;border-top:1px solid var(--line)}
/* chrome */
.chrome{position:fixed;inset:0;z-index:50;pointer-events:none}
.progress{position:absolute;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--violet),var(--green));width:0;transition:width .45s var(--ease)}
.ctrl{position:absolute;bottom:20px;right:24px;display:flex;gap:8px;pointer-events:auto}
.ctrl button{width:39px;height:39px;border-radius:11px;border:1px solid rgba(255,255,255,.16);background:rgba(20,26,61,.62);
  color:#fff;backdrop-filter:blur(10px);cursor:pointer;font-size:15px;display:grid;place-items:center;transition:transform .15s,background .2s}
.ctrl button:hover{background:rgba(74,58,193,.7)} .ctrl button:active{transform:scale(.92)}
.ctrl button:focus-visible{outline:2px solid var(--green);outline-offset:2px}
.counter{position:absolute;bottom:28px;left:24px;font-weight:700;font-size:13px;letter-spacing:.1em;color:#fff;opacity:.6;
  font-variant-numeric:tabular-nums;background:rgba(20,26,61,.5);padding:7px 13px;border-radius:9px;backdrop-filter:blur(8px)}
.arrow-zone{position:fixed;top:0;bottom:0;width:13%;z-index:40;cursor:pointer}
.arrow-zone.left{left:0}.arrow-zone.right{right:0}
.toc{position:fixed;inset:0;z-index:60;background:rgba(8,10,28,.96);backdrop-filter:blur(14px);padding:54px 64px;overflow:auto;display:none}
.toc.open{display:block}
.toc h3{font-weight:800;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:#8b7df0;margin-bottom:22px}
.toc-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:9px}
.toc-item{display:flex;flex-direction:column;gap:4px;padding:12px 14px;border-radius:11px;background:rgba(30,37,78,.7);
  border:1px solid rgba(255,255,255,.08);color:#fff;cursor:pointer;text-align:left;transition:transform .15s,border-color .2s}
.toc-item:hover{transform:translateY(-3px);border-color:#43d98f}
.toc-n{font-weight:800;font-size:16px;color:#43d98f} .toc-t{font-size:12px;color:#a9b2da;line-height:1.25}
.toc-close{position:absolute;top:26px;right:36px;font-size:22px;background:none;border:none;color:#fff;cursor:pointer}
@media (prefers-reduced-motion:reduce){
  .reveal{transition:none!important;opacity:1!important;transform:none!important}
  .bar-track i,.nsm-fill,.fn,.pyr-row{transition:none!important}
  .slide.active .bar-track i{transform:scaleX(1)} .slide.active .nsm-fill{width:42.5%}
}
"""

JS = r"""
const slides=[...document.querySelectorAll('.slide')];const total=slides.length;let cur=0;
const stage=document.querySelector('.stage'),progress=document.querySelector('.progress'),
counter=document.querySelector('.counter');
let mode=localStorage.getItem('aecode-mode2')||'mix';
const reduced=matchMedia('(prefers-reduced-motion:reduce)').matches;
function applyTheme(){slides.forEach(s=>{const b=s.dataset.base,e=mode==='mix'?b:mode;
  s.classList.toggle('is-dark',e==='dark');s.classList.toggle('is-light',e==='light');});}
function fit(){stage.style.transform='scale('+Math.min(innerWidth/1280,innerHeight/720)+')';}
function countUp(s){s.querySelectorAll('[data-count]').forEach(el=>{const t=parseFloat(el.dataset.count);
  if(isNaN(t))return;const dec=(el.dataset.count.split('.')[1]||'').length,d=850,t0=performance.now();
  (function st(n){const p=Math.min((n-t0)/d,1),e=1-Math.pow(1-p,3);el.textContent=(t*e).toFixed(dec);
  p<1?requestAnimationFrame(st):el.textContent=t.toFixed(dec);})(t0);});}
function go(n){n=Math.max(0,Math.min(total-1,n));slides[cur].classList.remove('active');cur=n;
  const s=slides[cur];s.classList.add('active');
  [...s.querySelectorAll('.reveal')].forEach((el,i)=>el.style.transitionDelay=(reduced?0:Math.min(i*50,600))+'ms');
  progress.style.width=((cur+1)/total*100)+'%';
  counter.textContent=String(cur+1).padStart(2,'0')+' / '+String(total).padStart(2,'0');
  if(!reduced)countUp(s);location.hash=cur+1;}
function next(){go(cur+1)}function prev(){go(cur-1)}
addEventListener('keydown',e=>{const k=e.key.toLowerCase();
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();next()}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();prev()}
  else if(e.key==='Home')go(0);else if(e.key==='End')go(total-1);
  else if(k==='t')cycleMode();else if(k==='f')toggleFs();else if(k==='o')toggleToc();
  else if(e.key==='Escape')document.querySelector('.toc').classList.remove('open');});
function cycleMode(){mode=mode==='mix'?'dark':mode==='dark'?'light':'mix';localStorage.setItem('aecode-mode2',mode);
  applyTheme();document.querySelector('#mode-ico').textContent=mode==='mix'?'◐':mode==='dark'?'●':'○';}
function toggleFs(){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
function toggleToc(){document.querySelector('.toc').classList.toggle('open')}
document.querySelector('.left').onclick=prev;document.querySelector('.right').onclick=next;
document.querySelector('#btn-prev').onclick=prev;document.querySelector('#btn-next').onclick=next;
document.querySelector('#btn-mode').onclick=cycleMode;document.querySelector('#btn-fs').onclick=toggleFs;
document.querySelector('#btn-toc').onclick=toggleToc;document.querySelector('.toc-close').onclick=toggleToc;
document.querySelectorAll('.toc-item').forEach(b=>b.onclick=()=>{go(+b.dataset.go);toggleToc()});
let tx=0;addEventListener('touchstart',e=>tx=e.touches[0].clientX,{passive:true});
addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50)dx<0?next():prev()});
addEventListener('resize',fit);applyTheme();fit();
go(Math.max(0,(parseInt(location.hash.slice(1))||1)-1));
document.querySelector('#mode-ico').textContent=mode==='mix'?'◐':mode==='dark'?'●':'○';
"""

HTML=f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AECODE · Deck Maestro Startup</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="deck"><div class="stage">{slides_html}</div></div>
<div class="chrome"><div class="progress"></div><div class="counter">01 / {total:02d}</div>
<div class="ctrl">
<button id="btn-toc" title="Índice (O)" aria-label="Índice">☰</button>
<button id="btn-mode" title="Tema (T)" aria-label="Tema"><span id="mode-ico">◐</span></button>
<button id="btn-prev" title="Anterior (←)" aria-label="Anterior">‹</button>
<button id="btn-next" title="Siguiente (→)" aria-label="Siguiente">›</button>
<button id="btn-fs" title="Pantalla completa (F)" aria-label="Pantalla completa">⛶</button>
</div></div>
<div class="arrow-zone left"></div><div class="arrow-zone right"></div>
<div class="toc"><button class="toc-close" aria-label="Cerrar">✕</button>
<h3>Índice · {total} slides</h3><div class="toc-grid">{toc_items}</div></div>
<script>{JS}</script></body></html>"""

out=pathlib.Path(__file__).parent/"index.html"
out.write_text(HTML,encoding="utf-8")
print(f"OK -> {out} ({total} slides, {len(HTML):,} bytes)")
