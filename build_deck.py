# -*- coding: utf-8 -*-
"""
Generador del Deck Maestro AECODE Startup — v4 "Enfoque Final 10/10"
Posicionamiento: plataforma de adopción tecnológica para construcción ("aprende, aplica, construye mejor").
Design system OFICIAL AECODE (DESIGN.md): Manrope · navy #0E1121 · violeta #4A3AC1 · verde #17B14E · azul #4465EE.
Light+dark combinado, logos reales, esquemas/gráficas (barras, apiladas, TAM/SAM/SOM, donut, mapa 2x2, flywheel,
timeline), responsive con reflow móvil e interactividad (barra de capítulos, transiciones, rueda, auto-play).
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
    out='<div class="barchart reveal">'
    for r in rows:
        label,pct,disp=r[0],r[1],r[2]; tone=r[3] if len(r)>3 else "violet"
        out+=(f'<div class="bar bar-{tone}"><div class="bar-top"><span>{label}</span>'
              f'<b>{disp}</b></div><div class="bar-track"><i style="--w:{pct:.1f}%"></i></div></div>')
    return out+'</div>'

def stackbar(years, segdefs, maxtotal):
    # years: [(label, [vals], total_disp)] · segdefs: [(name,color)]
    cols=""
    for label,vals,tot in years:
        total=sum(vals); h=total/maxtotal*100
        segs=""
        for i,v in enumerate(vals):
            ph=(v/total*100) if total else 0
            segs+=f'<span class="sb-seg" style="height:{ph:.2f}%;background:{segdefs[i][1]}"></span>'
        cols+=(f'<div class="sb-col"><div class="sb-bar" style="height:{h:.1f}%">{segs}</div>'
               f'<div class="sb-tot">{tot}</div><div class="sb-lab">{label}</div></div>')
    legend="".join(f'<span class="sb-leg"><i style="background:{c}"></i>{n}</span>' for n,c in segdefs)
    return f'<div class="stackbar reveal"><div class="sb-cols">{cols}</div><div class="sb-legend">{legend}</div></div>'

def tamsamsom(items):
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

def flow(steps):
    out='<div class="flow reveal">'
    for i,(t,k) in enumerate(steps):
        out+=f'<div class="flow-step {k}">{t}</div>'
        if i<len(steps)-1: out+='<i class="flow-arr">→</i>'
    return out+'</div>'

def donut(segs):
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

def flywheel(core):
    return f'''<div class="fly reveal"><div class="fly-ring">
      <div class="fly-node n1">Comunidad atrae profesionales AEC</div>
      <div class="fly-node n2">Eventos y contenido activan demanda</div>
      <div class="fly-node n3">Live Training vende y valida temas</div>
      <div class="fly-node n4">Se vuelve cápsulas, rutas y prácticas</div>
      <div class="fly-node n5">Data de adopción mejora el producto</div>
      <div class="fly-node n6">Empresas compran B2B + expertos</div>
      <div class="fly-core">{core}</div></div></div>'''

# ---------- definición de slides ----------
SLIDES=[]
def S(theme, chapter, layout, content):
    SLIDES.append(dict(theme=theme, chapter=chapter, layout=layout, content=content))

# 01 PORTADA
S("dark","AECODE","cover",f"""
  <div class="cover-logo reveal"><img class="logo-dark" src="brand/assets/logos/aecode-logo-principal-fondo-oscuro.png" alt="AECODE"><img class="logo-light" src="brand/assets/logos/aecode-logo-principal-fondo-blanco.png" alt="AECODE"></div>
  <img class="aecodito reveal" src="brand/assets/reference/aecodito-home.png" alt="">
  <h1 class="cover-title reveal">La plataforma de<br><span class="grad">adopción tecnológica</span><br>para la construcción</h1>
  <p class="cover-sub reveal">Ayuda a profesionales y empresas AEC a aprender, aplicar y medir el uso de BIM, IA, automatización y herramientas digitales en el trabajo real. <b>Aprende · Aplica · Construye mejor.</b></p>
  <div class="cover-meta reveal"><span>Enfoque final de startup · 10/10</span><span class="dot">·</span><span>file de entendimiento avanzado</span><span class="dot">·</span><span>{datetime.date.today().strftime('%b %Y')}</span></div>
  <div class="cover-hint reveal">← → o swipe · <b>T</b> tema · <b>F</b> full · <b>O</b> índice · <b>P</b> auto · rueda del mouse</div>
""")

# 02 HOOK
S("dark","Apertura","split",f"""
  {kicker("El hook")}
  {title('No faltan cursos.<br>Falta <span class="grad">adoptar tecnología</span> en el trabajo real.')}
  <div class="split">
   <div class="split-l">
     {lead('La construcción está incorporando BIM, IA, automatización y datos. Pero la adopción <b>no avanza al ritmo que el sector necesita</b>.')}
     {bullets(["No faltan cursos.","No faltan tutoriales.","No falta información.","No falta IA."])}
   </div>
   <div class="split-r">
     {card("El problema real", 'El conocimiento está <b>disperso</b>, no estructurado por rol y desconectado de las tareas reales. Eso abre una brecha entre lo que el profesional aprende, lo que la empresa necesita y lo que el proyecto exige.', tag="La grieta", tone="green")}
     {chip("El conocimiento es commodity · adoptarlo y aplicarlo es lo escaso")}
   </div>
  </div>
""")

# 03 TESIS
S("dark","Apertura","statement",f"""
  {kicker("La tesis en una frase")}
  {quote('AECODE acelera la <span class="grad">adopción tecnológica</span> en construcción: forma talento capaz de usar BIM, IA y automatización para trabajar mejor, ahorrar tiempo y aumentar productividad.')}
  {flow([("Aprende",""),("Aplica","hot"),("Construye mejor","win")])}
  {lead('AECODE <b>no existe para vender cursos</b>. Existe para que profesionales y empresas adopten tecnología más rápido y la conviertan en mejor empleabilidad, menos retrabajo y más productividad.')}
""")

# 04 DIVIDER I
S("dark","I · Problema","divider",f"""
  <div class="div-index reveal">01</div>
  <h2 class="div-title reveal">El problema<br>que <span class="grad">sí duele</span></h2>
  <p class="div-sub reveal">La construcción necesita adoptar tecnología más rápido, pero aprende de forma dispersa, lenta y desconectada del trabajo real.</p>
""")

# 05 PROBLEMA
S("dark","I · Problema","split",f"""
  {kicker("Problema central")}
  {title('El conocimiento está <span class="grad">disperso</span>, no conectado al trabajo')}
  <div class="split">
   <div class="split-l">
     {lead('El conocimiento no siempre está estructurado por rol, ni conectado con tareas reales, ni orientado a mejorar productividad. Eso genera una brecha entre tres mundos:')}
     {bullets(["Lo que el <b>profesional</b> aprende.","Lo que la <b>empresa</b> necesita.","Lo que el <b>proyecto</b> exige."])}
   </div>
   <div class="split-r">
     {card("Cómo se mide el problema", 'Baja adopción, baja finalización, poca aplicación práctica, horas perdidas, tareas repetitivas, errores, retrabajo y falta de visibilidad del avance del equipo.', tag="Medible", tone="blue")}
   </div>
  </div>
