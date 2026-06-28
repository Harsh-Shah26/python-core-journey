# Python Operators - Interview Questions

## Q1. What are operators in Python?

**Answer:**

Operators are special symbols used to perform operations on variables and values.

Example:

```python
a = 10
b = 5

print(a + b)
```

---

## Q2. What are the different types of operators in Python?

**Answer:**

Python mainly provides the following types of operators:

* Arithmetic Operators
* Comparison Operators
* Assignment Operators
* Logical Operators
* Membership Operators
* Identity Operators

---

## Q3. What are arithmetic operators?

**Answer:**

Arithmetic operators are used to perform mathematical operations.

Operators:

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `//` Floor Division
* `%` Modulus
* `**` Exponentiation (Power)

---

## Q4. What is the difference between `/` and `//`?

**Answer:**

`/` performs normal division and always returns a floating-point value.

`//` performs floor division and returns the largest integer less than or equal to the result.

Example:

```python
10 / 3     # 3.3333333333333335

10 // 3    # 3
```

---

## Q5. What does the `%` operator do?

**Answer:**

The modulus operator (`%`) returns the remainder after division.

Example:

```python
10 % 3     # 1
```

Common use:

* Even/Odd number checking

---

## Q6. What does `**` represent?

**Answer:**

The `**` operator is used for exponentiation (power).

Example:

```python
2 ** 4     # 16
```

---

## Q7. What are comparison operators?

**Answer:**

Comparison operators compare two values and always return either `True` or `False`.

Operators:

* `==`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

---

## Q8. What is the difference between `=` and `==`?

**Answer:**

`=` is an assignment operator.

`==` is a comparison operator.

Example:

```python
a = 10          # Assignment

print(a == 10)  # Comparison
```

---

## Q9. What is the difference between `==` and `!=`?

**Answer:**

`==` checks whether two values are equal.

`!=` checks whether two values are different.

Example:

```python
10 == 10      # True

10 != 10      # False
```

---

## Q10. What do `>=` and `<=` mean?

**Answer:**

`>=` means greater than or equal to.

`<=` means less than or equal to.

Examples:

```python
18 >= 18      # True

15 >= 18      # False

10 <= 20      # True
```

---

## Q11. What are logical operators?

**Answer:**

Logical operators are used to combine multiple conditions.

There are three logical operators:

* `and`
* `or`
* `not`

---

## Q12. How does the `and` operator work?

**Answer:**

The `and` operator returns `True` only when both conditions are `True`.

Example:

```python
age = 20
has_license = True

print(age >= 18 and has_license)
```

Output:

```python
True
```

---

## Q13. How does the `or` operator work?

**Answer:**

The `or` operator returns `True` if at least one condition is `True`.

Example:

```python
True or False
```

Output:

```python
True
```

---

## Q14. What does the `not` operator do?

**Answer:**

The `not` operator reverses the boolean value.

Example:

```python
not True
```

Output:

```python
False
```

---

## Q15. What are assignment operators?

**Answer:**

Assignment operators are used to assign or update the value of a variable.

Common assignment operators:

* `=`
* `+=`
* `-=`
* `*=`
* `/=`
* `//=`
* `%=`
* `**=`

---

## Q16. What does `+=` do?

**Answer:**

`+=` adds a value to the existing variable and stores the updated result.

Example:

```python
a = 10

a += 5

print(a)
```

Output:

```python
15
```

---

## Q17. What is the difference between `a = a + 5` and `a += 5`?

**Answer:**

There is no difference in the result.

`a += 5` is simply a shorter and cleaner way of writing:

```python
a = a + 5
```

---

## Q18. What is the output of the following code?

```python
a = 10
b = 3

print(a % b)
```

**Answer:**

```python
1
```

Because the remainder after dividing 10 by 3 is 1.

---

## Q19. Why are comparison operators important?

**Answer:**

Comparison operators are mainly used in decision-making statements such as:

* if
* if-else
* elif
* while

They help Python decide whether a condition is `True` or `False`.

---

## Q20. Where are operators used in real-world Python applications?

**Answer:**

Operators are commonly used in:

* User Authentication
* Login Validation
* Age Verification
* Permission Checking
* Calculations
* Search Filtering
* Django Conditions
* API Validations
* Business Logic
