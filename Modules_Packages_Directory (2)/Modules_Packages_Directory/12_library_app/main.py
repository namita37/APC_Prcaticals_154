# main.py - Library Application
from books.catalog import add_book, list_books, search_book
from members.register import add_member, list_members
from transactions.issue import issue_book, return_book

# Sample data setup
add_book(1, "Python Programming", "Guido")
add_book(2, "Data Structures", "Mark Weiss")
add_member("M001", "Alice")
add_member("M002", "Bob")

print("=== Books ===")
list_books()

print("\n=== Members ===")
list_members()

print("\n=== Issue Book ===")
print(issue_book("M001", 1))
print(issue_book("M002", 1))

print("\n=== Return Book ===")
print(return_book("M001", 1))

print("\n=== Updated Books ===")
list_books()

print("\n=== Search ===")
search_book("Python")
