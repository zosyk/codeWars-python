from unittest import TestCase

from CalculatingwithFunctions import *


class TestCalcWithFunctions(TestCase):
    def test1(self):
        self.assertEqual(seven(times(five())), 35)

    def test2(self):
        self.assertEqual(four(plus(nine())), 13)

    def test3(self):
        self.assertEqual(eight(minus(three())), 5)

    def test4(self):
        self.assertEqual(six(divided_by(two())), 3)

    def test5(self):
        self.assertEqual(eight(divided_by(three())), 2)
