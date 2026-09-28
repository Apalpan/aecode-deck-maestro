#!/usr/bin/env bash
# Prepara el entorno de la fábrica de clips AECODE (Linux/macOS).
#   bash clips/setup.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="${VENV:-$ROOT/.venv-clips}"
VOICE="${VOICE:-es_MX-claude-high}"
MODELS="$ROOT/MoneyPrinterTurbo/models/piper"

python3 -m venv "$VENV"
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -r "$ROOT/MoneyPrinterTurbo/requirements.txt" -r "$ROOT/clips/requirements.txt"
"$VENV/bin/python" -m playwright install chromium

mkdir -p "$MODELS"
if [ ! -f "$MODELS/vits-piper-$VOICE/tokens.txt" ]; then
  echo "Descargando voz Piper $VOICE ..."
  curl -sSL "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-$VOICE.tar.bz2" \
    | tar -xj -C "$MODELS"
fi

echo "Listo. Genera los clips con:"
echo "  $VENV/bin/python clips/factory.py"
