from csc148_queue import Queue


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None):
        """
        Create Tree self with content value and 0 or more children

        @param Tree self: this tree
        @param object value: value contained in this tree
        @param list[Tree|None] children: possibly-empty list of children
        @rtype: None
        """
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []

    def __eq__(self, other):
        """
        Return whether this Tree is equivalent to other.

        @param Tree self: this tree
        @param object|Tree other: object to compare to self
        @rtype: bool

        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        # print("{} == {}?".format(self.value, other.value))
        return (type(self) == type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0):
        """
        Produce a user-friendly strindent=ing representation of Tree self,
        indenting each level as a visual clue.

        @param Tree self: this tree
        @param int indent: amount to indent each level of tree
        @rtype: str

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])

    def __contains__(self, v):
        """
        Return whether Tree self contains v.

        @param Tree self: this tree
        @param object v: value to search this tree for

        # >>> t = Tree(17)
        # >>> t.__contains__(17)
        # True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(5)
        True
        """
        if not self.children:
            # self is a leaf
            return self.value == v
        else:
            # self is an interior node
            # this else block would probably also work for the base case!
            return ((self.value == v) or
                    (any([v in child for child in self.children])))
        # We can shorten the entire method: the lines from the else block are
        # sufficient (look closely to convince yourselves!):
        # return ((self.value == v) or
        #         (any([v in child for child in self.children])))
        # Any() stops early once it finds a True (no need to traverse the entire
        # list, *but* the list has to be fully generated first in memory.
        # We can avoid generating the entire list too, by turning the iterable
        # argument of any(), into a generator (just remove the []):
        #     return ((self.value == v) or
        #         (any(v in child for child in self.children)))

    def __repr__(self):
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        @param Tree self: this tree
        @rtype: str

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))


# helpful helper function
def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in level order, with up to arity children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int arity: maximum branching factor
    @rtype: Tree

    # >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    # Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


def leaf_count(t):
    """
    Return the number of leaves in Tree t.

    @param Tree t: tree to count the leaves of
    @rtype: int

    >>> t = Tree(7)
    >>> leaf_count(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> leaf_count(t)
    6
    """
    return (sum([leaf_count(c) for c in t.children]) +
            (0 if t.children else 1))


def height(t):
    """
    Return 1 + length of longest path of t.

    @param Tree t: tree to find height of
    @rtype: int

    >>> t = Tree(13)
    >>> height(t)
    1
    >>> t = descendants_from_list(Tree(13), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> height(t)
    3
    """
    return 1 + max([height(c) for c in t.children]) if t.children else 1


def count(t):
    """
    Return the number of nodes in Tree t.


    @param Tree t: tree to find number of nodes in
    @rtype: int

    >>> t = Tree(17)
    >>> count(t)
    1
    >>> t4 = descendants_from_list(Tree(17), [0, 2, 4, 6, 8, 10, 11], 4)
    >>> count(t4)
    8
    """
    return 1 + sum([count(n) for n in t.children])


# helper function that may be useful for other tree functions
def gather_lists(list_):
    """
    Concatenate all the sublists of L and return the result.

    @param list[list[object]] list_: list of lists to concatenate
    @rtype: list[object]

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list


def list_all(t):
    """
    Return list of values in t.

    @param Tree t: tree to list values of
    @rtype: list[object]

    >>> t = Tree(0)
    >>> list_all(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_all(t)
    >>> list_.sort()
    >>> list_
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    return [t.value] + gather_lists([list_all(c) for c in t.children])


def list_if(t, p):
    """
    Return a list of values in Tree t that satisfy predicate p(value).

    @param Tree t: tree to list values that satisfy predicate p
    @param (object)->bool p: predicate to check values with
    @rtype: list[object]

    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_if(t, p)
    >>> list_.sort()
    >>> list_
    [5, 6, 7, 8]
    >>> def p(v): return v % 2 == 0
    >>> list_ = list_if(t, p)
    >>> list_.sort()
    >>> list_
    [0, 2, 4, 6, 8]
    """
    # practice on your own!
    pass


def list_leaves(t):
    """
    Return list of values in leaves of t.

    @param Tree t: tree to list leaf values of
    @rtype: list[object]

    >>> t = Tree(0)
    >>> list_leaves(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_leaves(t)
    >>> list_.sort() # so list_ is predictable to compare
    >>> list_
    [3, 4, 5, 6, 7, 8]
    """
    # practice on your own!
    pass


def preorder_visit(t, act):
    """
    Visit each node of Tree t in preorder, and act on the nodes
    as they are visited.

    @param Tree t: tree to visit in preorder
    @param (Tree)->Any act: function to carry out on visited Tree node
    @rtype: None

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> preorder_visit(t, act)
    0
    1
    4
    5
    6
    2
    7
    3
    """
    act(t)
    for child in t.children:
        preorder_visit(child, act)


def postorder_visit(t, act):
    """
    Visit each node of t in postorder, and act on it when it is visited.

    @param Tree t: tree to be visited in postorder
    @param (Tree)->Any act: function to do to each node
    @rtype: None

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> postorder_visit(t, act)
    4
    5
    6
    1
    7
    2
    3
    0
    """
    for child in t.children:
        postorder_visit(child, act)
    act(t)


def levelorder_visit(t, act):
    """
    Visit every node in Tree t in level order and act on the node
    as you visit it.

    @param Tree t: tree to visit in level order
    @param (Tree)->Any act: function to execute during visit

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    nodes_to_be_processed = Queue()
    nodes_to_be_processed.add(t)
    while not nodes_to_be_processed.is_empty():
        next_node = nodes_to_be_processed.remove()
        act(next_node)
        for c in next_node.children:
            nodes_to_be_processed.add(c)


def visit_level(t, n, act):
    """
    Visit nodes of t at level n, act on them, and return the number visited.

    @param Tree t: tree to visit level n of
    @param int n: level (depth) to visit
    @param (Tree)->object act: function to execute at level n
    @rtype: int

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> visit_level(t, 1, act)
    1
    2
    3
    3
    """
    if n == 0:
        act(t)
        return 1
    else:
        return sum([visit_level(c, n-1, act) for c in t.children])


def levelorder_visit2(t, act):
    """
    Visit Tree t in level order and act on its nodes.

    @param Tree t: Tree to visit in level order
    @param (Tree)->object act: function to execute on visit
    @rtype: None

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit2(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    visited = visit_level(t, 0, act)
    n = 0
    while visited > 0:
        n += 1
        visited = visit_level(t, n, act)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    t3 = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
    t4 = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
    print(t3 == t4)
    # print(5 in t3)

    print("===========")
    print(str(t3))
    print("===========")
    print(repr(t3))
    t5 = eval(repr(t3))
    print("===========")
    print(str(t5))
    print(t5 == t3)
