# Python While Loop - Interview Questions

## Q1. What is a while loop?

**Answer:**

A `while` loop repeatedly executes a block of code as long as the given condition is `True`.

---

## Q2. Why do we use a while loop?

**Answer:**

A `while` loop is used when the number of iterations is not known in advance.

---

## Q3. What is the syntax of a while loop?

**Answer:**

```python
while condition:
    # code
```

---

## Q4. What happens if the condition becomes `False`?

**Answer:**

The loop stops executing.

---

## Q5. What is an infinite loop?

**Answer:**

An infinite loop is a loop that never ends because its condition never becomes `False`.

Example:

```python
i = 1

while i <= 5:
    print(i)
```

---

## Q6. How do you stop an infinite loop?

**Answer:**

Update the loop variable so that the condition eventually becomes `False`.

Example:

```python
i += 1
```

---

## Q7. What is the difference between `for` and `while`?

**Answer:**

| for                                    | while                               |
| -------------------------------------- | ----------------------------------- |
| Used when iterations are known         | Used when iterations are unknown    |
| Often uses `range()` or a sequence     | Uses a condition                    |
| Counter is often handled automatically | Counter is usually updated manually |

---

## Q8. Can a while loop execute zero times?

**Answer:**

Yes. If the condition is `False` initially, the loop body is never executed.

Example:

```python
i = 10

while i < 5:
    print(i)
```

---

## ⭐ Most Asked Fresher Interview Questions

* What is a while loop?
* Difference between `for` and `while`.
* What is an infinite loop?
* How do you stop an infinite loop?
* Can a while loop execute zero times?
