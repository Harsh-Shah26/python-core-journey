# Python Tuples Practice

# 1. Creating Tuple

fruits = ("Apple", "Banana", "Orange")

print(fruits)          # ('Apple', 'Banana', 'Orange')
print(len(fruits))     # 3

# 2. Empty Tuple

data = ()

print(data)            # ()

# 3. Single Element Tuple

fruit = ("Apple")

print(type(fruit))     # <class 'str'>

fruit = ("Apple",)

print(type(fruit))     # <class 'tuple'>

# 4. Mixed Data Tuple

data = ("Harsh", 21, 8.5, True)

print(data)            # ('Harsh', 21, 8.5, True)

# 5. Indexing

fruits = ("Apple", "Banana", "Orange", "Mango")

print(fruits[0])       # Apple
print(fruits[1])       # Banana
print(fruits[-1])      # Mango
print(fruits[-2])      # Orange

# 6. Slicing

fruits = ("Apple", "Banana", "Orange", "Mango")

print(fruits[:2])      # ('Apple', 'Banana')
print(fruits[1:3])     # ('Banana', 'Orange')
print(fruits[2:])      # ('Orange', 'Mango')
print(fruits[-2:])     # ('Orange', 'Mango')
print(fruits[:])       # ('Apple', 'Banana', 'Orange', 'Mango')

# 7. Tuple Immutability

fruits = ("Apple", "Banana", "Orange")

# fruits[1] = "Mango"  # TypeError

print(fruits)          # ('Apple', 'Banana', 'Orange')

# 8. count()

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))     # 3
print(numbers.count(50))     # 0

# 9. index()

fruits = ("Apple", "Banana", "Orange")

print(fruits.index("Banana"))     # 1

# 10. Tuple Packing

student = ("Harsh", 21, "Python")

print(student)             # ('Harsh', 21, 'Python')

# 11. Tuple Unpacking

student = ("Harsh", 21, "Python")

name, age, course = student

print(name)                # Harsh
print(age)                 # 21
print(course)              # Python