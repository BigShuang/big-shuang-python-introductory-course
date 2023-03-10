class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = ""

    def get_name(self):
        return self.name

    def show_info(self):
        print("%s is %s years old" % (self.get_name(), self.age))

    def say(self):
        print("%s say: %s" % (self.get_name(), self.sound))


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.kind = "Dog"
        self.sound = "Wang wang"

    def get_name(self):
        return "%s %s" % (self.kind, self.name)


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.kind = "Cat"
        self.sound = "miao~"

    def get_name(self):
        return "%s %s" % (self.kind, self.name)


class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.kind = "Sheep"
        self.sound = "Mie~"

    def get_name(self):
        return "%s %s" % (self.kind, self.name)


animals = [
    Dog("Duoduo", 10),
    Cat("Bubu", 12),
    Sheep("Lili", 15),
]

for a in animals:
    a.show_info()
    a.say()
