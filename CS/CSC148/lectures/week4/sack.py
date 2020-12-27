import random


class Sack:
    """
    A Sack with elements in no particular order.
    """

    def __init__(self):
        """
        Create a new, empty Sack self.

        @param Sack self: this Sack
        @rtype: None
        """
        # doing #2
        self._sack = []

        # two possible ways of representing this info
        # 1. a dictionary with some kind of generated
        # key where the values are the elements in the
        # Sack (you may not get the behaviour you want
        # with int keys - but you could use tuples
        # of ints eg. (0, 0), (0, 1), (0, 2), ...
        #
        # 2. a list where the elements are stored in
        # order, and we randomly choose an index to
        # remove

    def add(self, obj):
        """
        Add object obj to random position of Sack self.

        @param Sack self: this Sack
        @param object obj: object to place on Sack
        @rtype: None
        """
        self._sack.append(obj)

    def remove(self):
        """
        Remove and return some random element of Sack self.

        Assume Sack self is not empty.

        @param Sack self: this Sack
        @rtype: object

        >>> s = Sack()
        >>> s.add(7)
        >>> s.remove()
        7
        """
        index_to_remove = random.randint(0, self.size() - 1)
        return self._sack.pop(index_to_remove)

    def is_empty(self):
        """
        Return whether Sack self is empty.

        @param Sack self: this Sack
        @rtype: bool
        """
        return self.size() == 0

    def size(self):
        """
        Return the number of elements in Sack self.

        @param Sack self: this Sack
        @rtype: int
        """
        return len(self._sack)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

