class BTNode:
    '''Binary Tree node.'''

    def __init__(self, data, left=None, right=None):
        ''' (BTNode, object, BTNode, BTNode) -> NoneType

        Create BTNode (self) with data and children left and right.
        '''
        self.data, self.left, self.right = data, left, right

    def __repr__(self):
        ''' (BTNode) -> str

        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2, None, None), BTNode(3, None, None))
        '''
        return 'BTNode({}, {}, {})'.format(repr(self.data),
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self, indent=''):
        ''' (BTNode) -> str

        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        '''
        right_tree = self.right.__str__(indent + '    ') if self.right else ''
        left_tree = self.left.__str__(indent + '    ') if self.left else ''
        return right_tree + '{}{}\n'.format(indent, str(self.data)) + left_tree

###########################################################################
# Functions for lab 6
###########################################################################

def insert(node, data):
    ''' (BTNode, object) -> BTNode

    Insert data in BST rooted at node if necessary, and return new root.

    >>> b = BTNode(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    '''
    return_node = node
    if not node:
        return_node = BTNode(data)
    elif data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node


def evaluate(b):
    ''' (BTNode) -> float

    Evaluate the expression rooted at b.  If b is a leaf,
    return its float data.  Otherwise, evaluate b.left and
    b.right and combine them with b.data.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    >>> b = BTNode(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BTNode('*', BTNode(3.0), BTNode(4.0))
    >>> evaluate(b)
    12.0
    '''
    pass


def parenthesize(b):
    ''' (BTNode) -> str

    Parenthesize the expression rooted at b, so that float data is not parenthesized,
    but each pair of expressions joined by an operator are parenthesized.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    >>> b = BTNode(3.0)
    >>> print(parenthesize(b))
    3.0
    >>> b = BTNode('+', BTNode('*', BTNode(3.0), BTNode(4.0)), BTNode(7.0))
    >>> print(parenthesize(b))
    ((3.0*4.0)+7.0)
    '''
    pass


def list_between(node, start, end):
    ''' (BTNode, object, object) -> list

    Return a Python list of all values in the binary search tree
    rooted at node that are between start and end (inclusive).

    >>> b = BTNode(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> list_between(None, 0, 15)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    '''
    pass


def list_internal_between(node, start, end):
        ''' (BTNode, object, object) ->

        Return a Python list of the data from all internal nodes of
        the tree rooted at node that are between start and end,
        inclusive.

        >>> list_internal_between(None, 3, 13)
        []
        >>> b = BTNode(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> L = list_internal_between(b, 3, 13)
        >>> L.sort()
        >>> L
        [4, 8, 12]
        '''
        pass


def list_longest_path(node):
    ''' (BTNode) -> list

    List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> list_longest_path(BTNode(5, BTNode(3, BTNode(2), None), BTNode(7)))
    [5, 3, 2]
    '''
    pass


def is_leaf(node):
    ''' (BTNode) -> bool

    Return whether nodeis a leaf.

    >>> b = BTNode(1, BTNode(2))
    >>> is_leaf(b)
    False
    >>> is_leaf(b.left)
    True
    '''
    return not node.left and not node.right


if __name__ == '__main__':
    import doctest
    doctest.testmod()
