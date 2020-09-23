""" A class to represent a generic container """


class Container:
    """ Provides an API to inherit to containers """

    def __init__(self):
        """
        Create a new, empty Container self.

        @param Container self: this container
        @rtype: None
        """
        raise NotImplementedError

    def add(self, obj):
        """
        Add object obj to container self.

        @param Container self: this Container
        @param object obj: object to place on Container
        @rtype: None
        """
        # this means that subclasses of Container will have an add method
        # and an error will occur if they don't override it
        raise NotImplementedError('Override add in the subclass')

    def remove(self):
        """
        Remove the next element from Container self.

        Assume Container self is not empty.

        @param Container self: this Container
        @rtype: object
        """
        raise NotImplementedError('Override add in the subclass')

    def is_empty(self):
        """
        Return whether Container self is empty.

        @param Container self: this Container
        @rtype: bool
        """
        raise NotImplementedError('Override add in the subclass')

    def size(self):
        """
        Return the number of elements in Container self.

        @param Container self: this Container
        @rtype: int
        """
        raise NotImplementedError('Override add in the subclass')

class EmptyContainerException(Exception):
    """
    """
        pass
