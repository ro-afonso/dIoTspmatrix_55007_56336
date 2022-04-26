import unittest
import sys
import copy
from MatrixSparseDOK import *

MatrixSparseImplementation = MatrixSparseDOK


class TestMatrixSparseInit(unittest.TestCase):

    def test___init___zero_tuple(self):
        try:
            m = MatrixSparseImplementation((0.0,))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == '__init__() invalid arguments'

    def test___init___zero_list(self):
        try:
            m = MatrixSparseImplementation([0.0])
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == '__init__() invalid arguments'

    def test___init___zero_string(self):
        try:
            m = MatrixSparseImplementation('0.0')
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == '__init__() invalid arguments'


class TestMatrixSparseSetItem(unittest.TestCase):

    def test___setitem___pos_Position_1_1(self):
        m = MatrixSparseImplementation()
        m[Position(1, 1)] = 1.1
        self.assertEqual(1, len(m))

    def test___setitem___pos_tuple_1_1(self):
        m = MatrixSparseImplementation()
        m[1, 1] = 1.1
        self.assertEqual(1, len(m))

    def test___setitem___not_adding_item_as_value_zero(self):
        m = MatrixSparseImplementation(2.2)
        m[Position(1, 1)] = 1.1
        m[Position(2, 2)] = 2.2
        self.assertEqual(2.2, m[Position(2, 2)])
        self.assertEqual(1, len(m))

    def test___setitem___remove_item_from_matrix(self):
        m = MatrixSparseImplementation(0.0)
        m[Position(1, 1)] = 1.1
        m[Position(2, 2)] = 2.2
        m[Position(2, 2)] = 0.0
        self.assertEqual(0.0, m[Position(2, 2)])
        self.assertEqual(1, len(m))

    def test___setitem___pos_row_minus1(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((-1, 0), -1.0)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_col_minus1(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((0, -1), -1.0)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_row_1point1(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1.1, 0), 1.1)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_col_1point1(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((0, 1.1), 1.1)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_row_1point1_col_1point1(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1.1, 1.1), 1.1)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_row_tuple_col_tuple(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__(((), ()), 1.1)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_tuple_three_items(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1, 2, 3), 1.1)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___pos_zero_tuple(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1, 2, 3), 1.1)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___value_tuple(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1,1), (0.0,))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___value_list(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1,1), [0.0])
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test___setitem___value_string(self):
        m = MatrixSparseImplementation()
        try:
            m.__setitem__((1,1), '0.0')
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')


