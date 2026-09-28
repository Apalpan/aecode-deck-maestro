"""Build the self-contained deck: inline the fonts as base64 @font-face into index.html.

    python build.py            -> index.html (open directly in any browser, works offline)
"""
import base64
from pathlib import Path

HERE = Path(__file__).parent
FACES = [
    ("Instrument Serif", 400, "normal", "InstrumentSerif-400.woff2"),
    ("Instrument Serif", 400, "italic", "InstrumentSerif-400-italic.woff2"),
    ("Manrope", 400, "normal", "Manrope-400.woff2"),
    ("Manrope", 500, "normal", "Manrope-500.woff2"),
    ("Manrope", 600, "normal", "Manrope-600.woff2"),
    ("Manrope", 700, "normal", "Manrope-700.woff2"),
]


def font_css() -> str:
    rules = []
    for family, weight, style, file in FACES:
        data = base64.b64encode((HERE / "fonts" / file).read_bytes()).decode()
        rules.append(
            f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-style: {style}; '
            f'font-display: block; src: url(data:font/woff2;base64,{data}) format("woff2"); }}'
        )
    return "\n".join(rules)


def main() -> None:
    html = (HERE / "template.html").read_text(encoding="utf-8")
    assert "/*FONTS*/" in html
    out = html.replace("/*FONTS*/", font_css())
    (HERE / "index.html").write_text(out, encoding="utf-8")
    print(f"index.html: {len(out) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
