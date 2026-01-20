from db import connect

def add_book():
    title = input("Book title: ").strip()
    author = input("Author: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, status) VALUES (?, ?, 'Available')", (title, author))
    conn.commit()
    conn.close()

    print("Book added successfully.")

def view_books():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, status FROM books")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No books found.")
        return

    print("\nID | Title | Author | Status")
    print("-" * 40)
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
