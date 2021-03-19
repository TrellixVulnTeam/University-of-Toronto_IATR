class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self):
        """
        Create a new, empty Stack self.

        @param Stack self: this stack
        @rtype: None
        """
        self._stack = []
        # could make this work with underlying
        # dict or tuple, but a list will probably be the simplest
        # doesn't make big difference in our code if we use index 0 or -1 as 'top'
        # but - it turns out that it is more efficient to add/remove
        # the end of a list, rather than the beginning


    def add(self, obj):
        """
        Add object obj to top of Stack self.

        @param Stack self: this Stack
        @param object obj: object to place on Stack
        @rtype: None
        """
        self._stack.append(obj)


    def remove(self):
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        @param Stack self: this Stack
        @rtype: object

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._stack.pop()


    def is_empty(self):
        """
        Return whether Stack self is empty.

        @param Stack self: this Stack
        @rtype: bool
        """
        return len(self._stack) == 0

    def size(self):
        """
        Return the length of Stack self.

        @param Stack self: this Stack
        @rtype: int
        """
        return len(self._stack)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
