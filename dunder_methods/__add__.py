# __add__ method
# Used to define behavior of + operator between objects

class Numbers:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Numbers(self.value + other.value)


n1 = Numbers(10)
n2 = Numbers(5)

result = n1 + n2

print(result.value)