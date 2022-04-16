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


class TestMatrixSparseTranspose(unittest.TestCase):

    # transpose basic test
    def test_01_transpose_matrix_2x2_4items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (2, 1): 2.1, (2, 2): 2.2}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1.transpose()
        self.assertAlmostEqual(m2.zero, m1.zero)
        m2_data = {(1, 1): 1.1, (1, 2): 2.1, (2, 1): 1.2, (2, 2): 2.2}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertEqual(len(m1_data), len(m1))


class TestMatrixSparseAddNumber(unittest.TestCase):

    # __add__ with number basic test
    def test_01___add___m2x3_6items_with_number_0(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + 0
        self.assertAlmostEqual(m2.zero, m1.zero)
        m2_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])


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


class TestMatrixSparseMulNumber(unittest.TestCase):

    # __mul__ with number basic test
    def test_01___mul___m2x3_6items_to_number_1(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 * 1
        self.assertAlmostEqual(m2.zero, m1.zero)
        m2_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])


class TestMatrixSparseMulMatrix(unittest.TestCase):

    # __mul__ with matrix basic test
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
        self.assertAlmostEqual(m3.zero, m1.zero)
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


class TestMatrixSparseCompress(unittest.TestCase):

    # compress basic test
    def test_01_compress_m3x5_5items_with_optimal_compression(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = m1.compress()
        res = ((6, 1), 0.0, (8.1, 8.2, 6.3, 7.4, 8.5), (8, 8, 6, 7, 8), (0, 0, 0))
        self.assertEqual(vc, res)


class TestMatrixSparseDoi(unittest.TestCase):

    # doi basic test
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


class TestMatrixSparseDecompress(unittest.TestCase):

    # decompress basic test
    def test_01_decompress_m3x5_5items_with_optimal_compression(self):
        vc = ((6, 1), 0.0, (8.1, 8.2, 6.3, 7.4, 8.5), (8, 8, 6, 7, 8), (0, 0, 0))
        m1 = MatrixSparseImplementation.decompress(vc)
        m1_data = {(6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, 0.0)
        self.assertEqual(len(m1_data), len(m1))


if __name__ == '__main__':
    unittest.main()
