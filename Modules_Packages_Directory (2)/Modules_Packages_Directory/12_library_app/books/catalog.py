# books/catalog.py
_books = {}

def add_book(book_id, title, author):
    _books[book_id] = {"title": title, "author": author, "available": True}
    print(f"Book '{title}' added.")

def list_books():
    for bid, b in _books.items():
        status = "Available" if b["available"] else "Issued"
        print(f"  ID:{bid} | {b['title']} by {b['author']} | {status}")

def search_book(keyword):
    results = [(bid, b) for bid, b in _books.items() if keyword.lower() in b["title"].lower()]
    if results:
        for bid, b in results:
            print(f"  Found - ID:{bid} | {b['title']} by {b['author']}")
    else:
        print(f"No book found with keyword '{keyword}'.")

def get_book(book_id):
    return _books.get(book_id)
