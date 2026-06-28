# Python Sets - Interview Questions

## Q1. What is a set in Python?

**Answer:**

A set is an unordered, mutable collection of unique elements in Python.

---

## Q2. Why do we use sets?

**Answer:**

Sets are used when we want to store unique values and remove duplicate values automatically.

---

## Q3. Can a set contain duplicate values?

**Answer:**

No. Sets do not allow duplicate values.

Example:

```python
numbers = {10, 20, 10, 30}

print(numbers)
```

Output:

```python
{10, 20, 30}
```

---

## Q4. Is a set ordered?

**Answer:**

No. Sets are unordered collections, so elements do not have fixed positions.

---

## Q5. Can we access set elements using indexing?

**Answer:**

No. Since sets are unordered, indexing is not supported.

---

## Q6. Is a set mutable or immutable?

**Answer:**

A set is mutable. We can add or remove elements after creating it.

---

## Q7. How do you create an empty set?

**Answer:**

An empty set is created using `set()`.

Example:

```python
data = set()
```

`{}` creates an empty dictionary, not a set.

---

## Q8. What does `add()` do in a set?

**Answer:**

`add()` adds a single element to a set.

---

## Q9. What does `update()` do in a set?

**Answer:**

`update()` adds multiple elements to a set.

---

## Q10. What is the difference between `remove()` and `discard()`?

**Answer:**

`remove()` raises an error if the element does not exist.

`discard()` does not raise an error if the element does not exist.

---

## Q11. What does `pop()` do in a set?

**Answer:**

`pop()` removes and returns a random element because sets are unordered.

---

## Q12. What does `clear()` do in a set?

**Answer:**

`clear()` removes all elements from the set.

---

## Q13. What does `copy()` do in a set?

**Answer:**

`copy()` creates a shallow copy of the set.

---

## Q14. What does `union()` do?

**Answer:**

`union()` returns a new set containing all unique elements from both sets.

Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
```

Output:

```python
{1, 2, 3, 4, 5}
```

---

## Q15. What does `intersection()` do?

**Answer:**

`intersection()` returns common elements from both sets.

Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))
```

Output:

```python
{3}
```

---

## Q16. What does `difference()` do?

**Answer:**

`difference()` returns elements that are present in the first set but not in the second set.

Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.difference(set2))
```

Output:

```python
{1, 2}
```

---

## Q17. What is the difference between List and Set?

**Answer:**

| List              | Set                       |
| ----------------- | ------------------------- |
| Ordered           | Unordered                 |
| Allows duplicates | Does not allow duplicates |
| Supports indexing | Does not support indexing |
| Uses `[]`         | Uses `{}`                 |

---

## Q18. Can a set store different data types?

**Answer:**

Yes. A set can store different immutable data types such as strings, integers, floats, and booleans.

---

## Q19. When should we use a set?

**Answer:**

Use a set when duplicate values should not be allowed or when we need unique values.

---

## Q20. Why does `pop()` remove a random element in a set?

**Answer:**

Because sets are unordered, elements do not have fixed positions. Therefore, `pop()` removes and returns an arbitrary element.

---

## ⭐ Most Asked Fresher Interview Questions

* What is a set?
* Why do we use sets?
* Can a set contain duplicate values?
* Is a set ordered?
* Can we access set elements using index?
* Difference between List and Set.
* Difference between `remove()` and `discard()`.
* What does `union()` do?
* What does `intersection()` do?
* What does `difference()` do?
* How do you create an empty set?
