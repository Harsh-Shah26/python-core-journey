# Python Dictionaries - Interview Questions

## Q1. What is a dictionary in Python?

**Answer:**

A dictionary is an unordered, mutable collection of key-value pairs in Python.

---

## Q2. Why do we use dictionaries?

**Answer:**

Dictionaries store data as key-value pairs, making it easy to access values using meaningful keys instead of indexes.

---

## Q3. Can dictionary keys and values have different data types?

**Answer:**

Yes. Dictionary keys and values can have different data types.

Example:

```python
student = {
    "name": "Harsh",
    "age": 21,
    "cgpa": 8.5,
    "placed": False
}
```

---

## Q4. Is a dictionary mutable or immutable?

**Answer:**

A dictionary is mutable, which means we can add, update, or remove key-value pairs after creation.

---

## Q5. How do you access values in a dictionary?

**Answer:**

Dictionary values are accessed using their keys.

Example:

```python
student["name"]
```

---

## Q6. What is the difference between List and Dictionary?

**Answer:**

| List                 | Dictionary             |
| -------------------- | ---------------------- |
| Accessed using index | Accessed using key     |
| Uses `[]`            | Uses `{}`              |
| Stores values        | Stores key-value pairs |

---

## Q7. Can we update dictionary values?

**Answer:**

Yes. Since dictionaries are mutable, values can be updated using their keys.

Example:

```python
student["age"] = 22
```

---

## Q8. How do you add a new key-value pair?

**Answer:**

Assign a value to a new key.

Example:

```python
student["city"] = "Ahmedabad"
```

---

## Q9. What does `get()` do?

**Answer:**

`get()` safely returns the value of a key.

If the key does not exist, it returns `None` instead of raising an error.

---

## Q10. What is the difference between `get()` and `[]`?

**Answer:**

`student["city"]` raises a `KeyError` if the key does not exist.

`student.get("city")` returns `None` if the key does not exist.

---

## Q11. What does `keys()` do?

**Answer:**

`keys()` returns all keys of the dictionary.

---

## Q12. What does `values()` do?

**Answer:**

`values()` returns all values of the dictionary.

---

## Q13. What does `items()` do?

**Answer:**

`items()` returns all key-value pairs as tuples.

---

## Q14. What does `update()` do?

**Answer:**

`update()` updates existing key-value pairs or adds new key-value pairs.

Example:

```python
student.update({"age": 22})
```

---

## Q15. What does `pop()` do?

**Answer:**

`pop()` removes a key and returns its value.

Example:

```python
student.pop("age")
```

---

## Q16. What is the difference between `pop()` and `del`?

**Answer:**

`pop()` removes a key and returns its value.

`del` removes a key but does not return anything.

---

## Q17. What does `clear()` do?

**Answer:**

`clear()` removes all key-value pairs from the dictionary.

Example:

```python
student.clear()
```

---

## Q18. What does `copy()` do?

**Answer:**

`copy()` creates a shallow copy of the dictionary.

Example:

```python
new_student = student.copy()
```

---

## Q19. Can dictionary keys be duplicated?

**Answer:**

No. Dictionary keys must be unique.

If the same key is used again, the old value is overwritten.

Example:

```python
student = {
    "name": "Harsh",
    "name": "Rahul"
}

print(student)
```

Output:

```python
{'name': 'Rahul'}
```

---

## Q20. Can dictionary values be duplicated?

**Answer:**

Yes. Dictionary values can be duplicated.

Example:

```python
marks = {
    "Math": 90,
    "Science": 90,
    "English": 85
}
```

---

## ⭐ Most Asked Fresher Interview Questions

* What is a dictionary?
* Why do we use dictionaries?
* Difference between List and Dictionary.
* Is a dictionary mutable?
* Difference between `get()` and `[]`.
* Difference between `pop()` and `del`.
* Difference between `keys()`, `values()`, and `items()`.
* What does `update()` do?
* Can dictionary keys be duplicated?
* Can dictionary values be duplicated?
* What does `copy()` do?
* What does `clear()` do?
