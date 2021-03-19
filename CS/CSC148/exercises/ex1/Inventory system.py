class Inventory_system:
    """Create a inventory system to record one item information.

    === Attributes ===
    @type price: int | float
        item price
    @type description: str
        item description
    @type category: str
        item category
    @type item_num: int
        item number
    """

    def __init__(self, price, item_num, description, category):
        """ Create a Inventory system of item, incluing price, number, description and category.
        @type self: Inventory_system
        @type price: float | int
        @type item_num: int
        @description: str
        @category: str
        @rtype: None
        """
        self.price = price
        self.item_num = item_num
        self.description = description
        self.category = category

    def __str__(self):
        """ Return readable information about this item.
        @type self: Inventory_system
        @rtype: str
        """
        # return a new line
        return"""
        {} is {}$
        it's category is {} and item number is {}
        """.format(self.description, self.price, self.category, self.item_num)

    def discount(self, discount_percent):
        """Give price discount to this item.
        @type self: Inventory_system
        @type discount_percent: float
        @rtype: None
        """
        self.price = self.price * discount_percent

    def compare(self, other):
        """ Compare two item to see which is cheaper.
        @type self: Inventory_system
        @type other: Inventory_system
        @rtype: str
        """
        if self.price < other.price:
            return self.description
        elif self.price > other.price:
            return other.description
        else:
            return 'tie'

if __name__ == '__main__':
    item_1 = Inventory_system(10, 1001, 'T-shirt', 'Cloth')
    item_2 = Inventory_system(1000, 2001, 'BMW', 'Car')
    print(item_1)
    print(item_2)
    print(item_1.compare(item_2))
    item_2.discount(0.001)
    print(item_1.compare(item_2))
