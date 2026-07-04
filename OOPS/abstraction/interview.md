# Abstraction in Python

## Definition

Abstraction is the process of hiding implementation details and showing only the essential functionality to the user.

Example:
A user knows how to start a car but doesn't need to know how the engine works internally.

---

## Why do we use Abstraction?

- Hide implementation details.
- Improve security.
- Reduce code complexity.
- Force child classes to implement required methods.

---

## How to Implement Abstraction in Python?

Python provides the `abc` module.

```python
from abc import ABC, abstractmethod
```

- `ABC` → Abstract Base Class.
- `@abstractmethod` → Declares an abstract method.

---

## Rules

- Cannot create an object of an Abstract Class.
- Child class must implement all abstract methods.
- Otherwise, Python raises a `TypeError`.

---

## Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print("Engine Started")

car1 = Car()
car1.start_engine()
```

Output

```
Engine Started
```

---

# Interview Questions

### 1. What is Abstraction?

**Answer:**
Abstraction is the process of hiding implementation details and exposing only the essential functionality.

---

### 2. Which module is used for Abstraction in Python?

**Answer:**
The `abc` module.

---

### 3. What is `ABC`?

**Answer:**
`ABC` stands for Abstract Base Class. It is used to create abstract classes.

---

### 4. What is `@abstractmethod`?

**Answer:**
`@abstractmethod` is a decorator used to declare methods that must be implemented by child classes.

---

### 5. Can we create an object of an Abstract Class?

**Answer:**
No. An abstract class cannot be instantiated directly.

---

### 6. What happens if a child class doesn't implement an abstract method?

**Answer:**
Python raises a `TypeError` when creating the object.

---

# Key Points

- Hide implementation details.
- Show only essential functionality.
- Uses `ABC` and `@abstractmethod`.
- Child class must implement abstract methods.
- Cannot instantiate an abstract class directly.