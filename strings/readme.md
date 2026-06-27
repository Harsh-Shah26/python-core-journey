# 01 - Python Strings

## What is a String?

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

Example:

```python
name = "Harsh"
```

## Are Strings Mutable?

No. Strings are immutable in Python.

This means we cannot change a character directly after creating a string.

Example:

```python
name = "Harsh"
name[0] = "M"
```

This gives an error because strings do not support item assignment.

Correct way:

```python
name = "Marsh"
```

Here, Python creates a new string instead of changing the old one.

## Indexing

Indexing is used to access individual characters from a string.

```python
name = "Harsh Shah"
print(name[1])
```

Output:

```python
a
```

## Negative Indexing

Negative indexing starts from the end.

```python
name = "Harsh Shah"
print(name[-1])
```

Output:

```python
h
```

`-1` means last character, `-2` means second last character, and `-3` means third last character.

## Slicing

Slicing is used to extract part of a string.

```python
name = "Harsh Shah"
print(name[:3])
```

Output:

```python
Har
```

End index is excluded.

## Important String Methods

### upper()

Converts all characters to uppercase.

```python
fruit.upper()
```

### lower()

Converts all characters to lowercase.

```python
fruit.lower()
```

### title()

Converts the first character of every word to uppercase.

```python
fruit.title()
```

### capitalize()

Converts only the first character of the string to uppercase.

```python
fruit.capitalize()
```

### strip()

Removes spaces from the beginning and end.

```python
text.strip()
```

### replace()

Replaces one substring with another.

```python
fruit.replace("banana", "oranges")
```

### find()

Returns the index of the first occurrence. If not found, it returns `-1`.

```python
fruit.find("b")
```

### index()

Returns the index of the first occurrence. If not found, it raises an error.

```python
fruit.index("b")
```

### count()

Counts how many times a character or substring appears.

```python
fruit.count("a")
```

### startswith()

Checks if a string starts with a specific value.

```python
fruit.startswith("i")
```

### endswith()

Checks if a string ends with a specific value.

```python
fruit.endswith("banana")
```

### split()

Breaks a string into multiple parts.

```python
date = "26-01-2005"
print(date.split("-"))
```

Output:

```python
['26', '01', '2005']
```

### join()

Joins characters or strings using a separator.

```python
print("=".join("Harsh"))
```

Output:

```python
H=a=r=s=h
```

## f-Strings

f-strings are used to insert variables directly inside a string.

```python
name = "Harsh"
print(f"My name is {name}")
```

Output:

```python
My name is Harsh
```

# Interview Questions and Answers

## Q1. What is a string in Python?

A string is a sequence of characters enclosed in single, double, or triple quotes.

## Q2. Are strings mutable in Python?

No. Strings are immutable, meaning their content cannot be changed after creation.

## Q3. What happens when we modify a string?

Python creates a new string instead of changing the existing one.

## Q4. What is indexing?

Indexing is the process of accessing a character from a string using its position.

## Q5. What is negative indexing?

Negative indexing allows us to access characters from the end of the string. `-1` represents the last character.

## Q6. What is slicing?

Slicing is used to extract a portion of a string using the syntax `string[start:end]`.

## Q7. Is the end index included in slicing?

No. The end index is excluded.

## Q8. What is the difference between `find()` and `index()`?

`find()` returns `-1` if the substring is not found, while `index()` raises a `ValueError`.

## Q9. What does `strip()` do?

`strip()` removes leading and trailing spaces from a string.

## Q10. What is the use of `split()`?

`split()` breaks a string into multiple parts based on a separator.

## Q11. What is the use of `join()`?

`join()` joins characters or strings using a separator.

## Q12. What is an f-string?

An f-string is a formatted string literal used to insert variables and expressions directly inside a string.

## Q13. Why are string methods important in backend development?

String methods are used for input cleaning, validation, email handling, URL processing, file handling, and API data formatting.
