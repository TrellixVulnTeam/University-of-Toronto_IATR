from csc148_queue import Queue


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """

    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with data and children left and right.

        @param BinaryTree self: this binary tree
        @param object data: data of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.data, self.left, self.right = data, left, right

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
                self.data == other.data and
                self.left == other.left and
                self.right == other.right)

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
        # obtain a visual representation of the left subtree (recursively)
        left_tree = (self.left.__str__(indent + "    ")
                     if self.left
                     else "")
        # obtain a visual representation of the right subtree (recursively)
        right_tree = (self.right.__str__(indent + "    ")
                      if self.right
                      else "")
        # put them together with the root on a new line in between
        return (right_tree +
                "{}{}\n".format(indent, str(self.data)) +
                left_tree)

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        @param BinaryTree self: this binary tree
        @rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))

    def __contains__(self, value):
        """
        Return whether tree rooted at self contains value.

        @param BinaryTree self: binary tree to search for value
        @param object value: value to search for
        @rtype: bool

        >>> BinaryTree(5, BinaryTree(7), BinaryTree(9)).__contains__(7)
        True
        >>> BinaryTree(5, BinaryTree(7), BinaryTree(9)).__contains__(3)
        False
        """
        # We turned the external method contains into a special method of
        # a BinaryTree object. No need to have both.
        return (self.data == value or
                (self.left is not None and value in self.left) or
                (self.right is not None and value in self.right))


def contains(node, value):
    """
    Return whether tree rooted at node contains value.

    @param BinaryTree|None node: binary tree to search for value
    @param object value: value to search for
    @rtype: bool

    >>> contains(None, 5)
    False
    >>> contains(BinaryTree(5, BinaryTree(7), BinaryTree(9)), 7)
    True
    """
    # handling the None case will be trickier for a method
    if node is None:
        return False
    else:
        return (node.data == value or
                contains(node.left, value) or
                contains(node.right, value))


def height(t):
    """
    Return 1 + length of the longest path of t.
    @param BinaryTree t: binary tree to find the height of
    @rtype: int
    >>> t = BinaryTree(13)
    >>> height(t)
    1
    >>> height(BinaryTree(5, BinaryTree(3), BinaryTree(8, BinaryTree(7))))
    3
    """
    if t is None:
        return 0
    else:
        return 1 + max(height(t.left), height(t.right))


def evaluate(b):
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float data.  Otherwise, evaluate b.left and
    b.right and combine them with b.data.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain data in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float data

     @param BinaryTree b: binary tree representing arithmetic expression
     @rtype: float

    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    """
    if b.left is None and b.right is None:
        return b.data
    else:
        return eval(str(evaluate(b.left)) +
                    str(b.data) +
                    str(evaluate(b.right)))


def inorder_visit(node, act):
    """
    Visit each node of binary tree rooted at node in order and act.

    @param BinaryTree node: binary tree to visit
    @param (BinaryTree)->object act: function to execute on visit
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> inorder_visit(b, f)
    2
    4
    6
    8
    10
    12
    14
    """
    if node is not None:
        inorder_visit(node.left, act)
        act(node)
        inorder_visit(node.right, act)


def preorder_visit(t, act):
    """
    Visit BinaryTree t in preorder and act on nodes as you visit.

    @param BinaryTree|None t: binary tree to visit
    @param (BinaryTree)->Any act: function to use on nodes
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> preorder_visit(b, f)
    8
    4
    2
    6
    12
    10
    14
    """
    if t is not None:
        act(t)
        preorder_visit(t.left, act)
        preorder_visit(t.right, act)


def postorder_visit(t, act):
    """
    Visit BinaryTree t in postorder and act on nodes as you visit.

    @param BinaryTree|None t: binary tree to visit
    @param (BinaryTree)->Any act: function to use on nodes
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> postorder_visit(b, f)
    2
    6
    4
    10
    14
    12
    8
    """
    if t is not None:
        postorder_visit(t.left, act)
        postorder_visit(t.right, act)
        act(t)


def levelorder_visit(t, act):
    """
    Visit BinaryTree t in level order and act on nodes as they are visited

    @param BinaryTree|None t: binary tree to visit
    @param (BinaryTree)->Any act: function to use during visit
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> levelorder_visit(b, f)
    8
    4
    12
    2
    6
    10
    14
    """
    nodes = Queue()
    nodes.add(t)
    while not nodes.is_empty():
        next_node = nodes.remove()
        act(next_node)
        if next_node.left:
            nodes.add(next_node.left)
        if next_node.right:
            nodes.add(next_node.right)


def visit_level(t, n, act):
    """
    Visit each node of BinaryTree t at level n and act on it.  Return
    the number of nodes visited visited.

    @param BinaryTree|None t: binary tree to visit
    @param int n: level to visit
    @param (BinaryTree)->Any act: function to execute on nodes at level n
    @rtype: int

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> visit_level(b, 2, f)
    2
    6
    10
    14
    4
    """
    if t is None:
        return 0
    elif n == 0:
        act(t)
        return 1
    elif n > 0:
        return (visit_level(t.left, n-1, act) +
                visit_level(t.right, n-1, act))
    else:
        return 0


def levelorder_visit2(t, act):
    """
    Visit BinaryTree t in level order and act on each node.

    @param BinaryTree|None t: binary tree to visit
    @param (BinaryTree)->Any act: function to use during visit
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> levelorder_visit2(b, f)
    8
    4
    12
    2
    6
    10
    14
    """
    # this approach uses iterative deepening
    n = 0
    visited = visit_level(t, n, act)
    while visited > 0:
        n += 1
        visited = visit_level(t, n, act)


# the following functions assume a binary search tree
def bst_contains(node, value):
    """
    Return whether tree rooted at node contains value.

    Assume node is the root of a Binary Search Tree

    @param BinaryTree|None node: node of a Binary Search Tree
    @param object value: value to search for
    @rtype: bool

    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
    True
    """
    if node is None:
        return False
    elif node.data == value:
        return True
    elif value < node.data:
        return bst_contains(node.left, value)
    elif value > node.data:
        return bst_contains(node.right, value)
    else:
        assert False, "WTF!"


def find_max(node):
    """
    Find and return subnode with maximum data.

    Assume node is the root of a binary search tree.

    @param BinaryTree node: binary tree node to begin search from
    @rtype: BinaryTree

    >>> find_max(BinaryTree(5, BinaryTree(3), BinaryTree(7)))
    BinaryTree(7, None, None)
    """
    return find_max(node.right) if node.right is not None else node


def insert(node, data):
    """
    Insert data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param BinaryTree node: root of a binary search tree.
    @param object data: data to insert into BST, if necessary.

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> print(b)
            14
        12
            10
    8
            6
        4
            2
    <BLANKLINE>
    """
    return_node = node
    if not node:
        return_node = BinaryTree(data)
    elif data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # eval example - this is why you should be careful when using it:
    # if we pass a destructive command (say, to remove all our files), then eval
    # is not going to warn or stop us from self-destruction :)
    # import os
    # eval(input("your wish is my command:"))

    b = BinaryTree(8)
    b = insert(b, 4)
    b = insert(b, 2)
    b = insert(b, 6)
    print(b)
    # 8
    #         6
    #     4
    #         2

    def f(node): print(node.data)
    # add breakpoint on the following line before you start debugging ...
    levelorder_visit2(b, f)
