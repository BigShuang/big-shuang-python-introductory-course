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


shapes = [
    Rectangle(1, 2), EqualTriangle(3), Circle(4),
    Rectangle(5, 6), EqualTriangle(7), Circle(8),
]

areas = 0
for shape in shapes:
    areas += shape.get_area()

print(areas)
