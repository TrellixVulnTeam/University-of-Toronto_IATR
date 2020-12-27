"""CSC148 Exercise 2: Inheritance and Introduction to Stacks

=== CSC148 Fall 2016 ===
Diane Horton, David Liu, and Danny Heap
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 2.
It is divided into two parts:
- Task 1, which contai【期末】Exams.zip【期末】Exams.zipns a set of classes that build on your work from
  last week
- Task 2, which contains the skeleton of a simple function involving a Stack
  data structure.

Notes:
  1. When you override a method, you generally do not need to include a
     method docstring, unless there are subclass-specific details to describe.
     While PyCharm will complain about a missing docstring, you may ignore this
     warning *for this specific case*.
  2. A lot of starter code has been provided! Read through it carefully
     before starting. You may also find it interesting to compare our work
     against what you did for Exercise 1.
"""
# You will find these imports useful. Please do not import any others,
# or python_ta will deduct marks.

from math import sqrt  # sqrt used to calculate diagonal distances
import random          # used to generate random numbers


##############################################################################
# Task 1: Cars and other vehicles
##############################################################################
class SuperDuperManager:
    """A class responsible for keeping track of all cars in the system.
    """
    # @param dict[str, Vehicle] _vehicles:
    #    A map of unique string identifiers to the corresponding vehicles.
    #    For example, _vehicles['a01'] would be a vehicle corresponding to
    #    the id_ 'a01'.

    def __init__(self):
        """Initialize a new SuperDuperManager.

        Initially there are no vehicles in the system.

        @param SuperDuperManager self:
        @rtype: None
        """
        self._vehicles = {}

    def add_vehicle(self, vehicle_type, id_, fuel):
        """Add a new vehicle to the system of the given type.

        The new vehicle is identified by the string <id_>,
        and has initial amount of fuel <fuel>.

        Do nothing if there is already a vehicle with the given id.

        Precondition: <vehicle_type> is one of 'Car', 'Helicopter', or
                      'UnreliableMagicCarpet'.

        @param SuperDuperManager self:
        @param str vehicle_type:
        @param str id_:
        @param int fuel:
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._vehicles:
            if vehicle_type == 'Car':
                self._vehicles[id_] = Car(fuel)
            elif vehicle_type == 'Helicopter':
                self._vehicles[id_] = Helicopter(fuel)
            elif vehicle_type == 'UnreliableMagicCarpet':
                self._vehicles[id_] = UnreliableMagicCarpet(fuel)

    def move_vehicle(self, id_, new_x, new_y):
        """Move a vehicle with the given id.

        The vehicle called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no vehicle with the given id,
        or if the corresponding vehicle does not have enough fuel to move.

        @param SuperDuperManager self: SuperDuperManager
        @param str id_:
        @param int new_x:
        @param int new_y:
        @rtype: None
        """
        if id_ in self._vehicles:
            self._vehicles[id_].move(new_x, new_y)

    def get_vehicle_position(self, id_):
        """Return the position of the vehicle with the given id.

        Return a tuple of the (x, y) position of the vehicle.
        Return None if there is no vehicle with the given id.

        @param SuperDuperManager self: SuperDuperManager
        @param str id_: str
        @rtype: (int, int) | None
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].position

    def get_vehicle_fuel(self, id_):
        """Return the amount of fuel of the vehicle with the given id.

        Return None if there is no vehicle with the given id.

        @param SuperDuperManager self:
        @param str id_:
        @rtype: int | None
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].fuel


class Vehicle:
    """ A superclass for a vehicle in the Super Duper system.

    Note that this interface specifies *two* public attributes,
    and *two* public methods (the constructor is not considered public).

    Of the public methods, a default implementation is given for move,
    but not fuel_needed.

    It also defines a constructor that should be called by each of its
    subclasses.

    === Attributes ===
    @param tuple(int) position:
        The position of this vehicle.
    @param int fuel:
        The amount of fuel remaining for this vehicle.

    === Representation invariants ===
       fuel >= 0
    """
    def __init__(self, new_fuel, new_position):
        """Initialize a new Vehicle with the given fuel and position.

        Precondition: new_fuel >= 0

        @param Vehicle self: Vehicle itself
        @param int new_fuel: fuel amount
        @param (int, int) new_position: destination coordinates
        @rtype: None
        """
        self.fuel = new_fuel
        self.position = new_position

    def fuel_needed(self, new_x, new_y):
        """Return how much fuel would be used to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.

        @param Vehicle self: Vehicle itself
        @param int new_x: destination's x coordinate
        @param int new_y: destination's y coordinate
        @rtype: float
        """
        raise NotImplementedError

    def move(self, new_x, new_y):
        """Move this vehicle to a new position.

        Do nothing if this vehicle does not have enough fuel to move.

        @param Vehicle self: Vehicle itself
        @param int new_x: destination's x coordinate
        @param int new_y: destination's y coordinate
        @rtype: None
        """
        needed = self.fuel_needed(new_x, new_y)
        if needed <= self.fuel:
            self.position = (new_x, new_y)
            self.fuel -= needed


# TODO: Implement this class (you can use your work from Exercise 1)
class Car(Vehicle):
    """A Car in the Super Duper system.

    Car original position is at (0, 0).

    A Car can only move vertically and horizontally, and uses
    one unit of fuel per unit distance travelled.

    Do nothing if the Car does not have enough fuel to move.

    === Attributes ===
    @param tuple(int) position:
        The position of this Car.
    @param int fuel:
        The amount of fuel remaining for this Car.

    === Representation invariants ===
       fuel >= 0
    """
    def __init__(self, fuel, position=(0, 0)):
        """
        Initialize a new Car with the given fuel and position.

        Precondition: new_fuel >= 0

        @param Car self: Car itself.
        @param int fuel: fuel amount.
        @param (int, int) position: original position.
        @rtype: None
        """
        Vehicle.__init__(self, fuel, position)

    def fuel_needed(self, new_x, new_y):
        """Return how much fuel would be used to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this Car may not move to the given position.

        @param Car self: Car itself.
        @param int new_x: destination's x coordinate
        @param int new_y: destination's y coordinate
        @rtype: float
        """
        distance = abs(new_x - self.position[0]) + abs(new_y - self.position[1])
        return distance




# TODO: Implement this class. Note: We've imported the sqrt function for you.
class Helicopter(Vehicle):
    """
    A helicopter. Can travel diagonally between points.

    Hlicopter original position is (3, 5).

    After each move, amount of fuel will round down to the nearest integer.

    Do nothing if Helicopter does not have enough fuel to move.

    === Attributes ===
    @param tuple(int) position:
        The position of this vehicle.
    @param int fuel:
        The amount of fuel remaining for this vehicle.

    === Representation invariants ===
       fuel >= 0
    """

    def __init__(self, fuel, position=(3, 5)):
        """
        Create a Helicopter with fuel amount and default position

        Precondition: new_fuel >= 0

        @param Car self: Helicopter itself.
        @param int fuel: fuel amount.
        @param (int, int) position: original position.
        @rtype: None
        """
        Vehicle.__init__(self, fuel, position)

    def fuel_needed(self, new_x, new_y):
        """Return how much fuel would be used to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.

        @param Helicopter self: Helicopter itself
        @param int new_x: destination's x coordinates
        @param int new_y: destination's y coordinates
        @rtype: float
        """
        return sqrt((abs(new_x - self.position[0]))**2 +
                    (abs(new_y - self.position[1]))**2)

    def move(self, new_x, new_y):
        """Move this Helicopter to a new position.

        Do nothing if this Helicopter does not have enough fuel to move.

        @param Helicopter self: Helicopter itself
        @param int new_x: destination's x coordinates
        @param int new_y: destination's y coordinates
        @rtype: None
        """
        needed = self.fuel_needed(new_x, new_y)
        if needed <= self.fuel:
            self.position = (new_x, new_y)
            self.fuel = int(self.fuel - needed)

# TODO: Implement this class. Note: We've imported the random module for you.
class UnreliableMagicCarpet(Vehicle):
    """
    An unreliable magic carpet.

    An UnreliableMagicCarpet is created at random position (x, y), range of x is
    integer between 0 to 10 inclusively, range of y is integer between 0 to 10
    inclusively too.

    Does not need to use fuel to travel, but ends up in a random position
    within two horizontal and vertical units from the target destination.

    === Attributes ===
    @param tuple(int) position:
        The position of this vehicle.
    @param int fuel:
        The amount of fuel remaining for this vehicle.
    """
    def __init__(self, fuel, position=(random.randint(0, 10),
                                       random.randint(0, 10))):
        """
        Create a Helicopter with fuel amount and default position
        """
        Vehicle.__init__(self, fuel, position)

    def fuel_needed(self, new_x, new_y):
        """
        Return how much fuel would be used to move to the given position.

        Note: the amount returned always be 0 since
        UnreliableMagicCarpet does not consume fuel.

        @param UnreliableMagicCarpet self: UnreliableMagicCarpet itself
        @param int new_x: destination's x coordinates
        @param int new_y: destination's y coordinates
        @rtype: int
        """
        return 0

    def move(self, new_x, new_y):
        """
        Move this UnreliableMagicCarpet to a new position.

        Note: The UnreliableMagicCarpet will move to random position
        around taiget one.

        @param UnreliableMagicCarpet self: UnreliableMagicCarpet itself
        @param int new_x: destination's x coordinates
        @param int new_y: destination's y coordinates
        @rtype: None
        """
        needed = self.fuel_needed(new_x, new_y)
        if needed <= self.fuel:
            dx = random.randint(-2, 2)
            dy = random.randint(-2, 2)
            self.position = (new_x + dx, new_y + dy)


##############################################################################
# Task 2: Introduction to Stacks
##############################################################################
def reverse_top_two(stack):
    """Reverse the top two elements on <stack>.

    Precondition: <stack> has at least two items.

    @param Stack stack:
    @rtype: None

    >>> from obfuscated_stack import Stack
    >>> stack = Stack()
    >>> stack.add(1)
    >>> stack.add(2)
    >>> reverse_top_two(stack)
    >>> stack.remove()
    1
    >>> stack.remove()
    2
    """
    # TODO: implement this function after you've read about Stacks.
    top_1 = stack.remove()
    top_2 = stack.remove()
    stack.add(top_1)
    stack.add(top_2)

if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta
    python_ta.check_all(config='pylint.txt')

    # Uncomment and run before final submission. This checks for style errors
    # in addition to code inconsistencies and forbidden Python features.
    # python_ta.check_all(config='pylint.txt')
