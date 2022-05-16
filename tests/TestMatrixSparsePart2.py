import unittest
from MatrixSparseDOK import *

MatrixSparseImplementation = MatrixSparseDOK


class TestMatrixSparseEqual(unittest.TestCase):

    # __eq__ basic test
    def test_01___eq___m2x3_6items_with_itself(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        self.assertEqual(m1, m1)

    # __eq__ basic test for equal matrices with different zeros
    def test_02___eq___m2x3_6items_with_different_zeros(self):
        m1 = MatrixSparseImplementation(0.0)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(1.0)
        m2_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        self.assertNotEqual(m1, m2)

    # __eq__ test for equal matrices with 1 element
    def test_03___eq___m1x1_1item_with_m1x1_1item(self):
        m1 = MatrixSparseImplementation(1.0)
        m1_data = {(1, 1): 1.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(1.0)
        m2_data = {(1, 1): 1.1}
        for key, value in m2_data.items():
            m1[Position(key[0], key[1])] = value
        self.assertNotEqual(m1, m2)

    # __eq__ test for empty matrices
    def test_04___eq___empty_matrix_with_empty_matrix(self):
        m1 = MatrixSparseImplementation(1.0)
        m2 = MatrixSparseImplementation(1.0)
        self.assertEqual(m1, m2)

    # __eq__ test equal matrix to number
    def test_05___eq___(self):
        m1 = MatrixSparseImplementation(1.0)
        self.assertFalse(m1.__eq__(1.0))


class TestMatrixSparseIter(unittest.TestCase):

    # __iter__ basic test
    def test_01___iter___m2x3_6items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        test = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        test_list = list(test)
        i = 0
        for pos in m1:
            self.assertAlmostEqual(m1_data[test_list[i]], m1[pos])
            i += 1

    # __iter__ basic test for matrix with non-default zero
    def test_02___iter___m2x3_6items_zero_as_3(self):
        m1 = MatrixSparseImplementation(3.0)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        test = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        test_list = list(test)
        i = 0
        for pos in m1:
            self.assertAlmostEqual(m1_data[test_list[i]], m1[pos])
            i += 1

    # __iter__ basic test with unordered items
    def test_03___iter___m2x3_6items_unordered(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(2, 3): 2.3, (1, 3): 1.3, (2, 2): 2.2, (1, 2): 1.2, (2, 1): 2.1, (1, 1): 1.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        test = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        test_list = list(test)
        i = 0
        for pos in m1:
            self.assertAlmostEqual(m1_data[test_list[i]], m1[pos])
            i += 1

    # __iter__ test matrix with 1 element
    def test_04___iter___m1x1_1item(self):
        m1 = MatrixSparseImplementation(1.0)
        m1_data = {(1, 1): 1.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        test = {(1, 1): 1.1}
        test_list = list(test)
        i = 0
        for pos in m1:
            self.assertAlmostEqual(m1_data[test_list[i]], m1[pos])
            i += 1

    # __iter__ test empty matrix
    def test_05___iter___empty_matrix(self):
        m1 = MatrixSparseImplementation(1.0)
        for pos in m1:
            self.assertTrue(False, "__iter__ failed to execute")


class TestMatrixSparseTranspose(unittest.TestCase):

    # transpose basic test
    def test_01_transpose_matrix_2x2_4items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (2, 1): 2.1, (2, 2): 2.2}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1.transpose()
        m2_data = {(1, 1): 1.1, (1, 2): 2.1, (2, 1): 1.2, (2, 2): 2.2}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))

    # transpose basic test for matrix with non-default zero
    def test_02_transpose_matrix_2x3_6items_zero_as_3(self):
        m1 = MatrixSparseImplementation(3.0)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1.transpose()
        m2_data = {(1, 1): 1.1, (2, 1): 1.2, (3, 1): 1.3, (1, 2): 2.1, (2, 2): 2.2, (3, 2): 2.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))

    # transpose test matrix with 1 element
    def test_03_transpose_matrix_1x1_1item(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1.transpose()
        m2_data = {(1, 1): 1.1}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))

    # transpose test empty matrix
    def test_04_transpose_empty_matrix(self):
        m1 = MatrixSparseImplementation()
        m2 = m1.transpose()
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(0, len(m2))

    # transpose test for matrix 5x5 with 25 elements
    def test_05_transpose_matrix_5x5_25items(self):
        m1 = MatrixSparseImplementation(0.0)
        for row in range(5):
            for col in range(5):
                m1[Position(row, col)] = row * 5 + col + 1
        m2 = m1.transpose()
        for row in range(1, 6):
            for col in range(1, 6):
                self.assertAlmostEqual(m1[Position(col, row)], m2[Position(row, col)])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m1), len(m2))


