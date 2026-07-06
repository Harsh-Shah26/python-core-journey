import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Table Creation

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")


def add_student(name, age, grade):
    cursor.execute("""
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
    """, (name, age, grade))


# add_student("mohit kumar", 20, "A")
# add_student("Anjali kumari", 22, "B")
# conn.commit()  #comment it after cretae so u can update

def fetch_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def update_student(student_id, new_name, new_age, new_grade):
    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, grade = ?
    WHERE id = ?
    """, (new_name, new_age, new_grade, student_id))



# UPDATE
# update_student(1, "mohit singh", 21, "B+")
# conn.commit()
# print("Student updated successfully")

# READ after update
# fetch_all_students()


# DELETE
def delete_student(student_id):
    cursor.execute("""
    DELETE FROM students
    WHERE id = ?
    """, (student_id,))


delete_student(2)
conn.commit()

print("Student deleted successfully")
fetch_all_students()

conn.close()