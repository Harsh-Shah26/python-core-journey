# Python Lists - Interview Questions

## Q1. What is a list in Python?

**Answer:**

A list is an ordered, mutable collection in Python that can store multiple values of different data types.

Example:

```python
fruits = ["Apple", "Banana", "Orange"]
```

---

## Q2. Why do we use lists?

**Answer:**

Lists are used to store multiple values in a single variable, making data easier to manage and access.

---

## Q3. Can a list store different data types?

**Answer:**

Yes. A list can store different data types such as integers, strings, floats, booleans, and even other lists.

Example:

```python
data = ["Harsh", 21, 8.5, True]
```

---

## Q4. Is a list mutable or immutable?

**Answer:**

A list is mutable, which means we can modify, add, update, or remove elements after creating it.

---

## Q5. Does list indexing start from 0?

**Answer:**

Yes. Python list indexing starts from 0.

Example:

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])      # Apple
```

---

## Q6. What is the difference between indexing and slicing?

**Answer:**

Indexing is used to access a single element.

Slicing is used to access multiple elements (a range).

Example:

```python
fruits[1]      # Banana

fruits[1:3]    # ['Banana', 'Orange']
```

---

## Q7. Can we update a list after creating it?

**Answer:**

Yes. Since lists are mutable, we can update elements using their index.

Example:

```python
fruits = ["Apple", "Banana"]

fruits[1] = "Mango"
```

---

## Q8. What does `append()` do?

**Answer:**

`append()` adds a single element to the end of the list.

Example:

```python
fruits.append("Orange")
```

---

## Q9. What is the difference between `append()` and `insert()`?

**Answer:**

`append()` adds an element at the end of the list.

`insert()` adds an element at a specific index.

Example:

```python
fruits.append("Orange")

fruits.insert(1, "Orange")
```

---

## Q10. What is the difference between `append()` and `extend()`?

**Answer:**

`append()` adds a single object.

`extend()` adds multiple elements from another iterable.

Example:

```python
fruits = ["Apple"]

fruits.append(["Banana", "Orange"])
# ['Apple', ['Banana', 'Orange']]

fruits = ["Apple"]

fruits.extend(["Banana", "Orange"])
# ['Apple', 'Banana', 'Orange']
```

---

## Q11. What does `remove()` do?

**Answer:**

`remove()` removes an element by its value.

Example:

```python
fruits.remove("Banana")
```

---

## Q12. What does `pop()` do?

**Answer:**

`pop()` removes an element by index and returns the removed element.

If no index is given, it removes the last element.

Example:

```python
removed = fruits.pop()

print(removed)
```

---

## Q13. What is the difference between `remove()` and `pop()`?

**Answer:**

`remove()` removes an element by value.

`pop()` removes an element by index and returns the removed value.

---

## Q14. What is the difference between `del` and `pop()`?

**Answer:**

`del` deletes an element by index but does not return anything.

`pop()` deletes an element by index and returns the removed element.

---

## Q15. What is the difference between `del` and `clear()`?

**Answer:**

`clear()` removes all elements but keeps the list.

`del` can delete a specific element or the entire list.

Example:

```python
fruits.clear()

del fruits
```

---

## Q16. What does `count()` do?

**Answer:**

`count()` returns how many times a value appears in the list.

Example:

```python
numbers = [10, 20, 10, 30]

numbers.count(10)
```

---

## Q17. What does `index()` do?

**Answer:**

`index()` returns the index of the first occurrence of a value.

Example:

```python
fruits.index("Banana")
```

---

## Q18. What is the difference between `sort()` and `sorted()`?

**Answer:**

`sort()` modifies the original list.

`sorted()` returns a new sorted list without modifying the original.

Example:

```python
numbers.sort()

new_numbers = sorted(numbers)
```

---

## Q19. What does `reverse()` do?

**Answer:**

`reverse()` reverses the order of elements in the original list.

Example:

```python
numbers.reverse()
```

---

## Q20. What does `copy()` do?

**Answer:**

`copy()` creates a shallow copy of the list.

Example:

```python
new_list = old_list.copy()
```

---

## ⭐ Most Asked Fresher Interview Questions

* What is a list?
* Why do we use lists?
* Is a list mutable?
* Can a list store different data types?
* Difference between List and Tuple.
* Difference between `append()` and `extend()`.
* Difference between `append()` and `insert()`.
* Difference between `remove()` and `pop()`.
* Difference between `del` and `clear()`.
* Difference between `sort()` and `sorted()`.
* Difference between `sort()` and `reverse()`.
* What does `copy()` do?
* What is indexing?
* What is slicing?
* What is list traversal?
