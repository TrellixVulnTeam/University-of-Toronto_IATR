"""
Test loop and comprehension implementations.
"""

import unittest

from ex4 import dot_prod, matrix_vector_prod, pythagorean_triples
# from loop import dot_prod, matrix_vector_prod, pythagorean_triples


class DotProductTester(unittest.TestCase):
    def setUp(self: unittest.TestCase) -> None:
        self._zero_vector = [0.0, 0.0, 0.0]
        self._non_zero_vector_1 = [1.0, 2.0, 3.0]
        self._non_zero_vector_2 = [5.0, 6.0]

    def tearDown(self: unittest.TestCase) -> None:
        self._zero_vector = None
        self._non_zero_vector = None

    def test_zero_case(self: unittest.TestCase) -> bool:
        """Dot product of zero vectors is zero?"""
        self.assertEqual(dot_prod(self._zero_vector, self._zero_vector), 0.0)

    def test_regular_case(self: unittest.TestCase) -> bool:
        """Dot product of non-zero vectors"""
        self.assertEqual(dot_prod(self._non_zero_vector_2, self._non_zero_vector_2),
                         61.0)


class MatrixVectorProductTester(unittest.TestCase):
    def setUp(self: unittest.TestCase) -> None:
        self._identity_matrix = [[1, 0], [0, 1]]
        self._zero_vector = [0.0, 0.0]

    def tearDown(self: unittest.TestCase) -> None:
        self._identity_matrix = None
        self._zero_vector = None

    def test_zero_case(self: unittest.TestCase) -> bool:
        """Identity times zero matrix is zero"""
        self.assertEqual(matrix_vector_prod(self._identity_matrix,
                                            self._zero_vector),
                         self._zero_vector)


class PythagoreanTripleTester(unittest.TestCase):
    def test_10(self: unittest.TestCase) -> None:
        """triples up to 10"""
        self.assertEqual(set(pythagorean_triples(10)), {(3, 4, 5), (6, 8, 10)})


if __name__ == '__main__':
    unittest.main(exit=False)
