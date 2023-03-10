class User:
    def __init__(self, account, name, password):
        self.account = account
        self.name = name
        self.password = password


class Student(User):
    pass


class Teacher(User):
    pass


class Admin(User):
    pass


class System:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.admins = []

