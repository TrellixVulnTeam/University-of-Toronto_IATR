# we'll need this import for descendents_from_list
from csc148_queue import Queue

class Tree:
    ''' Represent a Bare-bones Tree ADT'''

    def __init__(self, value=None, children=None):
        ''' (Tree, object, list-of-Tree) -> NoneType

        Create Tree(self) with root containing value and
        0 or more children Trees.
        '''
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []
        # the functional if  on the line above is equivalent to:
       #if not children:
           #self.children = []
       #else:
           #self.children = children.copy()

    def __repr__(self):
        ''' (Tree) -> str

        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        '''
        # Our __repr__ is recursive, because it can also be called via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other):
        ''' (Tree, object) -> bool

        Return whether this Tree is equivalent to other.


        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        '''
        return (isinstance(other, Tree) and
                self.value == other.value and
                self.children == other.children)

    # omit __str__ for now..

##################################################################################
# Here are some module-level functions.  Alternatively these could be implemented
# as methods, but then they might not be appropriate for every Tree


def list_all(t):
    ''' (Tree) -> list

    Return a list of values in t.

    >>> t = Tree(0)
    >>> list_all(t)
    [0]
    >>> t = descendents_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_all(t)
    >>> L.sort()
    >>> L
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    '''
    pass

def list_leaves(t):
    ''' (Tree) -> list

    Return a list of values in leaves of t.

    >>> t = Tree(0)
    >>> list_leaves(t)
    [0]
    >>> t = descendents_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_leaves(t)
    >>> L.sort() # so list is predictable to compare
    >>> L
    [3, 4, 5, 6, 7, 8]
    '''
    pass

def list_interior(t):
    ''' (Tree) -> list

    Return a list of values in interior nodes of t.

    >>> t = Tree(0)
    >>> list_interior(t)
    []
    >>> t = descendents_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_interior(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    '''
    pass

def list_if(t, p):
    ''' (Tree, function) -> list

    Return a list of values in Tree t that satisfy p(value)

    >>> def p(v): return v > 4
    >>> t = descendents_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_if(t, p)
    >>> L.sort()
    >>> L
    [5, 6, 7, 8]
    >>> def p(v): return v % 2 == 0
    >>> L = list_if(t, p)
    >>> L.sort()
    >>> L
    [0, 2, 4, 6, 8]
    '''
    pass

def list_to_depth(t, n):
    ''' (Tree, int) -> list

    Return a list of values in t from nodes with paths no longer
    than n from root

    >>> t = Tree(0)
    >>> list_to_depth(t, 0)
    [0]
    >>> t = descendents_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_to_depth(t, 1)
    >>> L.sort()
    >>> L
    [0, 1, 2, 3]
    '''
    pass

def gather_lists(L):
    ''' (list-of-lists) -> list

    Concatenate all the sublists of L and return the result.

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    '''
    new_list = []
    for l in L:
        new_list += l
    return new_list


def descendents_from_list(t, L, arity):
    ''' (Tree, list, int) -> Tree

    Populate t's descendents from L, filling them
    in in level order, with up to arity children per node.
    Then return t.

    >>> descendents_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    '''
    q = Queue()
    q.enqueue(t)
    L = L.copy()
    while not q.is_empty(): # unlikely to happen
        new_t = q.dequeue()
        for i in range(0,arity):
            if len(L) == 0:
                return t # our work here is done
            else:
                new_t_child = Tree(L.pop(0))
                new_t.children.append(new_t_child)
                q.enqueue(new_t_child)
    return t


if __name__ == '__main__':
    import doctest
    doctest.testmod()

