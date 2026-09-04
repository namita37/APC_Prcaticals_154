filename = input("Enter book records file name: ")

def read_books():
    books = []
    with open(filename, "r") as file:
        for line in file:
            book_id, title, author, status = line.strip().split(",")
            books.append([book_id, title, author, status])
    return books

def save_books(books):
    with open(filename, "w") as file:
        for book in books:
            file.write(",".join(book) + "\n")

def add_book():
    books = read_books()
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    books.append([book_id, title, author, "Available"])
    save_books(books)
    print("Book added.")

def search_book():
    key = input("Enter book ID or title: ").lower()
    for book in read_books():
        if book[0] == key or book[1].lower() == key:
            print(book)
            return
    print("Book not found.")

def issue_book():
    book_id = input("Enter book ID: ")
    books = read_books()
    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Issued"
                save_books(books)
                print("Book issued.")
            else:
                print("Book is already issued.")
            return
    print("Book not found.")

def return_book():
    book_id = input("Enter book ID: ")
    books = read_books()
    for book in books:
        if book[0] == book_id:
            book[3] = "Available"
            save_books(books)
            print("Book returned.")
            return
    print("Book not found.")

def display_available():
    for book in read_books():
        if book[3] == "Available":
            print(book)

while True:
    print("\n1. Add book\n2. Search book\n3. Issue book\n4. Return book\n5. Display available\n6. Exit")
    choice = input("Enter choice: ")

    if choice == "1": add_book()
    elif choice == "2": search_book()
    elif choice == "3": issue_book()
    elif choice == "4": return_book()
    elif choice == "5": display_available()
    elif choice == "6": break
    else: print("Invalid choice.")
