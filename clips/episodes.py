"""
Serie «Historias de la IA» — AECODE.

Cada escena tiene:
  say   -> lo que dice la voz (y lo que MoneyPrinterTurbo usa para los subtítulos)
  type  -> plantilla visual de engine/stage.html
  resto -> datos de la plantilla. `*texto*` resalta con el gradiente AECODE.

Marcas de tiempo en datos: "c2" = cuando empieza la cláusula 2 de la escena
(las cláusulas se cortan en comas/puntos, igual que los subtítulos de MPT).
"""

SERIES = "Historias de la IA"
TOTAL = 3

# Cómo pronunciar palabras que el fonetizador en español lee mal.
# Solo afecta al audio: los subtítulos conservan la ortografía original.
LEXICON = {
    "AECODE": "a e cod",
    "IA": "i a",
    "ChatGPT": "chat ge pe te",
    "McCarthy": "Mac Carti",
    "Shannon": "Shánon",
    "Rochester": "Róchester",
    "Rockefeller": "Rókefeler",
    "Dartmouth": "Dártmuz",
    "AlphaGo": "Alfa Go",
    "DeepMind": "Dip Maind",
    "Lee Sedol": "Li Sedol",
    "Lee": "Li",
    "Attention Is All You Need": "Aténshon is ol iu nid",
    "All You Need Is Love": "Ol iu nid is lav",
    "Beatles": "Bítels",
    "Transformer": "Transfórmer",
    "Google": "Gúgol",
    "OpenAI": "Open ei ai",
    "Noam Shazeer": "Noam Shasír",
    "paper": "péiper",
    "13 500": "trece mil quinientos",
    "7 500": "siete mil quinientos",
    "10 000": "diez mil",
}

