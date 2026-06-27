# Python Strings Practice

# 1. String Basics
name = "Harsh Shah"
print(name)
print(len(name))          # 10

# 2. Indexing
print(name[0])            # starts from 0 so 'H'
print(name[1])            # a is on 2nd
print(name[-1])           # h means from LAST
print(name[-3])           # h '- STARTS FROM LAST AND from 0 but -1 so'


# 3. Slicing
print(name[:3])           # Har [Start from 0 to 2]
print(name[1:4])          # ars [start from 1 to 3]
print(name[2:])           # rsh Shah [start from 2 to till end]
print(name[-3:])          # hah [from -3 to till]
print(name[:])            # Harsh Shah [gieve whole because we have not specified]


# 4. String Immutability
# name[0] = "M"           # TypeError we can't change

new_name = name.replace("Harsh", "Marsh") #but we can replace and it returns new string

print(name)               # Harsh Shah
print(new_name)           # Marsh Shah


# 5. Case Methods
fruit = "i love banana"

print(fruit.upper())          # I LOVE BANANA
print(fruit.lower())          # i love banana
print(fruit.title())          # I Love Banana [capital each word's 1st CHAR]
print(fruit.capitalize())     # I love banana [Only capital 1st CHAR of 1st word]
print(fruit.swapcase())       # I LOVE BANANA [changing lower to uuper vice versa]


# 6. Space Methods
text = "   Python Strings   "

print(text.strip())           # Python Strings [removed space from both side]
print(text.lstrip())          # Python Strings___
print(text.rstrip())          # ___Python Strings


# 7. Replace Method
fruit = "i love banana"

print(fruit.replace("banana", "orange"))     # i love orange
print(fruit.replace("a", "@"))               # i love b@n@n@
print(fruit.replace("love", "like"))         # i like banana


# 8. Search Methods
print(fruit.find("b"))       # 7 
print(fruit.find("z"))       # -1 return if word not found

print(fruit.index("b"))      # 7
# print(fruit.index("z"))    # ValueError [it  returns ERROR if word not found]


# 9. Count Method
print(fruit.count("a"))          # 3 [a 3times appeard ]
print(fruit.count("banana"))     # 1
print(fruit.count("love"))       # 1
print(fruit.count("z"))          # 0


# 10. Startswith and Endswith
print(fruit.startswith("i"))         # True
print(fruit.startswith("love"))      # False

print(fruit.endswith("banana"))      # True
print(fruit.endswith("bananA"))      # False because A case-insensitive


# 11. String Checking Methods
print("Harsh".isalpha())         # True
print("Harsh123".isalpha())      # False

print("12345".isdigit())         # True
print("123abc".isdigit())        # False

print("Harsh123".isalnum())      # True
print("Harsh@123".isalnum())     # False

print("HELLO".isupper())         # True
print("hello".islower())         # True

print("   ".isspace())           # True
print("Hello World".isspace())   # False
print("\t\n".isspace())          # True because of escape sequence CHAR


# 12. Split Method
text = "i love banana"
print(text.split())                  # ['i', 'love', 'banana']

course = "Python-Django-DRF"
print(course.split("-"))             # ['Python', 'Django', 'DRF']


date = "26-01-2005"
print(date.split("-"))               # ['26', '01', '2005']


# 13. Join Method
text = "PYTHON"

print("=".join(text))       # P=Y=T=H=O=N
print("-".join(text))       # P-Y-T-H-O-N   


# 14. Date Split Example
date = "26-01-2005"
print(date.split("-"))  # ['26', '01', '2005']


# 15. f-Strings
student_name = "Harsh"
course = "Python Strings"
marks = 85

print(f"My name is {student_name}.")                    # Inserts variable
print(f"I am learning {course}.")                       # Inserts variable
print(f"My marks are {marks}.")                         # Inserts number
print(f"After adding 5 marks: {marks + 5}")              # Expression inside
print(f"{student_name} is learning {course} in detail.") # Multiple variables