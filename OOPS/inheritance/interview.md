# Inheritance in Python

## Definition

Inheritance is the process by which one class acquires the properties and methods of another class.

It promotes code reusability.

---

# Advantages

- Code Reusability
- Easy Maintenance
- Less Code Duplication
- Extensibility

---

# Types of Inheritance

## 1. Single Inheritance

One Parent → One Child

Example:

Animal → Dog

---

## 2. Multiple Inheritance

Multiple Parents → One Child

Example:

Father + Mother → Child

---

## 3. Multilevel Inheritance

GrandParent → Parent → Child

Example:

GrandFather → Father → Son

---

## 4. Hierarchical Inheritance

One Parent → Multiple Children

Example:

Animal → Dog

Animal → Cat

---

## 5. Hybrid Inheritance

Combination of two or more inheritance types.

---

# Method Overriding

Definition:

Method Overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

Example:

Parent:
sound()

Child:
sound()

The child method overrides the parent method.

---

# super()

Definition:

super() is used to access the parent class methods and constructor.

Example:

super().__init__()

super().show()

---

# Constructor Inheritance

If the child class does not define its own constructor, Python automatically calls the parent constructor.

If the child defines its own constructor, use:

super().__init__()

to call the parent constructor.

---

# MRO (Method Resolution Order)

Definition:

MRO determines the order in which Python searches for methods in an inheritance hierarchy.

Check using:

ClassName.mro()

Example:

D → B → C → A → object

---

# Important Functions

issubclass(Child, Parent)

Returns True if Child inherits Parent.

Example:

issubclass(Dog, Animal)

---

isinstance(object, Class)

Checks whether an object belongs to a class.

Example:

isinstance(d, Dog)

---

# Interview Questions

## 1. What is Inheritance?

Answer:

Inheritance is a mechanism that allows one class to acquire the properties and methods of another class.

---

## 2. Why do we use Inheritance?

Answer:

- Code Reusability
- Easy Maintenance
- Extensibility
- Reduces Code Duplication

---

## 3. How many types of inheritance are there in Python?

Answer:

- Single
- Multiple
- Multilevel
- Hierarchical
- Hybrid

---

## 4. What is Method Overriding?

Answer:

Method Overriding is when a child class provides its own implementation of a parent class method.

---

## 5. What is super()?

Answer:

super() is used to call parent class methods and constructors.

---

## 6. What is MRO?

Answer:

MRO (Method Resolution Order) is the order in which Python searches for methods in an inheritance hierarchy.

---

## 7. What is the difference between Parent Class and Child Class?

Parent Class:
Also called Base Class or Superclass.

Child Class:
Also called Derived Class or Subclass.

---

# Key Points

- Inheritance promotes code reusability.
- Python supports 5 types of inheritance.
- Child classes inherit parent properties and methods.
- Method Overriding provides runtime polymorphism.
- super() accesses parent members.
- MRO decides method lookup order.