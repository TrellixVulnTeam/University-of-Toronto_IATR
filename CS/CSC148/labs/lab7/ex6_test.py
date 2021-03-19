import unittest
from ex6 import (Tree, descendants_from_list, list_internal, arity,
                 contains_test_passer, list_if, count)
from hypothesis import given
from hypothesis.strategies import integers, lists
from random import randint
from math import ceil


class TestListInternal(unittest.TestCase):
    def test_empty_tree(self):
        t = Tree()
        self.assertEqual(list_internal(t), [])

    def test_one_node(self):
        v = randint(0, 10)
        t = Tree(v)
        self.assertEqual(list_internal(t), [])

    @given(lists(elements=integers(min_value=0, max_value=30),
                 min_size=5, max_size=13))
    def test_height_three(self, lst):
        t = descendants_from_list(Tree(lst[0]), lst[1:], 3)
        num = ceil((len(lst) - 4) / 3)
        l1 = list_internal(t)
        l1.sort()
        l2 = lst[:num + 1]
        l2.sort()
        self.assertEqual(l1, l2)

    @given(lists(elements=integers(min_value=0, max_value=30),
                 min_size=41, max_size=121))
    def test_height_five(self, lst):
        t = descendants_from_list(Tree(lst[0]), lst[1:], 3)
        num = ceil((len(lst) - 40) / 3)
        l1 = list_internal(t)
        l1.sort()
        l2 = lst[:num + 13]
        l2.sort()
        self.assertEqual(l1, l2)


class TestArity(unittest.TestCase):
    def test_empty_tree(self):
        t = Tree()
        self.assertEqual(arity(t), 0)

    def test_one_node(self):
        v = randint(0, 10)
        t = Tree(v)
        self.assertEqual(arity(t), 0)

    @given(lists(elements=integers(min_value=12, max_value=30),
                 min_size=9, max_size=20),
           lists(elements=integers(min_value=2, max_value=8),
                 min_size=1, max_size=2))
    def testRecursiveStep(self, lst, lst_branch):
        t = Tree(0)
        for i in lst_branch:
            new_t = descendants_from_list(Tree(0), lst, i)
            t.children.append(new_t)
        self.assertEqual(arity(t), max(lst_branch))


class TestContainsTestPassr(unittest.TestCase):
    def test_one_node(self):
        t = Tree(5)
        test = lambda num: num % 2 != 0
        self.assertEqual(contains_test_passer(t, test), True)

    @given(lists(elements=integers(min_value=1, max_value=30),
                 min_size=9, max_size=20))
    def testRecursiveStep(self, lst):
        odd = list(map(lambda x: x * 2 + 1, lst))
        even = list(map(lambda x: x * 2, lst))
        t_odd = Tree(0)
        t_even = Tree(0)
        descendants_from_list(t_odd, odd, 3)
        descendants_from_list(t_even, even, 4)
        test = lambda num: num % 2 != 0  # this means return True if num is odd
        self.assertEqual(contains_test_passer(t_even, test), False)
        self.assertEqual(contains_test_passer(t_odd, test), True)


class TestListIf(unittest.TestCase):
    def test_one_node(self):
        v = randint(0, 10)
        t = Tree(v)
        p = lambda x: x % 2 != 0
        self.assertEqual(list_if(t, p), [v] if p(v) else [])

    @given(lists(elements=integers(min_value=1, max_value=30),
                 min_size=9, max_size=20))
    def testRecursiveStep(self, lst):
        odd = list(map(lambda x: x * 2 + 1, lst))
        even = list(map(lambda x: x * 2, lst))
        t_odd = Tree(0)
        t_even = Tree(0)
        descendants_from_list(t_odd, odd, 3)
        descendants_from_list(t_even, even, 4)
        p = lambda x: x % 2 != 0  # this means return True if num is odd
        l1 = list_if(t_even, p)
        l2 = list_if(t_odd, p)
        l1.sort()
        l2.sort()
        odd.sort()
        self.assertEqual(l1, [])
        self.assertEqual(l2, odd)


class TestCount(unittest.TestCase):
    def test_empty_tree(self):
        t = Tree()
        self.assertEqual(count(t), 1)

    def test_one_node(self):
        v = randint(0, 10)
        t = Tree(v)
        self.assertEqual(count(t), 1)

    @given(lists(elements=integers(min_value=3, max_value=30),
                 min_size=9, max_size=20))
    def testRecursiveStep(self, lst):
        t = Tree(0)
        descendants_from_list(t, lst, 3)
        self.assertEqual(count(t), len(lst) + 1)

if __name__ == '__main__':
    unittest.main()
