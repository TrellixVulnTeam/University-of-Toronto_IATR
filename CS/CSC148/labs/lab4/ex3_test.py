"""ex3 unittest

"""
import unittest
from hypothesis import given
from hypothesis.strategies import integers, text, lists, characters
from ex4 import max_length, count_even, count_above


class TestListAll(unittest.TestCase):
    def test_empty_list(self):
        obj = []
        self.assertEqual(list_all(obj), [])

    @given(integers(min_value=-30, max_value=30),
           text(min_size=0, max_size=10))
    def test_object(self, obj1, obj2):
        self.assertEqual(list_all(obj1), [obj1])
        self.assertEqual(list_all(obj2), [obj2])

    @given(lists(elements=integers(), min_size=3, max_size=10),
           lists(elements=characters(), min_size=3, max_size=10))
    def test_nonnested_list(self, obj1, obj2):
        self.assertEqual(list_all(obj1), obj1)
        self.assertEqual(list_all(obj2), obj2)

    def test_nested_list(self):
        lst_int = [1, [2], 6, [9, 7]]
        lst_char = ['a', ['b', 'c'], ['d']]
        obj = [1, ['a', 'b'], 2, [3, [4, 'c', ['d']]]]
        lst = [1, 'a', 'b', 2, 3, 4, 'c', 'd']
        self.assertEqual(list_all(lst_int), [1, 2, 6, 9, 7])
        self.assertEqual(list_all(lst_char), ['a', 'b', 'c', 'd'])
        self.assertEqual(list_all(obj), lst)


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


class TestListOver(unittest.TestCase):
    @given(integers(min_value=1, max_value=10))
    def test_empty_list(self, n):
        obj = []
        self.assertEqual(list_over(obj, n), [])

    @given(text(min_size=0, max_size=10),
           integers(min_value=1, max_value=5))
    def test_object(self, obj, n):
        l = len(obj)
        if l > n:
            self.assertEqual(list_over(obj, n), [obj])
        else:
            self.assertEqual(list_over(obj, n), [])

    @given(lists(elements=text(max_size=10), min_size=0, max_size=20),
           lists(elements=text(min_size=16, max_size=20),
                 min_size=0, max_size=20),
           integers(min_value=10, max_value=15))
    def test_nonnested_list(self, obj1, obj3, n):
        self.assertEqual(list_over(obj1, n), [])
        obj2 = ['a', 'ape', 'apple', 'acceleration', 'accumulator']
        self.assertEqual(list_over(obj2, 5), ['acceleration', 'accumulator'])
        self.assertEqual(list_over(obj3, n), obj3)

    def test_nested_list(self):
        obj = ['a', ['ape', ['apple']], ['appendix',
               'acceleration', 'accumulator'], 'affectionate', ['asterisk']]
        result = ['acceleration', 'accumulator', 'affectionate']
        self.assertEqual(list_over(obj, 8), result)


class TestListEven(unittest.TestCase):
    def test_empty_list(self):
        obj = []
        self.assertEqual(list_even(obj), [])

    @given(integers(min_value=0, max_value=30))
    def test_object(self, obj):
        if obj % 2 == 0:
            self.assertEqual(list_even(obj), [obj])
        else:
            self.assertEqual(list_even(obj), [])

    def test_nonnested_list(self):
        obj1 = [2, 4, 6, 8, 10]
        obj2 = [1, 3, 5, 7, 9]
        obj3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(list_even(obj1), obj1)
        self.assertEqual(list_even(obj2), [])
        self.assertEqual(list_even(obj3), obj1)

    def test_nested_list(self):
        lst1 = [1, [2], 6, [9, 7], 10, 23, [65, 79], 24]
        self.assertEqual(list_even(lst1), [2, 6, 10, 24])
        lst2 = [3, 1, [44, 55], [127535, [127535, 4323]], 5]
        self.assertEqual(list_even(lst2), [44])
        lst3 = [0, 0, 0, [[0, [[0, 0], 0], 0], 0], 0]
        self.assertEqual(list_even(lst3), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        lst4 = [[[[]]],[[]],[]]
        self.assertEqual(list_even(lst4), [])


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


class TestCountAll(unittest.TestCase):
    def test_empty_list(self):
        obj = []
        self.assertEqual(count_all(obj), 0)

    @given(integers(min_value=-30, max_value=30),
           text(min_size=0, max_size=10))
    def test_object(self, obj1, obj2):
        self.assertEqual(count_all(obj1), 1)
        self.assertEqual(count_all(obj2), 1)

    @given(lists(elements=integers(), min_size=3, max_size=10),
           lists(elements=characters(), min_size=3, max_size=10))
    def test_nonnested_list(self, obj1, obj2):
        self.assertEqual(count_all(obj1), len(obj1))
        self.assertEqual(count_all(obj2), len(obj2))

    def test_nested_list(self):
        lst1 = [1, [2], 6, [9, 7], 10, 23, [65, [79]], 24]
        self.assertEqual(count_all(lst1), 10)
        lst2 = [3, 1, [43, 55], [127535, [127535, 4323]], 5]
        self.assertEqual(count_all(lst2), 8)
        lst3 = [0, 0, 0, [[0, [[0, 0], 0], 0], 0], 0]
        self.assertEqual(count_all(lst3), 10)
        lst4 = [[[[]]], [[]], []]
        self.assertEqual(count_all(lst4), 0)


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