""")

# 06 PROBLEMA SMART
S("dark","I · Problema","table",f"""
  {kicker("Formulación SMART")}
  {title('Un problema <span class="grad">específico y temporal</span>')}
  {table(["Dimensión","Formulación"],[
   ["<b>Específico</b>","Profesionales y empresas AEC deben aplicar BIM, IA y automatización en diseño, coordinación, planificación, costos y gestión."],
   ["<b>Medible</b>","Baja adopción, baja finalización, horas perdidas, tareas repetitivas, errores, retrabajo y nula visibilidad del avance."],
   ["<b>Alcanzable</b>","AECODE ya validó demanda con programas en vivo, ventas, comunidad, expertos y primeras líneas B2B y On-demand."],
   ["<b>Relevante</b>","La productividad del sector depende de que las personas adopten tecnología, no solo de que las empresas compren software."],
   ["<b>Temporal</b>","2025–2030: BIM, IA y digitalización hacen urgente la formación práctica de talento tecnológico."],
  ], hi=[0])}
""")

# 07 DOLOR POR CLIENTE
S("dark","I · Problema","cards",f"""
  {kicker("Dolor por cliente")}
  {title('Tres clientes, <span class="grad">un mismo síntoma</span>')}
  {grid([
   card("Profesional · B2C", 'Quiere ahorrar tiempo, automatizar, usar IA sin perderse y diferenciarse para mejores proyectos y salario.<br><br><b>Dolor:</b> aprende disperso y no traduce lo aprendido en valor profesional concreto.', num="01"),
   card("Empresa · B2B", 'Quiere equipos productivos, adopción real de herramientas y visibilidad del avance.<br><br><b>Dolor:</b> invierte en capacitación o tecnología, pero el equipo no cambia su forma de trabajar.', num="02", tone="green"),
   card("Proyecto", 'Necesita menos errores, menos retrabajo, mejor coordinación y procesos más automatizados.<br><br><b>Dolor:</b> la baja adopción termina afectando tiempos, costos, calidad y productividad.', num="03", tone="blue"),
  ], 3)}
""")

# 08 DIVIDER II
S("light","II · Solución","divider",f"""
  <div class="div-index reveal">02</div>
  <h2 class="div-title reveal">La solución<br>y el <span class="grad">producto</span></h2>
  <p class="div-sub reveal">No entras a ver videos. Entras a aprender herramientas, aplicar casos reales, automatizar tareas y medir tu avance.</p>
""")

# 09 SOLUCIÓN + FLUJO
S("light","II · Solución","flow",f"""
  {kicker("La solución")}
  {title('Acelera la adopción con <span class="grad">rutas prácticas + IA</span>')}
  {flow([("Diagnóstico",""),("Ruta por rol",""),("Microlearning",""),("Práctica","hot"),("Evidencia","hot"),("Progreso","win")])}
  {lead('AECODE estructura el conocimiento técnico AEC en <b>rutas por rol</b>. El profesional aprende herramientas, aplica casos reales, automatiza tareas y genera evidencia de avance. La empresa no compra capacitación: compra una forma de <b>acelerar la adopción tecnológica</b> de su equipo.')}
  {grid([
   card("Diagnóstico","Nivel actual, objetivo y brechas.", num="◆"),
   card("Práctica aplicada","Casos reales sobre tareas concretas.", num="◆", tone="blue"),
   card("Progreso medible","Evidencia y dashboard de adopción.", num="◆", tone="green"),
  ], 3, "cards-sm")}
""")

# 10 LEARNING OS
S("light","II · Solución","split",f"""
  {kicker("Cómo se combina")}
  {title('Un <span class="grad">Learning OS</span> para construcción')}
  <div class="split">
   <div class="split-l">
     {bullets(["<b>Diagnóstico</b> de nivel, objetivo y brechas.","<b>Rutas por rol</b> conectadas a tareas reales.","<b>Microlearning</b> de conceptos y herramientas.","<b>Práctica aplicada</b> con casos reales."])}
   </div>
   <div class="split-r">
     {bullets(["<b>Evidencia</b> de avance: reportes, dashboards, modelos, scripts.","<b>AI Coach</b> que diagnostica, recomienda y guía.","<b>Dashboard</b> de rutas, prácticas y adopción del equipo.","<b>Comunidad de expertos</b> del sector."])}
   </div>
  </div>
  {chip("El usuario no consume teoría: ejecuta, aplica y demuestra avance")}
""")

# 11 CATEGORÍA
S("light","II · Solución","cards",f"""
  {kicker("Categoría correcta")}
  {title('No es solo EdTech: es <span class="grad">adopción tecnológica</span>')}
  {grid([
   card("Plataforma de adopción tecnológica","La categoría más fuerte y defendible para construcción.", num="◆", tone="green"),
   card("Learning OS para construcción","Sistema operativo de aprendizaje aplicado por rol.", num="◆"),
   card("Workforce transformation","Plataforma de transformación de talento AEC en LATAM.", num="◆", tone="blue"),
  ], 3, "cards-sm")}
  {quote('Para un jurado no técnico: <span class="grad">AECODE ayuda a que profesionales y empresas de construcción adopten tecnología más rápido.</span>')}
""")

# 12 PROPUESTA DE VALOR
S("light","II · Solución","cards",f"""
  {kicker("Propuesta de valor")}
  {title('Valor claro para <span class="grad">cada actor</span>')}
  {grid([
   card("Para profesionales","Aprende BIM, IA y automatización para ahorrar tiempo, mejorar tu perfil y aplicar tecnología en proyectos reales.", num="01"),
   card("Para empresas","Capacita a tu equipo en herramientas digitales y mide su avance para acelerar adopción y productividad.", num="02", tone="green"),
   card("Para proyectos","Forma equipos capaces de reducir errores, automatizar procesos y ejecutar con más eficiencia.", num="03", tone="blue"),
   card("Para el sector","Construye talento digital para una industria más productiva, competitiva y preparada.", num="04"),
  ], 4, "cards-sm")}
""")

# 13 PRODUCTO 7 MÓDULOS
S("light","II · Solución","table",f"""
  {kicker("Producto")}
  {title('Siete módulos, <span class="grad">un sistema</span>')}
  {table(["Módulo","Función"],[
   ["<b>1 · Diagnóstico</b>","Identifica nivel actual, objetivo profesional y brechas."],
   ["<b>2 · Rutas por rol</b>","BIM, planificación, costos, coordinación, gestión, automatización, IA."],
   ["<b>3 · Microlearning</b>","Cápsulas cortas de conceptos, herramientas y procedimientos."],
   ["<b>4 · Práctica aplicada</b>","Casos reales para aplicar lo aprendido en tareas concretas."],
   ["<b>5 · Evidencia</b>","Entregables, reportes, dashboards, modelos o scripts que demuestran avance."],
   ["<b>6 · AI Coach</b>","Diagnostica, recomienda, guía, resuelve dudas y mide progreso."],
   ["<b>7 · Dashboard</b>","Rutas, avance, prácticas, evidencias y adopción del equipo."],
  ], hi=[0])}
""")

# 14 INNOVACIÓN IA
S("light","II · Solución","cards",f"""
  {kicker("Innovación · IA aplicada")}
  {title('La IA es el <span class="grad">motor</span>, no un curso más')}
  {grid([
   card("Diagnostica","Detecta nivel, rol, objetivo y brecha de cada usuario.", num="01"),
   card("Recomienda y guía","Arma la ruta, sugiere cápsulas y acompaña la práctica.", num="02", tone="blue"),
   card("Mide y da feedback","Revisa evidencias, da feedback preliminar y mide progreso real.", num="03", tone="green"),
  ], 3)}
  {lead('Ventaja compuesta: <b>más usuarios → más datos de adopción → mejores rutas y recomendaciones</b>. La IA escala personalización y acompañamiento sin escalar horas humanas, lo que protege el margen.')}
