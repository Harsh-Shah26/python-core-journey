# JSON in Python

## What is JSON?

JSON (JavaScript Object Notation) is a lightweight data-interchange format used to exchange data between applications, servers, and APIs.

It is language-independent and easy for humans to read and write.

---

# Why do we use JSON?

- Data exchange between Frontend and Backend.
- REST APIs.
- Store configuration files.
- Save and transfer structured data.
- Database import/export.

---

# Python Dictionary vs JSON

Python Dictionary

```python
student = {
    "name": "Harsh",
    "age": 21,
    "is_student": True
}
```

JSON

```json
{
    "name": "Harsh",
    "age": 21,
    "is_student": true
}
```

## Differences

| Python | JSON |
|---------|------|
| dict | String Format |
| True | true |
| False | false |
| None | null |
| Single quotes allowed | Double quotes only |

---

# JSON Functions

## 1. json.dumps()

### Purpose

Converts a Python object into a JSON string.

Example

```python
json.dumps(student)
```

Returns

```python
<class 'str'>
```

---

## 2. json.loads()

### Purpose

Converts a JSON string into a Python object.

Example

```python
json.loads(json_string)
```

Returns

```python
<class 'dict'>
```

---

## 3. json.dump()

### Purpose

Writes a Python object into a JSON file.

Example

```python
with open("student.json", "w") as file:
    json.dump(student, file)
```

---

## 4. json.load()

### Purpose

Reads a JSON file and converts it into a Python object.

Example

```python
with open("student.json", "r") as file:
    data = json.load(file)
```

Returns

```python
<class 'dict'>
```

---

# Pretty Print

Use

```python
indent=4
```

Example

```python
json.dump(student, file, indent=4)
```

This makes JSON readable.

---

# Complete Conversion Flow

Python Dictionary

↓

json.dumps()

↓

JSON String

↓

json.loads()

↓

Python Dictionary

-----------------------------

Python Dictionary

↓

json.dump()

↓

JSON File (.json)

↓

json.load()

↓

Python Dictionary

---

# Real Django Example

Frontend sends JSON:

```json
{
    "username": "harsh",
    "password": "1234"
}
```

In Django:

```python
import json

data = json.loads(request.body)
```

In Django REST Framework (DRF):

```python
request.data
```

DRF automatically converts JSON into a Python dictionary.

---

# Interview Questions

## 1. What is JSON?

Answer:

JSON (JavaScript Object Notation) is a lightweight data-interchange format used to exchange data between applications and APIs.

---

## 2. Why do we use JSON?

Answer:

- Data exchange
- APIs
- Configuration files
- Data storage
- Frontend-Backend communication

---

## 3. Difference between json.dump() and json.dumps()?

Answer:

json.dump()

- Writes Python object to a JSON file.

json.dumps()

- Converts Python object into a JSON string.

---

## 4. Difference between json.load() and json.loads()?

Answer:

json.load()

- Reads JSON data from a file.

json.loads()

- Converts a JSON string into a Python object.

---

## 5. Why does json.dumps() return <class 'str'>?

Answer:

Because JSON is a text format, not a Python data type. Therefore, json.dumps() returns a Python string containing JSON-formatted text.

---

## 6. Difference between Python Dictionary and JSON?

Answer:

Python Dictionary is a Python object.

JSON is a text format used to exchange data.

---

## 7. Why do we use indent=4?

Answer:

It formats JSON with proper indentation, making it easy to read.

---

## 8. What is request.data in Django REST Framework?

Answer:

request.data automatically converts incoming JSON into a Python dictionary, so there is no need to call json.loads() manually.

---

# Memory Trick ⭐

```
dumps = Python Object → JSON String

loads = JSON String → Python Object

dump = Python Object → JSON File

load = JSON File → Python Object
```

---

# Key Interview Points

- JSON is a text format.
- JSON is language-independent.
- dumps() returns a Python string.
- loads() returns a Python object.
- dump() writes to a file.
- load() reads from a file.
- JSON uses double quotes.
- Python uses True/False/None.
- JSON uses true/false/null.
- DRF automatically parses JSON using request.data.