# Python For Loop - Interview Questions

## Q1. What is a for loop in Python?

**Answer:**

A `for` loop is used to iterate over a sequence and execute a block of code for each item.

---

## Q2. Why do we use a for loop?

**Answer:**

A `for` loop reduces code repetition and makes programs shorter, cleaner, and easier to maintain.

---

## Q3. What can a for loop iterate over?

**Answer:**

A `for` loop can iterate over:

* String
* List
* Tuple
* Dictionary
* Set
* range()

---

## Q4. What does `range()` do?

**Answer:**

`range()` generates a sequence of numbers.

---

## Q5. Does `range(5)` include 5?

**Answer:**

No.

`range(5)` generates:

```
0 1 2 3 4
```

---

## Q6. What is the syntax of `range()`?

**Answer:**

```python
range(start, stop, step)
```

---

## Q7. What is the default starting value of `range()`?

**Answer:**

The default starting value is `0`.

Example:

```python
range(5)
```

Output:

```
0 1 2 3 4
```

---

## Q8. Is the stop value included in `range()`?

**Answer:**

No.

The stop value is always excluded.

---

## Q9. What does the step value do?

**Answer:**

The step value specifies the increment or decrement between numbers.

Example:

```python
range(2, 11, 2)
```

Output:

```
2 4 6 8 10
```

---

## Q10. Can the step value be negative?

**Answer:**

Yes.

A negative step is used for reverse iteration.

Example:

```python
range(10, 0, -1)
```

---

## Q11. Is `i` a keyword in Python?

**Answer:**

No.

`i` is just a variable name. Any valid variable name can be used.

---

## Q12. Can we use any variable name instead of `i`?

**Answer:**

Yes.

Example:

```python
for number in range(5):
    print(number)
```

---

## Q13. What is the difference between `range(5)` and `range(1, 6)`?

**Answer:**

`range(5)` generates:

```
0 1 2 3 4
```

`range(1, 6)` generates:

```
1 2 3 4 5
```

---

## Q14. How do you print numbers in reverse using a for loop?

**Answer:**

Use a negative step.

Example:

```python
for i in range(10, 0, -1):
    print(i)
```

---

## Q15. How do you print only even numbers using `range()`?

**Answer:**

Use step value `2`.

Example:

```python
for i in range(2, 21, 2):
    print(i)
```

---

## ⭐ Most Asked Fresher Interview Questions

* What is a for loop?
* Why do we use loops?
* What does `range()` do?
* Does `range()` include the stop value?
* Difference between `range(5)` and `range(1,6)`.
* What is the purpose of the step value?
* Can the step value be negative?
* Can we use any variable name instead of `i`?
