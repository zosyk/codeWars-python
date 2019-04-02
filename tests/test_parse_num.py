from unittest import TestCase
import parse_numbers


class TestParse_num(TestCase):
    def test1(self):
        self.assertEqual(123, parse_numbers.parse_num('a1adf23ads'))

    def test2(self):
        self.assertEqual(0, parse_numbers.parse_num('a0adf0ads'))

    def test2(self):
        self.assertEqual(714, parse_numbers.parse_num('7b1adsf4'))
