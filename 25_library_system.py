books = {}

def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return "Book issued"
    return "Book not available"

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        return "Book returned"
    return "Book not found"

def search_book(title):
    return [book for book in books.values()
            if title.lower() in book["title"].lower()]

def display_available_books():
    return [book["title"] for book in books.values() if book["available"]]


add_book(1, 'Python Basics')
print(issue_book(1))
print(return_book(1))
print(display_available_books())
