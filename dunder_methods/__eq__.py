# __eq__ method
# Used to define behavior of == operator between objects

class Book:

    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title == other.title


book1 = Book("Python")
book2 = Book("Python")
book3 = Book("Django")

print(book1 == book2)
print(book1 == book3)