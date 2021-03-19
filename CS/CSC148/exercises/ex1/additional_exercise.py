class Roster:
    """
    A Roster

    === Attributes ===
    @type list: list
        all member in this Roster
    """

    def __init__(self):
        """
        Create a Roster

        @type self: Roster
        @rtype: None
        """

        self.list = []

    def add(self, member):
        """
        Add a member into this Roster.

        @type self: Roster
        @type member: int | float | str | list
        @rtype: None
        """
        self.list.append(member)

    def remove(self, member):
        """
        Remove a member from this Roster.

        @type self: Roster
        @type member: int | float | str | list
        @rtype: None
        """

        self.list.remove(member)

    def display(self):
        """
        Return a user-friendly string representation of
        Point self.

        @type self: Roster
        @rtype: None
        """
        for item in self.list:
            print(item)

class ClassRoster(Roster):
    """
    A ClassRoster

    === Attributes ===
    @type limit: int
    @type list: list

        The student number limit of this course
    """
    def __init__(self, limit):
        """
        Create a ClassRoster

        @type self: ClassRoster
        @type limit: int
        @rtype: None
        """
        Roster.__init__(self)
        self.limit = limit

    def add(self, member):
        """
        Add a member to the ClassRoster

        @type self: ClassRoster
        @type member: int
        @rtype: None
        """
        if len(self.list) < self.limit:
            Roster.add(self, member)


class InventoryRoster(Roster):
    """
    A InventoryRoster

    === Attributes ===
    @type list: list
    @type
    """

    def __init__(self):
        """
        Create a InventoryRoster.

        @type self: InventoryRoster
        @rtype: None
        """
        Roster.__init__(self)

    def __str__(self):
        """
        Return a user-friendly string representation of
        Point self.

        @type self: InventoryRoster
        @rtype: str
        """
        s = ''
        for item in self.list:
            s += "This {} is {}$ and it's number is {}\n".format(item[2], item[0], item[1])
        return s

    def discount(self, number, discount):
        """
        Make a discout to one assigned item
        @type self: InventoryRoster
        @type discount: float
        @rtype: None
        """
        for i in range(len(self.list)):
            if self.list[i][1] == number:
                self.list[i][0] = self.list[i][0] * discount

    def __eq__(self, other):
        """
        Return True iff this Inventory Roster is same as other
        """
        new_1 = self.list[:]
        new_2 = other.list[:]
        new_1.sort()
        new_2.sort()
        return type(self) == type(other) and new_1 == new_2


if __name__ == "__main__":
    c1 = ClassRoster(3)
    c1.add(10)
    c1.add(20)
    c1.add(30)
    c1.add(50)
    c1.remove(20)
    c1.add(40)
    c1.display()

    I1 = InventoryRoster()
    I1.add([100, 2000, 'basketball', 'ball'])
    I1.add([200, 3000, 'T-shirt', 'Cloth'])
    print(I1)
    I1.discount(3000, 0.9)
    print('After Discount')
    print(I1)

    I2 = InventoryRoster()
    I2.add([500,4000, 'haha', 'houhou'])
    print(I1 == I2)
