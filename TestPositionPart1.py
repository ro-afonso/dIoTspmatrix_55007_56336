import unittest
import sys
from Position import *


class TestPositionInit(unittest.TestCase):

    def test_position_init_input_1_1(self):
        p = Position(1, 1)
        self.assertIsInstance(p, Position)

    def test_position_init_input_maxsize_maxsize(self):
        p = Position(sys.maxsize, sys.maxsize)
        self.assertIsInstance(p, Position)

    def test_position_init_input_row_minus1(self):
        try:
            Position(-1, 0)
        except ValueError as error:
            self.assertEqual(str(error), '__init__() invalid arguments')

    def test_position_init_input_col_minus1(self):
        try:
            Position(0, -1)
        except ValueError as error:
            self.assertEqual(str(error), '__init__() invalid arguments')

    def test_position_init_input_row_1point1(self):
        try:
            Position(1.1, 0)
        except ValueError as error:
            self.assertEqual(str(error), '__init__() invalid arguments')

    def test_position_init_input_col_1point1(self):
        try:
            Position(0, 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__init__() invalid arguments')

    def test_position_init_input_row_1point1_col_1point1(self):
        try:
            Position(1.1, 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__init__() invalid arguments')

    def test_position_init_input_row_tuple_col_tuple(self):
        try:
            Position((), ())
        except ValueError as error:
            self.assertEqual(str(error), '__init__() invalid arguments')

    def test_position_init_input_three_items(self):
        try:
            Position(1, 2, 3)
        except TypeError as error:
            self.assertEqual(str(error), '__init__() takes 3 positional arguments but 4 were given')


class TestPositionEqual(unittest.TestCase):

    def test_position_eq_same_position_object(self):
        p = Position(1, 1)
        self.assertEqual(p, p)

    def test_position_eq_equal_positions(self):
        self.assertEqual(Position(1, 1), Position(1, 1))

    def test_position_eq_different_positions(self):
        self.assertNotEqual(Position(1, 2), Position(2, 1))


class TestPositionStr(unittest.TestCase):

    def test_position_str_formatting_input_1_1(self):
        self.assertEqual(str(Position(1, 1)), '(1, 1)')

    def test_position_str_incorrect_formatting_input_1_1(self):
        self.assertNotEqual(str(Position(1, 1)), '(1,1)')

    def test_position_str_input_maxsize_maxsize(self):
        self.assertEqual(str(Position(sys.maxsize, sys.maxsize)), '(' + str(sys.maxsize) + ', ' + str(sys.maxsize) + ')')


class TestPositionGet(unittest.TestCase):

    def test_position_get_row_position_1_1(self):
        p = Position(1, 1)
        self.assertEqual(p[0], 1)

    def test_position_get_col_position_1_1(self):
        p = Position(1, 1)
        self.assertEqual(p[1], 1)

    def test_position_get_index_out_of_range(self):
        p = Position(1, 1)
        try:
            p.__getitem__(2)
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')


if __name__ == '__main__':
    unittest.main()