class TestMatrixSparseGetItem(unittest.TestCase):

    def test___getitem___using_Position_on_m1x1_with_1item(self):
        m = MatrixSparseImplementation()
        m[Position(1, 1)] = 1.1
        self.assertEqual(m[Position(1, 1)], 1.1)

    def test___getitem___using_tuple_m1x1_with_1item(self):
        m = MatrixSparseImplementation()
        m[Position(1, 1)] = 1.1
        self.assertEqual(m[1, 1], 1.1)

    def test___getitem___pos_row_minus1(self):
        m = MatrixSparseImplementation()
        m[Position(1, 1)] = 1.1
        try:
            m.__getitem__((-1, 0))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_col_minus1(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__((0, -1))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_row_1point1(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__((1.1, 0))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_col_1point1(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__((0, 1.1))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_row_1point1_col_1point1(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__((1.1, 1.1))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_row_tuple_col_tuple(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__(((), ()))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_tuple_three_items(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__((1, 2, 3))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test___getitem___pos_zero_tuple(self):
        m = MatrixSparseImplementation()
        try:
            m.__getitem__((1, 2, 3))
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')


class TestMatrixSparseZeroGetter(unittest.TestCase):

    def test_zerogetter_empty_matrix_zero_default(self):
        m = MatrixSparseImplementation()
        self.assertEqual(0.0, m.zero)

    def test_zerogetter_empty_matrix_zero_0(self):
        m = MatrixSparseImplementation(0.0)
        self.assertEqual(0.0, m.zero)

    def test_zerogetter_empty_matrix_zero_maxsize(self):
        m = MatrixSparseImplementation(sys.maxsize)
        self.assertEqual(sys.maxsize, m.zero)

    def test_zerogetter_empty_matrix_zero_minus_maxsize(self):
        m = MatrixSparseImplementation(-sys.maxsize)
        self.assertEqual(-sys.maxsize, m.zero)


class TestMatrixSparseZeroSetter(unittest.TestCase):

    def test_zerosetter_change_zero_from_1_to_0(self):
        m = MatrixSparseImplementation(1.0)
        m.zero = 0.0
        self.assertEqual(0.0, m.zero)
        self.assertEqual(0, len(m))

    def test_zerosetter_change_zere_from_default_to_1e7(self):
        m = MatrixSparseImplementation()
        m.zero = 1e7
        self.assertEqual(1e7, m.zero)
        self.assertEqual(0, len(m))

    def test_zerosetter_change_zero_from_default_to_minus_1e7(self):
        m = MatrixSparseImplementation()
        m.zero = -1e7
        self.assertEqual(-1e7, m.zero)
        self.assertEqual(0, len(m))

    def test_zerosetter_change_zero_from_default_to_1point1_removing_matrix_elements(self):
        m = MatrixSparseImplementation(0.0)
        m[Position(1, 1)] = 1.1
        m.zero = 1.1
        m.zero = 2.2
        self.assertEqual(2.2, m[Position(1, 1)])
        self.assertEqual(0, len(m))

    def test_zerosetter_after_multiple_zero_sets(self):
        m = MatrixSparseImplementation(6.0)
        m[Position(1, 1)] = 1.1
        m[Position(2, 2)] = 2.2
        m[Position(3, 3)] = 3.3
        m[Position(4, 4)] = 4.4
        m[Position(5, 5)] = 5.5
        m.zero = 1.1
        m.zero = 2.2
        m.zero = 3.3
        m.zero = 4.4
        m.zero = 5.5
        self.assertEqual(5.5, m.zero)
        self.assertEqual(0, len(m))


class TestMatrixSparseCopy(unittest.TestCase):

    def test___copy___empty_matrix_with_zero_as_1(self):
        m = MatrixSparseImplementation(1.0)
        self.assertEqual(1.0, m.__copy__().zero)

    def test___copy___empty_matrix_adding_element_to_copy(self):
        m = MatrixSparseImplementation()
        m2 = m.__copy__()
        m2.zero = 1e7
        m[1, 1] = 1.1
        self.assertEqual(1e7, m2[1, 1])
        self.assertEqual(0, len(m2))
        self.assertEqual(1, len(m))

    def test___copy___deepcopy_empty_matrix_adding_element_to_copy(self):
        m = MatrixSparseImplementation()
        m2 = copy.deepcopy(m)
        m2.zero = 1e7
        m[1, 1] = 1.1
        self.assertEqual(1e7, m2[1, 1])
        self.assertEqual(0, len(m2))
        self.assertEqual(1, len(m))


class TestMatrixSparseDim(unittest.TestCase):

    def test_dim_empty_matrix(self):
        self.assertEqual((), MatrixSparseImplementation().dim())

    def test_dim_m1x1(self):
        m = MatrixSparseImplementation()
        m[1, 2] = 1.2
        dim = m.dim()
        self.assertEqual(Position(1, 2), dim[0])
        self.assertEqual(Position(1, 2), dim[1])

    def test_dim_m3x3(self):
        m = MatrixSparseImplementation(0.0)
        m[Position(1, 2)] = 1.2
        m[Position(2, 1)] = 2.1
        m[Position(2, 3)] = 2.3
        m[Position(3, 2)] = 3.2
        dim = m.dim()
        self.assertEqual(Position(1, 1), dim[0])
        self.assertEqual(Position(3, 3), dim[1])

    def test_dim_m10000000x10000000(self):
        m = MatrixSparseImplementation(1e7)
        m[Position(1, 10000000)] = 1.1
        m[Position(10000000, 1)] = 1.1
        dim = m.dim()
        self.assertEqual(Position(1, 1), dim[0])
        self.assertEqual(Position(10000000, 10000000), dim[1])


class TestMatrixSparseStr(unittest.TestCase):

    def test___str___m2x2_2items(self):
        m = MatrixSparseImplementation()
        m[Position(1, 2)] = 1.2
        m[Position(2, 1)] = 2.1
        self.assertEqual("0 1.2\n2.1 0", str(m))

    def test___str___m2x3_4items(self):
        m = MatrixSparseImplementation()
        m[Position(1, 2)] = 1.2
        m[Position(1, 3)] = 1.3
        m[Position(2, 2)] = 2.2
        m[Position(2, 4)] = 2.4
        self.assertEqual("1.2 1.3 0\n2.2 0 2.4", str(m))

    def test___str___m2x3_4items_zero_as_3(self):
        m = MatrixSparseImplementation(3)
        m[Position(1, 2)] = 1.2
        m[Position(1, 3)] = 1.3
        m[Position(2, 2)] = 2.2
        m[Position(2, 4)] = 2.4
        self.assertEqual("1.2 1.3 3\n2.2 3 2.4", str(m))

    def test___str___m1x1_1item(self):
        m = MatrixSparseImplementation()
        m[Position(1, 1)] = 1.1
        self.assertEqual("1.1", str(m))

    def test___str___matrix_emtpy(self):
        m = MatrixSparseImplementation()
        self.assertEqual("", str(m))


class TestMatrixSparseRow(unittest.TestCase):

    def test_row_m2x2_2items(self):
        m = MatrixSparseImplementation()
        init = {(1, 2): 1.2, (2, 1): 2.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 0.0, (1, 2): 1.2}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_row_m2x2_2items_zero_as_3(self):
        m = MatrixSparseImplementation(3.0)
        init = {(1, 2): 1.2, (2, 1): 2.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 3.0, (1, 2): 1.2}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_row_m1x1_1item(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 1.1}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_row_m1x100_100items(self):
        m = MatrixSparseImplementation()
        vals = tuple([x for x in range(1, 100)])
        for i in vals:
            m[Position(1, vals[-i])] = i
        m2 = m.row(1)
        for i in vals:
            self.assertAlmostEqual(m2[Position(1, vals[-i])], m[Position(1, vals[-i])])

    def test_row_m1000x1000_4items(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1, (1, 1000): 1.1000, (1000, 1): 1000.1, (1000, 1000): 1000.1000}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 1.1, (1, 1000): 1.1000}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])


class TestMatrixSparseCol(unittest.TestCase):

    def test_col_m2x2_2items(self):
        m = MatrixSparseImplementation()
        init = {(1, 2): 1.2, (2, 1): 2.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.col(2)
        test = {(1, 2): 1.2, (2, 2): 0.0}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_col_m2x2_2items_zero_as_3(self):
        m = MatrixSparseImplementation(3.0)
        init = {(1, 2): 1.2, (2, 1): 2.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.col(1)
        test = {(1, 1): 3.0, (2, 1): 2.1}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_col_m1x1_1item(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 1.1}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_col_m1x100_100items(self):
        m = MatrixSparseImplementation()
        vals = tuple([x for x in range(1, 100)])
        for i in vals:
            m[Position(vals[-i], 1)] = i
        m2 = m.col(1)
        for i in vals:
            self.assertAlmostEqual(m2[Position(vals[-i], 1)], m[Position(vals[-i], 1)])

    def test_col_m1000x1000_4items(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1, (1, 1000): 1.1000, (1000, 1): 1000.1, (1000, 1000): 1000.1000}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.col(1000)
        test = {(1, 1000): 1.1000, (1000, 1000): 1000.1000}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])


class TestMatrixSparseDiagonal(unittest.TestCase):

    def test_diagonal_m2x2_2items(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1, (2, 2): 2.2}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.diagonal()
        test = {(1, 1): 1.1, (2, 2): 2.2}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_diagonal_m3x3_2items_zero_as_3(self):
        m = MatrixSparseImplementation(3.0)
        init = {(1, 1): 1.1, (3, 3): 3.3}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.diagonal()
        test = {(1, 1): 1.1, (2, 2): 3.0, (3, 3): 3.3}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_diagonal_m1x1_1item(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.diagonal()
        test = {(1, 1): 1.1}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_diagonal_m1000x1000_4items(self):
        m = MatrixSparseImplementation()
        init = {(1, 1): 1.1, (1, 1000): 1.1000, (1000, 1): 1000.1, (1000, 1000): 1000.1000}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.diagonal()
        test = {(1, 1): 1.1, (1000, 1000): 1000.1000}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])


class TestMatrixSparseSparsity(unittest.TestCase):

    def test_sparsity_empty_matrix(self):
        m = MatrixSparseImplementation()
        self.assertAlmostEqual(1.0, m.sparsity())

    def test_sparsity_m2x2_with_2items(self):
        m = MatrixSparseImplementation()
        m[1, 2] = 1.2
        m[2, 1] = 2.1
        self.assertAlmostEqual(0.5, m.sparsity())

    def test_sparsity_m1x1_1item_after_change_of_zero(self):
        m = MatrixSparseImplementation()
        m[1, 2] = 1.2
        m[2, 1] = 2.1
        m.zero = 1.2
        self.assertAlmostEqual(0.0, m.sparsity())

    def test_sparsity_m1001x1001_9631items_random(self):
        seed = 100001

        def randint(a, b):
            nonlocal seed
            seed = (seed * 125) % 2796203
            return a + seed % (b - a + 1)

        vals = [Position(randint(1, 999), randint(1, 999)) for x in range(10000)]
        m = MatrixSparseImplementation()
        m[Position(0, 0)] = 1.0
        m[Position(1000, 1000)] = 1000.1000
        for i in vals:
            m[i] = randint(1, 10000)
        self.assertAlmostEqual( (1001 * 1001 - 9631) / float(1001 * 1001), m.sparsity() )


if __name__ == '__main__':
    unittest.main()
