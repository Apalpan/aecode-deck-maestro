import os
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

from app.config import config
from app.services import piper_engine, voice


class PiperTtsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self._pause = config.piper.get("sentence_pause")
        config.piper["sentence_pause"] = 0.5

    def tearDown(self):
        if self._pause is None:
            config.piper.pop("sentence_pause", None)
        else:
            config.piper["sentence_pause"] = self._pause

    def _fake_synthesize(self, text, voice_name, speed):
        # 1 second of tone per sentence, so timings are easy to assert.
        rate = 1000
        return np.full(rate, 0.5, dtype=np.float32), rate

    def test_voice_name_dispatches_to_piper(self):
        self.assertTrue(voice.is_piper_voice("piper:es_MX-claude-high"))
        self.assertFalse(voice.is_piper_voice("es-MX-JorgeNeural-Male"))

    def test_sentence_timings_and_subtitle_alignment(self):
        text = "Primera frase, con coma. Segunda frase."
        voice_file = os.path.join(self.tmp.name, "audio.wav")
        with patch.object(piper_engine, "synthesize", side_effect=self._fake_synthesize):
            sub_maker = voice.tts(
                text=text,
                voice_name="piper:es_MX-claude-high-Male",
                voice_rate=1.0,
                voice_file=voice_file,
            )

        self.assertIsNotNone(sub_maker)
        self.assertEqual(sub_maker.subs, ["Primera frase", "con coma", "Segunda frase"])
        # Second sentence starts after 1s of speech + 0.5s pause.
        self.assertEqual(sub_maker.offset[2][0], 15000000)
        self.assertEqual(sub_maker.offset[-1][1], 30000000)
        self.assertAlmostEqual(voice.get_audio_duration(voice_file), 3.0, places=2)

        subtitle_file = os.path.join(self.tmp.name, "subtitle.srt")
        voice.create_subtitle(sub_maker=sub_maker, text=text, subtitle_file=subtitle_file)
        with open(subtitle_file, encoding="utf-8") as f:
            srt = f.read()
        self.assertIn("Segunda frase", srt)
        self.assertIn("00:00:01,500 --> 00:00:03,000", srt)

    def test_lexicon_only_changes_spoken_text(self):
        with patch.dict(config.piper, {"lexicon": {"IA": "i a"}}):
            self.assertEqual(piper_engine.apply_lexicon("La IA y la IAx"), "La i a y la IAx")


if __name__ == "__main__":
    unittest.main()
