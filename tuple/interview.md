# Python Tuples - Interview Questions

## Q1. What is a tuple in Python?

**Answer:**

A tuple is an ordered, immutable collection in Python that can store multiple values of different data types.

---

## Q2. Why do we use tuples?

**Answer:**

Tuples are used to store data that should not be modified after creation.

---

## Q3. Is a tuple mutable or immutable?

**Answer:**

A tuple is immutable, which means we cannot modify, add, update, or remove elements after creation.

---

## Q4. Can a tuple store different data types?

**Answer:**

Yes. A tuple can store different data types such as strings, integers, floats, booleans, and even lists.

Example:

```python
data = ("Harsh", 21, 8.5, True)
```

---

## Q5. What is the difference between List and Tuple?

**Answer:**

| List            | Tuple              |
| --------------- | ------------------ |
| Mutable         | Immutable          |
| Uses `[]`       | Uses `()`          |
| Can be modified | Cannot be modified |
| More methods    | Fewer methods      |

---

## Q6. Does tuple indexing start from 0?

**Answer:**

Yes. Tuple indexing starts from 0.

---

## Q7. What is the difference between indexing and slicing?

**Answer:**

Indexing accesses a single element.

Slicing accesses multiple elements (a range).

---

## Q8. Why is a comma required in a single-element tuple?

**Answer:**

Without a comma, Python treats it as a normal value instead of a tuple.

Example:

```python
("Apple")      # String

("Apple",)     # Tuple
```

---

## Q9. Can we modify a tuple after creating it?

**Answer:**

No. Tuples are immutable, so their elements cannot be modified after creation.

---

## Q10. What happens if we try to modify a tuple?

**Answer:**

Python raises a `TypeError`.

---

## Q11. Which methods are available for tuples?

**Answer:**

Only two commonly used methods are available:

* `count()`
* `index()`

---

## Q12. What does `count()` do?

**Answer:**

`count()` returns the number of occurrences of a specified value.

Example:

```python
numbers = (10, 20, 10, 30)

numbers.count(10)
```

---

## Q13. What does `index()` do?

**Answer:**

`index()` returns the index of the first occurrence of a value.

Example:

```python
fruits = ("Apple", "Banana", "Orange")

fruits.index("Banana")
```

---

## Q14. What is tuple packing?

**Answer:**

Tuple packing means storing multiple values inside a tuple.

Example:

```python
student = ("Harsh", 21, "Python")
```

---

## Q15. What is tuple unpacking?

**Answer:**

Tuple unpacking means assigning tuple elements to multiple variables.

Example:

```python
student = ("Harsh", 21, "Python")

name, age, course = student
```

---

## Q16. Why do tuples have fewer methods than lists?

**Answer:**

Tuples are immutable, so methods that modify data such as `append()`, `insert()`, `remove()`, `pop()`, and `sort()` are not available.

---

## Q17. Can a tuple contain duplicate values?

**Answer:**

Yes. Tuples can contain duplicate values.

Example:

```python
numbers = (10, 20, 10, 30)
```

---

## Q18. Can a tuple contain a list?

**Answer:**

Yes. A tuple can contain a list as one of its elements.

Example:

```python
data = ("Harsh", [10, 20, 30])
```

---

## Q19. When should we use a tuple instead of a list?

**Answer:**

Use a tuple when the data should remain constant and should not be modified after creation.

---

## Q20. What is the main advantage of tuples?

**Answer:**

The main advantage of tuples is data safety. Since tuples are immutable, they prevent accidental modification of data.

---

## ⭐ Most Asked Fresher Interview Questions

* What is a tuple?
* Is tuple mutable or immutable?
* Difference between List and Tuple.
* Why is a comma required in a single-element tuple?
* Can tuples store different data types?
* Can tuples contain duplicate values?
* What methods are available in tuples?
* What is tuple unpacking?
* When should we use tuples instead of lists?
* Why do tuples have fewer methods than lists?
