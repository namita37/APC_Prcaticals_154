available_books = {"Python Basics", "Java Programming", "DBMS", "Web Development"}
requested_books = {"Python Basics", "DBMS", "C Programming", "Web Development"}

available_requested = requested_books & available_books

print("Requested books available:", available_requested)