""")

# 15 ARQUITECTURA
S("dark","II · Solución","cards",f"""
  {kicker("Arquitectura del producto")}
  {title('Frontstage · Backstage · <span class="grad">IA</span>')}
  {grid([
   card("Frontstage", bullets(["Diagnóstico → ruta por rol","Dashboard personal","Skill / práctica + evidencia","Progreso y badges"]), num="◐"),
   card("Backstage", bullets(["CMS de rutas y cápsulas","Rúbricas y revisión humana","Admin analytics","Dashboard B2B por equipo"]), num="◑", tone="blue"),
   card("Capa de IA", bullets(["Diagnóstico + recomendación","AI Coach (RAG sectorial)","Feedback preliminar de evidencia","Nudges de abandono"]), num="◓", tone="green"),
  ], 3)}
  {lead('Regla de oro: <b>medir adopción y práctica aplicada</b>, no solo consumo de contenido. El control humano valida lo crítico.')}
""")

# 16 STACK
S("dark","II · Solución","table",f"""
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
     {card("Eventos mínimos del funnel", '<code>landing_view · signup_completed · onboarding_completed · route_accepted · skill_started · practice_completed · evidence_uploaded · payment_completed</code>', tag="Analytics", tone="blue")}
     {note('Mock data al inicio · analítica de eventos desde el día 1 para medir adopción y práctica.')}
   </div>
  </div>
""")

# 17 DIFERENCIACIÓN
S("dark","II · Solución","table",f"""
  {kicker("Diferenciación")}
  {title('AECODE <span class="grad">vs. todo lo demás</span>')}
  {table(["Comparación","Ellos","AECODE"],[
   ["<b>vs. Academia</b>","Vende cursos, mide asistencia, entrega contenido","Acelera adopción, mide práctica y aplicación"],
   ["<b>vs. Plataformas horizontales</b>","Enseñan de todo para todos","Se especializa en construcción"],
   ["<b>vs. ChatGPT</b>","Entrega respuestas","Entrega ruta, contexto, práctica, acompañamiento y medición"],
   ["<b>vs. Consultora</b>","Capacita proyecto por proyecto","Convierte conocimiento validado en producto escalable"],
  ], hi=[2])}
""")

# 18 DIVIDER III
S("light","III · Mercado","divider",f"""
  <div class="div-index reveal">03</div>
  <h2 class="div-title reveal">Mercado<br>y <span class="grad">por qué ahora</span></h2>
  <p class="div-sub reveal">Una vertical con alto dolor, necesidad creciente y un comprador estructural emergente.</p>
""")

# 19 POR QUÉ AHORA
S("light","III · Mercado","chart",f"""
  {kicker("Por qué ahora")}
  {title('El sector <span class="grad">dice usar IA</span>, pero casi nadie la ejecuta')}
  <div class="split">
   <div class="split-l">{barchart([
     ("Firmas AEC que “usan IA”",75,"75%","violet"),
     ("La usa de forma regular",12,"12%","blue"),
     ("Confía en su propia data",29,"29%","green"),
     ("Planea aumentar inversión en IA",94,"94%","violet"),
   ])}</div>
   <div class="split-r">
     {lead('La brecha no es de <i>tecnología</i> — es de <b>adopción y capacidad operativa</b>. Entre 2025 y 2030, la presión por BIM, IA, automatización y digitalización hace urgente formar talento práctico.')}
     {chip("El contenido se comoditiza · la adopción y la evidencia se vuelven el activo escaso")}
   </div>
  </div>
  {note('Datos del vault 2025–2026 · refrescar contra fuente oficial antes de un pitch público.')}
""")

# 20 5 VECTORES / BRECHA
S("light","III · Mercado","split",f"""
  {kicker("La presión estructural")}
  {title('Tecnología que entra, <span class="grad">talento que falta</span>')}
  <div class="split">
   <div class="split-l">
     {stat("499","Trabajadores AEC faltantes (EE.UU. 2026)","Deloitte", suffix="K")}
     {stat("77","Del capital contech fue a IA en 2025","vs. 35% en 2024", suffix="%", tone="green")}
   </div>
   <div class="split-r">
     {bullets([
       'Mercado AEC <b>gigante y subdigitalizado</b> (productividad plana 20 años).',
       'Inflexión de IA 2025–2026: de asistente a agente.',
       'El mercado contrata por <b>capacidad</b>, pero no sabe verificarla.',
       'Perú: <b>Plan BIM</b> = mandato estatal de digitalización (demanda estructural).',
     ])}
   </div>
  </div>
""")

# 21 VALIDACIÓN DE MERCADO
S("light","III · Mercado","cards",f"""
  {kicker("Validación clara de mercado")}
  {title('La demanda <span class="grad">ya paga</span>')}
  {grid([
   card('<span class="card-big">×4</span> ventas 2024 → 2025 (US$30K → US$120K).',"", tag="Crecimiento"),
   card('<span class="card-big">300</span> clientes activos en los últimos 90 días.',"", tag="Tracción", tone="green"),
   card('<span class="card-big">95K</span> de alcance de comunidad en 14 países.',"", tag="Distribución", tone="blue"),
   card('<span class="card-big">+200</span> expertos / aliados del sector.',"", tag="Red"),
   card('<span class="card-big">+100</span> alianzas activas.',"", tag="Partners", tone="green"),
   card('<span class="card-big">3</span> motores ya en marcha: Live, B2B y On-demand.',"", tag="Modelo", tone="blue"),
  ], 3, "cards-sm")}
""")

# 22 TAM/SAM/SOM
S("light","III · Mercado","tss",f"""
  {kicker("Mercado · dimensionamiento bottom-up")}
  {title('TAM / SAM / <span class="grad">SOM</span>')}
  <div class="split">
    <div class="split-l">{tamsamsom([
      ("TAM","US$360 M","1.2M usuarios × US$300/año"),
      ("SAM","US$87.5 M","350K usuarios × US$250/año"),
      ("SOM 3 años","US$2.5 M","10K clientes × US$250/año"),
    ])}</div>
    <div class="split-r">
      {lead('La meta de 3 años es ambiciosa pero defendible: <b>capturar US$2.5M es &lt;3% del SAM</b>.')}
      {chip("AECODE no necesita dominar el mercado: captura una porción de una vertical con alto dolor")}
    </div>
  </div>
""")

# 23 COMPETENCIA
S("dark","III · Mercado","map",f"""
  {kicker("Panorama competitivo")}
  {title('Ser <span class="grad">profundo</span> donde todos son <span class="grad">anchos</span>')}
  <div class="split">
   <div class="split-l">{map2x2([
     (78,18,"AECODE","green",True),
     (16,70,"Coursera / Udemy / Platzi","ink",False),
     (62,40,"Academias BIM","ink",False),
     (40,30,"Consultoras","ink",False),
     (14,86,"YouTube","ink",False),
     (34,84,"ChatGPT","ink",False),
   ], ("Horizontal","Vertical AEC"), ("Adopción + práctica","Solo contenido"))}</div>
   <div class="split-r">{table(["Competidor","Limitación"],[
     ["Coursera / Udemy / Platzi","Poca especialización AEC"],
     ["Academias BIM","Menor escalabilidad e IA"],
     ["Consultoras","Intensivo en horas humanas"],
     ["YouTube","Sin ruta ni medición"],
     ["ChatGPT","Sin estructura sectorial ni práctica"],
   ])}</div>
  </div>
  {chip("AECODE no compite por cantidad de contenido: por especialización, aplicación y adopción")}
