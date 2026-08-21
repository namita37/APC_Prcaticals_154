books = {101: "Python Basics", 102: "Java Programming", 103: "Web Development"}

while True:
    print("\n1. Add book")
    print("2. Search book")
    print("3. Remove book")
    print("4. Display all books")
    print("5. Count total books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        book_name = input("Enter book name: ")
        books[book_id] = book_name
        print("Book added.")

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print("Book:", books[book_id])
        else:
            print("Book not found.")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == 4:
        for book_id, book_name in books.items():
            print(book_id, ":", book_name)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice.")
