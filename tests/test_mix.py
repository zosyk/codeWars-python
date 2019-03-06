from unittest import TestCase
from stringsMix import mix


class TestMix(TestCase):

    def test1(self):
        self.assertEqual("2:eeeee/2:yy/=:hh/=:rr", mix("Are they here", "yes, they are here"))

    def test2(self):
        self.assertEqual("1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg", mix("looping is fun but dangerous", "less dangerous than coding"))

    def test3(self):
        self.assertEqual("1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt", mix(" In many languages", " there's a pair of functions"))

    def test4(self):
        self.assertEqual("1:ee/1:ll/1:oo", mix("Lords of the Fallen", "gamekult"))

    def test5(self):
        self.assertEqual("", mix("codewars", "codewars"))

    def test6(self):
        self.assertEqual("1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr", mix("A generation must confront the looming ", "codewarrs"))
