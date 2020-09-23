import unittest
from ex7 import BinaryTree, parenthesize, list_longest_path, list_between, count_shallower
from hypothesis import given
from hypothesis.strategies import integers, lists, floats
from random import randint


class TestPR(unittest.TestCase):
    @given(floats(min_value=0.0, max_value=20.0))
    def test_single_node(self, num):
        b = BinaryTree(num)
        self.assertEqual(parenthesize(b), str(num))


class TestLLP(unittest.TestCase):
    def test_empty(self):
        b = None
        self.assertEqual(list_longest_path(b), [])

    def test_one_node(self):
        num = randint(0, 20)
        b = BinaryTree(num)
        self.assertEqual(list_longest_path(b), [num])

    @given(lists(elements=integers(), min_size=6, max_size=6))
    def test_recursion(self, lst):
        b1 = BinaryTree(lst[0], BinaryTree(lst[1]))
        b2 = BinaryTree(lst[3])
        b = BinaryTree(lst[5], b1, b2)
        self.assertEqual(list_longest_path(b), [lst[5], lst[0], lst[1]])


class TestLB(unittest.TestCase):
    @given(integers(max_value=10), integers(min_value=11))
    def test_empty(self, start, end):
        b = None
        self.assertEqual(list_between(b, start, end), [])

    def test_one_node(self):
        num = randint(0, 20)
        b = BinaryTree(num)
        self.assertEqual(list_between(b, 0, 20), [num])
        self.assertEqual(list_between(b, 21, 30), [])

    def test_recursion(self):
        b_left = BinaryTree(4, BinaryTree(2), BinaryTree(6))
        b_right = BinaryTree(12, BinaryTree(10), BinaryTree(14))
        b = BinaryTree(8, b_left, b_right)
        self.assertEqual(list_between(b, 0, 1), [])
        self.assertEqual(list_between(b, 14, 15), [14])


class TestCS(unittest.TestCase):
    def test_empty(self):
        depth = randint(0, 10)
        b = None
        self.assertEqual(count_shallower(b, depth), 0)

    def test_one_node(self):
        depth = randint(1, 10)
        num = randint(0, 10)
        b = BinaryTree(num)
        self.assertEqual(count_shallower(b, depth), 1)
        self.assertEqual(count_shallower(b, 0), 0)

    @given(lists(elements=integers(), min_size=6, max_size=6))
    def test_recursion(self, lst):
        b1 = BinaryTree(lst[0], BinaryTree(lst[1]))
        b2 = BinaryTree(lst[3])
        b = BinaryTree(lst[5], b1, b2)
        self.assertEqual(count_shallower(b, 2), 3)
        self.assertEqual(count_shallower(b, 3), 4)
        self.assertEqual(count_shallower(b, 0), 0)


if __name__ == '__main__':
    unittest.main()
