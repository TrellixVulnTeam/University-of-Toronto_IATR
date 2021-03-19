"""CSC148 Exercise 1: Composition of classes

=== CSC148 Winter 2017 ===
Diane Horton, David Liu, Danny Heap
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for Exercise 1.
It contains two classes that work together:
- SuperDuperManager, which manages all the cars in the system
- Car, a class which represents a single car in the system

Your task is to design and implement the Car class, and then modify the
SuperDuperManager methods so that they make proper use of the Car class.

You are not allowed to modify the public interface of any of the
SuperDuperManager methods.  We have marked the parts of the code you
should change with TODOs, which you should remove once you've
completed them.

Note:
     You'll notice we use a trailing underscore for the parameter name
     "id_" in a few places. It is used to avoid conflicts with Python
     keywords. Here we want to have a parameter named "id", but that is
     already the name of a built-in function. So we call it "id_" instead.
"""


class SuperDuperManager:
    """ A class responsible for keeping track of all cars in the system.
    """
    def __init__(self):
        """Initialize a new SuperDuperManager.

        There are no cars in the system when first created.

        @type self: SuperDuperManager
        @rtype: None
        """
        self._cars = {}

    def add_car(self, id_, fuel):
        """Add a new car to the system.

        The new car is identified by the string <id_>, and has initial amount
        of fuel <fuel>.

        Do nothing if there is already a car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @type fuel: int
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._cars:
            # TODO: Add the new car.
            self._cars[id_] = Car(fuel)

    def move_car(self, id_, new_x, new_y):
        """Move the car with the given id.

        The car called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no car with the given id,
        or if the corresponding car does not have enough fuel.

        @type self: SuperDuperManager
        @type id_: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id_ in self._cars:
            # TODO: Move the car with id <id_>.
            distance = abs(new_x - self._cars[id_].position[0]) + \
                       abs(new_y - self._cars[id_].position[1])
            if distance <= self._cars[id_].fuel:
                self._cars[id_].position = (new_x, new_y)
                self._cars[id_].fuel = self._cars[id_].fuel - distance


    def get_car_position(self, id_):
        """Return the position of the car with the given id.

        Return a tuple of the (x, y) position of the car with id <id_>.
        Return None if there is no car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: (int, int) | None
        """
        if id_ in self._cars:
            # TODO: Get the position of the car with id <id_>.
            return self._cars[id_].position
        return None

    def get_car_fuel(self, id_):
        """Return the amount of fuel of the car with the given id.

        Return None if there is no car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: int | None
        """
        if id_ in self._cars:
            # TODO: Get the amount of fuel of the car with id <id_>.
            return self._cars[id_].fuel
        return None

    def dispatch(self, x, y):
        """Move a car to the given location.

        Choose a car to move based on the following criteria:
        (1) Only consider cars that *can* move to the location.
            (Ignore ones that don't have enough fuel.)
        (2) After (1), choose the car that would move the *least* distance to
            get to the location.
        (3) If there is a tie in (2), pick the car whose id comes first
            alphabetically. Use < to compare the strings.
        (4) If no cars can move to the given location, do nothing.

        @type self: SuperDuperManager
        @type x: int
        @type y: int
        @rtype: None
        """
        # TODO: Implement this method!
        res_distance = []
        res_id = []

        #deal tie situation, create tie_id list
        tie_id = []
        for k, v in self._cars.items():
            distance = abs(x - v.position[0]) + \
                                  abs(y - v.position[1])
            if distance <= v.fuel:
                res_distance.append(distance)
                res_id.append(k)

        if len(res_distance) != 0:
            closest_distance = min(res_distance)

            if res_distance.count(closest_distance) == 1:
                closest_id = res_id[res_distance.index(closest_distance)]
                self.move_car(closest_id, x, y)
            else:
                for i in range(len(res_distance)):
                    if res_distance[i] == closest_distance:
                        tie_id.append(res_id[i])

                tie_id.sort()
                self.move_car(tie_id[0], x, y)




# TODO: Design and implement this class.
# TODO: Remember to document all attributes and methods!

class Car:
    """A car in the Super system.

    === Attributes ===
    @type fuel: int
        fuel amout the car remain
    @type position: list of int
        car position
    """
    def __init__(self, fuel, position=(0, 0)):
        """
        Creat a car with fuel amount and default position.

        @type self: Car
        @rtype = None
        """
        self.fuel = fuel
        self.position = position



if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta
    python_ta.check_all()

    # Uncomment and run before final submission. This checks for style errors
    # in addition to code inconsistencies and forbidden Python features.
    # python_ta.check_all()
    #a = SuperDuperManager()
    #a.add_car('bmw', 10)
    #a.add_car('toyota', 10)
    #a.add_car('cooper', 6)
    #a.add_car('benz', 8)
    #a.dispatch(2, 3)
    #print(a.get_car_position('benz'))
    #print(a.get_car_fuel('benz'))
    #a.move_car('toyota', 4, 5)
    #a.dispatch(5, 6)
    #print(a.get_car_position('bmw'))
    #print(a.get_car_fuel('bmw'))
