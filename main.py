
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

    def validate_age(self):
        if self.age < 18:
            print("Is minor")


p1 = Person("John", 17)
p1.myfunc()
p1.validate_age()
