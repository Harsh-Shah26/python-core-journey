# Date & Time in Python

## Module

```python
from datetime import datetime, timedelta
```

---

# Why do we use datetime?

The `datetime` module is used to work with dates, times, time differences, and formatting.

Common Uses:

- Current date & time
- Date formatting
- String to Date conversion
- Date calculations
- Future & Past dates

---

# datetime.now()

Returns the current local date and time.

Example:

```python
now = datetime.now()
```

Useful Attributes

```python
now.year
now.month
now.day

now.hour
now.minute
now.second

now.date()
now.time()
```

---

# strftime()

## Purpose

Converts a datetime object into a formatted string.

Example

```python
now.strftime("%d-%m-%Y")
```

---

# Common Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| %d | Day | 04 |
| %m | Month | 07 |
| %Y | Year | 2026 |
| %y | Year (2 digits) | 26 |
| %A | Full Weekday | Saturday |
| %a | Short Weekday | Sat |
| %B | Full Month | July |
| %b | Short Month | Jul |
| %H | 24-Hour | 14 |
| %I | 12-Hour | 02 |
| %M | Minute | 30 |
| %S | Second | 45 |
| %p | AM / PM | PM |

---

# strptime()

## Purpose

Converts a formatted string into a datetime object.

Example

```python
date = datetime.strptime("04-07-2026", "%d-%m-%Y")
```

---

# timedelta()

## Purpose

Used to add or subtract dates and times.

Examples

```python
today + timedelta(days=7)

today - timedelta(days=30)
```

Common Uses

- Next 7 days
- Last 30 days
- Yesterday
- Tomorrow

---

# Interview Questions

## 1. What is the datetime module?

Answer:

The datetime module is used to work with dates, times, formatting, and date calculations.

---

## 2. What does datetime.now() return?

Answer:

It returns the current local date and time.

---

## 3. Difference between strftime() and strptime()?

Answer:

strftime()

- Converts datetime → String

strptime()

- Converts String → datetime

---

## 4. What is timedelta()?

Answer:

timedelta is used to add or subtract days, weeks, hours, minutes, and seconds from a datetime object.

---

## 5. How do you get tomorrow's date?

Answer:

```python
datetime.now() + timedelta(days=1)
```

---

## 6. How do you get yesterday's date?

Answer:

```python
datetime.now() - timedelta(days=1)
```

---

## 7. How do you get the current year?

Answer:

```python
now.year
```

---

## 8. How do you format a date?

Answer:

Using `strftime()`.

Example:

```python
now.strftime("%d-%m-%Y")
```

---

# Memory Trick ⭐

```
datetime.now()

Current Date & Time

-------------------------

strftime()

DateTime
↓

Formatted String

-------------------------

strptime()

Formatted String
↓

DateTime

-------------------------

timedelta()

Date Calculation
```

---

# Key Interview Points

- `datetime.now()` → Current date & time.
- `strftime()` → datetime → String.
- `strptime()` → String → datetime.
- `timedelta()` → Date calculations.
- `%p` → AM/PM.
- `%A` → Full weekday.
- `%B` → Full month.
- `now.year`, `now.month`, `now.day` → Date components.
- `now.hour`, `now.minute`, `now.second` → Time components.