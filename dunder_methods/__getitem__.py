# __getitem__ method
# Used to make object support indexing like obj[index]

class MyList:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]


my_list = MyList([1, 2, 3, 4, 5])

print(my_list[2])