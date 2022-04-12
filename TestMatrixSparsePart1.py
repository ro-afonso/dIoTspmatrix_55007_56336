import unittest
import sys
import copy
from MatrixSparseDOK import *


class TestMatrixSparseInit(unittest.TestCase):

    def test_matrixsparse_init_zero_default(self):
        self.assertTrue(isinstance(MatrixSparseDOK(), MatrixSparseDOK))

    def test_matrixsparse_init_zero_1point0(self):
        self.assertTrue(isinstance(MatrixSparseDOK(1.0), MatrixSparseDOK))

    def test_matrixsparse_init_zero_maxsize(self):
        self.assertTrue(isinstance(MatrixSparseDOK(sys.maxsize), MatrixSparseDOK))

    def test_matrixsparse_init_zero_tuple(self):
        try:
            self.assertTrue(isinstance(MatrixSparseDOK((0.0,)), MatrixSparseDOK))
        except ValueError as error:
            assert str(error) == '__init__() invalid arguments'

    def test_matrixsparse_init_zero_list(self):
        try:
            self.assertTrue(isinstance(MatrixSparseDOK([0.0]), MatrixSparseDOK))
        except ValueError as error:
            assert str(error) == '__init__() invalid arguments'

    def test_matrixsparse_init_zero_string(self):
        try:
            self.assertTrue(isinstance(MatrixSparseDOK('0.0'), MatrixSparseDOK))
        except ValueError as error:
            assert str(error) == '__init__() invalid arguments'


