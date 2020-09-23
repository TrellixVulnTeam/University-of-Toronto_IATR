import unittest
from hypothesis import given
from ex5 import LinkedListNode, LinkedList
from hypothesis.strategies import integers, lists


class TestNodeEq(unittest.TestCase):
    @given(integers(min_value=-100, max_value=100))
    def test_diff_type(self, a):
        n1 = LinkedListNode(a)
        self.assertEqual(n1 == a, False)

    @given(integers(min_value=-10, max_value=10),
           integers(min_value=11, max_value=20))
    def test_single_node(self, a, b):
        n1 = LinkedListNode(a)
        n2 = LinkedListNode(b)
        n3 = LinkedListNode(a, None)
        self.assertEqual(n1 == n2, False)
        self.assertEqual(n1 == n3, True)

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=-10, max_value=20))
    def test_diff_length(self, a, b):
        n1 = LinkedListNode(a)
        n2 = LinkedListNode(a, LinkedListNode(b))
        n3 = LinkedListNode(a, LinkedListNode(b, LinkedListNode(a)))

        self.assertEqual(n1 == n2, False)
        self.assertEqual(n1 == n3, False)
        self.assertEqual(n2 == n3, False)

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=21, max_value=30))
    def test_same_length(self, a, b):
        n1 = LinkedListNode(a, LinkedListNode(b, LinkedListNode(a)))
        n2 = LinkedListNode(a, LinkedListNode(b, LinkedListNode(a)))
        n3 = LinkedListNode(a, LinkedListNode(b, LinkedListNode(b)))

        self.assertEqual(n1 == n2, True)
        self.assertEqual(n1 == n3, False)


class TestLinkedListEq(unittest.TestCase):
    @given(integers(min_value=-100, max_value=100))
    def test_diff_type(self, a):
        l1 = LinkedList()
        l1.append(a)
        self.assertEqual(l1 == [a], False)

    def test_empty(self):
        l1 = LinkedList()
        l2 = LinkedList()
        self.assertEqual(l1 == l2, True)

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=21, max_value=30))
    def test_single_node(self, a, b):
        l1 = LinkedList()
        l1.append(a)
        l2 = LinkedList()
        l2.prepend(a)
        l3 = LinkedList()
        l3.append(b)
        self.assertEqual(l1 == l2, True)
        self.assertEqual(l2 == l3, False)

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=21, max_value=30))
    def test_diff_length(self, a, b):
        l1 = LinkedList()
        l1.append(a)
        l2 = LinkedList()
        l2.prepend(a)
        l2.append(b)
        self.assertEqual(l1 == l2, False)

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=21, max_value=30))
    def test_same_length(self, a, b):
        l1 = LinkedList()
        l1.append(a)
        l1.prepend(b)
        l2 = LinkedList()
        l2.prepend(a)
        l2.append(b)
        l3 = LinkedList()
        l3.append(b)
        l3.prepend(a)
        self.assertEqual(l1 == l2, False)
        self.assertEqual(l2 == l3, True)


class TestDeleteAfter(unittest.TestCase):
    def test_empty(self):
        l1 = LinkedList()
        l1.delete_after(1)
        self.assertEqual(str(l1),
                         "I'm so empty... experiencing existential angst!!!")

    @given(integers(min_value=21, max_value=30),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=2, max_size=10))
    def test_n_nexist(self, n, lst):
        l1 = LinkedList()
        l2 = LinkedList()
        for item in lst:
            l1.append(item)
            l2.append(item)
        l1.delete_after(n)
        self.assertEqual(l1 == l2, True)

    @given(integers(min_value=21, max_value=30),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=2, max_size=10))
    def test_n_exist(self, n, lst):
        l1 = LinkedList()
        for item in lst:
            l1.append(item)
        l1.prepend(n)
        l1.delete_after(n)
        self.assertEqual(l1.size == len(lst), True)
        self.assertEqual(l1[1] == lst[1], True)

    @given(integers(min_value=21, max_value=30),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=2, max_size=10))
    def test_delete_end(self, n, lst):
        l1 = LinkedList()
        for item in lst:
            l1.append(item)
        l1.append(n)
        l1.delete_after(n)
        self.assertEqual(l1.size == len(lst) + 1, True)


class TestSetItem(unittest.TestCase):
    def test_index_error(self):
        l1 = LinkedList()
        with self.assertRaises(IndexError):
            l1.__setitem__(2, 0)

    @given(integers(min_value=0, max_value=9),
           integers(min_value=21, max_value=30),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=10, max_size=10))
    def test_setable(self, idx, v, lst):
        l1 = LinkedList()
        for item in lst:
            l1.append(item)
        s = l1.size
        l1[idx] = v

        self.assertEqual(l1.size, s)
        self.assertEqual(l1[idx], v)


class TestInsertBefore(unittest.TestCase):
    def test_empty(self):
        l1 = LinkedList()
        l1.insert_before(1, 1)
        self.assertEqual(str(l1),
                         "I'm so empty... experiencing existential angst!!!")

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=21, max_value=30),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=2, max_size=10))
    def test_v2_nexist(self, v1, v2, lst):
        l1 = LinkedList()
        l2 = LinkedList()
        for item in lst:
            l1.append(item)
            l2.append(item)
        l1.insert_before(v1, v2)
        self.assertEqual(l1 == l2, True)

    @given(integers(min_value=-10, max_value=20),
           integers(min_value=21, max_value=30),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=2, max_size=10))
    def test_v2_exist(self, v1, v2, lst):
        l1 = LinkedList()
        for item in lst:
            l1.append(item)
        l1.prepend(v2)
        l1.insert_before(v1, v2)
        self.assertEqual(l1.size == len(lst) + 2, True)
        self.assertEqual(l1.front.value == v1, True)


class TestAdd(unittest.TestCase):
    def test_empty(self):
        l1 = LinkedList()
        size1 = l1.size
        l2 = LinkedList()
        size2 = l2.size
        l3 = l1 + l2

        self.assertEqual(l3.size, 0)
        self.assertEqual(l1.size, size1)
        self.assertEqual(l2.size, size2)

    @given(lists(elements=integers(min_value=1, max_value=20),
                 min_size=2, max_size=10),
           lists(elements=integers(min_value=31, max_value=50),
                 min_size=2, max_size=10))
    def test_nonEmpty(self, lst1, lst2):
        l1 = LinkedList()
        for item in lst1:
            l1.append(item)
        size1 = l1.size
        l2 = LinkedList()
        for item in lst2:
            l2.append(item)
        size2 = l2.size

        l3 = l1 + l2

        self.assertEqual(l3.size, size1 + size2)
        self.assertEqual(l1.size, size1)
        self.assertEqual(l2.size, size2)


class TestCopyAndLength(unittest.TestCase):
    def test_copy(self):
        l1 = LinkedList()
        self.assertEqual(str(l1.copy()),
                         "I'm so empty... experiencing existential angst!!!")

        l1.append(1)
        l1.append(2)
        l1.append(3)

        c_l1 = l1.copy()
        self.assertEqual(c_l1 == l1, True)

        n = l1.front
        nc = c_l1.front
        self.assertEqual(id(n) == id(nc), False)

    def test_length(self):
        l1 = LinkedList()
        self.assertEqual(len(l1), 0)

        l1.append(1)
        l1.append(2)
        self.assertEqual(len(l1), 2)


if __name__ == '__main__':
    unittest.main()