""")

# 24 DIVIDER IV
S("dark","IV · Modelo & Finanzas","divider",f"""
  <div class="div-index reveal">04</div>
  <h2 class="div-title reveal">Modelo de negocio<br>y <span class="grad">finanzas</span></h2>
  <p class="div-sub reveal">Live valida. B2B ancla. On-demand AI escala. La historia no es solo crecimiento: es transición de mix.</p>
""")

# 25 MODELO 3 MOTORES
S("dark","IV · Modelo & Finanzas","cards",f"""
  {kicker("Modelo de negocio")}
  {title('<span class="grad">Live valida. B2B ancla. On-demand AI escala.</span>')}
  {grid([
   card("Motor 1 · B2C Live","Programas en vivo, cohortes y workshops. Genera caja, valida demanda, construye comunidad y produce contenido fuente.", num="◆"),
   card("Motor 2 · B2B","Venta a empresas, constructoras, consultoras e instituciones. Sube ticket, mejora recurrencia y conecta capacitación con productividad.", num="◆", tone="green"),
   card("Motor 3 · On-demand AI","Microlearning, suscripción, certificaciones y AI Coach. Escala con menor costo marginal, mejora margen y crea activos reutilizables.", num="◆", tone="blue"),
  ], 3)}
""")

# 26 B2B2C
S("dark","IV · Modelo & Finanzas","flow",f"""
  {kicker("Modelo B2B2C")}
  {title('<span class="grad">Empresa paga. Profesional aprende. Industria valida.</span>')}
  {flow([("Empresa impulsa y paga","hot"),("Profesional aprende y aplica",""),("Industria valida la adopción","win")])}
  {lead('La empresa gana productividad. El profesional gana empleabilidad. AECODE gana <b>mayor LTV y menor CAC relativo</b>. El producto, además, genera datos de avance, práctica y adopción que mejoran todo el sistema.')}
  {grid([
   card("Empresa","Gana productividad y adopción real.", num="◆", tone="green"),
   card("Profesional","Gana empleabilidad y mejor perfil.", num="◆"),
   card("AECODE","Gana LTV, datos y menor CAC.", num="◆", tone="blue"),
  ], 3, "cards-sm")}
""")

# 27 VENTAS POR AÑO
S("dark","IV · Modelo & Finanzas","chart",f"""
  {kicker("Tracción financiera")}
  {title('De US$30K a una meta de <span class="grad">US$420K</span>')}
  <div class="split">
   <div class="split-l">{barchart([
     ("2024 · validación inicial",7.1,"US$30K","ink"),
     ("2025 · ×4",28.6,"US$120K","violet"),
     ("2026E · diversificado",52.4,"US$220K","blue"),
     ("2027 Target con inversión",100,"US$420K","green"),
   ])}</div>
   <div class="split-r">
     {lead('AECODE ya validó que el mercado paga: pasó de US$30K (2024) a <b>US$120K (2025), ×4</b>. Proyecta US$220K en 2026 con una estructura más diversificada.')}
     {chip("El objetivo con capital: acelerar 2027 a US$420K mejorando la calidad del revenue")}
   </div>
  </div>
  {note('2027 base sin inversión ≈ US$370K. Cifras de trabajo · conciliar con contabilidad antes de due diligence.')}
""")

# 28 MIX DE INGRESOS
S("dark","IV · Modelo & Finanzas","chart",f"""
  {kicker("Mix de ingresos por modelo")}
  {title('La historia no es crecimiento: es <span class="grad">transición</span>')}
  {stackbar([
    ("2024",[30,0,0],"US$30K"),
    ("2025",[107,8,5],"US$120K"),
    ("2026E",[132,55,33],"US$220K"),
    ("2027 Target",[160,140,120],"US$420K"),
  ], [("B2C Live","#4465EE"),("B2B","#17B14E"),("On-demand AI","#6D70F9")], 420)}
  {lead('En 2024 AECODE era <b>100% B2C Live</b>. En 2026, B2B + On-demand AI representan <b>40%</b>. En 2027 Target, <b>62%</b>. Es una migración hacia líneas más escalables, rentables y defendibles.')}
""")

# 29 MÁRGENES DE CONTRIBUCIÓN
S("dark","IV · Modelo & Finanzas","chart",f"""
  {kicker("Márgenes de contribución")}
  {title('No solo más ventas: <span class="grad">mejor economía</span>')}
  <div class="split">
   <div class="split-l">{barchart([
     ("2024",35,"35.0%","ink"),
     ("2025",37,"37.0%","violet"),
     ("2026E",42.5,"42.5%","blue"),
     ("2027 Target",47.1,"47.1%","green"),
   ])}</div>
   <div class="split-r">{table(["Línea","Margen contrib.","Contrib. 2027T"],[
     ["B2C Live","35%","US$56K"],
     ["B2B","50%","US$70K"],
     ["On-demand AI","60%","US$72K"],
     ["<b>Total</b>","<b>47.1% pond.</b>","<b>US$198K</b>"],
   ], hi=[0])}</div>
  </div>
  {lead('El margen ponderado sube de <b>35% a 47.1%</b> porque el negocio migra a B2B y On-demand AI. Esa mejora de mix es lo que hace a la startup más invertible. (Margen de contribución por línea, no neto consolidado.)')}
""")

# 30 B2C LIVE 2026
S("dark","IV · Modelo & Finanzas","chart",f"""
  {kicker("Realidad reciente · B2C Live 2026")}
  {title('Caja mensual <span class="grad">probada y prudente</span>')}
  <div class="split">
   <div class="split-l">{barchart([
     ("Marzo 2026",87,"US$13K","violet"),
     ("Abril 2026",80,"US$12K","blue"),
     ("Mayo 2026",100,"US$15K","green"),
   ])}</div>
   <div class="split-r">
     {lead('El B2C Live ya genera <b>US$12K–15K mensuales</b> en meses recientes.')}
     {chip("Forecast anual B2C Live 2026 = US$132K (~US$11K/mes): prudente y defendible")}
   </div>
  </div>
""")

# 31 PRICING
S("dark","IV · Modelo & Finanzas","table",f"""
  {kicker("Pricing")}
  {title('Una escalera del <span class="grad">workshop al enterprise</span>')}
  {table(["Oferta","Rango","Objetivo"],[
   ["<b>Workshop live B2C</b>","US$40–60","Adquisición + caja"],
   ["<b>Programa / cohorte</b>","US$120–250","Ticket medio B2C"],
   ["<b>On-demand individual</b>","US$19/mes · US$180/año","Recurrencia escalable"],
   ["<b>Teams B2B2C</b>","US$12–15 usuario/mes","Recurrencia por equipo"],
   ["<b>B2B Starter (≤15)</b>","~US$3,000","Entrada empresa"],
   ["<b>B2B Growth (≤40)</b>","~US$8,000","Cuenta empresa"],
  ], hi=[0,1])}
  {note('Rangos de trabajo · validar contra histórico real de tickets antes de fundraising externo.')}
