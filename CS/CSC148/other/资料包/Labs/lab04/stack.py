'''Stack ADT.
'''

class Stack:

    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType

        Initialize new Stack self.
        '''
        self._data = [] # _data is not part of the public interface

    def pop(self):
        ''' (Stack) -> object

        Remove and return the top item from self.

        >>> s = Stack()
        >>> s.push(2)
        >>> s.push(3)
        >>> s.pop()
        3
        '''
        return self._data.pop()

    def is_empty(self):
        ''' (Stack) -> bool

        Return whether the self is empty.

        >>> s = Stack()
        >>> s.push(4)
        >>> s.pop()
        4
        >>> s.is_empty()
        True
        '''
        return self._data == []

    def push(self, o):
        ''' (Stack, object) -> NoneType

        Place object o on top of Stack self.
        '''
        self._data.append(o)

        # implementation of __eq__, __str__,
        # and __repr__ left as an exercise

if __name__  ==  '__main__':
    import doctest
    doctest.testmod()
    # uncomment lines below to test performance
#    import time
#    s = Stack()
#    items = range(100000)
#
#    # start the clock
#    start = time.time()
#
#    for i in items:
#        s.push(i)
#
#    for i in items:
#        s.pop()
#
#    end = time.time()
#    print ("It took ", end - start, "to push/pop", len(items), "items")




