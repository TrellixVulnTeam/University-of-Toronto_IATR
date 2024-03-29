"""exercises with binary trees
"""


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.

    === Attributes ===
    @param object value: value for this binary tree node
    @param BinaryTree|None left: left child of this binary tree node
    @param BinaryTree|None right: right child of this binary tree node
    """

    def __init__(self, value, left=None, right=None):
        """
        Create BinaryTree self with value and children left and right.

        @param BinaryTree self: this binary tree
        @param object value: value of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.value, self.left, self.right = value, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        @param BinaryTree self: this binary tree
        @param Any other: object to check equivalence to self
        @rtype: bool

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.value == other.value and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        @param BinaryTree self: this binary tree
        @rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.value),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.value)) +
                left_tree)

    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.

        @param BinaryTree self: binary tree to search for value
        @param object value: value to search for
        @rtype: bool

        >>> BinaryTree(5, BinaryTree(7), BinaryTree(9)).__contains__(7)
        True
        """
        return (self.value == value or
                (self.left and value in self.left) or
                (self.right and value in self.right))


def parenthesize(b):
    """
    Return a parenthesized expression equivalent to the arithmetic
    expression tree rooted at b.

    Assume:  -- b is a binary tree
             -- interior nodes contain value in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float value

    @param BinaryTree b: arithmetic expression tree
    @rtype: str

    >>> b1 = BinaryTree(3.0)
    >>> print(parenthesize(b1))
    3.0
    >>> b2 = BinaryTree(4.0)
    >>> b3 = BinaryTree(7.0)
    >>> b4 = BinaryTree("*", b1, b2)
    >>> parenthesize(b4)
    '(3.0 * 4.0)'
    >>> b5 = BinaryTree("+", b4, b3)
    >>> print(parenthesize(b5))
    ((3.0 * 4.0) + 7.0)
    """
    if b.left is None and b.right is None:
        return str(b.value)
    else:
        return "({} {} {})".format(parenthesize(b.left),\
                                   b.value,\
                                   parenthesize(b.right))


def list_longest_path(node):
    """
    List the value in a longest path of node.

    @param BinaryTree|None node: tree to list longest path of
    @rtype: list[object]

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BinaryTree(5))
    [5]
    >>> b1 = BinaryTree(7)
    >>> b2 = BinaryTree(3, BinaryTree(2), None)
    >>> b3 = BinaryTree(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    # node is None
    if node is None:
        return []

    # base case, no left and right children
    elif node.left is None and node.right is None:
        return [node.value]

    # have children
    else:
        longest = []
        path = list_longest_path(node.left)
        if len(path) > len(longest):
            longest = path

        path2 = list_longest_path(node.right)
        if len(path2) > len(longest):
            longest = path2
        return [node.value] + longest


def list_between(node, start, end):
    """
    Return a Python list of all values in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BinaryTree where all nodes in the subtree
    rooted at t.left are less than t.value, and all nodes in the subtree
    rooted at t.right are more than t.value

    @param BinaryTree|None node: binary tree to list values from
    @param object start: starting value for list insertion
    @param object end: stopping value for list insertion
    @rtype: list[object]

    >>> b_left = BinaryTree(4, BinaryTree(2), BinaryTree(6))
    >>> b_right = BinaryTree(12, BinaryTree(10), BinaryTree(14))
    >>> b = BinaryTree(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    # if node is None
    if node is None:
        return []
    # no children
    if node.left is None and node.right is None and \
                    node.value in range(start, end):
        return [node.value]
    # have children
    else:
        path = list_between(node.left, start, end)
        path2 = list_between(node.right, start, end)

        if node.value in range(start, end):
            return [node.value] + path + path2
        else:
            return path + path2


def count_shallower(t, n):
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    @param BinaryTree|None t: binary tree to count
    @param int n: depth below which not to count

    >>> t = BinaryTree(0, BinaryTree(1, BinaryTree(2)), BinaryTree(3))
    >>> count_shallower(t, 2)
    3
    """
    acc = 0
    if t is None:
        return 0
    elif n == 0:
        return 0
    else:
        acc += count_shallower(t.left, n-1)
        acc += count_shallower(t.right, n-1)
        return 1 + acc

if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
