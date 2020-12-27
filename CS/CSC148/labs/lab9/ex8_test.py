import unittest
from ex8 import BinaryTree, LinkedListNode, LinkedList
from hypothesis import given
from hypothesis.strategies import integers, lists, floats
from random import randint


class Queue:
    ''' Represent a FIFO queue.
    '''

    def __init__(self):
        ''' (Queue) -> NoneType

        Create and initialize new queue self.
        '''
        self._data = []

    def add(self, o):
        ''' (Queue, object) -> NoneType

        Add o at the back of this queue.
        '''
        self._data.append(o)

    def remove(self):
        ''' (Queue) -> object

        Remove and return front object from self.

        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        '''
        return self._data.pop(0)

    def is_empty(self):
        ''' (Queue) -> bool

        Return True queue self is empty, False otherwise.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        '''
        return self._data == []


def descendants_from_list(t, list_):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int branching: maximum branching factor
    @rtype: Tree

    >>> descendants_from_list(BinaryTree(0), [1, 2, 3, 4])
    BinaryTree(0, BinaryTree(1, BinaryTree(3, None, None), BinaryTree(4, None, None)), BinaryTree(2, None, None))
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, 2):
            if len(list_) == 0:
                return t  # our work here is done
            elif i == 0:
                new_t_child = BinaryTree(list_.pop(0))
                new_t.left = new_t_child
                q.add(new_t_child)
            else:
                new_t_child = BinaryTree(list_.pop(0))
                new_t.right = new_t_child
                q.add(new_t_child)
    return t


def post(t):
    if t is None:
        return []
    return post(t.left) + post(t.right) + [t.value]


def i(t):
    if t is None:
        return []
    return i(t.left) + [t.value] + i(t.right)


def pre(t):
    if t is None:
        return []
    return [t.value] + pre(t.left) + pre(t.right)


class TestLongest(unittest.TestCase):
    def test_one_node(self):
        num = randint(0, 20)
        b = BinaryTree(num)
        lnk = LinkedList()
        lnk.append(num)
        self.assertTrue(str(b.longest()) == str(lnk))

    @given(lists(elements=integers(min_value=10, max_value=50), min_size=6, max_size=6))
    def test_recursion(self, lst):
        b1 = BinaryTree(lst[0], BinaryTree(lst[1]))
        b2 = BinaryTree(lst[3])
        b = BinaryTree(lst[5], b1, b2)
        lst = [lst[5], lst[0], lst[1]]
        lnk = LinkedList()
        for item in lst:
            lnk.append(item)
        lnk2 = b.longest()
        self.assertEqual(str(lnk2) == str(lnk), True)


class TestTraversal(unittest.TestCase):
    def test_one_node(self):
        v = randint(0, 10)
        t = BinaryTree(v)
        result = LinkedList()
        result.append(v)
        self.assertTrue(str(t.preorder()) == str(result))
        self.assertTrue(str(t.inorder()) == str(result))
        self.assertTrue(str(t.postorder()) == str(result))

    @given(lists(elements=integers(min_value=0, max_value=30),
                 min_size=14, max_size=51))
    def test_pre_recursion(self, lst):
        t = descendants_from_list(BinaryTree(lst[0]), lst[1:])
        pre_lst = pre(t)
        pre_lnk = LinkedList()
        for item in pre_lst:
            pre_lnk.append(item)
        self.assertTrue(str(t.preorder()) == str(pre_lnk))

    @given(lists(elements=integers(min_value=0, max_value=30),
                 min_size=14, max_size=51))
    def test_in_recursion(self, lst):
        t = descendants_from_list(BinaryTree(lst[0]), lst[1:])
        in_lst = i(t)
        in_lnk = LinkedList()
        for item in in_lst:
            in_lnk.append(item)
        self.assertTrue(str(t.inorder()) == str(in_lnk))

    @given(lists(elements=integers(min_value=0, max_value=30),
                 min_size=14, max_size=51))
    def test_post_recursion(self, lst):
        t = descendants_from_list(BinaryTree(lst[0]), lst[1:])
        post_lst = post(t)
        post_lnk = LinkedList()
        for item in post_lst:
            post_lnk.append(item)
        self.assertTrue(str(t.postorder()) == str(post_lnk))


if __name__ == '__main__':
    unittest.main()
