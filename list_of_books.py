books = ["Python", "Java", "C", "HTML"]
books.append("SQL")
book = input("Enter book to search: ")
if book in books:
    print("Book found")
else:
    print("Book not found")
books.remove("C")
print("All books:", books)
print("Total books:", len(books))