""")

# 32 DIVIDER V
S("light","V · Métricas & Growth","divider",f"""
  <div class="div-index reveal">05</div>
  <h2 class="div-title reveal">Métricas norte<br>y <span class="grad">growth</span></h2>
  <p class="div-sub reveal">No basta crecer en ventas: AECODE crece con mejor calidad de ingresos y práctica aplicada real.</p>
""")

# 33 NORTH STAR DUAL
S("light","V · Métricas & Growth","cards",f"""
  {kicker("North Star Metric")}
  {title('Dos estrellas: <span class="grad">producto y negocio</span>')}
  {grid([
   card("NSM de producto", '<b>Prácticas aplicadas completadas por mes.</b><br><br>No mide consumo pasivo: mide aplicación real. Sirve para B2C, B2B y On-demand, y conecta aprendizaje con productividad.', tag="Producto", tone="green"),
   card("NSM de negocio", '<b>% de revenue escalable (B2B + On-demand AI).</b><br><br>Mide la transformación del negocio. La meta: pasar de <b>40% (2026)</b> a <b>62% (2027 Target)</b>.', tag="Negocio", tone="blue"),
  ], 2)}
  {chip("Crecer en ventas no basta · AECODE debe crecer con mejor calidad de ingresos")}
""")

# 34 NSM POR MODELO
S("light","V · Métricas & Growth","table",f"""
  {kicker("NSM por modelo")}
  {title('Cada motor con su <span class="grad">métrica norte</span>')}
  {table(["Modelo","NSM","Métricas clave"],[
   ["<b>B2C Live</b>","Alumnos que completan una práctica final aplicable por cohorte","Seats, finalización, recompra, margen por cohorte, NPS"],
   ["<b>B2B</b>","Colaboradores activos por empresa que completan prácticas/mes","ACV, usuarios/cuenta, renovación, NRR, CAC B2B, payback"],
   ["<b>On-demand AI</b>","Usuarios que completan una práctica asistida por IA/mes","MAU, rutas, uso del AI Coach, free→pago, W4/M3, MRR/ARR"],
  ], hi=[0])}
""")

# 35 RETENCIÓN & NPS
S("light","V · Métricas & Growth","split",f"""
  {kicker("Retención & calidad")}
  {title('Objetivos de <span class="grad">retención y recurrencia</span>')}
  <div class="split">
   <div class="split-l">{table(["Métrica","Objetivo"],[
     ["Retención W4","30%–45%"],
     ["Retención M3","20%–35%"],
     ["LTV / CAC",">3"],
     ["Renovación B2B",">70%"],
     ["NRR B2B",">100%"],
   ], hi=[0])}</div>
   <div class="split-r">
     {lead('El loop de <b>práctica + evidencia + progreso visible</b> es el antídoto a la deserción: el avance se siente real.')}
     {note('Métricas recurrentes (MRR/ARR, CAC por canal, cohortes) aún inmaduras. La inversión las consolida. Hoy se reporta ventas, run-rate y contribución por línea — no se infla recurrencia.')}
   </div>
  </div>
""")

# 36 GROWTH METRICS
S("light","V · Métricas & Growth","chart",f"""
  {kicker("Métricas de growth")}
  {title('No empezamos desde <span class="grad">tráfico frío</span>')}
  <div class="statrow">
    {stat("95","Alcance de comunidad","8k WhatsApp activo", suffix="K+", tone="blue")}
    {stat("14","Países con presencia","alcance regional", tone="violet")}
    {stat("300","Clientes activos (90 días)","tracción reciente", tone="green")}
    {stat("200","Expertos / aliados","+100 alianzas", suffix="+", tone="violet")}
  </div>
  {lead('La ventaja de AECODE es que parte de <b>comunidad, autoridad sectorial y contenido validado</b>. La inversión debe mejorar el sistema de conversión, retención y monetización — no crear demanda desde cero.')}
""")

# 37 GTM
S("light","V · Métricas & Growth","flow",f"""
  {kicker("Go-to-Market")}
  {title('Un canal <span class="grad">natural y barato</span>')}
  {flow([("Comunidad","hot"),("Live Training",""),("Microlearning",""),("B2B","hot"),("Expansión LATAM","win")])}
  <div class="split">
   <div class="split-l">{bullets([
     '<b>Comunidad vertical</b> (+95K, 14 países) = adquisición, validación y distribución.',
     '<b>Contenido y eventos</b>: webinars, talleres y charlas activan demanda.',
     '<b>Live Training</b> convierte demanda y valida qué temas pagan.',
   ])}</div>
   <div class="split-r">{bullets([
     '<b>Microlearning</b> convierte cursos exitosos en rutas reutilizables.',
     '<b>B2B2C</b> entra a empresas, sube ticket y retención.',
     '<b>Expansión LATAM</b> vía comunidad, expertos, alianzas e instituciones.',
   ])}</div>
  </div>
  {chip("Comunidad baja CAC · Live valida · B2B sube ticket · On-demand AI escala margen")}
""")

# 38 COMUNIDAD & FLYWHEEL
S("light","V · Métricas & Growth","flywheel",f"""
  {kicker("Comunidad & flywheel")}
  {title('La comunidad es <span class="grad">canal, producto y moat</span>')}
  {flywheel('AECODE<br><small>95k · 14 países</small>')}
  {lead('Cada evento produce grabación, cápsula, resumen, post, base de Q&A para el AI Hub y un CTA a diagnóstico. La comunidad reduce CAC, valida temas y alimenta el producto con datos de adopción.')}
""")

# 39 MOAT
S("dark","VI · Defensibilidad","cards",f"""
  {kicker("Moat compuesto")}
  {title('El contenido se copia. <span class="grad">El moat, no.</span>')}
  {grid([
   card("Comunidad vertical AEC","+95K en 14 países → CAC bajo.", num="01"),
   card("Red de expertos","+200 especialistas del sector.", num="02", tone="blue"),
   card("Programas validados","Vendidos y probados con demanda real.", num="03", tone="green"),
   card("Rutas por rol + casos reales","Conocimiento estructurado y aplicado.", num="04"),
   card("Data de habilidades AEC","Avance, práctica y adopción propietarios.", num="05", tone="blue"),
   card("IA especializada + B2B2C","Contexto sectorial y modelo de distribución.", num="06", tone="green"),
  ], 3, "cards-sm")}
  {lead('Más: <b>marca sectorial</b> y la <b>conversión de cursos en activos digitales</b> reutilizables. El moat está en la combinación de comunidad, data, expertos, producto, distribución y especialización.')}
""")

# 40 DIVIDER VII
S("dark","VII · Inversión","divider",f"""
  <div class="div-index reveal">06</div>
  <h2 class="div-title reveal">La inversión<br>y el <span class="grad">impacto</span></h2>
  <p class="div-sub reveal">El capital no financia una idea: financia convertir una operación validada en plataforma escalable.</p>
