# Python Dictionaries Practice

# 1. Creating Dictionary

student = {
    "name": "Harsh",
    "age": 21,
    "course": "Python"
}

print(student)

# 2. Empty Dictionary

data = {}

print(data)

# 3. Different Data Types

student = {
    "name": "Harsh",
    "age": 21,
    "cgpa": 8.5,
    "placed": False
}

print(student)

# 4. Accessing Values

student = {
    "name": "Harsh",
    "age": 21,
    "course": "Python"
}

print(student["name"])      # Harsh
print(student["age"])       # 21
print(student["course"])    # Python

# 5. Updating Values

student["age"] = 22

print(student)

# 6. Adding New Key-Value Pair

student["city"] = "Ahmedabad"

print(student)

# 7. get()

print(student.get("name"))      # Harsh  GET(()returns NONE if missing KEYS
print(student.get("city"))      # Ahmedabad
print(student.get("salary"))    # None

# 8. keys()

print(student.keys())

# 9. values()

print(student.values())

# 10. items()

print(student.items())

# 11. update()

student.update({"age": 23})

print(student)

student.update({"country": "India"})

print(student)

# 12. pop()

removed = student.pop("country")

print(removed)
print(student)

# 13. del

del student["course"]

print(student)

# 14. clear()

temp = {
    "name": "Harsh",
    "age": 21
}

temp.clear()

print(temp)

# 15. copy()

new_student = student.copy()
print(new_student)