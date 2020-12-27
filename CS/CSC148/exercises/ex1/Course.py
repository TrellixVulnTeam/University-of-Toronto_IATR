class Course:
    """ Create a Course includes students information of this course.

    === Attribute ===
    @type limit: int
    @type student_list: list
    """
    def __init__(self, limit):
        """ Creat a new Course with limit number students
        @type self: Course
        @type limit: int
        @rtype: None
        """
        self.limit = limit
        self.list = []

    def change_limit(self, new_limit):
        """ Change course litmi with new_limit number
        @type self: Course
        @type new_limit: int
        @rtype: None
        """
        self.limit = new_limit

    def add(self, id):
        """add student into this course
        @type self: Course
        @type id: int
        @rtype: None
        """
        if id not in self.list and len(self.list) < self.limit:
            self.list.append(id)

    def drop(self,id):
        """drop student from this course
        @type self: Course
        @type id: int
        @rtype: None
        """
        if id in self.list:
            self.list.remove(id)



if __name__ == '__main__':
    c = Course(5)
    c.add(1)
    c.add(2)
    c.add(3)
    c.add(4)
    c.add(5)
    c.add(6)
    c.drop(5)
    c.change_limit(10)
    c.add(10)
    c.add(20)
    print(c.list)
