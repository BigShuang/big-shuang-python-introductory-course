class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

r1 = Rectangle(10, 20)
print(r1.get_area())  # 200
