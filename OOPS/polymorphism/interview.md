# Polymorphism in Python

## Definition

Polymorphism means "One Interface, Many Forms".

The same method, function, or operator behaves differently depending on the object.

---

## Types / Examples

### 1. Method Overriding

A child class provides its own implementation of a method already defined in the parent class.

Example:

Dog.sound()
Cat.sound()

Same method name, different behavior.

---

### 2. Built-in Polymorphism

Python built-in functions work differently with different data types.

Example:

len("Harsh")
len([1, 2, 3, 4])
len((10, 20))

---

### 3. Method Overloading

Python does not support true method overloading like Java or C++.

But similar behavior can be achieved using:

- Default arguments
- *args
- **kwargs

Example:

def add(self, a, b, c=0)

---

### 4. Duck Typing

Python focuses on behavior, not object type.

If an object has the required method, Python can use it.

Example:

car.start()
bike.start()

---

### 5. Operator Overloading

Same operator behaves differently for different data types.

Example:

10 + 20
"Hello" + "World"
[1, 2] + [3, 4]

---

# Interview Questions

## 1. What is Polymorphism?

Answer:

Polymorphism means one interface with multiple forms. The same method or function behaves differently based on the object.

---

## 2. Does Python support Method Overloading?

Answer:

Python does not support true method overloading like Java or C++.

However, similar behavior can be achieved using default arguments, *args, or **kwargs.

---

## 3. Does Python support Method Overriding?

Answer:

Yes. Python supports method overriding through inheritance.

---

## 4. What is Duck Typing?

Answer:

Duck typing means Python checks whether an object has the required behavior or method, instead of checking its exact type.

---

## 5. What is Operator Overloading?

Answer:

Operator overloading allows the same operator to behave differently for different data types.

---

# Key Points

- Polymorphism means one interface, many forms.
- Method overriding is supported.
- True method overloading is not supported in Python.
- Duck typing is common in Python.
- Operators like + are polymorphic.