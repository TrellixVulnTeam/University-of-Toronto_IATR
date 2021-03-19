class Student:
    """
    Create a student.
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'This student is easy 4.0'

    #__str__ has high priority than __repr__
    def __str__(self):
        return 'Zhang A +'

    def _get_name(self):
        print('This is get')
        return self._name

    def _set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception('Input a string, bro')

    name = property(_get_name, _set_name)

if __name__ == "__main__":
    s = Student('harry')
    print(s)
    s.name = 'jerry'
    print(s.name)
    #s.name = 5
