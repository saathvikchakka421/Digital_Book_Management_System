from db import connect

def issue_book():
    try:
        book_id = int(input("Book ID: "))
        student_id = int(input("Student ID: "))
    except:
        print("Invalid input.")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT status FROM books WHERE id=?", (book_id,))
    book = cur.fetchone()

    if not book:
        print("Book not found.")
        conn.close()
        return

    if book[0] != "Available":
        print("Book not available.")
        conn.close()
        return

    cur.execute("UPDATE books SET status='Issued' WHERE id=?", (book_id,))
    cur.execute("INSERT INTO transactions (book_id, student_id, action) VALUES (?, ?, 'Issued')", (book_id, student_id))

    conn.commit()
    conn.close()

    print("Book issued successfully.")

def return_book():
    try:
        book_id = int(input("Book ID: "))
    except:
        print("Invalid input.")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute("UPDATE books SET status='Available' WHERE id=?", (book_id,))
    cur.execute("INSERT INTO transactions (book_id, student_id, action) VALUES (?, 0, 'Returned')", (book_id,))

    conn.commit()
    conn.close()

    print("Book returned successfully.")
