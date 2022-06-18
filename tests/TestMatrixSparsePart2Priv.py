import unittest
from MatrixSparseDOK import *

MatrixSparseImplementation = MatrixSparseDOK


# PRIVATE TESTS TO EXECUTE FOR EVALUATION


class TestMatrixSparseProperties(unittest.TestCase):

    # test matrix transporse of transporse property: (A’)’ = A
    def test_01_transpose_of_transpose(self):
        m1 = MatrixSparseDOK()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1.transpose()
        m3 = m2.transpose()
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertEqual(len(m1_data), len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])

    # test transpose compatibility with scalar multiplication: (kA)' = kA’
    def test_02_transpose_compatibility_with_scalar_multiplication(self):
        m1 = MatrixSparseDOK()
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + 5
        m2t = m2.transpose()
        m1t = m1.transpose()
        m3 = m1t + 5
        m2_m3_data = {(1, 1): 6.1, (2, 1): 6.2, (3, 1): 6.3, (1, 2): 7.1, (2, 2): 7.2, (3, 2): 7.3}
        self.assertAlmostEqual(m2t.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertEqual(len(m2_m3_data), len(m2t))
        self.assertEqual(len(m2_m3_data), len(m3))
        for key, value in m2_m3_data.items():
            self.assertAlmostEqual(value, m2t[Position(key[0], key[1])])
            self.assertAlmostEqual(value, m3[Position(key[0], key[1])])

    #  test transpose compatibility with addition: (A + B)’ = A’ + B’
    def test_03_transpose_compatibility_with_addition(self):
        m1 = MatrixSparseImplementation(1)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(1)
        m2_data = {(1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 + m2
        m3t = m3.transpose()
        m1t = m1.transpose()
        m2t = m2.transpose()
        m4 = m1t + m2t
        m3t_m4_data = {(1, 1): 1.1, (2, 1): 1.2, (3, 1): 2.6, (1, 2): 4.2, (2, 2): 2.2, (3, 2): 2.3}
        self.assertAlmostEqual(m3t.zero, m1.zero)
        self.assertAlmostEqual(m4.zero, m1.zero)
        self.assertEqual(len(m3t_m4_data), len(m3t))
        self.assertEqual(len(m3t_m4_data), len(m4))
        for key, value in m3t_m4_data.items():
            self.assertAlmostEqual(value, m3t[Position(key[0], key[1])])
            self.assertAlmostEqual(value, m4[Position(key[0], key[1])])

    #  test transpose compatibility with multiplication: (A * B)’ = B’ * A’
    def test_04_transpose_compatibility_with_multiplication(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1, (1, 2): 2, (1, 3): 3, (2, 1): 4, (2, 2): 5, (2, 3): 6}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation()
        m2_data = {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4, (3, 1): 5, (3, 2): 6}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 * m2
        m3t = m3.transpose()
        m1t = m1.transpose()
        m2t = m2.transpose()
        m4 = m2t * m1t
        m3t_m4_data = {(1, 1): 22, (2, 1): 28, (1, 2): 49, (2, 2): 64}
        self.assertAlmostEqual(m3t.zero, m1.zero)
        self.assertAlmostEqual(m4.zero, m1.zero)
        self.assertEqual(len(m3t_m4_data), len(m3t))
        self.assertEqual(len(m3t_m4_data), len(m4))
        for key, value in m3t_m4_data.items():
            self.assertAlmostEqual(value, m3t[Position(key[0], key[1])])
            self.assertAlmostEqual(value, m4[Position(key[0], key[1])])


class TestMatrixSparseIndividualFunctions(unittest.TestCase):

    # __iter__ test nested interations
    def test_01___iter___nested_iterations_m2x3_2items(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(1, 1): 1.1, (2, 3): 2.3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        i = 0
        for pos1 in m1:
            for pos2 in m1:
                i += 1
        self.assertEqual(i, 4, "failed exectution of nested interations")

    # __add__ test matrix with number 1 which results in items being null
    def test_02___add___m1x2_2items_with_number_1_resulting_in_null_items(self):
        m1 = MatrixSparseImplementation(2.2)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 + 1
        self.assertAlmostEqual(m2.zero, m1.zero)
        m2_data = {(1, 1): 2.1}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __add__ test matrix with matrix which results in items being null
    def test_03___add___m1x3_3items_with_m1x3_3items_resulting_in_null_items(self):
        m1 = MatrixSparseImplementation(4.0)
        m1_data = {(1, 1): 1, (1, 2): 2, (1, 3): 3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(4.0)
        m2_data = {(1, 1): 1, (1, 2): 2, (1, 3): 3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 + m2
        m3_data = {(1, 1): 2.0, (1, 3): 6.0}
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

    # __mul__ test matrix with number 1 which results in items being null
    def test_04___mul___m1x2_2items_with_number_1(self):
        m1 = MatrixSparseImplementation(2.2)
        m1_data = {(1, 1): 1.1, (1, 2): 1.2}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = m1 * 2
        self.assertAlmostEqual(m2.zero, m1.zero)
        m2_data = {(1, 2): 2.4}
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])
        self.assertAlmostEqual(m2.zero, m1.zero)
        self.assertEqual(len(m2_data), len(m2))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])

    # __mul__ test matrix with matrix which results in items being null
    def test_05___mul___m1x3_3items_with_m3x1_3items_resulting_in_null_items(self):
        m1 = MatrixSparseImplementation(14.0)
        m1_data = {(1, 1): 1, (1, 2): 2, (1, 3): 3}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        m2 = MatrixSparseImplementation(14.0)
        m2_data = {(1, 1): 1, (2, 1): 2, (3, 1): 3}
        for key, value in m2_data.items():
            m2[Position(key[0], key[1])] = value
        m3 = m1 * m2
        self.assertAlmostEqual(m3.zero, m1.zero)
        self.assertAlmostEqual(m3.zero, m2.zero)
        self.assertEqual(0, len(m3))
        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        for key, value in m2_data.items():
            self.assertAlmostEqual(value, m2[Position(key[0], key[1])])

    # eye test matrix 2x2 with unitary value same as zero value
    def test_06_eye_m2x2(self):
        m1 = MatrixSparseImplementation.eye(3, 4, 4)
        self.assertAlmostEqual(m1.zero, 4.0)
        self.assertEqual(0, len(m1))

    # compress basic test non-optimal compression with one negative offset
    def test_07_compress_m3x5_5items_non_optimal_compression_with_one_negative_offset(self):
        m1 = MatrixSparseImplementation()
        m1_data = {(6, 1): 6.1, (6, 5): 6.5, (7, 2): 7.2, (7, 5): 7.5, (8, 5): 8.5}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value
        vc = m1.compress()
        res = ((6, 1), 0.0, (6.1, 8.5, 7.2, 0.0, 6.5, 7.5), (6, 8, 7, -1, 6, 7), (0, 1, -3))
        self.assertEqual(res, vc)



class TestMatrixSparseLargeStructures(unittest.TestCase):

    # __eq__ test large matrices
    def test_01___eq___m1000x1000_9596items_random(self):
        seed = 100001

        def randint(a, b):
            nonlocal seed
            seed = (seed * 125) % 2796203
            return a + seed % (b - a + 1)

        vals = [Position(randint(1, 998), randint(1, 998)) for x in range(10000)]
        m1 = MatrixSparseImplementation(-1.0)
        m1[Position(0, 0)] = 1.0
        m1[Position(999, 999)] = 999.999
        m2 = MatrixSparseImplementation(-1.0)
        m2[Position(0, 0)] = 1.0
        m2[Position(999, 999)] = 999.999
        for i in vals:
            random = randint(1, 10000)
            m1[i] = random
            m2[i] = random
        self.assertEqual(m1, m2)

    # compress test for large matrix
    def test_02_compress_m100x100_102items_random(self):
        seed = 100001

        def randint(a, b):
            nonlocal seed
            seed = (seed * 125) % 2796203
            return a + seed % (b - a + 1)

        vals = [Position(randint(1, 98), randint(1, 98)) for x in range(100)]
        m1 = MatrixSparseImplementation(-1.0)
        m1[Position(0, 0)] = 1.0
        m1[Position(99, 99)] = 99.99
        for i in vals:
            random = randint(1, 100)
            m1[i] = random

        vc = m1.compress()

        res1 = ((0, 0), -1.0,
               (86.0, 10.0, 58.0, 94.0, 70.0, 61.0, 58.0, 39.0, 27.0, 40.0, 42.0, 82.0, 67.0, 69.0, 44.0, 55.0, 58.0,
                67.0, 42.0, 70.0, 40.0, 60.0, 69.0, 43.0, 93.0, 25.0, 65.0, 54.0, 1.0, 91.0, 92.0, 16.0, 20.0, 66.0,
                12.0, 36.0, 37.0, 76.0, 28.0, 46.0, 52.0, 5.0, 93.0, 40.0, 6.0, 19.0, 84.0, 100.0, 74.0, 94.0, 21.0,
                26.0, 85.0, 49.0, 57.0, 10.0, 62.0, 61.0, 91.0, 47.0, 26.0, 18.0, 44.0, 87.0, 1.0, 17.0, 51.0, 86.0,
                63.0, 73.0, 20.0, 50.0, 61.0, 22.0, 19.0, 55.0, 2.0, 31.0, 61.0, 56.0, 1.0, 27.0, 3.0, 24.0, 68.0, 31.0,
                57.0, 46.0, 29.0, 44.0, 79.0, 73.0, 72.0, 50.0, 65.0, 91.0, 82.0, 88.0, 18.0, 56.0, 56.0, 99.99, -1.0,
                -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                -1.0, -1.0, -1.0),
               (20, 81, 6, 5, 15, 17, 35, 71, 78, 23, 3, 35, 4, 63, 7, 12, 6, 63, 16, 32, 71, 15, 20, 6, 19, 4, 26, 20,
                0, 5, 23, 23, 61, 78, 73, 78, 33, 43, 96, 81, 42, 35, 62, 81, 19, 16, 63, 33, 81, 32, 39, 84, 12, 7, 62,
                42, 71, 39, 20, 5, 2, 43, 70, 70, 15, 26, 84, 86, 73, 17, 3, 9, 86, 61, 14, 22, 96, 24, 27, 37, 41, 44,
                45, 50, 51, 52, 56, 59, 66, 72, 17, 79, 80, 82, 83, 85, 87, 88, 92, 93, 97, 99, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1),
               (28, 0, -17, -5, -9, -19, -15, 8, 0, 54, 0, 0, -26, 0, 3, -24, -28, -4, 0, -43, -13, 0, -21, -55, 70, 0,
                15, 5, 0, 0, 0, 0, -7, -6, 0, -47, 0, -3, 0, 10, 0, 14, 35, -20, 20, 48, 0, 0, 0, 0, 5, 66, 29, 0, 0, 0,
                36, 0, 0, 4, 0, 21, -21, -28, 0, 0, 57, 0, 0, 0, 13, -15, -2, 1, 0, 0, 0, 0, -36, 37, 51, -40, 48, 4,
                -31, 50, 35, 91, 3, 0, 0, 0, 82, 5, 0, 0, -20, 23, 0, 2))

        res2 = ((0, 0), -1.0,
               (86.0, 10.0, 58.0, 94.0, 70.0, 61.0, 58.0, 39.0, 27.0, 40.0, 42.0, 82.0, 67.0, 69.0, 44.0, 55.0, 58.0,
                67.0, 42.0, 70.0, 40.0, 60.0, 69.0, 43.0, 93.0, 25.0, 65.0, 54.0, 1.0, 91.0, 92.0, 16.0, 20.0, 66.0,
                12.0, 36.0, 37.0, 76.0, 28.0, 46.0, 52.0, 5.0, 93.0, 40.0, 6.0, 19.0, 84.0, 100.0, 74.0, 94.0, 21.0,
                26.0, 85.0, 49.0, 57.0, 10.0, 62.0, 61.0, 91.0, 47.0, 26.0, 18.0, 44.0, 87.0, 1.0, 17.0, 51.0, 86.0,
                63.0, 73.0, 20.0, 50.0, 61.0, 22.0, 19.0, 55.0, 2.0, 31.0, 61.0, 56.0, 1.0, 27.0, 3.0, 24.0, 68.0, 31.0,
                57.0, 46.0, 29.0, 44.0, 79.0, 73.0, 72.0, 50.0, 65.0, 91.0, 82.0, 88.0, 18.0, 56.0, 56.0, 99.99),
               (20, 81, 6, 5, 15, 17, 35, 71, 78, 23, 3, 35, 4, 63, 7, 12, 6, 63, 16, 32, 71, 15, 20, 6, 19, 4, 26, 20,
                0, 5, 23, 23, 61, 78, 73, 78, 33, 43, 96, 81, 42, 35, 62, 81, 19, 16, 63, 33, 81, 32, 39, 84, 12, 7, 62,
                42, 71, 39, 20, 5, 2, 43, 70, 70, 15, 26, 84, 86, 73, 17, 3, 9, 86, 61, 14, 22, 96, 24, 27, 37, 41, 44,
                45, 50, 51, 52, 56, 59, 66, 72, 17, 79, 80, 82, 83, 85, 87, 88, 92, 93, 97, 99),
               (28, 0, -17, -5, -9, -19, -15, 8, 0, 54, 0, 0, -26, 0, 3, -24, -28, -4, 0, -43, -13, 0, -21, -55, 70, 0,
                15, 5, 0, 0, 0, 0, -7, -6, 0, -47, 0, -3, 0, 10, 0, 14, 35, -20, 20, 48, 0, 0, 0, 0, 5, 66, 29, 0, 0, 0,
                36, 0, 0, 4, 0, 21, -21, -28, 0, 0, 57, 0, 0, 0, 13, -15, -2, 1, 0, 0, 0, 0, -36, 37, 51, -40, 48, 4,
                -31, 50, 35, 91, 3, 0, 0, 0, 82, 5, 0, 0, -20, 23, 0, 2))

        if vc == res1:
            self.assertEqual(vc, res1)
        else:
            self.assertEqual(vc, res2)

    # doi test for large matrix
    def test_03_doi_m100x100_102items_random(self):
        m1 = MatrixSparseImplementation(-1.0)
        m1_data = {(0, 0): 1.0, (99, 99): 99.99, (56, 50): 57.0, (81, 83): 40.0, (41, 66): 1.0, (23, 64): 40.0,
                   (23, 86): 16.0, (7, 6): 44.0, (84, 82): 26.0, (42, 20): 10.0, (63, 45): 67.0, (70, 50): 87.0,
                   (32, 56): 94.0, (78, 71): 36.0, (81, 41): 10.0, (88, 94): 88.0, (16, 73): 19.0, (3, 75): 20.0,
                   (24, 7): 31.0, (15, 88): 1.0, (33, 42): 37.0, (5, 48): 91.0, (22, 96): 55.0, (17, 94): 79.0,
                   (45, 34): 3.0, (62, 63): 93.0, (15, 28): 70.0, (72, 91): 44.0, (35, 53): 58.0, (39, 40): 21.0,
                   (80, 41): 72.0, (4, 34): 25.0, (78, 44): 27.0, (2, 77): 26.0, (5, 22): 94.0, (97, 77): 56.0,
                   (42, 5): 52.0, (63, 41): 69.0, (92, 16): 18.0, (73, 67): 63.0, (61, 52): 22.0, (19, 67): 93.0,
                   (12, 78): 85.0, (43, 57): 76.0, (93, 94): 56.0, (32, 26): 70.0, (9, 17): 50.0, (43, 81): 18.0,
                   (63, 74): 84.0, (20, 71): 91.0, (62, 75): 57.0, (96, 58): 28.0, (35, 88): 5.0, (71, 71): 62.0,
                   (82, 45): 50.0, (20, 40): 54.0, (33, 53): 100.0, (5, 78): 47.0, (35, 58): 82.0, (71, 35): 40.0,
                   (81, 88): 74.0, (39, 47): 61.0, (52, 56): 31.0, (79, 54): 73.0, (26, 50): 17.0, (17, 73): 73.0,
                   (37, 82): 56.0, (23, 85): 92.0, (6, 38): 43.0, (78, 69): 66.0, (51, 18): 68.0, (85, 45): 91.0,
                   (87, 5): 82.0, (3, 15): 42.0, (86, 32): 86.0, (20, 13): 86.0, (73, 33): 12.0, (59, 83): 46.0,
                   (50, 78): 24.0, (19, 87): 6.0, (20, 35): 69.0, (83, 90): 65.0, (16, 46): 42.0, (7, 45): 49.0,
                   (17, 9): 61.0, (6, 17): 58.0, (12, 41): 55.0, (96, 96): 2.0, (70, 49): 44.0, (26, 11): 65.0,
                   (66, 31): 29.0, (84, 97): 51.0, (6, 31): 58.0, (14, 71): 19.0, (27, 73): 61.0, (44, 61): 27.0,
                   (71, 22): 39.0, (61, 11): 20.0, (4, 21): 67.0, (15, 45): 60.0, (86, 37): 61.0, (81, 79): 46.0}
        for key, value in m1_data.items():
            m1[Position(key[0], key[1])] = value

        vc = ((0, 0), -1.0,
               (86.0, 10.0, 58.0, 94.0, 70.0, 61.0, 58.0, 39.0, 27.0, 40.0, 42.0, 82.0, 67.0, 69.0, 44.0, 55.0, 58.0,
                67.0, 42.0, 70.0, 40.0, 60.0, 69.0, 43.0, 93.0, 25.0, 65.0, 54.0, 1.0, 91.0, 92.0, 16.0, 20.0, 66.0,
                12.0, 36.0, 37.0, 76.0, 28.0, 46.0, 52.0, 5.0, 93.0, 40.0, 6.0, 19.0, 84.0, 100.0, 74.0, 94.0, 21.0,
                26.0, 85.0, 49.0, 57.0, 10.0, 62.0, 61.0, 91.0, 47.0, 26.0, 18.0, 44.0, 87.0, 1.0, 17.0, 51.0, 86.0,
                63.0, 73.0, 20.0, 50.0, 61.0, 22.0, 19.0, 55.0, 2.0, 31.0, 61.0, 56.0, 1.0, 27.0, 3.0, 24.0, 68.0, 31.0,
                57.0, 46.0, 29.0, 44.0, 79.0, 73.0, 72.0, 50.0, 65.0, 91.0, 82.0, 88.0, 18.0, 56.0, 56.0, 99.99),
               (20, 81, 6, 5, 15, 17, 35, 71, 78, 23, 3, 35, 4, 63, 7, 12, 6, 63, 16, 32, 71, 15, 20, 6, 19, 4, 26, 20,
                0, 5, 23, 23, 61, 78, 73, 78, 33, 43, 96, 81, 42, 35, 62, 81, 19, 16, 63, 33, 81, 32, 39, 84, 12, 7, 62,
                42, 71, 39, 20, 5, 2, 43, 70, 70, 15, 26, 84, 86, 73, 17, 3, 9, 86, 61, 14, 22, 96, 24, 27, 37, 41, 44,
                45, 50, 51, 52, 56, 59, 66, 72, 17, 79, 80, 82, 83, 85, 87, 88, 92, 93, 97, 99),
               (28, 0, -17, -5, -9, -19, -15, 8, 0, 54, 0, 0, -26, 0, 3, -24, -28, -4, 0, -43, -13, 0, -21, -55, 70, 0,
                15, 5, 0, 0, 0, 0, -7, -6, 0, -47, 0, -3, 0, 10, 0, 14, 35, -20, 20, 48, 0, 0, 0, 0, 5, 66, 29, 0, 0, 0,
                36, 0, 0, 4, 0, 21, -21, -28, 0, 0, 57, 0, 0, 0, 13, -15, -2, 1, 0, 0, 0, 0, -36, 37, 51, -40, 48, 4,
                -31, 50, 35, 91, 3, 0, 0, 0, 82, 5, 0, 0, -20, 23, 0, 2))

        dim = m1.dim()
        for r in range( dim[0][0], dim[1][0]+1 ):
            for c in range(dim[0][1], dim[1][1]+1):
                self.assertAlmostEqual(MatrixSparseImplementation.doi(vc, Position(r, c)), m1[Position(r, c)])

    # decompress test for large matrix
    def test_04_decompress_m100x100_102items_random(self):
        res = ((0, 0), -1.0,
               (86.0, 10.0, 58.0, 94.0, 70.0, 61.0, 58.0, 39.0, 27.0, 40.0, 42.0, 82.0, 67.0, 69.0, 44.0, 55.0, 58.0,
                67.0, 42.0, 70.0, 40.0, 60.0, 69.0, 43.0, 93.0, 25.0, 65.0, 54.0, 1.0, 91.0, 92.0, 16.0, 20.0, 66.0,
                12.0, 36.0, 37.0, 76.0, 28.0, 46.0, 52.0, 5.0, 93.0, 40.0, 6.0, 19.0, 84.0, 100.0, 74.0, 94.0, 21.0,
                26.0, 85.0, 49.0, 57.0, 10.0, 62.0, 61.0, 91.0, 47.0, 26.0, 18.0, 44.0, 87.0, 1.0, 17.0, 51.0, 86.0,
                63.0, 73.0, 20.0, 50.0, 61.0, 22.0, 19.0, 55.0, 2.0, 31.0, 61.0, 56.0, 1.0, 27.0, 3.0, 24.0, 68.0, 31.0,
                57.0, 46.0, 29.0, 44.0, 79.0, 73.0, 72.0, 50.0, 65.0, 91.0, 82.0, 88.0, 18.0, 56.0, 56.0, 99.99),
               (20, 81, 6, 5, 15, 17, 35, 71, 78, 23, 3, 35, 4, 63, 7, 12, 6, 63, 16, 32, 71, 15, 20, 6, 19, 4, 26, 20,
                0, 5, 23, 23, 61, 78, 73, 78, 33, 43, 96, 81, 42, 35, 62, 81, 19, 16, 63, 33, 81, 32, 39, 84, 12, 7, 62,
                42, 71, 39, 20, 5, 2, 43, 70, 70, 15, 26, 84, 86, 73, 17, 3, 9, 86, 61, 14, 22, 96, 24, 27, 37, 41, 44,
                45, 50, 51, 52, 56, 59, 66, 72, 17, 79, 80, 82, 83, 85, 87, 88, 92, 93, 97, 99),
               (28, 0, -17, -5, -9, -19, -15, 8, 0, 54, 0, 0, -26, 0, 3, -24, -28, -4, 0, -43, -13, 0, -21, -55, 70, 0,
                15, 5, 0, 0, 0, 0, -7, -6, 0, -47, 0, -3, 0, 10, 0, 14, 35, -20, 20, 48, 0, 0, 0, 0, 5, 66, 29, 0, 0, 0,
                36, 0, 0, 4, 0, 21, -21, -28, 0, 0, 57, 0, 0, 0, 13, -15, -2, 1, 0, 0, 0, 0, -36, 37, 51, -40, 48, 4,
                -31, 50, 35, 91, 3, 0, 0, 0, 82, 5, 0, 0, -20, 23, 0, 2))

        m1 = MatrixSparseImplementation.decompress(res)

        m1_data = {(0, 0): 1.0, (99, 99): 99.99, (56, 50): 57.0, (81, 83): 40.0, (41, 66): 1.0, (23, 64): 40.0,
                   (23, 86): 16.0, (7, 6): 44.0, (84, 82): 26.0, (42, 20): 10.0, (63, 45): 67.0, (70, 50): 87.0,
                   (32, 56): 94.0, (78, 71): 36.0, (81, 41): 10.0, (88, 94): 88.0, (16, 73): 19.0, (3, 75): 20.0,
                   (24, 7): 31.0, (15, 88): 1.0, (33, 42): 37.0, (5, 48): 91.0, (22, 96): 55.0, (17, 94): 79.0,
                   (45, 34): 3.0, (62, 63): 93.0, (15, 28): 70.0, (72, 91): 44.0, (35, 53): 58.0, (39, 40): 21.0,
                   (80, 41): 72.0, (4, 34): 25.0, (78, 44): 27.0, (2, 77): 26.0, (5, 22): 94.0, (97, 77): 56.0,
                   (42, 5): 52.0, (63, 41): 69.0, (92, 16): 18.0, (73, 67): 63.0, (61, 52): 22.0, (19, 67): 93.0,
                   (12, 78): 85.0, (43, 57): 76.0, (93, 94): 56.0, (32, 26): 70.0, (9, 17): 50.0, (43, 81): 18.0,
                   (63, 74): 84.0, (20, 71): 91.0, (62, 75): 57.0, (96, 58): 28.0, (35, 88): 5.0, (71, 71): 62.0,
                   (82, 45): 50.0, (20, 40): 54.0, (33, 53): 100.0, (5, 78): 47.0, (35, 58): 82.0, (71, 35): 40.0,
                   (81, 88): 74.0, (39, 47): 61.0, (52, 56): 31.0, (79, 54): 73.0, (26, 50): 17.0, (17, 73): 73.0,
                   (37, 82): 56.0, (23, 85): 92.0, (6, 38): 43.0, (78, 69): 66.0, (51, 18): 68.0, (85, 45): 91.0,
                   (87, 5): 82.0, (3, 15): 42.0, (86, 32): 86.0, (20, 13): 86.0, (73, 33): 12.0, (59, 83): 46.0,
                   (50, 78): 24.0, (19, 87): 6.0, (20, 35): 69.0, (83, 90): 65.0, (16, 46): 42.0, (7, 45): 49.0,
                   (17, 9): 61.0, (6, 17): 58.0, (12, 41): 55.0, (96, 96): 2.0, (70, 49): 44.0, (26, 11): 65.0,
                   (66, 31): 29.0, (84, 97): 51.0, (6, 31): 58.0, (14, 71): 19.0, (27, 73): 61.0, (44, 61): 27.0,
                   (71, 22): 39.0, (61, 11): 20.0, (4, 21): 67.0, (15, 45): 60.0, (86, 37): 61.0, (81, 79): 46.0}

        for key, value in m1_data.items():
            self.assertAlmostEqual(value, m1[Position(key[0], key[1])])
        self.assertAlmostEqual(m1.zero, -1.0)
        self.assertEqual(len(m1_data), len(m1))


if __name__ == '__main__':
    unittest.main()
