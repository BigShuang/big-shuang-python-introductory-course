class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class EqualTriangle:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side * 3 ** (1/2) / 4


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


r1 = Rectangle(1, 1)
t1 = EqualTriangle(1)
c1 = Circle(1)

print("Rectangle area: %s" % r1.get_area())
print("EqualTriangle area: %s" % t1.get_area())
print("Circle area: %s" % c1.get_area())
