from db import setup
from books import add_book, view_books
from students import add_student, view_students
from transactions import issue_book, return_book

def menu():
    while True:
        print("\n--- Digital Book Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Student")
        print("4. View Students")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

setup()
menu()
