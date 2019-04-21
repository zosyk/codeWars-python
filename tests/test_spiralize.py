from unittest import TestCase

from make_spiral import spiralize


class TestSpiralize(TestCase):

    def test1(self):
        self.assertEqual([[1]], spiralize(1))

    def test2(self):
        self.assertEqual([[1, 1],
                          [0, 1]], spiralize(2))

    def test3(self):
        self.assertEqual([[1, 1, 1],
                          [0, 0, 1],
                          [1, 1, 1]], spiralize(3))

    def test4(self):
        self.assertEqual([[1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 1],
                          [1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1]], spiralize(5))

    def test5(self):
        self.assertEqual([[1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0, 1, 0, 1],
                          [1, 0, 1, 0, 0, 1, 0, 1],
                          [1, 0, 1, 1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1]], spiralize(8))


    def test6(self):
        self.assertEqual([[1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0, 1, 0, 1],
                          [1, 0, 1, 0, 0, 1, 0, 1],
                          [1, 0, 1, 1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1]], spiralize(100))
