""" Rational numbers are ratios of two integers p/q, where p is called
the numerator and q is called the denominator. The denominator q is non-zero.
Operations on rationals include addition, multiplication, and comparisons:
>, <, >=, <=, ==
"""


class Rational:
    """ A class to represent a rational number.

    Attributes
    ==========
    @type num: int
        The numerator of the rational number
    @type denom: int
        The denominator of the rational number
    """

    def __init__(self, numerator, denominator):
        """ Initialize a new Rational with numerator and denominator.

        @type self: Rational
        @type numerator: int
        @type denominator: int
        @rtype: None

        >>> r1 = Rational(1, 2)
        >>> r1.num
        1
        >>> r1.denom
        2
        """

        self.num = numerator
        self.denom = denominator

    def __str__(self):
        """ Return a user-friendly string representation of this Rational.

        @type self: Rational
        @rtype: str

        >>> r1 = Rational(1, 2)
        >>> str(r1)
        '1 / 2'
        """

        return '{} / {}'.format(self.num, self.denom)



    def __eq__(self, other):
        """ Return whether or not this Rational is the same as other.

        @type self: Rational
        @type other: Rational | Any

        >>> r1 = Rational(1, 2)
        >>> r2 = Rational(1, 2)
        >>> r1 == r2
        True
        >>> r3 = Rational(1, 3)
        >>> r1 == r3
        False
        """

        #return self.num == other.num and self.denom == other.denom

        return type(self) == type(other) and self.num * other.denom == other.num * other.denom

        #using '/', we could do this but it might not always work the way we want because of rounding error from the
        #limitation of representing numbers on computer



    def to_float(self):
        """ Return the float representation of this Rational.

        @type self: Rational
        @rtype: float

        >>> r1 = Rational(1, 2)
        >>> r1.to_float()
        0.5
        >>> r2 = Rational(6, 3)
        >>> r2.to_float()
        2.0
        """

        return self.num / self.denom

    def __add__(self, other):
        """ Return a Rational that is the sum of this Rational and other.

        @type self: Rational
        @type other: Rational
        @rtype: Rational

        >>> r1 = Rational(4, 7)
        >>> r2 = Rational(2, 3)
        >>> r3 = r1 + r2
        >>> str(r3)
        '26 / 21'
        """

        return Ration(self.num * other.denom + other.num * self.denom, self.denom * other.denom)


    def __mul__(self, other):
        """ Return a Rational that is the product of this Rational and other.

        @type self: Rational
        @type other: Rational
        @rtype: Rational

        >>> r1 = Rational(11, 3)
        >>> r2 = Rational(4, 2)
        >>> r3 = r1 * r2
        >>> str(r3)
        '44 / 6'
        """

        return Rational(self.num * other.num, self.denom * other.denom)

    def __lt__(self, other):
        '''Return whether or not this Rational is lee than other

        @type self: Rational
        @type other: Rational
        @rtype: bool

        >>> r1 = Rational(1, 4)
        >>> r2 = Rational(1, 2)
        >>> r1 < r2
        True
        '''

        return self.num * other.denom < other.num * self.denom
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    r1 = Rational(1, 2)
    print(r1)
    r2 = Rational(1, 4)
    print(r2)
    r3 = r1 + r2
    print(r3)
    r4 = r1 * r2
    print(r4)
    rational_list = [r1, r2, r3, r4]
    rational_list.sort()
    for rational in rational_list:
        print(rational)