EPISODES = [
    # ------------------------------------------------------------------ EP 01
    dict(
        slug="ep01-el-verano-que-invento-la-ia",
        number=1,
        title="El verano que inventó la IA",
        next_title="La jugada 37",
        scenes=[
            dict(
                type="hook",
                say="En 1956, diez científicos creyeron que resolverían la inteligencia artificial en un solo verano.",
                kicker="1956 · Dartmouth College",
                headline="Resolver la IA en *un solo verano*",
            ),
            dict(
                type="rewind",
                say="Este 2026 se cumplen 70 años de aquel taller en Dartmouth, el evento que fundó la IA.",
                label="Este año se cumplen",
                counter_from=2026,
                counter_to=1956,
                badge="70 años",
                caption="Dartmouth Summer Research Project on Artificial Intelligence",
            ),
            dict(
                type="people",
                say="Lo propusieron McCarthy, Minsky, Rochester y Shannon. Y bautizaron el campo: inteligencia artificial.",
                people=[
                    ["John McCarthy", "Dartmouth College"],
                    ["Marvin Minsky", "Harvard"],
                    ["Nathaniel Rochester", "IBM"],
                    ["Claude Shannon", "Bell Labs"],
                ],
                term="Artificial Intelligence",
                term_note="Término acuñado en la propuesta · 31 ago 1955",
                term_at="c4",
            ),
            dict(
                type="stats",
                say="El plan: dos meses, diez personas y 13 500 dólares. La Fundación Rockefeller aprobó 7 500.",
                title="El plan",
                stats=[
                    ["2", "meses", "c1"],
                    ["10", "personas", "c2"],
                    ["US$ 13 500", "solicitados", "c2+1.1"],
                ],
                strike=["US$ 7 500", "aprobados por la Fundación Rockefeller", "c3"],
            ),
            dict(
                type="quote",
                say="Su apuesta: un avance significativo si un grupo selecto trabajaba junto durante un verano.",
                quote="A significant advance can be made… if a carefully selected group of scientists work on it together for a summer.",
                translation="Un avance significativo… si un grupo selecto trabaja junto durante un verano.",
                source="Propuesta de Dartmouth · 1955",
            ),
            dict(
                type="statement",
                say="70 años después, ese verano sigue.",
                text="70 años después,<br>*ese verano sigue.*",
            ),
            dict(
                type="curves",
                say="La lección: sobreestimamos lo que una tecnología hace en un año, y subestimamos lo que hace en diez.",
                label="La lección · Ley de Amara",
                short="1 año: sobreestimamos",
                long="10 años: subestimamos",
            ),
            dict(
                type="cta",
                say="Sigue a AECODE. Próxima historia: la jugada 37.",
            ),
        ],
    ),
    # ------------------------------------------------------------------ EP 02
    dict(
        slug="ep02-la-jugada-37",
        number=2,
        title="La jugada 37",
        next_title="La canción detrás de ChatGPT",
        scenes=[
            dict(
                type="hook",
                say="Hace 10 años, una máquina hizo una jugada que ningún humano habría hecho.",
                kicker="Seúl · marzo de 2016",
                headline="Una jugada que *ningún humano* habría hecho",
            ),
            dict(
                type="versus",
                say="AlphaGo, de DeepMind, enfrentaba a Lee Sedol, leyenda mundial del Go.",
                left=["AlphaGo", "DeepMind"],
                right=["Lee Sedol", "18 títulos mundiales"],
                footer="Reto Google DeepMind · 5 partidas",
            ),
            dict(
                type="goboard",
                say="En la segunda partida, jugada 37, puso una piedra que los comentaristas tomaron por error.",
                label="Partida 2 · Jugada 37",
                note="Ilustrativo",
            ),
            dict(
                type="dots",
                say="AlphaGo calculó que un humano la jugaría con una probabilidad de 1 en 10 000.",
                big="1 en 10 000",
                caption="Probabilidad estimada de que un humano la jugara",
            ),
            dict(
                type="timer",
                say="Lee Sedol salió de la sala y tardó unos quince minutos en responder.",
                minutes=15,
                caption="Lee Sedol sale de la sala",
            ),
            dict(
                type="score",
                say="AlphaGo ganó 4 a 1. Pero en la cuarta partida, Lee respondió con su propia genialidad: la jugada 78.",
                left=["AlphaGo", "4"],
                right=["Lee Sedol", "1"],
                chip="Jugada 78 · «El toque de Dios»",
                chip_at="c3",
            ),
            dict(
                type="lesson",
                say="La lección: la IA no solo imita a los expertos; puede mostrarnos caminos que no veíamos.",
                text="La IA no solo imita a los expertos: *puede mostrarnos caminos que no veíamos.*",
                chips=["Diseño generativo", "Optimización estructural", "Planificación de obra"],
            ),
            dict(
                type="cta",
                say="Sigue a AECODE. Próxima historia: la canción detrás de ChatGPT.",
            ),
        ],
    ),
    # ------------------------------------------------------------------ EP 03
    dict(
        slug="ep03-la-cancion-detras-de-chatgpt",
        number=3,
        title="La canción detrás de ChatGPT",
        next_title=None,
        scenes=[
            dict(
                type="acronym",
                say="La T de ChatGPT nació de un paper con título de canción de los Beatles.",
                kicker="2017 → 2026",
                word="ChatGPT",
                expand=["Generative", "Pre-trained", "Transformer"],
            ),
            dict(
                type="paper",
                say="En 2017, ocho investigadores de Google publicaron Attention Is All You Need.",
                title="Attention Is All You Need",
                authors=["Vaswani", "Shazeer", "Parmar", "Uszkoreit", "Jones", "Gomez", "Kaiser", "Polosukhin"],
                venue="Google Brain · Google Research · NeurIPS 2017",
                cites="+100 000 citas",
            ),
            dict(
                type="morph",
                say="El título juega con All You Need Is Love. Y el nombre Transformer se eligió porque sonaba bien.",
                a=["All You Need Is Love", "The Beatles · 1967"],
                b=["Attention Is All You Need", "Google · 2017"],
                chip="«Transformer»: el nombre que sonaba bien",
                chip_at="c1",
            ),
            dict(
                type="attention",
                say="Su idea clave es la atención: mirar todas las palabras a la vez y decidir cuáles importan.",
                tokens=["La", "viga", "soporta", "la", "losa", "del", "tercer", "piso"],
                focus=2,
                weights=[0.15, 0.95, 0, 0.1, 0.85, 0.2, 0.35, 0.55],
                label="Atención: cada palabra mira a todas las demás",
            ),
            dict(
                type="race",
                say="Cinco años después llegó ChatGPT: un millón de usuarios en cinco días, y cien millones en dos meses.",
                title="Meses hasta 100 M de usuarios",
                bars=[["ChatGPT", 2, "2 meses"], ["TikTok", 9, "9 meses"], ["Instagram", 30, "30 meses"]],
                chip="1 millón de usuarios en 5 días",
                source="Fuente: UBS vía Reuters (feb 2023)",
            ),
            dict(
                type="news",
                say="Y la novedad: en junio de 2026, Noam Shazeer, coautor del paper, dejó Google por OpenAI.",
                badge="Novedad",
                date="18 jun 2026",
                headline="Noam Shazeer, coautor del Transformer y co-líder de Gemini, deja Google por OpenAI",
                detail="Google lo había traído de vuelta en 2024 con un acuerdo reportado de US$ 2 700 M.",
                source="Fuente: CNBC · 18/06/2026",
            ),
            dict(
                type="lesson",
                say="La lección: una idea simple, bien nombrada y publicada a tiempo, puede cambiar una industria entera.",
                text="Una idea simple, bien nombrada y publicada a tiempo *puede cambiar una industria entera.*",
                chips=["Idea simple", "Buen nombre", "Publicar a tiempo"],
            ),
            dict(
                type="cta",
                say="Sigue a AECODE y aprende a aplicar la IA en la construcción.",
            ),
        ],
    ),
]