class TestMatrixSparseSetItem(unittest.TestCase):

    def test_matrixsparse_setitem_pos_Position_1_1(self):
        m = MatrixSparseDOK()
        m[Position(1, 1)] = 1.1
        self.assertEqual(1, len(m))

    def test_matrixsparse_setitem_pos_tuple_1_1(self):
        m = MatrixSparseDOK()
        m[1, 1] = 1.1
        self.assertEqual(1, len(m))

    def test_matrixsparse_setitem_not_adding_item_as_value_zero(self):
        m = MatrixSparseDOK(2.2)
        m[Position(1, 1)] = 1.1
        m[Position(2, 2)] = 2.2
        self.assertEqual(2.2, m[Position(2, 2)])
        self.assertEqual(1, len(m))

    def test_matrixsparse_setitem_remove_item_from_matrix(self):
        m = MatrixSparseDOK(0.0)
        m[Position(1, 1)] = 1.1
        m[Position(2, 2)] = 2.2
        m[Position(2, 2)] = 0.0
        self.assertEqual(0.0, m[Position(2, 2)])
        self.assertEqual(1, len(m))

    def test_matrixsparse_setitem_pos_row_minus1(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((-1, 0), -1.0)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_col_minus1(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((0, -1), -1.0)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_row_1point1(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1.1, 0), 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_col_1point1(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((0, 1.1), 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_row_1point1_col_1point1(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1.1, 1.1), 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_row_tuple_col_tuple(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__(((), ()), 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_tuple_three_items(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1, 2, 3), 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_pos_zero_tuple(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1, 2, 3), 1.1)
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_value_tuple(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1,1), (0.0,))
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_value_list(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1,1), [0.0])
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')

    def test_matrixsparse_setitem_value_string(self):
        m = MatrixSparseDOK()
        try:
            m.__setitem__((1,1), '0.0')
        except ValueError as error:
            self.assertEqual(str(error), '__setitem__() invalid arguments')


class TestMatrixSparseGetItem(unittest.TestCase):

    def test_matrixsparse_getitem_using_Position_on_m1x1_with_1item(self):
        m = MatrixSparseDOK()
        m[Position(1, 1)] = 1.1
        self.assertEqual(m[Position(1, 1)], 1.1)

    def test_matrixsparse_getitem_using_tuple_m1x1_with_1item(self):
        m = MatrixSparseDOK()
        m[Position(1, 1)] = 1.1
        self.assertEqual(m[1, 1], 1.1)

    def test_matrixsparse_getitem_pos_row_minus1(self):
        m = MatrixSparseDOK()
        m[Position(1, 1)] = 1.1
        try:
            m.__getitem__((-1, 0))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_col_minus1(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__((0, -1))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_row_1point1(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__((1.1, 0))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_col_1point1(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__((0, 1.1))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_row_1point1_col_1point1(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__((1.1, 1.1))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_row_tuple_col_tuple(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__(((), ()))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_tuple_three_items(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__((1, 2, 3))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')

    def test_matrixsparse_getitem_pos_zero_tuple(self):
        m = MatrixSparseDOK()
        try:
            m.__getitem__((1, 2, 3))
        except ValueError as error:
            self.assertEqual(str(error), '__getitem__() invalid arguments')


class TestMatrixSparseZeroGet(unittest.TestCase):

    def test_matrixsparse_zeroget_empty_matrix_zero_default(self):
        m = MatrixSparseDOK()
        self.assertEqual(0.0, m.zero)

    def test_matrixsparse_zeroget_empty_matrix_zero_0(self):
        m = MatrixSparseDOK(0.0)
        self.assertEqual(0.0, m.zero)

    def test_matrixsparse_zeroget_empty_matrix_zero_maxsize(self):
        m = MatrixSparseDOK(sys.maxsize)
        self.assertEqual(sys.maxsize, m.zero)

    def test_matrixsparse_zeroget_empty_matrix_zero_minus_maxsize(self):
        m = MatrixSparseDOK(-sys.maxsize)
        self.assertEqual(-sys.maxsize, m.zero)


class TestMatrixSparseZeroSet(unittest.TestCase):

    def test_matrixsparse_zeroset_change_zero_from_1_to_0(self):
        m = MatrixSparseDOK(1.0)
        m.zero = 0.0
        self.assertEqual(0.0, m.zero)
        self.assertEqual(0, len(m))

    def test_matrixsparse_zeroset_change_zere_from_default_to_1e7(self):
        m = MatrixSparseDOK()
        m.zero = 1e7
        self.assertEqual(1e7, m.zero)
        self.assertEqual(0, len(m))

    def test_matrixsparse_zeroset_change_zero_from_default_to_minus_1e7(self):
        m = MatrixSparseDOK()
        m.zero = -1e7
        self.assertEqual(-1e7, m.zero)
        self.assertEqual(0, len(m))

    def test_matrixsparse_zeroget_change_zero_from_default_to_1point1_removing_matrix_elements(self):
        m = MatrixSparseDOK(0.0)
        m[Position(1, 1)] = 1.1
        m.zero = 1.1
        m.zero = 2.2
        self.assertEqual(2.2, m[Position(1, 1)])
        self.assertEqual(0, len(m))

    def test_matrixsparse_zeroget_after_multiple_zero_sets(self):
        m = MatrixSparseDOK(6.0)
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

    def test_matrixsparse_copy_empty_matrix_with_zero_as_1(self):
        m = MatrixSparseDOK(1.0)
        self.assertEqual(1.0, m.__copy__().zero)

    def test_matrixsparse_copy_empty_matrix_adding_element_to_copy(self):
        m = MatrixSparseDOK()
        m2 = m.__copy__()
        m2.zero = 1e7
        m[1, 1] = 1.1
        self.assertEqual(1e7, m2[1, 1])
        self.assertEqual(0, len(m2))
        self.assertEqual(1, len(m))

    def test_matrixsparse_copy_deepcopy_empty_matrix_adding_element_to_copy(self):
        m = MatrixSparseDOK()
        m2 = copy.deepcopy(m)
        m2.zero = 1e7
        m[1, 1] = 1.1
        self.assertEqual(1e7, m2[1, 1])
        self.assertEqual(0, len(m2))
        self.assertEqual(1, len(m))


class TestMatrixSparseDim(unittest.TestCase):

    def test_matrixsparse_dim_empty_matrix(self):
        self.assertEqual((), MatrixSparseDOK().dim())

    def test_matrixsparse_dim_m1x1(self):
        m = MatrixSparseDOK()
        m[1, 2] = 1.2
        dim = m.dim()
        self.assertEqual(Position(1, 2), dim[0])
        self.assertEqual(Position(1, 2), dim[1])

    def test_matrixsparse_dim_m3x3(self):
        m = MatrixSparseDOK(0.0)
        m[Position(1, 2)] = 1.2
        m[Position(2, 1)] = 2.1
        m[Position(2, 3)] = 2.3
        m[Position(3, 2)] = 3.2
        dim = m.dim()
        self.assertEqual(Position(1, 1), dim[0])
        self.assertEqual(Position(3, 3), dim[1])

    def test_matrixsparse_dim_m10000000x10000000(self):
        m = MatrixSparseDOK(1e7)
        m[Position(1, 10000000)] = 1.1
        m[Position(10000000, 1)] = 1.1
        dim = m.dim()
        self.assertEqual(Position(1, 1), dim[0])
        self.assertEqual(Position(10000000, 10000000), dim[1])


class TestMatrixSparseStr(unittest.TestCase):

    def test_01_str_m2x2_2items(self):
        m = MatrixSparseDOK()
        m[Position(1, 2)] = 1.2
        m[Position(2, 1)] = 2.1
        self.assertEqual("0 1.2\n2.1 0", str(m))

    def test_02_str_m2x2_2items(self):
        m = MatrixSparseDOK()
        m[Position(2, 3)] = 1.2
        m[Position(3, 2)] = 2.1
        self.assertEqual("0 1.2\n2.1 0", str(m))


class TestMatrixSparseRow(unittest.TestCase):

    def test_01_row_m2x2_2items(self):
        m = MatrixSparseDOK()
        init = {(1, 2): 1.2, (2, 1): 2.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 0.0, (1, 2): 1.2}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_02_row_m1000x1000_4items(self):
        m = MatrixSparseDOK()
        init = {(1, 1): 1.1, (1, 1000): 1.1000, (1000, 1): 1000.1, (1000, 1000): 1000.1000}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.row(1)
        test = {(1, 1): 1.1, (1, 1000): 1.1000}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])


class TestMatrixSparseCol(unittest.TestCase):

    def test_01_col_m2x2_2items(self):
        m = MatrixSparseDOK()
        init = {(1, 2): 1.2, (2, 1): 2.1}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.col(2)
        test = {(1, 2): 1.2, (2, 2): 0.0}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    def test_02_col_m1000x1000_4items(self):
        m = MatrixSparseDOK()
        init = {(1, 1): 1.1, (1, 1000): 1.1000, (1000, 1): 1000.1, (1000, 1000): 1000.1000}
        for key, value in init.items():
            m[Position(key[0], key[1])] = value
        m2 = m.col(1000)
        test = {(1, 1000): 1.1000, (1000, 1000): 1000.1000}
        for key, value in test.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])


class TestMatrixSparseSparsity(unittest.TestCase):

    def test_matrixsparse_sparsity_of_empty_matrix(self):
        m = MatrixSparseDOK()
        self.assertEqual(1.0, m.sparsity())

    def test_matrixsparse_sparsity_of_m2x2_with_2items(self):
        m = MatrixSparseDOK()
        m[1, 2] = 1.2
        m[2, 1] = 2.1
        self.assertEqual(0.5, m.sparsity())

    def test_matrixsparse_sparsity_of_m1x1_with_1item_after_change_of_zero(self):
        m = MatrixSparseDOK()
        m[1, 2] = 1.2
        m[2, 1] = 2.1
        m.zero = 1.2
        self.assertEqual(0.0, m.sparsity())


if __name__ == '__main__':
    unittest.main()