""")

# 41 USO DE CAPITAL
S("dark","VII · Inversión","ask",f"""
  {kicker("Uso de capital")}
  {title('US$125K para escalar la <span class="grad">plataforma</span>')}
  <div class="ask-grid reveal">
    <div class="ask-left">{donut([("IA + plataforma",60,"#6D70F9"),("Growth LATAM / B2B2C",30,"#17B14E"),("Microlearning",10,"#4465EE")])}</div>
    <div class="ask-right">
      {bullets([
        '<b>60% · US$75K</b> — AI Coach, rutas, dashboard, evidencia y analytics.',
        '<b>30% · US$37.5K</b> — adquisición, alianzas y ventas B2B (LATAM).',
        '<b>10% · US$12.5K</b> — cápsulas, prácticas y rutas reutilizables.',
      ])}
      {note('Instrumento tipo SAFE o capital semilla estratégico. Alternativas por audiencia: ProInnóvate, angels, clientes B2B.')}
    </div>
  </div>
""")

# 42 IMPACTO DEL CAPITAL
S("dark","VII · Inversión","table",f"""
  {kicker("Impacto esperado del capital")}
  {title('Cinco variables que <span class="grad">se mueven juntas</span>')}
  {table(["Métrica","2026E","2027 Target"],[
   ["Revenue total","US$220K","<b>US$420K</b>"],
   ["B2B + On-demand","40%","<b>62%</b>"],
   ["Margen de contribución ponderado","42.5%","<b>47.1%</b>"],
   ["Contribución estimada","US$93.5K","<b>US$198K</b>"],
   ["Dependencia de Live","60%","<b>38%</b>"],
   ["On-demand AI","15%","<b>29%</b>"],
  ], hi=[2])}
  {chip("Más revenue · más B2B · más On-demand · más margen · menos dependencia de Live")}
""")

# 43 EQUIPO
S("dark","VII · Inversión","split",f"""
  {kicker("Equipo")}
  {title('+12 personas que <span class="grad">ya ejecutaron</span>')}
  <div class="split">
   <div class="split-l">
     {bullets([
       'Producto · desarrollo full stack · sistemas · data.',
       'Automatización e inteligencia artificial.',
       'Estrategia comercial · business development.',
       'Marketing · growth · coordinación académica.',
       'Administración · finanzas · soporte operativo.',
     ])}
   </div>
   <div class="split-r">
     {quote('No es un equipo con intención: ya construyó comunidad, vendió programas y <span class="grad">creció ×4</span> de 2024 a 2025.')}
     {lead('La pregunta no es si pueden vender. Ya vendieron. Es si pueden convertir esa tracción en <b>plataforma escalable</b> — y la inversión está diseñada para eso.')}
   </div>
  </div>
""")

# 44 RIESGOS
S("dark","VII · Inversión","table",f"""
  {kicker("Riesgos & mitigación")}
  {title('Riesgos <span class="grad">nombrados y cubiertos</span>')}
  {table(["Riesgo","Mitigación"],[
   ["Ser percibidos como academia","Posicionamiento como plataforma de adopción tecnológica"],
   ["Dependencia de Live Training","Migración a B2B y On-demand AI"],
   ["CAC alto","Comunidad vertical + B2B2C + referidos"],
   ["Baja retención","Rutas, prácticas, AI Coach, progreso visible"],
   ["Competidores horizontales","Especialización AEC y casos reales"],
   ["Métricas recurrentes inmaduras","Separar ventas, run-rate y ARR real"],
  ], hi=[0])}
""")

# 45 EVALUACIÓN JURADO
S("light","VII · Inversión","cards",f"""
  {kicker("Evaluación · jurado de aceleradora")}
  {title('Seis criterios, <span class="grad">10/10</span>')}
  {grid([
   card("Problema y solución","Claro y alineado: adopción tecnológica con rutas, IA y evidencia.", num="10", tone="green"),
   card("Valor e innovación","Plataforma vertical con IA, comunidad y B2B2C — no solo cursos.", num="10"),
   card("Validación / tracción","Ventas, ×4, clientes activos, comunidad, expertos, alianzas.", num="10", tone="blue"),
   card("Modelo y escalabilidad","Live valida · B2B ancla · On-demand AI escala margen.", num="10", tone="green"),
   card("Equipo y ejecución","Multidisciplinario y con resultados probados.", num="10"),
   card("Presentación","Narrativa que conecta IA, productividad, mercado e inversión.", num="10", tone="blue"),
  ], 3, "cards-sm")}
""")

# 46 EVALUACIÓN INVERSIONISTA
S("light","VII · Inversión","split",f"""
  {kicker("Evaluación · inversionista")}
  {title('Atractivo hoy, <span class="grad">más invertible</span> mañana')}
  <div class="split">
   <div class="split-l">
     {card("Lo que atrae", bullets(["Ya hay ventas y crecimiento probado","Comunidad vertical y mercado especializado","El mix mejora margen con el tiempo","Uso de capital claro y equipo que ejecutó"]), tag="Fortalezas", tone="green")}
   </div>
   <div class="split-r">
     {card("Lo que debe madurar", bullets(["MRR / ARR reales","CAC por canal · LTV por línea","Retención por cohortes · NRR","Dashboard financiero mensual"]), tag="A construir", tone="blue")}
   </div>
  </div>
  {quote('Hoy no inflamos métricas recurrentes. Reportamos ventas, run-rate y contribución por línea. La inversión construye la capa de plataforma, IA y suscripción para subir ARR real, retención y escalabilidad.')}
""")

# 47 RESUMEN EJECUTIVO
S("light","VII · Inversión","chart",f"""
  {kicker("Resumen ejecutivo · una mirada")}
  {title('Por qué AECODE es <span class="grad">atractiva para semilla</span>')}
  <div class="statrow">
    {stat("4","Crecimiento 2024 → 2025","US$30K → US$120K", prefix="×", tone="green")}
    {stat("220","Revenue proyectado 2026E","US$ miles", prefix="US$", suffix="K", tone="violet")}
    {stat("62","Revenue escalable 2027 Target","B2B + On-demand AI", suffix="%", tone="blue")}
    {stat("125","Ask · SAFE / semilla","60% IA · 30% growth · 10% contenido", prefix="US$", suffix="K", tone="green")}
  </div>
  {lead('Demanda validada con ventas · comunidad regional · equipo completo · modelo híbrido que mejora margen · ruta clara a mayor escalabilidad. <b>La inversión convierte una operación validada en plataforma vertical.</b>')}
""")

# 48 CIERRE
S("dark","VIII · Cierre","close",f"""
  <div class="cover-logo reveal"><img class="logo-dark" src="brand/assets/logos/aecode-logo-principal-fondo-oscuro.png" alt="AECODE"><img class="logo-light" src="brand/assets/logos/aecode-logo-principal-fondo-blanco.png" alt="AECODE"></div>
  {quote('AECODE está migrando de una operación educativa validada hacia una <span class="grad">plataforma vertical de adopción tecnológica</span> para la construcción en LATAM.')}
  <div class="close-cols reveal">
    <div class="close-c"><div class="close-h">Esta migración mejora</div>{bullets(["Crecimiento","Margen de contribución","Escalabilidad"])}</div>
    <div class="close-c"><div class="close-h">El ask</div>{bullets(["US$125K SAFE / semilla","60% IA + plataforma","Tracción: ×4, 300 clientes, 14 países"])}</div>
  </div>
  <div class="close-cta reveal">AECODE: aprende, aplica, construye mejor · apalpan@genplusdesign.com</div>
