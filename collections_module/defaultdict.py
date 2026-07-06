from collections import defaultdict

student = defaultdict(int)
print(student["age"])  # returns 0 without error


#2)
students = defaultdict(list)

students["Python"].append("Harsh")
students["Python"].append("Rahul")

students["Java"].append("Jay")
print(students)


#3( default string empty)
data = defaultdict(str)
print(data["name"])

#4) SETS
numbers = defaultdict(set)

numbers["A"].add(10)
numbers["A"].add(20)
numbers["A"].add(10)

print(numbers)