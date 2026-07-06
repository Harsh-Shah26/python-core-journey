# namedtuple
# Used to create tuple with named fields
from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

s1=Student("harsh",21)
print(s1.name)
print(s1.age)  #while normal tuple print(student[1])


#deque = Double Ended Queue