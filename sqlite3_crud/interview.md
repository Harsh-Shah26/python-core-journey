# SQLite CRUD Interview Notes

---

# 1. What is SQLite?

**Answer:**

SQLite is a lightweight, serverless, self-contained Relational Database Management System (RDBMS). It stores the entire database in a single `.db` file and does not require a separate database server.

---

# 2. Why SQLite?

- Lightweight
- No installation required
- Serverless
- Easy to learn
- Best for small applications
- Default database in Django

---

# 3. What is sqlite3?

`sqlite3` is Python's built-in module that allows Python programs to interact with SQLite databases.

```python
import sqlite3
```

---

# 4. How do you connect to a database?

```python
conn = sqlite3.connect("student.db")
```

### Explanation

- Creates a connection with the database.
- If `student.db` doesn't exist, SQLite creates it automatically.

---

# 5. What is Connection Object?

The Connection object represents the connection between Python and the database.

It is used for:

- commit()
- rollback()
- close()
- creating Cursor

---

# 6. What is Cursor?

```python
cursor = conn.cursor()
```

Cursor executes SQL queries and fetches data.

Think of Cursor as the bridge between Python and SQLite.

---

# 7. Connection vs Cursor

| Connection | Cursor |
|------------|--------|
| Connects Python to Database | Executes SQL Queries |
| Created using connect() | Created using cursor() |
| Used for commit() | Used for execute() |
| Used for close() | Used for fetch() |

---

# 8. What does execute() do?

```python
cursor.execute("SELECT * FROM students")
```

It sends SQL queries from Python to SQLite.

---

# 9. What is CREATE TABLE?

```sql
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
grade TEXT
);
```

Creates a new table.

---

# 10. Why IF NOT EXISTS?

```sql
CREATE TABLE IF NOT EXISTS students
```

Prevents an error if the table already exists.

---

# 11. Explain Table Columns

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
name TEXT NOT NULL
age INTEGER
grade TEXT
```

### id

Unique identifier.

### PRIMARY KEY

Uniquely identifies every row.

### AUTOINCREMENT

Automatically generates IDs.

Example:

```
1
2
3
4
```

### TEXT

Stores string values.

### INTEGER

Stores integer values.

### NOT NULL

Column cannot store NULL values.

---

# 12. INSERT

```python
cursor.execute("""
INSERT INTO students(name,age,grade)
VALUES(?,?,?)
""",(name,age,grade))
```

Adds new records.

---

# 13. Why use ? placeholders?

Because they

- Prevent SQL Injection
- Are safer
- Allow dynamic values

---

# 14. What is SQL Injection?

SQL Injection is a security attack where malicious SQL code is inserted through user input.

Wrong:

```python
cursor.execute(f"DELETE FROM students WHERE id={id}")
```

Correct:

```python
cursor.execute(
"DELETE FROM students WHERE id=?",
(id,)
)
```

---

# 15. Why `(student_id,)`?

SQLite expects parameters as tuples.

Correct

```python
(student_id,)
```

Wrong

```python
(student_id)
```

Without the comma it becomes an integer instead of a tuple.

---

# 16. commit()

```python
conn.commit()
```

Permanently saves database changes.

Required after

- INSERT
- UPDATE
- DELETE

Not required after

- SELECT

---

# 17. What happens without commit()?

Changes remain temporary.

After closing the connection, all changes are lost.

---

# 18. SELECT

```python
cursor.execute("SELECT * FROM students")
```

Retrieves records.

---

# 19. fetchone() vs fetchall()

## fetchone()

Returns only one row.

```python
row = cursor.fetchone()
```

Example

```
(1,'Harsh',21,'A')
```

---

## fetchall()

Returns all rows.

```python
rows = cursor.fetchall()
```

Example

```
(1,'Harsh',21,'A')
(2,'Mohit',22,'B')
```

---

# 20. UPDATE

```python
cursor.execute("""
UPDATE students
SET name=?,age=?,grade=?
WHERE id=?
""",(new_name,new_age,new_grade,student_id))
```

Updates existing records.

---

# 21. Why WHERE in UPDATE?

Correct

```sql
UPDATE students
SET grade='A'
WHERE id=1;
```

Wrong

```sql
UPDATE students
SET grade='A';
```

Without WHERE every row gets updated.

---

# 22. DELETE

```python
cursor.execute("""
DELETE FROM students
WHERE id=?
""",(student_id,))
```

Deletes records.

---

# 23. Why WHERE in DELETE?

Correct

```sql
DELETE FROM students
WHERE id=1;
```

Wrong

```sql
DELETE FROM students;
```

Without WHERE the entire table becomes empty.

---

# 24. What happens if ID doesn't exist?

SQLite throws no error.

It simply deletes **0 rows**.

---

# 25. close()

```python
conn.close()
```

Closes the database connection and releases resources.

---

# 26. CRUD

| Operation | SQL |
|------------|-----|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

---

# 27. Why no commit() after SELECT?

Because SELECT only reads data.

It does not modify the database.

---

# 28. Is SQLite good for production?

Suitable for:

- Learning
- Small applications
- Desktop software

Not ideal for:

- Large enterprise applications
- High concurrent users

Instead use

- MySQL
- PostgreSQL
- Oracle
- SQL Server

---

# 29. Why is SQLite Django's default database?

- Lightweight
- Easy setup
- No installation
- Single database file
- Perfect for beginners

---

# 30. Explain your CRUD Project

**Answer**

>I built a Student Management CRUD application using Python's built-in sqlite3 module. I created a students table with id, name, age and grade fields. I implemented Create, Read, Update and Delete operations using SQL queries. I used parameterized queries (?) to prevent SQL Injection, commit() to save changes permanently and close() to release database resources. This project helped me understand how Python interacts with relational databases before moving to Django ORM.

---

# 31. SQLite vs Django ORM

| SQL | Django ORM |
|------|------------|
| INSERT | Student.objects.create() |
| SELECT | Student.objects.all() |
| UPDATE | student.save() |
| DELETE | student.delete() |

---

# 32. Most Asked Interview Questions

- What is SQLite?
- What is sqlite3?
- What is Connection?
- What is Cursor?
- Difference between Connection and Cursor?
- What does execute() do?
- What is commit()?
- Why commit()?
- What is close()?
- What is PRIMARY KEY?
- What is AUTOINCREMENT?
- What is NOT NULL?
- What is SQL Injection?
- Why use ? placeholders?
- Difference between fetchone() and fetchall()?
- Why WHERE in UPDATE?
- Why WHERE in DELETE?
- Explain CRUD.
- Explain your Student CRUD project.
- Difference between SQLite and MySQL.
- How is SQLite related to Django ORM?

---

# Quick Revision

- `connect()` → Connect Database
- `cursor()` → Execute Queries
- `execute()` → Run SQL
- `commit()` → Save Changes
- `fetchone()` → One Record
- `fetchall()` → All Records
- `close()` → Close Connection

CRUD

- Create → INSERT
- Read → SELECT
- Update → UPDATE
- Delete → DELETE