# __repr__ method
# Used to define developer-friendly object representation

class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"


s1 = Student("Harsh")

print(repr(s1))