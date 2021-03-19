import unittest
from stack import Stack

class TestEmptyStack(unittest.TestCase):
    """
    Test behaviour of an empty stack
    """

    def setUp(self):
        """
        Set uo an empty stack
        """
        self.stack = Stack()

    def tearDown(self):
        """
        Clean up
        """
        self.stack = None

    def testIsEmpty(self):
        """ Test is_empty() on an empty stack"""

       #self.assertEqual(self.stack.is_empty(), True)
       assert self.stack.is_empty(), \
           'is_empty returned False on an empty stack'

    def testAdd(self):
        """
        Test addding to an empty stack
        """
        self.stack.add('cats')
        assert self.stack.remove() == 'cats', 'wrong item on the top of the stack'

class TestManyItemStack(unittest.TestCase):
    """
    Test behaviour of a stack with mant items
    """


# Generalize Stack and  Sack as Container
class Container:
    def add(self):
        """
        Add object obj to top of Stack self.

        @param Stack self: this Stack
        @param object obj: object to place on Stack
        @rtype: None
        """
        # this means that subclass of container will have an add method
        # and an error will occur if they don't override it
        raise NotImplementedError('Override add in the subclass')

if __name__ == '__main__':
    unittest.main(exit = False)




