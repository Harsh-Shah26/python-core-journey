# Magic (Dunder) Methods in Python

## Definition

Magic Methods (also called Dunder Methods) are special methods whose names start and end with double underscores (__).

They allow Python developers to customize the behavior of objects.

Examples:

- __init__()
- __str__()
- __repr__()
- __len__()
- __eq__()
- __add__()
- __getitem__()

---

# 1. __init__()

## Purpose

Used to initialize an object.

It is automatically called when an object is created.

Example:

obj = Student("Harsh")

Python internally calls:

Student.__init__(obj, "Harsh")

---

# 2. __str__()

## Purpose

Defines how the entire object should look when printed.

Example:

print(obj)

Python internally calls:

obj.__str__()

Without __str__()

<__main__.Employee object at 0x...>

With __str__()

Employee(Name=Harsh, Salary=50000)

Use Cases

- Printing objects
- Logging
- Debugging
- Django Admin
- User-friendly object representation

---

# 3. __repr__()

## Purpose

Returns the developer-friendly representation of an object.

Example:

repr(obj)

Python internally calls:

obj.__repr__()

Difference

__str__()

→ Human-readable

__repr__()

→ Developer-friendly representation

---

# 4. __len__()

## Purpose

Defines the behavior of len().

Example

len(obj)

Python internally calls

obj.__len__()

---

# 5. __eq__()

## Purpose

Defines the behavior of == between two objects.

Example

obj1 == obj2

Python internally calls

obj1.__eq__(obj2)

---

# 6. __add__()

## Purpose

Defines the behavior of + operator.

Example

obj1 + obj2

Python internally calls

obj1.__add__(obj2)

---

# 7. __getitem__()

## Purpose

Allows objects to support indexing.

Example

obj[0]

Python internally calls

obj.__getitem__(0)

---

# Summary

| Method | Purpose |
|---------|---------|
| __init__ | Constructor |
| __str__ | User-friendly object representation |
| __repr__ | Developer representation |
| __len__ | Supports len() |
| __eq__ | Supports == |
| __add__ | Supports + |
| __getitem__ | Supports indexing [] |

---

# Interview Questions

## 1. What are Magic (Dunder) Methods?

Answer:

Magic methods are special methods surrounded by double underscores that allow us to customize the behavior of Python objects.

---

## 2. Why do we use __init__()?

Answer:

__init__() is a constructor that initializes object attributes when an object is created.

---

## 3. What is __str__()?

Answer:

__str__() returns a user-friendly string representation of an object. It is automatically called when an object is printed using print().

---

## 4. Why use __str__() if we can print obj.name?

Answer:

obj.name returns only one attribute.

__str__() defines the string representation of the entire object.

It is especially useful when printing objects directly, logging, debugging, and in frameworks like Django Admin, where objects are displayed automatically.

---

## 5. Difference between __str__() and __repr__()

Answer:

| __str__() | __repr__() |
|------------|-------------|
| Human-readable | Developer-friendly |
| Called by print(obj) | Called by repr(obj) |

---

## 6. What is __len__()?

Answer:

__len__() defines the behavior of len(object).

---

## 7. What is __eq__()?

Answer:

__eq__() defines how two objects are compared using the == operator.

---

## 8. What is __add__()?

Answer:

__add__() defines the behavior of the + operator for objects.

---

## 9. What is __getitem__()?

Answer:

__getitem__() allows objects to support indexing using square brackets ([]).

---

## 10. What is the difference between print(obj) and print(obj.name)?

Answer:

print(obj.name)

- Prints only one attribute.

print(obj)

- Prints the entire object.
- Uses __str__() if it exists.
- Otherwise, Python prints the default object representation.

---

# Key Interview Points

- Dunder = Double UNDERscore.
- Magic methods customize object behavior.
- __init__() → Constructor.
- __str__() → User-friendly representation.
- __repr__() → Developer representation.
- __len__() → len()
- __eq__() → ==
- __add__() → +
- __getitem__() → []
- print(obj) internally calls obj.__str__().
- len(obj) internally calls obj.__len__().
- obj1 + obj2 internally calls obj1.__add__(obj2).
- obj1 == obj2 internally calls obj1.__eq__(obj2).
- obj[index] internally calls obj.__getitem__(index).