""")

# ---------- render ----------
def render_slide(i,s):
    return (f'<section class="slide" data-base="{s["theme"]}" data-ch="{esc(s["chapter"])}" data-idx="{i}">'
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
  opacity:0;visibility:hidden;pointer-events:none;transition:opacity .5s var(--ease),transform .55s var(--ease-out);overflow:hidden}
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
.grid-2{grid-template-columns:repeat(2,1fr)} .grid-3{grid-template-columns:repeat(3,1fr)} .grid-4{grid-template-columns:repeat(4,1fr)}
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
/* stackbar */
.stackbar{display:flex;flex-direction:column;gap:16px;width:100%}
.sb-cols{display:flex;align-items:flex-end;justify-content:space-around;gap:18px;height:226px;padding:0 6px;border-bottom:2px solid var(--card-line)}
.sb-col{flex:1;max-width:120px;display:flex;flex-direction:column;align-items:center;gap:7px;height:100%;justify-content:flex-end}
.sb-bar{width:60px;border-radius:8px 8px 0 0;overflow:hidden;display:flex;flex-direction:column-reverse;
  transform:scaleY(0);transform-origin:bottom;transition:transform .85s var(--ease-out)}
.slide.active .sb-bar{transform:scaleY(1)}
.sb-seg{width:100%;display:block}
.sb-tot{font-weight:800;font-size:15px;color:var(--fg);font-variant-numeric:tabular-nums}
.sb-lab{font-size:12.5px;font-weight:700;color:var(--muted);letter-spacing:.03em}
.sb-legend{display:flex;gap:20px;justify-content:center;flex-wrap:wrap}
.sb-leg{display:flex;align-items:center;gap:7px;font-size:13.5px;color:var(--muted);font-weight:600}
.sb-leg i{width:13px;height:13px;border-radius:4px}
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
/* flow */
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.flow-step{font-weight:700;font-size:15px;padding:11px 16px;border-radius:11px;background:var(--card);border:1px solid var(--card-line);color:var(--fg)}
.flow-step.hot{border-color:var(--accent2);color:var(--accent2);box-shadow:0 0 22px rgba(68,101,238,.18)}
.flow-step.win{background:var(--grad3);color:#fff;border:none}
.flow-arr{color:var(--accent);font-weight:800;font-size:18px;font-style:normal}
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
/* flywheel */
.fly{display:flex;justify-content:center;margin:4px 0}
.fly-ring{position:relative;width:560px;height:286px}
.fly-core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:128px;height:128px;border-radius:50%;
  display:grid;place-items:center;text-align:center;font-weight:800;font-size:17px;color:#fff;
  background:radial-gradient(circle,#6D70F9,#4A3AC1);box-shadow:0 0 50px rgba(74,58,193,.45)}
.fly-core small{font-weight:600;font-size:11px;opacity:.85}
.fly-node{position:absolute;font-size:12.5px;font-weight:600;line-height:1.25;width:170px;padding:9px 13px;border-radius:10px;
  background:var(--card);border:1px solid var(--card-line);color:var(--fg)}
.fly-node.n1{left:0;top:-4px}.fly-node.n2{right:0;top:-4px;text-align:right}
.fly-node.n3{right:-16px;top:46%;transform:translateY(-50%);text-align:right}
.fly-node.n4{right:0;bottom:-4px;text-align:right}.fly-node.n5{left:0;bottom:-4px}
.fly-node.n6{left:-16px;top:46%;transform:translateY(-50%)}
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
/* ---- interactividad ---- */
.card,.stat{transition:transform .2s var(--ease),box-shadow .25s,border-color .25s}
.slide.active .card:hover,.slide.active .stat:hover{transform:translateY(-4px);border-color:var(--accent);box-shadow:0 16px 34px rgba(8,10,30,.22)}
.flow-step,.tree-node{transition:transform .18s var(--ease),border-color .2s}
.slide.active .flow-step:hover{transform:translateY(-2px);border-color:var(--accent2)}
/* barra segmentada por capítulo */
.segbar{position:absolute;top:0;left:0;right:0;height:6px;display:flex;gap:2px;pointer-events:auto}
.seg{flex:var(--c) 1 0;height:5px;align-self:flex-start;background:rgba(140,151,220,.24);position:relative;cursor:pointer;
  transition:height .2s,background .25s}
.seg:hover,.seg.cur{height:8px;background:rgba(140,151,220,.4)}
.seg i{position:absolute;left:0;top:0;height:100%;width:var(--f,0%);background:linear-gradient(90deg,#4465EE,#17B14E);transition:width .45s var(--ease)}
.seg .lab{position:absolute;top:12px;left:0;font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
  color:#e7eaff;background:rgba(14,17,33,.94);border:1px solid rgba(124,126,223,.4);padding:4px 9px;border-radius:7px;white-space:nowrap;
  opacity:0;transform:translateY(-4px);transition:opacity .2s,transform .2s;pointer-events:none;z-index:6}
.seg:hover .lab{opacity:1;transform:none}
#btn-play.playing{background:rgba(74,58,193,.85);color:#fff;box-shadow:0 0 18px rgba(124,126,223,.6)}
/* ---- responsive móvil (reflow real) ---- */
body.mobile .deck{place-items:stretch}
body.mobile .stage{width:100vw;height:100dvh;transform:none!important}
body.mobile .slide{display:block;overflow-y:auto;overflow-x:hidden;-webkit-overflow-scrolling:touch}
body.mobile .slide-inner{position:static;height:auto;min-height:100%;justify-content:flex-start;
  padding:56px clamp(18px,5.5vw,30px) 82px;gap:clamp(13px,3.4vw,20px)}
body.mobile .slide-foot{left:clamp(18px,5.5vw,30px);right:clamp(18px,5.5vw,30px);bottom:18px}
body.mobile .slide-mark{top:18px;right:18px;height:24px}
body.mobile .split,body.mobile .ask-grid,body.mobile .grid-2,body.mobile .grid-3,body.mobile .grid-4,
body.mobile .tss,body.mobile .donut-wrap{display:flex;flex-direction:column;gap:13px}
body.mobile .statrow{grid-template-columns:1fr 1fr}
body.mobile .s-title{font-size:clamp(24px,6.6vw,34px);max-width:none}
body.mobile .cover-title{font-size:clamp(29px,8.4vw,44px)}
body.mobile .div-title{font-size:clamp(32px,8.4vw,52px)}
body.mobile .bigquote{font-size:clamp(21px,5.6vw,30px);max-width:none}
body.mobile .lead,body.mobile .div-sub,body.mobile .cover-sub{font-size:clamp(15px,3.9vw,18px);max-width:none}
body.mobile .layout-cover{padding-right:clamp(18px,5.5vw,30px)}
body.mobile .aecodito{position:static;width:158px;align-self:center;margin:4px 0 0;animation:none}
body.mobile .table-wrap{overflow-x:auto} body.mobile .dt{min-width:480px}
body.mobile .tss-rings{margin:0 auto} body.mobile .fly{overflow:hidden}
body.mobile .fly-ring{transform:scale(.6);margin:-60px auto}
body.mobile .map2x2{height:230px}
body.mobile .flow{justify-content:center}
body.mobile .stackbar{overflow-x:auto} body.mobile .sb-cols{gap:10px;height:194px} body.mobile .sb-bar{width:44px}
body.mobile .ctrl{bottom:14px;right:11px;gap:7px} body.mobile .ctrl button{width:42px;height:42px}
body.mobile .counter{bottom:18px;left:11px} body.mobile .arrow-zone{display:none}
body.mobile .donut{width:150px;height:150px} body.mobile .donut-hole{inset:26px}
body.mobile .toc{padding:48px 22px} body.mobile .toc-grid{grid-template-columns:repeat(2,1fr)}
@media (prefers-reduced-motion:reduce){
  .reveal{transition:none!important;opacity:1!important;transform:none!important}
  .slide{transition:opacity .2s!important}
  .bar-track i,.nsm-fill,.fn,.sb-bar,.seg i{transition:none!important}
  .slide.active .bar-track i{transform:scaleX(1)} .slide.active .sb-bar{transform:scaleY(1)}
}
"""

