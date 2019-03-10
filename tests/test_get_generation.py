from unittest import TestCase

from conwaysGame import get_generation


class TestGet_generation(TestCase):

    def test1(self):
        start = [[1, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
        end = [[0, 1, 0],
               [0, 0, 1],
               [1, 1, 1]]
        resp = get_generation(start, 1)
        self.assertTrue(resp == end, 'Got\n' + htmlize(resp) + '\ninstead of\n' + htmlize(end))

    def test2(self):
        start = [[1, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
        end = [[1, 0, 1],
               [0, 1, 1],
               [0, 1, 0]]
        resp = get_generation(start, 2)
        self.assertTrue(resp == end, 'Got\n' + htmlize(resp) + '\ninstead of\n' + htmlize(end))

# -*- coding: utf-8 -*-
def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)
