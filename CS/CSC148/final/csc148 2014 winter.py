# CSC148 FINAL 2014 APRIL SAMPLE SOLUTIONS


# Question1

class MultiIterator(list):

    def __init__(self):
        """
        """

        super().__init__()
        self.iterator_dict = {}

    def new_iterator(self):
        """
        """

        i = 0
        while i in self.iterator_dict:
            i += 1

        self.iterator_dict[i] = 0
        return i

    def reset(self, i):
        """
        """

        if i not in self.iterator_dict:
            raise Exception('No iteration i')
        else:
            self.iterator_dict[i] = 0

    def next(self, i):
        """
        """

        if i not in self.iterator_dict:
            raise Exception("No iteration i!")
        else:
            if self.iterator_dict[i] < self.__len__() - 1:
                self.iterator_dict[i] += 1
            else:
                self.iterator_dict[i] = 0


# Question2
# >>> t1 = Tree(1, [Tree(2), Tree(4, [Tree(3)]))
# >>> t2 = Tree(1, [Tree(3), Tree(2), Tree(4)])
# False

# >>> t1 = Tree(1, [Tree(2,[Tree(3))], Tree(4))
# >>> t2 = Tree(1, [Tree(3), Tree(4)])
# True

def same_leaves(t1, t2):
    """
    """

    l1 = leaves_list(t1)
    l2 = leaves_list(t2)

    return l1 == l2

def leaves_list(tree):
    """ Return a list of this tree's leaves
    """

    if tree.children == []:
        return [tree.value]
    else:
        result = []
        for child in tree.children:
            result.extend(leaves_list(child))

        result.sort()
        return result

# Question 3
class Tree:
    def __init__(self, value,children):
        self.value = value
        self.children = children

    def purge_clones(self):

        # Base case:
        if self.children == []:
            return

        # Recursive step:
        i = 0
        while i < len(self.children):
            if self.children[i].value == self.value:
                self.children.remove(self.children[i])
            i += 1

        for child in self.children:
            child.purge_clnoes()

    # Test case
    # Please consider empty case
    # multiple node that do nothing
    # multiple node that modify this Tree
    # mulitple node that cut the Tree's node (i.e: a child has the same value have been "cut off"
    # and this child also has children

# Question 4
def deepen(t):

    # Base case:
    new_node = Tree(t.value)
    t.children.insert(0, new_node)

    if len(t.children) == 1:
        return
    # Recursive step:
    for child in t.children[1:]:
        deepen(child)


# Question 5
def contain(node, value):# CSC148 FINAL 2014 APRIL SAMPLE SOLUTIONS


# Question1

class MultiIterator(list):

    def __init__(self):
        """
        """

        super().__init__()
        self.iterator_dict = {}

    def new_iterator(self):
        """
        """

        i = 0
        while i in self.iterator_dict:
            i += 1

        self.iterator_dict[i] = 0
        return i

    def reset(self, i):
        """
        """

        if i not in self.iterator_dict:
            raise Exception('No iteration i')
        else:
            self.iterator_dict[i] = 0

    def next(self, i):
        """
        """

        if i not in self.iterator_dict:
            raise Exception("No iteration i!")
        else:
            if self.iterator_dict[i] < self.__len__() - 1:
                self.iterator_dict[i] += 1
            else:
                self.iterator_dict[i] = 0


# Question2
# >>> t1 = Tree(1, [Tree(2), Tree(4, [Tree(3)]))
# >>> t2 = Tree(1, [Tree(3), Tree(2), Tree(4)])
# False

# >>> t1 = Tree(1, [Tree(2,[Tree(3))], Tree(4))
# >>> t2 = Tree(1, [Tree(3), Tree(4)])
# True

def same_leaves(t1, t2):
    """
    """

    l1 = leaves_list(t1)
    l2 = leaves_list(t2)

    return l1 == l2

def leaves_list(tree):
    """ Return a list of this tree's leaves
    """

    if tree.children == []:
        return [tree.value]
    else:
        result = []
        for child in tree.children:
            result.extend(leaves_list(child))

        result.sort()
        return result

# Question 3
class Tree:
    def __init__(self, value,children):
        self.value = value
        self.children = children

    def purge_clones(self):

        # Base case:
        if self.children == []:
            return

        # Recursive step:
        i = 0
        while i < len(self.children):
            if self.children[i].value == self.value:
                self.children.remove(self.children[i])
            i += 1

        for child in self.children:
            child.purge_clnoes()

    # Test case
    # Please consider empty case
    # multiple node that do nothing
    # multiple node that modify this Tree
    # mulitple node that cut the Tree's node (i.e: a child has the same value have been "cut off"
    # and this child also has children

# Question 4
def deepen(t):

    # Base case:
    new_node = Tree(t.value)
    t.children.insert(0, new_node)

    if len(t.children) == 1:
        return
    # Recursive step:
    for child in t.children[1:]:
        deepen(child)


# Question 5
def contain(node, value):
    if node is None:
        return False
    else:
        pointer = node.head
        while pointer:
            if pointer.value == value:
                return True
            pointer = pointer.next
        return False


def append_unique_data(bt, n):
    """
    """

    # do it in a different way from the package answer.
    temp_list = preorder_visit(bt)
    result = []
    while temp_list:  # loop over and remove the duplicate, also change the order.
        temp = temp_list.pop(0)
        if temp not in result:
            result.append(temp)

    first_node = LListNode(result.pop(0))
    if n:
        n.next = first_node

    pointer = first_node
    while temp_list:
        pointer2 = LListNode(result.pop(0))
        pointer.next = pointer2
        pointer = pointer.next

    return first_node

# This question is too troublesome
# Because we have to deal with linkedlist node not linkedlist.

def preorder_visit(bt):

    if bt is None:
        return []
    else:
        return [bt.value] + preorder_visit(bt.left) + preorder_visit(bt.right)

# Question 6
# (a)
# O(n log(n))
# First, the complexity of merge sort is O(n log(n))
# and then find the largest element which is O(1)
# So, in summary, the complexity of doing this is O(n log(n))

# (b)
# O(1)
# L[i] and L[i + 1] is in O(1)
# so take both of them and make a comparison is in O(1)

# (c)
# O(n^2)
# In the worst case, there are n - 1 comparisons
# Each comparisons take n comparisons ( to make sure each element in the small list is the same)
# In summary, the complexity of doing this is O(n^2)

# O(n^3) ??
# In the question above, we discuss that for the first element, there's

# (d)
# O(log(n))
# I think the recursive step should return f2(n // 2), otherwise there's an infinite recursion.
# the function f2 is in O(log(n))
# and each of the function f2 is O(1)
# In summary, the complexity of this function is O(log(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()