JS = r"""
const slides=[...document.querySelectorAll('.slide')];const total=slides.length;let cur=0;
const stage=document.querySelector('.stage'),counter=document.querySelector('.counter'),segbar=document.querySelector('#segbar');
let mode=localStorage.getItem('aecode-mode2')||'mix';
const reduced=matchMedia('(prefers-reduced-motion:reduce)').matches;
// capítulos -> barra segmentada
const chapters=[];
slides.forEach((s,i)=>{const c=s.dataset.ch,last=chapters[chapters.length-1];
  if(last&&last.name===c){last.count++}else{chapters.push({name:c,start:i,count:1})}});
chapters.forEach(ch=>{const seg=document.createElement('div');seg.className='seg';seg.style.setProperty('--c',ch.count);
  seg.innerHTML='<i></i><span class="lab">'+ch.name+'</span>';
  seg.title=ch.name;seg.onclick=()=>{stopPlay();go(ch.start)};segbar.appendChild(seg);
  ch.el=seg;ch.fill=seg.querySelector('i');});
function updateSeg(){chapters.forEach(ch=>{const endEx=ch.start+ch.count;let f=0;
  if(cur>=endEx)f=100;else if(cur<ch.start)f=0;else f=((cur-ch.start+1)/ch.count)*100;
  ch.fill.style.width=f+'%';ch.el.classList.toggle('cur',cur>=ch.start&&cur<endEx);});}
function applyTheme(){slides.forEach(s=>{const b=s.dataset.base,e=mode==='mix'?b:mode;
  s.classList.toggle('is-dark',e==='dark');s.classList.toggle('is-light',e==='light');});}
function isMobile(){return matchMedia('(max-width:820px),(orientation:portrait) and (max-width:1024px)').matches}
function fit(){if(isMobile()){document.body.classList.add('mobile');stage.style.transform='none';}
  else{document.body.classList.remove('mobile');stage.style.transform='scale('+Math.min(innerWidth/1280,innerHeight/720)+')';}}
function countUp(s){s.querySelectorAll('[data-count]').forEach(el=>{const t=parseFloat(el.dataset.count);
  if(isNaN(t))return;const dec=(el.dataset.count.split('.')[1]||'').length,d=850,t0=performance.now();
  (function st(n){const p=Math.min((n-t0)/d,1),e=1-Math.pow(1-p,3);el.textContent=(t*e).toFixed(dec);
  p<1?requestAnimationFrame(st):el.textContent=t.toFixed(dec);})(t0);});}
function go(n){n=Math.max(0,Math.min(total-1,n));if(n===cur&&slides[cur].classList.contains('active')){countUp(slides[cur]);return}
  const dir=n>cur?1:-1,mob=document.body.classList.contains('mobile');
  const out=slides[cur];out.classList.remove('active');
  if(!reduced&&!mob)out.style.transform='translateX('+(-dir*34)+'px)';
  cur=n;const s=slides[cur];
  if(!reduced&&!mob){s.style.transition='none';s.style.transform='translateX('+(dir*34)+'px)';void s.offsetWidth;s.style.transition='';}
  s.classList.add('active');s.style.transform='';if(mob)s.scrollTop=0;
  [...s.querySelectorAll('.reveal')].forEach((el,i)=>el.style.transitionDelay=(reduced?0:Math.min(i*48,560))+'ms');
  counter.textContent=String(cur+1).padStart(2,'0')+' / '+String(total).padStart(2,'0');
  updateSeg();if(!reduced)countUp(s);location.hash=cur+1;}
function next(){go(cur+1)}function prev(){go(cur-1)}
addEventListener('keydown',e=>{const k=e.key.toLowerCase();
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();stopPlay();next()}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();stopPlay();prev()}
  else if(e.key==='Home'){stopPlay();go(0)}else if(e.key==='End'){stopPlay();go(total-1)}
  else if(k==='t')cycleMode();else if(k==='f')toggleFs();else if(k==='o')toggleToc();else if(k==='p')togglePlay();
  else if(e.key==='Escape')document.querySelector('.toc').classList.remove('open');});
let wlock=false;
addEventListener('wheel',e=>{if(document.body.classList.contains('mobile')||wlock)return;
  const d=Math.abs(e.deltaY)>=Math.abs(e.deltaX)?e.deltaY:e.deltaX;if(Math.abs(d)<26)return;
  wlock=true;setTimeout(()=>wlock=false,720);stopPlay();d>0?next():prev();},{passive:true});
function cycleMode(){mode=mode==='mix'?'dark':mode==='dark'?'light':'mix';localStorage.setItem('aecode-mode2',mode);
  applyTheme();document.querySelector('#mode-ico').textContent=mode==='mix'?'◐':mode==='dark'?'●':'○';}
function toggleFs(){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
function toggleToc(){document.querySelector('.toc').classList.toggle('open')}
let timer=null;
function setPlay(p){const b=document.querySelector('#btn-play');b.classList.toggle('playing',p);
  b.querySelector('#play-ico').textContent=p?'❚❚':'▶';}
function togglePlay(){timer?stopPlay():(timer=setInterval(()=>{cur>=total-1?stopPlay():next()},7000),setPlay(true));}
function stopPlay(){if(timer){clearInterval(timer);timer=null;setPlay(false);}}
document.querySelector('.left').onclick=()=>{stopPlay();prev()};
document.querySelector('.right').onclick=()=>{stopPlay();next()};
document.querySelector('#btn-prev').onclick=()=>{stopPlay();prev()};
document.querySelector('#btn-next').onclick=()=>{stopPlay();next()};
document.querySelector('#btn-mode').onclick=cycleMode;document.querySelector('#btn-fs').onclick=toggleFs;
document.querySelector('#btn-toc').onclick=toggleToc;document.querySelector('#btn-play').onclick=togglePlay;
document.querySelector('.toc-close').onclick=toggleToc;
document.querySelectorAll('.toc-item').forEach(b=>b.onclick=()=>{stopPlay();go(+b.dataset.go);toggleToc()});
let tx=0,ty=0;addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY},{passive:true});
addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;
  if(Math.abs(dx)>55&&Math.abs(dx)>Math.abs(dy)*1.4){stopPlay();dx<0?next():prev()}});
let rt;addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(fit,120)});
applyTheme();fit();go(Math.max(0,(parseInt(location.hash.slice(1))||1)-1));
document.querySelector('#mode-ico').textContent=mode==='mix'?'◐':mode==='dark'?'●':'○';
"""

HTML=f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AECODE · Deck Maestro Startup</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="deck"><div class="stage">{slides_html}</div></div>
<div class="chrome"><div class="segbar" id="segbar"></div><div class="counter">01 / {total:02d}</div>
<div class="ctrl">
<button id="btn-toc" title="Índice (O)" aria-label="Índice">☰</button>
<button id="btn-play" title="Auto-play (P)" aria-label="Auto-play"><span id="play-ico">▶</span></button>
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
