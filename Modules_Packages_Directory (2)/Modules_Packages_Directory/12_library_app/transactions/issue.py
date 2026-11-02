# transactions/issue.py
from books.catalog import get_book
from members.register import get_member

def issue_book(member_id, book_id):
    member = get_member(member_id)
    book   = get_book(book_id)
    if not member: return "Member not found."
    if not book:   return "Book not found."
    if not book["available"]: return f"'{book['title']}' is not available."
    book["available"] = False
    member["issued_books"].append(book_id)
    return f"'{book['title']}' issued to {member['name']}."

def return_book(member_id, book_id):
    member = get_member(member_id)
    book   = get_book(book_id)
    if not member: return "Member not found."
    if not book:   return "Book not found."
    if book_id in member["issued_books"]:
        member["issued_books"].remove(book_id)
    book["available"] = True
    return f"'{book['title']}' returned by {member['name']}."
