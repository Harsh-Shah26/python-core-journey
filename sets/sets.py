# Python Sets Practice

# 1. Creating Set

fruits = {"Apple", "Banana", "Orange"}

print(fruits)          # Unordered output

# 2. Empty Set

data = set()

print(data)            # set()
print(type(data))      # <class 'set'>

# 3. Empty Dictionary

data = {}

print(type(data))      # <class 'dict'>

# 4. Duplicate Values

numbers = {10, 20, 30, 20, 10}

print(numbers)         # {10, 20, 30}

# 5. Mixed Data Set

data = {"Harsh", 21, 8.5, True}

print(data)            # Unordered output

# 6. add()

fruits = {"Apple", "Banana"}

fruits.add("Orange")

print(fruits)          # Adds one element

# 7. update()

fruits = {"Apple", "Banana"}

fruits.update({"Orange", "Mango"})

print(fruits)          # Adds multiple elements

# 8. remove()

fruits = {"Apple", "Banana", "Orange"}

fruits.remove("Banana")

print(fruits)          # Banana removed

# 9. discard()

fruits = {"Apple", "Banana"}

fruits.discard("Mango")

print(fruits)          # No error

# 10. pop()

fruits = {"Apple", "Banana", "Orange"}

removed = fruits.pop()

print(removed)         # Random element
print(fruits)          # Remaining set

# 11. clear()

fruits = {"Apple", "Banana", "Orange"}

fruits.clear()

print(fruits)          # set()

# 12. copy()

numbers = {10, 20, 30}

new_numbers = numbers.copy()

print(new_numbers)     # {10, 20, 30}

# 13. union()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))        # {1, 2, 3, 4, 5}

# 14. intersection()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2)) # {3}

# 15. difference()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.difference(set2))   # {1, 2}