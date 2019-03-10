from unittest import TestCase
from chainAddingFunction import add

class TestAdd(TestCase):
    def test1(self):
        self.assertTrue(add(1) == 1)
        self.assertTrue(add(1)(2) == 3)
        self.assertTrue(add(1)(2)(3) == 6)

