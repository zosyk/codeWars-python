from unittest import TestCase

import decodeMorse


class TestDecodeMorse(TestCase):
    def test1(self):
        self.assertEqual('HEY JUDE', decodeMorse.decodeMorse('.... . -.--   .--- ..- -.. .'))
