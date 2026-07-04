# Encapsulation in Python

## Definition

Encapsulation is the process of wrapping data and methods into a single unit and restricting direct access to data.

In Python, encapsulation is achieved using public, protected, and private members.

---

## Access Types

### 1. Public Member

Syntax:

name

Accessible from anywhere.

---

### 2. Protected Member

Syntax:

_name

It is only a convention.

It means this member should be used inside the class and subclasses.

---

### 3. Private Member

Syntax:

__name

Python applies name mangling to private members.

Direct access is not allowed normally.

---

## Name Mangling

When we create a private variable like:

__salary

Python internally changes it to:

_Employee__salary

This is called Name Mangling.

---

## Getter and Setter

Getter:

Used to read private data.

Setter:

Used to update private data with validation.

Example:

get_salary()
set_salary()

---

# Interview Questions

## 1. What is Encapsulation?

Answer:

Encapsulation is the process of binding data and methods together and restricting direct access to the data.

---

## 2. Why do we use Encapsulation?

Answer:

- Data hiding
- Controlled access
- Better security
- Easy maintenance
- Validation before updating data

---

## 3. Does Python support private variables?

Answer:

Python does not support true private variables.

It uses name mangling with double underscore.

---

## 4. What is Name Mangling?

Answer:

Name mangling is a process where Python internally changes a private variable name.

Example:

__salary becomes _Employee__salary

---

## 5. What is the difference between Getter and Setter?

Answer:

Getter is used to read private data.

Setter is used to update private data with validation.

---

# Key Points

- Public: name
- Protected: _name
- Private: __name
- Getter returns data.
- Setter updates data.
- Encapsulation protects data from invalid direct changes.w