# deque = Double Ended Queue
from collections import deque

numbers = deque([10,20,30])
print(numbers)

numbers.append(40)
print(numbers)

numbers.appendleft(5)
print(numbers)

numbers.popleft()
print(numbers)


# deque (Double Ended Queue) is a collection that allows fast insertion and deletion from both the left and right ends.
