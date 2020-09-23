import unittest
from hypothesis import given
from hypothesis.strategies import floats, text, lists, characters, integers
from ex4 import dot_prod, matrix_vector_prod, pythagorean_triples, \
    max_length, count_even, count_above


def dp(u, v):
    """
    Return the dot product of u and v

    @param list[float] u: vector of floats
    @param list[float] v: vector of floats
    @rtype: float
    """
    assert len(u) == len(v)
    # sum of products of pairs of corresponding coordinates of u and v
    return sum([u_coord * v_coord for u_coord, v_coord in zip(u, v)])


def mvp(m, u):
    """
    Return the matrix-vector product of m x u

    @param list[list[float]] m: matrix
    @param list[float] u: vector
    @rtype: list[float]
    """
    return [dp(v, u) for v in m]


def pt(n):
    """
    Return list of pythagorean triples as non-descending tuples
    of ints from 1 to n.

    Assume n is positive.

    @param int n: upper bound of pythagorean triples
    """
    # helper to check whether a triple is pythagorean and non_descending
    # you could also use a lambda instead of this nested function def.
    def _ascending_pythagorean(t):
        # """
        # Return whether t is pythagorean and non-descending.
        #
        # @param tuple[int] t: triple of integers to check
        # """
        return (t[0] <= t[1] <= t[2]) and (t[0]**2 + t[1]**2) == t[2]**2

    # filter just the ones that satisfy ascending_pythagorean
    # produce a list from the filter for ascending_pythagoreans from...
    return list(filter(_ascending_pythagorean,
                       # ...list of all triples in the range 1..n
                       [(i, j, k)
                        for i in range(1, n + 1)
                        for j in range(1, n + 1)
                        for k in range(1, n + 1)]))


class TestDotProduct(unittest.TestCase):
    @given(lists(elements=floats(min_value=0.0, max_value=100.0),
                 min_size=10, max_size=10),
           lists(elements=floats(min_value=0.0, max_value=50.0),
                 min_size=10, max_size=10))
    def test_dot_product(self, u, v):
        self.assertEqual(dp(u, v), dot_prod(u, v))


class TestMatrixVectorProduct(unittest.TestCase):
    @given(lists(elements=lists(elements=floats(min_value=0.0, max_value=100.0),
                 min_size=10, max_size=10), min_size=2, max_size=20),
           lists(elements=floats(min_value=0.0, max_value=50.0),
                 min_size=10, max_size=10))
    def test_matrix_vector_product(self, u, v):
        self.assertEqual(mvp(u, v), matrix_vector_prod(u, v))


class TestPythagoreanTriples(unittest.TestCase):
    @given(integers(min_value=0, max_value=30))
    def test_pythagorean_triples(self, n):
        self.assertEqual(pt(n), pythagorean_triples(n))


class TestMaxLength(unittest.TestCase):
    def test_empty_list(self):
        obj = []
        self.assertEqual(max_length(obj), 0)

    @given(integers(min_value=-30, max_value=30),
           text(min_size=0, max_size=10))
    def test_object(self, obj1, obj2):
        self.assertEqual(max_length(obj1), 0)
        self.assertEqual(max_length(obj2), 0)

    @given(lists(elements=integers(), min_size=3, max_size=10),
           lists(elements=characters(), min_size=3, max_size=10))
    def test_nonnested_list(self, obj1, obj2):
        self.assertEqual(max_length(obj1), len(obj1))
        self.assertEqual(max_length(obj2), len(obj2))

    def test_nested_list(self):
        lst_int = [1, [2], 6, [9, 7]]
        lst_char = ['a', ['b', 'c'], ['d']]
        mixed1 = [1, ['a', 'b'], 2, [3, [4, 'c', ['d']]]]
        mixed2 = [1, ['a', 'b', 'c', 'd'], [2, [3, 4]]]
        self.assertEqual(max_length(lst_int), 4)
        self.assertEqual(max_length(lst_char), 3)
        self.assertEqual(max_length(mixed1), 4)
        self.assertEqual(max_length(mixed2), 4)


class TestCountEven(unittest.TestCase):
    def test_empty_list(self):
        obj = []
        self.assertEqual(count_even(obj), 0)

    @given(integers(min_value=0, max_value=30))
    def test_object(self, obj):
        if obj % 2 == 0:
            self.assertEqual(count_even(obj), 1)
        else:
            self.assertEqual(count_even(obj), 0)

    def test_nonnested_list(self):
        obj1 = [2, 4, 6, 8, 10]
        obj2 = [1, 3, 5, 7, 9]
        obj3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(count_even(obj1), 5)
        self.assertEqual(count_even(obj2), 0)
        self.assertEqual(count_even(obj3), 5)

    def test_nested_list(self):
        lst1 = [1, [2], 6, [9, 7], 10, 23, [65, 79], 24]
        self.assertEqual(count_even(lst1), 4)
        lst2 = [3, 1, [43, 55], [127535, [127535, 4323]], 5]
        self.assertEqual(count_even(lst2), 0)
        lst3 = [0, 0, 0, [[0, [[0, 0], 0], 0], 0], 0]
        self.assertEqual(count_even(lst3), 10)
        lst4 = [[[[]]], [[]], []]
        self.assertEqual(count_even(lst4), 0)


class TestCountAbove(unittest.TestCase):
    @given(integers(min_value=1, max_value=10))
    def test_empty_list(self, n):
        obj = []
        self.assertEqual(count_above(obj, n), 0)

    @given(integers(min_value=1, max_value=10),
           integers(min_value=5, max_value=30))
    def test_object(self, n, obj):
        if n >= obj:
            self.assertEqual(count_above(obj, n), 0)
        else:
            self.assertEqual(count_above(obj, n), 1)

    def test_nonnested_list(self):
        obj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        obj3 = [5, 344, 38852, 324325342]

        self.assertEqual(count_above(obj1, 5), 5)
        self.assertEqual(count_above(obj3, 324325342), 0)
        self.assertEqual(count_above(obj3, 4), 4)

    def test_nested_list(self):
        lst1 = [1, [2], 6, [9, 7], 10, 23, [65, 79], 24]
        self.assertEqual(count_above(lst1, 30), 2)
        self.assertEqual(count_above(lst1, 100), 0)
        self.assertEqual(count_above(lst1, 0), 10)
        lst2 = [5, 4, 38, [[2, 3], 5], 38]
        self.assertEqual(count_above(lst2, 5), 2)
        self.assertEqual(count_above(lst2, 38), 0)


if __name__ == '__main__':
    unittest.main()
