# MoneyPrinterTurbo (vendored)

Copia de [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) (licencia MIT, ver `LICENSE`).

| Campo | Valor |
|---|---|
| Upstream | https://github.com/harry0703/MoneyPrinterTurbo |
| Commit | `d7b738345e2298d3e21738140190b8a6a68cd39f` (v1.3.7, 2026-09-28) |
| Método | `git archive HEAD` (sin historial del upstream) |

## Diferencias con upstream

1. **Fuentes excluidas** de `resource/fonts/` por licencia propietaria y porque solo sirven para chino/vietnamita:
   `MicrosoftYaHeiBold.ttc`, `MicrosoftYaHeiNormal.ttc`, `STHeitiLight.ttc`, `STHeitiMedium.ttc`, `UTM Kabel KT.ttf`.
   Si necesitas subtítulos en chino, descárgalas del upstream en tu máquina (no las subas a este repo).
2. **Fuentes añadidas**: Manrope (tipografía de marca AECODE, licencia OFL) en `resource/fonts/Manrope-*.ttf`.
3. **Voz offline `piper:`**: nuevo proveedor de TTS local (Piper vía `sherpa-onnx`) en
   `app/services/piper_engine.py` + integración en `app/services/voice.py` y `app/config/config.py`.
   Funciona sin API keys ni internet una vez descargado el modelo (ver `../clips/README.md`).

## Actualizar desde upstream

```bash
git clone --depth 1 https://github.com/harry0703/MoneyPrinterTurbo.git /tmp/mpt
# Compara y porta los cambios; conserva los tres puntos de arriba.
```
