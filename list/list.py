

# 1. Creating List
fruits = ["Apple", "Banana", "Orange", "Mango"]
print(fruits)          # ['Apple', 'Banana', 'Orange', 'Mango']
print(len(fruits))     # 4


# 2. Empty List creation
students = []
print(students)        # [] 


# 3. Mixed Data List
data = ["Harsh", 21, 8.5, True]
print(data)            # ['Harsh', 21, 8.5, True]


# 4. Indexing
fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[0])       # Apple
print(fruits[1])       # Banana
print(fruits[-1])      # Mango
print(fruits[-2])      # Orange


# 5. Slicing
fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[:2])      # ['Apple', 'Banana']
print(fruits[1:3])     # ['Banana', 'Orange']
print(fruits[2:])      # ['Orange', 'Mango']
print(fruits[-2:])     # ['Orange', 'Mango']
print(fruits[:])       # ['Apple', 'Banana', 'Orange', 'Mango']


# 6. Updating List
fruits = ["Apple", "Banana", "Orange"]
fruits[1] = "Mango"
print(fruits)          # ['Apple', 'Mango', 'Orange']


# 7. append()  add in the end of the list
fruits = ["Apple", "Banana"]
fruits.append("Orange")
print(fruits)          # ['Apple', 'Banana', 'Orange']


# 8. insert() can be done using indexing 
fruits = ["Apple", "Orange"]

fruits.insert(1, "Banana")

print(fruits)          # ['Apple', 'Banana', 'Orange']


# 9. extend() add multiple items in the LIST
fruits = ["Apple", "Banana"]
fruits.extend(["Orange", "Mango"])

print(fruits)          # ['Apple', 'Banana', 'Orange', 'Mango']


# 10. append() vs extend()
fruits = ["Apple"]

fruits.append(["Banana", "Orange"])
print(fruits)          # ['Apple', ['Banana', 'Orange']]

#EXTEND() 
fruits = ["Apple"]

fruits.extend(["Banana", "Orange"])
print(fruits)          # ['Apple', 'Banana', 'Orange']


# 11. remove() BY VALUE
fruits = ["Apple", "Banana", "Orange"]

fruits.remove("Banana")
print(fruits)          # ['Apple', 'Orange']


# 12. pop() by indexing NUM and also return DELETED ITEMS
fruits = ["Apple", "Banana", "Orange"]
removed = fruits.pop(1)

print(removed)         # Banana
print(fruits)          # ['Apple', 'Orange']


# 13. pop() Without Index
fruits = ["Apple", "Banana", "Orange"]

removed = fruits.pop()

print(removed)         # Orange
print(fruits)          # ['Apple', 'Banana']


# 14. del
fruits = ["Apple", "Banana", "Orange"]

del fruits[1]
print(fruits)          # ['Apple', 'Orange']


# 15. clear() the  WHOLE LIST
fruits = ["Apple", "Banana", "Orange"]

fruits.clear()
print(fruits)          # []


# METHODS

# 16. count()
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))     # 3
print(numbers.count(50))     # 0


# 17. index()
fruits = ["Apple", "Banana", "Orange"]

print(fruits.index("Banana"))     # 1


# 18. sort()
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)          # [1, 2, 3, 4]


# 19. reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()

print(numbers)          # [4, 3, 2, 1]


# 20. copy()
numbers = [10, 20, 30] 

new_numbers = numbers.copy()

print(new_numbers)      # [10, 20, 30]


# 21. Traversal Without Loop
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])        # Apple
print(fruits[1])        # Banana
print(fruits[2])        # Orange