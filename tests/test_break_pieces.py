from unittest import TestCase
import break_pieces


def print_shapes(shapes):
    for shape in shapes:
        shape = shape.split('\n')
        for row in shape:
            print(row)


class TestBreak_pieces(TestCase):

    def test1(self):
        shape = '\n'.join(["+------------+",
                           "|            |",
                           "|            |",
                           "|            |",
                           "+------+-----+",
                           "|      |     |",
                           "|      |     |",
                           "+------+-----+"])

        expected = ['\n'.join(["+------------+",
                               "|            |",
                               "|            |",
                               "|            |",
                               "+------------+"]),
                    '\n'.join(["+------+",
                               "|      |",
                               "|      |",
                               "+------+"]),
                    '\n'.join(["+-----+",
                               "|     |",
                               "|     |",
                               "+-----+"])]

        actual = break_pieces.break_pieces(shape)
        print("Expected:")
        print_shapes(sorted(expected))
        print("\n\n Actual:")
        print_shapes(sorted(actual))
        self.assertEqual(sorted(expected), sorted(actual))

    def test2(self):
        shape = '\n'.join(["+-----+      ",
                           "|     |      ",
                           "|     |      ",
                           "+-----+-----+",
                           "      |     |",
                           "      |     |",
                           "      +-----+"])

        expected = ['\n'.join(["+-----+",
                               "|     |",
                               "|     |",
                               "+-----+"]),
                    '\n'.join(["+-----+",
                               "|     |",
                               "|     |",
                               "+-----+"])
                    ]

        actual = break_pieces.break_pieces(shape)
        print("Expected:")
        print_shapes(sorted(expected))
        print("\n\n Actual:")
        print_shapes(sorted(actual))
        self.assertEqual(sorted(expected), sorted(actual))

    def test3(self):
        shape = '\n'.join(["+-------------------+--+",
                           "|                   |  |",
                           "|                   |  |",
                           "|  +----------------+  |",
                           "|  |                   |",
                           "|  |                   |",
                           "+--+-------------------+"])

        expected = ['\n'.join(["                 +--+",
                               "                 |  |",
                               "                 |  |",
                               "+----------------+  |",
                               "|                   |",
                               "|                   |",
                               "+-------------------+"]),
                    '\n'.join(["+-------------------+",
                               "|                   |",
                               "|                   |",
                               "|  +----------------+",
                               "|  |",
                               "|  |",
                               "+--+"])
                    ]

        actual = break_pieces.break_pieces(shape)
        print("Expected:")
        print_shapes(sorted(expected))
        print("\n\n Actual:")
        print_shapes(sorted((actual)))
        self.assertEqual(sorted(expected), sorted(actual))

    def test4(self):
        shape = '\n'.join([
                           "        +-+        ",
                           "        | |        ",
                           "      +-+-+-+      ",
                           "      |     |      ",
                           "   +--+-----+--+   ",
                           "   |           |   ",
                           "+--+-----------+--+",
                           "|                 |",
                           "+-----------------+"])

        expected = ['\n'.join(["+-+",
                               "| |",
                               "+-+"]),
                    '\n'.join(["+-----+",
                               "|     |",
                               "+-----+"]),
                    '\n'.join(["+-----------+",
                               "|           |",
                               "+-----------+"]),
                    '\n'.join(["+-----------------+",
                               "|                 |",
                               "+-----------------+"])
                    ]

        actual = break_pieces.break_pieces(shape)
        print("Expected:")
        print_shapes(sorted(expected))
        print("\n\n Actual:")
        print_shapes(sorted((actual)))
        self.assertEqual(sorted(expected), sorted(actual))

    def test5(self):
        shape = '\n'.join([
                           "+-----------------+",
                           "|                 |",
                           "|   +-------------+",
                           "|   |",
                           "|   |",
                           "|   |",
                           "|   +-------------+",
                           "|                 |",
                           "|                 |",
                           "+-----------------+"])

        expected = ['\n'.join([
                           "+-----------------+",
                           "|                 |",
                           "|   +-------------+",
                           "|   |",
                           "|   |",
                           "|   |",
                           "|   +-------------+",
                           "|                 |",
                           "|                 |",
                           "+-----------------+"])
                    ]

        actual = break_pieces.break_pieces(shape)
        print("Expected:")
        print_shapes(sorted(expected))
        print("\n\n Actual:")
        print_shapes(sorted((actual)))
        self.assertEqual(sorted(expected), sorted(actual))