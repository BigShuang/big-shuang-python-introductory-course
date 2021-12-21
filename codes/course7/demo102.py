class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle.__init__(10, 20)
print(rect.width)
