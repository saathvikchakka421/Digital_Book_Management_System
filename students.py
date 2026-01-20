from db import connect

def add_student():
    name = input("Student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    print("Student added successfully.")

def view_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No students found.")
        return

    print("\nID | Name")
    print("-" * 20)
    for r in rows:
        print(f"{r[0]} | {r[1]}")
