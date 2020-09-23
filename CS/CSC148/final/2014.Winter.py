# 2014 Winter
from stack import *
from linked_list import *

# Question 1

class Car :
    def __init__ (self , fuel , eff ):
        """ (Car , int , int ) -> NoneType
        Create a new car at position (0 ,0) with a starting fuel
        of " fuel " and a fuel efficiency of eff .
        """
        pass

    def move (self , new_x , new_y ):
        """ (Car , int , int ) -> NoneType
        Move this car to position (new_x , new_y ) and decrease
        its fuel accordingly . Raise NotEnoughFuelError if the
        car does not have enough fuel to complete the move .
        """
        pass
    
class TeleportCar(Car):
    def __init__(self):
        super().__init__(20, 2)
        self.tele_charge = tele_charge
    
    def move(self, new_x, new_y):
        try:
            super().move(self, new_x, new_y)
        except NotEnoughFuelError:
            if self.tele_charge >= 1:
                self.tele_charge -= 1
            else:
                raise NotEnoughFuelError

# Question 3

def combine(stack1, stack2):
    """ (Stack of int , Stack of int) -> Stack of int
    Return a new stack containing the elements of stack1,
    and then the elements of stack2 above them.
    
    >>> stack1 = Stack()
    >>> stack1.add(1)
    >>> stack1.add(2)
    >>> stack1.add(3)
    >>> stack2 = Stack()
    >>> stack2.add(7)
    >>> stack2.add(8)
    >>> stack2.add(9)
    >>> combine(stack1, stack2)
    $B[1, 2, 3, 7, 8, 9]T
    """

    res = Stack()
        
    new_stack1 = Stack()
    new_stack2 = Stack()
        
    while not stack1.is_empty():
        element = stack1.remove()
        new_stack1.add(element)
    
    while not stack2.is_empty():
        element = stack2.remove()
        new_stack2.add(element)
            
    while not new_stack1.is_empty():
        element = new_stack1.remove()
        stack1.add(element)
        res.add(element)
            
    while not new_stack2.is_empty():
        element = new_stack2.remove()
        stack2.add(element)
        res.add(element)
    
    return res

# Question 5

def insert_sorted(lst, item):
    """
    (LinkedListRec, item) -> LinkedListRec
    
    Precondition : lst is sorted in non - decreasing
    Insert item into the correct location in lst,
    so that lst is still sorted after the function completes.
    
    >>> lst = LinkedList()
    >>> lst.append(3)
    >>> lst.append(7)
    >>> lst.append(10)           # [3 -> 7 -> 10]
    >>> insert_sorted(lst, 5)    # [3 -> 5 -> 7 -> 10]
    """


    if lst.front is None:
        lst.front = lst.back = LinkedListNode(item, None)
        lst.size += 1
    else:
        if item < lst.front.value:
            new_node = LinkedListNode(item, None)
            new_node.next_ = lst.front
            lst.front = new_node
            lst.size += 1
        else:
            last_front = lst.front
            lst.front = lst.front.next_
            insert_sorted(lst, item)
            last_front.next_ = lst.front
            lst.front = last_front
            lst.size += 1
            
# Question 7

def fast_intersection(lst1, lst2):
    """(list, list) -> list
    Precondition : lst1 and lst2 have no duplicate elements , and
    both lst1 and lst2 are sorted in ascending order . 
    Return a list containing the elements that appear in both lists , in ascending order .
    >>> fast_intersection([1, 2, 5], [1, 2, 3])
    [1, 2]
    """
    #common = []
    #for item in lst1 :
        #if item in lst2 :
            #common . append ( item )
    #return common

    index1 = 0
    index2 = 0
    common = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] == lst2[index2]:
            common.append(lst1[index1])
            index1 += 1
            index2 += 1
        elif lst1[index1] < lst2[index2]:
            index1 += 1
        else:
            index2 += 1

    return common
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
