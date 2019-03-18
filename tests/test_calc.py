from unittest import TestCase

from evalMathExpr import calc


class TestCalc(TestCase):
    tests = [
        ["1 + 1 + 3 + 4", 9],
        ["(2 / (2 + 3.33) * 4) - -6", 7.50093808630394],
        ["(2 + (2 + 3.33) * 2) - -6", 18.66],
        ["8/16", 0.5],
        ["3 -(-1)", 4],
        ["2 + -2", 0],
        ["10- 2- -5", 13],
        ["(((10)))", 10],
        ["3 * 5", 15],
        ["6 + -(4)", 2],
        ["6 + -( -4)", 10],
        ["-7 * -(6 / 3)", 14],
        ["-2 * -(6.5 - -0.5)", 14],
        ["2 + 2 * 2", 6]
    ]

    def test1(self):
        for test in self.tests:
            self.assertEqual(test[1], calc(test[0]))
