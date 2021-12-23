class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("%s is %s years old" % (self.name, self.age))

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.kind = "dog"

    def show_info(self):
        super().show_info()
        print("%s's kind is %s" % (self.name, self.kind))

class Pet(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner

    def show_info(self):
        super().show_info()
        print("%s's owner is %s" % (self.name, self.owner))


class PetDog(Pet, Dog):
    pass


pd = PetDog("dd", 19, "Lee")
pd.show_info()
