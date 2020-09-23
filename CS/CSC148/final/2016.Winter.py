# 2016 Winter

from binary_tree import BinaryTree
from linked_list import *
from tree import *

# Question 1

class TrackRunners:
    def __init__(self, identity, age):
        self._id = identity
        self._age = age
        self.record = {}
    
    def add_result(self, dis, t):
        if dis in self.record:
            self.record[dis].append(t)
        else:
            self.record[dis] = [t]
            
    def report_best(self):
        res = {}
        for dis, t in self.record.items():
            res[dis] = min(t)
        
        return res
            
class RunnerRoster:
    def __init__(self):
        self.manager = []
        
    def add(self, runner):
        self.manager.append(runner)
        
    def report_fastest(self):
        res = {}
        for runner in self.manager:
            best = runner.report_best()
            for d, t in best.items():
                if d in res:
                    if t <= res[d][1]:
                        res[d] = [runner._id, t]
                else:
                    res[d] = [runner._id, t]
        
        return res
    
# Question 3
    
def merge(list1, list2):
    """
    Merge list1 and list2 by placing list2's nodes into the
    correct position in listl to preserve ordering. When
    complete listl will contain all the values from both lists,
    in order, and list2 will be empty.
    Assume list1 and list2 contain comparable values in nondecreasing order
    
    @param LinkedList listl: ordered linked list
    @param LinkedList list2: ordered linked list
    @rtype: None
    
    >>> listl = LinkedList()
    >>> listl.append(1)
    >>> listl.append(3)
    >>> listl.append(5)
    >>> list2 = LinkedList()
    >>> list2.append(2)
    >>> list2.append(6)
    >>> merge(listl, list2)
    >>> print(listl.front)
    1 -> 2 -> 3 -> 5 -> 6 ->|
    >>> print(list2.front)
    """
    
    if list1 is None:
        list1.front = list2.front
        list1.back = list2.back
        
    elif list2 is not None:
        # create an empty LL to store the result
        res = LinkedList()
        
        curr1 = list1.front
        curr2 = list2.front
        while not (curr1 is None or curr2 is None):
            if curr1.value < curr2.value:
                # remember current low-node
                c = curr1
                # go next
                curr1 = curr1.next_
            else:
                # remember current low-node
                c = curr2
                # go next
                curr2 = curr2.next_

            # append the low-node to res
            res.append(c.value)
        
        # handle the longer tail
        if curr1 is not None:
            res.back.next_ = curr1
            res.back = list1.back
        if curr2 is not None:
            res.back.next_ = curr2
            res.back = list2.back

        # reset the front and back
        list1.front = res.front
        list1.back = res.back
    
    # clean list2
    list2.front = list2.back = None


# Question 4

def concatenate_flat(list_):
    """
    Return the concatenation, from left to right, of strings contained
    in flat (depth 1) sublists contained in list_ , but no other strings.
    Assume all non-list elements of list_ or its nested sub-lists are
    strings
    
    @param list list_: possibly nested sub-list to concatenate from
    @rtype: str
    >>> concatenate_flat(["five", [["four" , "by"], "three"], ["two"]]) 
    'fourbytwo'
    """
            
    if len(list_) == 0:
        return ""
    elif all(isinstance(sub, str) for sub in list_):
        return "".join(s for s in list_)
    else:
        return "".join(concatenate_flat(sub) for sub in list_ if isinstance(sub, list))


# Question 5


def pathlength_sets(t):
    """
    Replace the value of each node in Tree t by a set containing all
    path lengths from that node to any leaf. A path's length is the
    number of edges it contains.
    
    Oparam Tree t: tree to record path lengths in
    @rtype: None
    
    >>> t = Tree(5)
    >>> pathlength_sets(t)
    >>> print(t)
    {0}
    >>> t.children.append(Tree(17))
    >>> t.children.append(Tree(13, [Tree(11)]))
    >>> pathlength_sets(t)
    >>> print(t)
    {1, 2}
       {0}
       {1}
          {0}
    """

    # not a nested list: it is a leaf
    if t.children == []:
        t.value = set([0])
    else:
        # go into the lower level
        for c in t.children:
            pathlength_sets(c)
        
        # after handling the lower level
        # get the set of values for current root
        t.value = set()
        for c in t.children:
            for item in c.value:
                t.value.add(item + 1)
        

# Question 6

def swap_even(t, depth=0):
    """
    Swap left and right children of nodes at even depth.

    Recall that the root has depth 0, its children have depth 1,
    grandchildren have depth 2, and so on.

    @param BinaryTree t: tree to carry out swapping on.
    @param int depth: distance from the root
    @rtype: None

    >>> b1 = BinaryTree(1, BinaryTree(2, BinaryTree(3)))
    >>> b4 = BinaryTree(4, BinaryTree(5), b1)
    >>> print(b4)
        1
            2
                3
    4
        5
    <BLANKLINE>
    >>> swap_even(b4)
    >>> print(b4)
        5
    4
        1
                3
            2
    <BLANKLINE>
    """
    if t is None:
        return None
    elif depth % 2 == 0:
        t.left, t.right = t.right, t.left
    else:
        pass
    swap_even(t.left, depth+1)
    swap_even(t.right, depth+1)
    

if __name__ == '__main__':
    # Question 1
    runner1 = TrackRunners('R001', 22)
    runner1.add_result(100, 9.8)
    runner1.add_result(100, 9.5)
    runner1.add_result(200, 14.2)
    runner1.add_result(200, 14.5)
    assert sorted(runner1.report_best().items()) == [(100, 9.5), (200, 14.2)]
    runner2 = TrackRunners('R002', 21)
    runner2.add_result(100, 9.4)
    runner2.add_result(100, 9.5)
    runner2.add_result(200, 15.6)
    runner2.add_result(200, 14.8)
    runner2.add_result(1500, 200)
    rr = RunnerRoster()
    rr.add(runner1)
    rr.add(runner2)
    assert sorted(rr.report_fastest().items()) == [(100, ['R002', 9.4]), 
                                                   (200, ['R001', 14.2]), 
                                                   (1500, ['R002', 200])]
    
    import doctest
    doctest.testmod