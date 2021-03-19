from test_1 import Shape

class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    r1 = Rectangle(5,5)
    print(r1.area())



