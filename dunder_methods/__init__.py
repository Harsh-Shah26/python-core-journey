# __init__ method
# Constructor method
# Automatically called when object is created

class Person:

    def __init__(self, name):
        self.name = name


person1 = Person("Mohit")

print(person1.name)