class TestMatrixSparseAddNumber(unittest.TestCase):

    # __add__ basic test with number 0
    def test_01___add___m2x3_6items_with_number_0(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + 0
        m2_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __add__ basic test with number 1
    def test_02___add___m2x3_6items_with_number_1(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + 1
        m2_data = {(1, 1): 2.1, (1, 2): 2.2, (1, 3): 2.3, (2, 1): 3.1, (2, 2): 3.2, (2, 3): 3.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __add__ basic test with number 1
    def test_03___add___m2x3_6items_with_number_minus_1(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + -1
        m2_data = {(1, 1): 0.1, (1, 2): 0.2, (1, 3): 0.3, (2, 1): 1.1, (2, 2): 1.2, (2, 3): 1.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __add__ test matrix 1 element with number 1
    def test_04___add___m1x1_1item_with_number_1(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + 1
        m2_data = {(1, 1): 2.1}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __add__ test empty matrix with number 1
    def test_05___add___empty_matrix_with_number_1(self):
        m1 = MatrixSparseImplementation(1.0)
        m2 = m1 + 1
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(0, len(m2))


class TestMatrixSparseAddMatrix(unittest.TestCase):

    # __add__ with matrix basic test
    def test_01___add___m2x3_6items_with_itself(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + m1
        m2_data = {(1, 1): 2.2, (1, 2): 2.4, (1, 3): 2.6, (2, 1): 4.2, (2, 2): 4.4, (2, 3): 4.6}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __add__ with matrix simple test non_overlapping matrices
    def test_02___add___m1x3_3items_with_non_overlapping_m1x3_3items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation()
        m2_data = {(2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 + m2
        m3_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertEqual(len(m2_data), len(m2))

    # __add__ with matrix simple test overlapping matrices
    def test_03___add___m2x3_4items_with_overlapping_m2x3_4items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation()
        m2_data = {(1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 + m2
        m3_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 2.6, (2, 1): 4.2, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertEqual(len(m2_data), len(m2))

    # __add__ with matrix simple test of overlapping matrices with zero as 1
    def test_04___add___m2x3_4items_with_overlapping_m2x3_4items_zeros_as_1(self):
        m1 = MatrixSparseImplementation(1)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(1)
        m2_data = {(1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 + m2
        m3_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 2.6, (2, 1): 4.2, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertEqual(len(m2_data), len(m2))

    # __add__ matrix test of incompatible matrices having different zeros
    def test_05___add___m2x3_4items_with_m2x3_4items_different_zeros(self):
        m1 = MatrixSparseImplementation(1)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(2)
        m2_data = {(1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        try:
            m3 = m1 + m2
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == '_add_matrix() incompatible matrices'


class TestMatrixSparseMulNumber(unittest.TestCase):

    # __mul__ basic test with number 1
    def test_01___mul___m2x3_6items_to_number_1(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 * 1
        m2_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __mul__ basic test with number 2
    def test_02___mul___m2x3_6items_to_number_2(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 * 2
        m2_data = {(1, 1): 2.2, (1, 2): 2.4, (1, 3): 2.6, (2, 1): 4.2, (2, 2): 4.4, (2, 3): 4.6}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __mul__ basic test with number 1/2
    def test_03___mul___m2x3_6items_to_number_minus_1(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 * (1/2)
        m2_data = {(1, 1): 1.1/2, (1, 2): 1.2/2, (1, 3): 1.3/2, (2, 1): 2.1/2, (2, 2): 2.2/2, (2, 3): 2.3/2}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __mul__ test matrix one element with number 2
    def test_04___mul___m1x1_1item_with_number_2(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 * 2
        m2_data = {(1, 1): 2.2}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __mul__ test empty matrix with number 2
    def test_05___mul___empty_matrix_with_number_2(self):
        m1 = MatrixSparseImplementation(1.0)
        m2 = m1 * 2
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(0, len(m2))


class TestMatrixSparseMulMatrix(unittest.TestCase):

    # __mul__ with matrix basic test 4 items
    def test_01___mul___m2x3_4items_to_m3x2_4items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1, (1, 3): 2, (2, 1): 3, (2, 3): 4}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation()
        m2_data = {(1, 1): 1, (1, 2): 2, (3, 1): 3, (3, 2): 4}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 * m2
        m3_data = {(1, 1): 7, (1, 2): 10, (2, 1): 15, (2, 2): 22}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    # __mul__ with matrix basic test 6 items
    def test_02___mul___m2x3_6items_by_m3x2_6items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1, (1, 2): 2, (1, 3): 3, (2, 1): 4, (2, 2): 5, (2, 3): 6}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation()
        m2_data = {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4, (3, 1): 5, (3, 2): 6}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 * m2
        m3_data = {(1, 1): 22, (1, 2): 28, (2, 1): 49, (2, 2): 64}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertEqual(len(m2_data), len(m2))

    # __mul__ with matrix basic test with non-default zero
    def test_03___mul___m2x3_4items_by_m3x2_4items_zeros_as_5(self):
        m1 = MatrixSparseImplementation(5)
        m1_data = {(1, 1): 1, (1, 3): 2, (2, 1): 3, (2, 3): 4}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(5)
        m2_data = {(1, 1): 1, (1, 2): 2, (3, 1): 3, (3, 2): 4}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 * m2
        m3_data = {(1, 1): 7, (1, 2): 10, (2, 1): 15, (2, 2): 22}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertEqual(len(m2_data), len(m2))

    # __mul__ matrix with one element by matrix with one element
    def test_04___mul___m1x1_1item_by_m1x1_1item(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(2, 2): 3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation()
        m2_data = {(3, 3): 5}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 * m2
        m3_data = {(2, 3): 15}
        for key, value in m3_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(len(m3_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertEqual(len(m2_data), len(m2))

    # __mul__ matrix test of incompatible matrices having different zeros
    def test_05___mul___incompatible_m2x3_4items_with_m3x2_4items_different_zeros(self):
        m1 = MatrixSparseImplementation(1)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(2)
        m2_data = {(1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        try:
            m3 = m1 * m2
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == '_mul_matrix() incompatible matrices'


class TestMatrixSparseEye(unittest.TestCase):

    # eye basic test
    def test_01_eye_m3x3_default_parameters(self):
        m1 = MatrixSparseImplementation.eye(3)
        m1_data = {(0, 0): 1.0, (0, 1): 0.0, (0, 2): 0.0,
                  (1, 0): 0.0, (1, 1): 1.0, (1, 2): 0.0,
                  (2, 0): 0.0, (2, 1): 0.0, (2, 2): 1.0}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, 0.0)
        self.assertEqual(3, len(m1))

    # eye basic test with non-default parameters
    def test_02_eye_m3x3_identity_as_5_zero_as_8(self):
        m1 = MatrixSparseImplementation.eye(3, 4, 8)
        m1_data = {(0, 0): 4.0, (0, 1): 8.0, (0, 2): 8.0,
                   (1, 0): 8.0, (1, 1): 4.0, (1, 2): 8.0,
                   (2, 0): 8.0, (2, 1): 8.0, (2, 2): 4.0}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, 8.0)
        self.assertEqual(3, len(m1))

    # eye test matrix 1x1
    def test_03_eye_m1x1(self):
        m1 = MatrixSparseImplementation.eye(1, 4, 8)
        m1_data = {(0, 0): 4}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, 8.0)
        self.assertEqual(len(m1_data), len(m1))

    # eye test empty matrix
    def test_04_eye_empty_matrix(self):
        m1 = MatrixSparseImplementation.eye(0, 4, 8)
        self.assertAlmostEqual(m1.zero, 8.0)
        self.assertEqual(0, len(m1))

    # eye test invalid parameters
    def test_05_eye_m3x3_invalid_parameter_size(self):
        try:
            MatrixSparseImplementation.eye(-1, 4, 8)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == 'eye() invalid parameters'


class TestMatrixSparseCompress(unittest.TestCase):

    # compress basic test optimal compression
    def test_01_compress_m3x5_5items_with_optimal_compression(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = m1.compress()
        res = ((6, 1), 0.0, (8.1, 8.2, 6.3, 7.4, 8.5), (8, 8, 6, 7, 8), (0, 0, 0))
        self.assertEqual(vc, res)

    # compress basic test non-optimal compression
    def test_02_compress_m3x5_7items_with_non_optimal_compression(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 2): 6.2, (6, 4): 6.4, (7, 3): 7.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = m1.compress()
        res1 = ((6, 1),  0.0, (8.1, 8.2, 0.0, 6.2, 8.5, 6.4, 7.3, 7.4, 0.0), (8, 8, -1, 6, 8, 6, 7, 7, -1), (2, 4, 0))
        res2 = ((6, 1),  0.0, (8.1, 8.2, 0.0, 6.2, 8.5, 6.4, 7.3, 7.4), (8, 8, -1, 6, 8, 6, 7, 7), (2, 4, 0))
        if vc == res1:
            self.assertEqual(vc, res1)
        else:
            self.assertEqual(vc, res2)

    # compress test one-column matrix
    def test_03_compress_m4x1_2items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 2): 6.2, (9, 2): 9.2}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = m1.compress()
        res = ((6, 2), 0.0, (6.2, 9.2), (6, 9), (0, 0, 0, 1))
        self.assertEqual(vc, res)

    # compress test small diagonal matrix
    def test_04_compress_m5x5_diagonal(self):
        m1 = MatrixSparseImplementation(1.0)
        m1_data = {(2, 2): 2.2, (3, 3): 3.3, (4, 4): 4.4, (5, 5): 5.5, (6, 6): 6.6}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = m1.compress()
        res = ((2, 2), 1.0, (2.2, 3.3, 4.4, 5.5, 6.6), (2, 3, 4, 5, 6), (0, 0, 0, 0, 0))
        self.assertEqual(vc, res)

    # compress test with dense matrix
    def test_05_compress_dense_m3x1_2items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (3, 1): 3.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        try:
            vc = m1.compress()
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == 'compress() dense matrix'


class TestMatrixSparseDoi(unittest.TestCase):

    # doi basic test from optimally compressed matrix
    def test_01_doi_m3x5_5items_with_optimal_compression(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = ((6, 1), 0.0, (8.1, 8.2, 6.3, 7.4, 8.5), (8, 8, 6, 7, 8), (0, 0, 0))
        dim = m1.dim()
        for r in range( dim[0][0], dim[1][0]+1 ):
            for c in range(dim[0][1], dim[1][1] + 1):
                self.assertAlmostEqual(MatrixSparseImplementation.doi(vc, Position(r, c)), m1[Position(r, c)])

    # doi basic test from non-optimally compressed matrix
    def test_02_doi_m3x5_7items_with_non_optimal_compression(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 2): 6.2, (6, 4): 6.4, (7, 3): 7.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = ((6, 1),  0.0, (8.1, 8.2, 0.0, 6.2, 8.5, 6.4, 7.3, 7.4), (8, 8, -1, 6, 8, 6, 7, 7), (2, 4, 0))
        dim = m1.dim()
        for r in range(dim[0][0], dim[1][0] + 1):
            for c in range(dim[0][1], dim[1][1] + 1):
                self.assertAlmostEqual(MatrixSparseImplementation.doi(vc, Position(r, c)), m1[Position(r, c)])

    # doi test one-column matrix
    def test_03_doi_03_compress_m4x1_2items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 2): 6.2, (9, 2): 9.2}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = ((6, 2), 0.0, (6.2, 9.2), (6, 9), (0, 0, 0, 1))
        dim = m1.dim()
        for r in range(dim[0][0], dim[1][0] + 1):
            for c in range(dim[0][1], dim[1][1] + 1):
                self.assertAlmostEqual(MatrixSparseImplementation.doi(vc, Position(r, c)), m1[Position(r, c)])

    # doi test small diagonal matrix
    def test_04_doi_m2x2_diagonal(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(2, 2): 2.2, (2, 3): 1.0, (3, 2): 1.0, (3, 3): 3.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = ((2, 2), 1.0, (2.2, 3.3), (2, 3), (0, 0))
        dim = m1.dim()
        for r in range(dim[0][0], dim[1][0] + 1):
            for c in range(dim[0][1], dim[1][1] + 1):
                self.assertAlmostEqual(MatrixSparseImplementation.doi(vc, Position(r, c)), m1[Position(r, c)])

    # doi test invalid compressed vector due to invalid upper left position
    def test_05_doi_invalid_compressed_vector_invalid_uppper_left_corner_type(self):
        vc = ((6, 1, 1),  0.0, (8.1, 8.2, 0.0, 6.2, 8.5, 6.4, 7.3, 7.4), (8, 8, -1, 6, 8, 6, 7, 7), (2, 4, 0))
        try:
            self.assertAlmostEqual(MatrixSparseImplementation.doi(vc, Position(6, 2)), 6.2)
            self.assertTrue(False, "Failed to Raise Exception")
        except ValueError as error:
            assert str(error) == 'doi() invalid parameters'


class TestMatrixSparseDecompress(unittest.TestCase):

    # decompress basic test from optimally compressed matrix
    def test_01_decompress_m3x5_5items_with_optimal_compression(self):
        vc = ((6, 1), 0.0, (8.1, 8.2, 6.3, 7.4, 8.5), (8, 8, 6, 7, 8), (0, 0, 0))
        m1 = MatrixSparseImplementation.decompress(vc)
        m1_data = {(6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, 0.0)
        self.assertEqual(len(m1_data), len(m1))

    # decompress basic test from non-optimally compressed matrix
    def test_02_decompress_m3x5_7items_with_non_optimal_compression(self):
        vc = ((6, 1),  0.0, (8.1, 8.2, 0.0, 6.2, 8.5, 6.4, 7.3, 7.4), (8, 8, -1, 6, 8, 6, 7, 7), (2, 4, 0))
        m1 = MatrixSparseImplementation.decompress(vc)
        m1_data = {(6, 2): 6.2, (6, 4): 6.4, (7, 3): 7.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, vc[1])
        self.assertEqual(len(m1_data), len(m1))

    # decompress test one-column matrix
    def test_03_decompress_m4x1_2items(self):
        vc = ((6, 2), 0.0, (6.2, 9.2), (6, 9), (0, 0, 0, 1))
        m1 = MatrixSparseImplementation.decompress(vc)
        m1_data = {(6, 2): 6.2, (9, 2): 9.2}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, vc[1])
        self.assertEqual(len(m1_data), len(m1))

    # decompress test small diagonal matrix
    def test_04_decompress_m2x2_diagonal(self):
        vc = ((2, 2), 1.0, (2.2, 3.3), (2, 3), (0, 0))
        m1 = MatrixSparseImplementation.decompress(vc)
        m1_data = {(2, 2): 2.2, (3, 3): 3.3}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, vc[1])
        self.assertEqual(len(m1_data), len(m1))

    # decompress test matrix all rows with same density
    def test_05_decompress_m5x5_9items_3_rows_same_density(self):
        vc = ((0, 0), 0.0, (1.0, 11.0, 3.0, 13.0, 5.0, 15.0, 21.0, 0.0, 23.0, 0.0, 25.0), (0, 2, 0, 2, 0, 2, 4, -1, 4, -1, 4), (0, 0, 1, 0, 6))
        m1 = MatrixSparseImplementation.decompress(vc)
        m1_data = {(0, 0): 1.0, (0, 2): 3.0, (0, 4): 5.0, (2, 0): 11.0, (2, 2): 13.0, (2, 4): 15.0, (4, 0): 21.0, (4, 2): 23.0, (4, 4): 25.0}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, vc[1])
        self.assertEqual(len(m1_data), len(m1))


if __name__ == '__main__':
    unittest.main()
