# __len__ method
# Used to define behavior of len(object)

class Basket:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


basket = Basket(["banana", "cherry", "apple"])

print(len(basket))