class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Pet(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner


p = Pet("lili", 10, "Li hua")
