from unittest import TestCase
from coloredTriangles import triangle


class TestTriangle(TestCase):

    def test1(self):
        self.assertEqual('R', triangle('GB'))

    def test2(self):
        self.assertEqual('R', triangle('RRR'))

    def test3(self):
        self.assertEqual('B', triangle('RGBG'))

    def test4(self):
        self.assertEqual('G', triangle('RBRGBRB'))

    def test5(self):
        self.assertEqual('G', triangle('RBRGBRBGGRRRBGBBBGG'))

    def test5(self):
        self.assertEqual('B', triangle('B'))
