class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("This is %s" % self.name)


class Child(Parent):
    def greet(self):
        print("Hi, I'm %s" % self.name)


p = Parent("Zhang san")
c = Child("Li si")
p.greet()
c.greet()
