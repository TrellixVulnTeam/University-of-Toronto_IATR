class GradeEntry:
    """
    A course GradeEntry, including course name, course weight and course grade.

    === Attributes ===:
    @type name: str
        course identifier
    @type weight: float
        course weight
    @type grade: str | int
        course grade
    """

    def __init__(self, name, weight, grade):
        """
        Create a GradeEntry which includes course name, course weight and course
        grade that student gets.

        @type self: GradeEntry
        @type name: str
        @type weight: float
        @type grade: str | int
        @rtype: None
        """

        self.name = name
        self.weight = weight
        self.grade = grade
        self.get_point()

    def __eq__(self, other):
        """
        Return if this GradeEntry is equivalent to other.

        @type self: GradeEntry
        @type other: GradeEntry
        @rtype: bool

        >>> g1 = GradeEntry('CSC148', 1.0, 90)
        >>> g2 = GradeEntry('MAT235', 1.0, 'A+')
        >>> g3 = GradeEntry('MAT235', 1.0, 'A+')
        >>> g1 == g2
        False
        >>> g2 == g3
        True
        """

        raise NotImplementedError('Subclassneeded')

    def __str__(self):
        """
        Return a user-friendly string representation of
        GradeEntry self.

        @type self: GradeEntry
        @rtype: str

        >>> g = GradeEntry('ANT100', 1.0, 85)
        >>> print(g)
        'This student gets 85 on ANT100 which has weight 1.0'
        """

        raise NotImplementedError('Subclassneeded')

    def get_point(self):
        raise NotImplementedError('Subclassneeded')

class NumericGradeEntry(GradeEntry):
    """
    A course GradeEntry, including course name, course weight and course grade.

    === Attributs ===:
    @type _point: float | None
        the course point
    """

    def __init__(self, name, weight, grade):
        """
        Create a GradeEntry which includes course name, course weight, course
        grade that student gets.

        @type self: GradeEntry
        @type name: str
        @type weight: float
        @type grade: int
        @type _point: None
        @rtype: None

        >>> g = NumericGradeEntry('CSC148', 1.0, 90)
        >>> g._point
        None
        """

        GradeEntry.__init__(self, name, weight, grade)
        self._point = None

    def __eq__(self, other):
        """
        Return True iff this NumericGradeEntry is equivalent to other.

        @type self: NumericGradeEntry
        @type other: NumericGradeEntry
        @rtype: bool

        >>> g1 = NumericGradeEntry('CSC148', 1.0, 90)
        >>> g2 = NumericGradeEntry('MAT235', 1.0, 80)
        >>> g3 = NumericGradeEntry('MAT235', 1.0, 80)
        >>> g1 == g2
        False
        >>> g2 == g3
        True
        """

        return isinstance(self, type(other)) and self.name == other.name \
               and self.weight == other.weight and self.grade == other.grade

    def __str__(self):
        """
        Return a user-friendly string representation of NumericGradeEntry self.

        @type self: NumericGradeEntry
        @rtype: str

        >>> g1 = NumericGradeEntry('CSC148', 1.0, 90)
        >>> print(g1)
        This student gets 90 on CSC148 which has weight 1.0
        """

        return ' This student gets {} on {} which has weight {}'.\
            format(self.grade, self.name, self.weight)

    def get_point(self):
        """
        Return point basing on grade.

        @type self: GradeEntry
        @rtype: float

        >>> g = NumericGradeEntry('CSC148', 1.0, 90)
        >>> g.get_point()
        4.0
        """
        if self.grade <= 49:
            return 0.0
        elif 50 <= self.grade <= 52:
            return 0.7
        elif 53 <= self.grade <= 56:
            return 1.0
        elif 57 <= self.grade <= 59:
            return 1.3
        elif 60 <= self.grade <= 62:
            return 1.7
        elif 63 <= self.grade <= 66:
            return 2.0
        elif 67 <= self.grade <= 69:
            return 2.3
        elif 70 <= self.grade <= 72:
            return 2.7
        elif 73 <= self.grade <= 76:
            return 3.0
        elif 77 <= self.grade <= 79:
            return 3.3
        elif 80 <= self.grade <= 84:
            return 3.7
        elif 85 <= self.grade <= 89:
            return 4.0
        elif 90 <= self.grade <= 100:
            return 4.0

    point = property(get_point)


class LetterGradeEntry(GradeEntry):
    """
    A course LetterGradeEntry, including course name, course weight
    and course grade.

    === Attributs ===:
    @type _point: float | None
        the course point
    """

    def __init__(self, name, weight, grade):
        """
        Create a GradeEntry which includes course name, course weight, course
        grade that student gets.

        @type self: LetterGradeEntry
        @type name: str
        @type weight: float
        @type grade: str
        @type _point: None
        @rtype: None

        >>> g = LetterGradeEntry('CSC148', 1.0, 90)
        >>> g._point
        None
        """

        GradeEntry.__init__(self, name, weight, grade)
        self._point = None

    def __eq__(self, other):
        """
        Return True iff this NumericGradeEntry is equivalent to other.

        @type self: LetterGradeEntry
        @type other: LetterGradeEntry
        @rtype: bool

        >>> g1 = LetterGradeEntry('CSC148', 1.0, B)
        >>> g2 = LetterGradeEntry('MAT235', 1.0, 'A+')
        >>> g3 = LetterGradeEntry('MAT235', 1.0, 'A+')
        >>> g1 == g2
        False
        >>> g2 == g3
        True
        """

        return isinstance(self, type(other)) and self.name == other.name \
               and self.weight == other.weight and self.grade == other.grade

    def __str__(self):
        """
        Return a user-friendly string representation of NumericGradeEntry self.

        @type self: LetterGradeEntry
        @rtype: str

        >>> g1 = NumericGradeEntry('CSC148', 1.0, A)
        >>> print(g1)
        This student gets A on CSC148 which has weight 1.0
        """

        return ' This student gets {} on {} which has weight {}'. \
            format(self.grade, self.name, self.weight)

    def get_point(self):
        """
        Return point basing on grade.

        @type self: GradeEntry
        @rtype: float

        >>> g = LetterGradeEntry('CSC148', 1.0, 'A+')
        >>> g.get_point()
        4.0
        """
        if self.grade == 'F':
            return 0.0
        elif self.grade == 'D-':
            return 0.7
        elif self.grade == 'D':
            return 1.0
        elif self.grade == 'D+':
            return 1.3
        elif self.grade == 'C-':
            return 1.7
        elif self.grade == 'C':
            return 2.0
        elif self.grade == 'C+':
            return 2.3
        elif self.grade == 'B-':
            return 2.7
        elif self.grade == 'B':
            return 3.0
        elif self.grade == 'B+':
            return 3.3
        elif self.grade == 'A-':
            return 3.7
        elif self.grade == 'A':
            return 4.0
        elif self.grade == 'A+':
            return 4.0

    point = property(get_point)


if __name__ == "__main__":
    g1 = LetterGradeEntry('CSC148', 2.0, 'A+')
    g2 = NumericGradeEntry('CSC165', 2.0, 90)
    g3 = LetterGradeEntry('CSC240', 1.0, 'A+')
    print(g1.point)
    print(g2.point)
    print(g1)
    print(g2)
    grades = [g1, g2, g3]
    for g in grades:
        print('Weight: {}, grade: {}, points: {}'.
              format(g.weight, g.grade, g.point))
    total = sum(g.point * g.weight for g in grades)
    total_weight = sum([g.weight for g in grades])
    print('GPA = {}'.format(total / total_weight))

#    g4 = GradeEntry('ANT100', 1.0, 90)
#    print(g4)

