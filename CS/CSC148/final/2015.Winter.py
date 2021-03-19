# Question 1



# Question 2

class BTNode:
    '''Binary Tree node.'''
    
    def __init__(self, data, left=None, right=None):
        ''' (BTNode, object, BTNode, BTNode) -> NoneType
        
        Create BTNode (self) with data and children left and right.
        '''
        self.data, self.left, self.right = data, left, right
        
def occurs(root, s):
    ''' (BTNode or None, str) -> bool
    
    Return whether or not s equals a sequence of characters
    along some path from the root to a leaf, inclusive, and in
    that order. The empty str ("") is considered to occur in
    the empty tree, denoted None.
    
    Assume each node in the tree rooted at root contains a str of length 1.
    
    >>> left = BTNode('b', None, BTNode('d', BTNode('e'), None))
    >>> right = BTNode('c', BTNode('e'), BTNode('f', BTNode('h'), BTNode('i')))
    >>> whole = BTNode('a', left, right)
    >>> occurs(whole, 'acfh')
    True
    >>> occurs(whole, 'ace')
    True
    >>> occurs(whole, 'bde')
    False
    '''
    
    def path_list(root_, path=""):
        ''' (BTNode or None, str) -> list of str
        
        Return a list of str to represent all possible paths from the root
        to a leaf.
        '''
        
        paths = []
        
        if not root_.left and not root_.right:
            path += root_.data
            paths.append(path)
            return paths
        else:
            path += root_.data
            if root_.left:
                paths += path_list(root_.left, path)
            if root_.right:
                paths += path_list(root_.right, path)
                
        return paths
    
    return s in path_list(root)

# Question 6

class LLNode:
    def __init__(self, value, nxt=None):
        self.value, self.nxt = value, nxt

class Queue:
    def __init__(self):
        self._front = self._back = None
        
    def enqueue(self, o):
        new_node = LLNode(o)
        if self._back:
            self._back.nxt = new_node
            self._back = new_node
        else:
            self._back = self._front = new_node
    
    def dequeue(self):
        new_value = self._front.value
        self._front = self._front.nxt
        if self._front is None:
            self._back = self._front
        return new_value
    
    def is_empty(self):
        return self._front == None and self._back == None
    
    
class LeakyQueue(Queue):
    
    def defer(self, from_value, to_value):
        '''
        >>> lq = LeakyQueue()
        >>> lq.enqueue(1)
        >>> lq.enqueue(2)
        >>> lq.enqueue(3)
        >>> lq.enqueue(4)
        >>> lq.defer(1, 3)
        >>> lq.dequeue()
        3
        >>> lq.dequeue()
        2
        >>> lq.dequeue()
        1
        >>> lq.dequeue()
        4
        '''
                
        res = Queue()
        
        from_found = False
        to_found = False
        
        while not self.is_empty():
            curr = self.dequeue()
            if curr is not None:
                if curr != from_value and curr != to_value:
                    res.enqueue(curr)
                elif curr == from_value:
                    res.enqueue(to_value)
                    from_found = True
                elif curr == to_value and from_found:
                    res.enqueue(from_value)
                    
        while not res.is_empty():
            self.enqueue(res.dequeue())
                    
                    
                
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
