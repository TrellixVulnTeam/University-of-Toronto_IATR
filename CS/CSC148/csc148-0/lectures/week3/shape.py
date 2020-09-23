""" Demonstration of Inheritance """
# ignore documentation references to Square for now

from turtle import Turtle
from lectures.week2.point import Point


class Shape:
    """
    A shape that can draw itself, move, and
    report area and perimeter.

    === Attributes ===
    @type corners: list[Point]
       corners of this square
    @type perimeter: float
       length to traverse corners
    @type area: float
        area of this Square
    """
    def __init__(self, corners):
        """
        Create a new Square self with corners.

        Assume the corners are traversed in order, that
        the sides are of equal length, and that the vertices
        are right angles.

        @type self: Square
        @type corners: list[Point]
        @rtype: None
        """
        # shallow copy of corners
        self.corners = corners[:]
        self._turtle = Turtle()
        self._set_perimeter()
        self._set_area()


    # perimeter will likely be computed in the same way for most
    # potential subclasses
    def _set_perimeter(self):
        """
        Set Square self's perimeter to the sum of the distances
        between corners.

        @type self: Square
        @rtype: None
        """
        distance_list = []
        for i in range(len(self.corners)):
            distance_list.append(self.corners[i].distance(
                    self.corners[i - 1]))
        self._perimeter = sum(distance_list)

    def _get_perimeter(self):
        """
        Return the perimeter of this Square

        @type self: Square
        @rtype: float
        """
        return self._perimeter

    # perimeter is immutable --- no setter method in property
    perimeter = property(_get_perimeter)

    # area will be computed differently for most shapes
    def _set_area(self):
        """
        Set the area of Square self to the square of
        its sides.

        @type self: Square
        @rtype: None
        """
        # impossible so we have the method defined, but it doesn't do
        # anything meaningful
        # the actual behaviour should be implemented in the subclass
        self._area = -1

    def _get_area(self):
        """
        Return the area of Square self.

        @type self: Square
        @rtype: float

        >>> Square([Point(1, 1), Point(2, 1), Point(2, 2), Point(1, 2)]).area
        1.0
        """
        return self._area

    # area is immutable --- no setter method in property
    area = property(_get_area)

    def move_to(self, x_offset, y_offset):
        """
        Move Square self to a new position by adding
        Point offset_point to each corner.

        @type self: Square
        @type x_offset: float | int
        @type y_offset: float | int
        @rtype: None
        """
        for c in self.corners:
            c.move(x_offset, y_offset)

    def draw(self):
        """
        Draw Square self.

        @type self: Square
        @rtype: None
        """
        self._turtle.penup()
        self._turtle.goto(self.corners[-1].x, self.corners[-1].y)
        self._turtle.pendown()
        for i in range(len(self.corners)):
            self._turtle.goto(self.corners[i].x, self.corners[i].y)
        self._turtle.penup()
        self._turtle.goto(0, 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = Square([Point(1, 1), Point(1, 2), Point(2, 2), Point(2, 1)])
    print(s.area)
    print(s.perimeter)
    s.draw()
