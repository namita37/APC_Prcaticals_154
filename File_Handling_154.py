# Program 1: Create student.txt and Write Student Information

with open("student.txt", "w") as file:
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")
    semester = input("Enter semester: ")
    file.write("Name: " + name + "\n")
    file.write("Roll Number: " + roll + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")
print("Student information written successfully.")


print("\n" + "=" * 70 + "\n")

# Program 2: Display Complete Contents of a Text File

filename = input("Enter file name: ")
with open(filename, "r") as file:
    print(file.read())


print("\n" + "=" * 70 + "\n")

# Program 3: Append Student Information to an Existing File

with open("student.txt", "a") as file:
    information = input("Enter additional student information: ")
    file.write(information + "\n")
print("Information appended successfully.")


print("\n" + "=" * 70 + "\n")

# Program 4: Read a Text File Line by Line

filename = input("Enter file name: ")
with open(filename, "r") as file:
    for line in file:
        print(line, end="")


print("\n" + "=" * 70 + "\n")

# Program 5: Count Total Number of Lines in a Text File

filename = input("Enter file name: ")
with open(filename, "r") as file:
    lines = file.readlines()
print("Total number of lines =", len(lines))


print("\n" + "=" * 70 + "\n")

# Program 6: Count Total Number of Words in a Text File

filename = input("Enter file name: ")
with open(filename, "r") as file:
    words = file.read().split()
print("Total number of words =", len(words))


print("\n" + "=" * 70 + "\n")

# Program 7: Count Total Number of Characters Including Spaces

filename = input("Enter file name: ")
with open(filename, "r") as file:
    content = file.read()
print("Total number of characters =", len(content))


print("\n" + "=" * 70 + "\n")

# Program 8: Display File Lines in Reverse Order

filename = input("Enter file name: ")
with open(filename, "r") as file:
    lines = file.readlines()
for line in reversed(lines):
    print(line, end="")


print("\n" + "=" * 70 + "\n")

# Program 9: Count Vowels and Consonants in a Text File

filename = input("Enter file name: ")
with open(filename, "r") as file:
    content = file.read()
vowels = consonants = 0
for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)


print("\n" + "=" * 70 + "\n")

# Program 10: Count Alphabets Digits Spaces and Special Characters

filename = input("Enter file name: ")
with open(filename, "r") as file:
    content = file.read()
alphabets = digits = spaces = special = 0
for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Alphabets =", alphabets)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)


print("\n" + "=" * 70 + "\n")

# Program 11: Find the Longest Word in a Text File

filename = input("Enter file name: ")
with open(filename, "r") as file:
    words = file.read().split()
if words:
    print("Longest word =", max(words, key=len))
else:
    print("File is empty.")


print("\n" + "=" * 70 + "\n")

# Program 12: Count Occurrence of Each Word Using Dictionary

filename = input("Enter file name: ")
with open(filename, "r") as file:
    words = file.read().lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)


print("\n" + "=" * 70 + "\n")

# Program 13: Search a Word and Display Occurrences and Line Numbers

filename = input("Enter file name: ")
search_word = input("Enter word to search: ").lower()
count = 0
line_numbers = []
with open(filename, "r") as file:
    for number, line in enumerate(file, start=1):
        occurrences = line.lower().split().count(search_word)
        if occurrences:
            count += occurrences
            line_numbers.append(number)
print("Number of occurrences =", count)
print("Line numbers =", line_numbers)


print("\n" + "=" * 70 + "\n")

# Program 14: Replace a Word in a Text File

filename = input("Enter file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
with open(filename, "r") as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open(filename, "w") as file:
    file.write(content)
print("Word replaced successfully.")


print("\n" + "=" * 70 + "\n")

# Program 15: Remove Single-Line Comments from a Python Source File

source_file = input("Enter Python source file name: ")
output_file = input("Enter output file name: ")
with open(source_file, "r") as file:
    lines = file.readlines()
with open(output_file, "w") as file:
    for line in lines:
        if not line.lstrip().startswith("#"):
            file.write(line)
print("Output file created successfully.")


print("\n" + "=" * 70 + "\n")

# Program 16: Create Another File with Text in Uppercase

source_file = input("Enter source file name: ")
output_file = input("Enter output file name: ")
with open(source_file, "r") as file:
    content = file.read()
with open(output_file, "w") as file:
    file.write(content.upper())
print("Uppercase file created successfully.")


print("\n" + "=" * 70 + "\n")

# Program 17: Process Student Records from a File

with open("students.csv", "w") as file:
    file.write("RollNo,Name,Marks\n101,Amit,85\n102,Priya,92\n103,Rahul,78\n")
students = []
with open("students.csv", "r") as file:
    next(file)
    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))
print("All Records:")
for s in students:
    print(s)
print("Highest Marks:", max(students, key=lambda x: x[2]))
print("Average Marks =", sum(s[2] for s in students) / len(students))
print("Students Scoring More Than 80:")
for s in students:
    if s[2] > 80:
        print(s)


print("\n" + "=" * 70 + "\n")

# Program 18: Process Employee Records from a File

def display_employees(data):
    for e in data:
        print(e)
def highest_paid(data):
    return max(data, key=lambda x: x[3])
def average_salary(data):
    return sum(e[3] for e in data) / len(data)
def above_salary(data, amount):
    return [e for e in data if e[3] > amount]

with open("employees.txt", "w") as file:
    file.write("101,Amit,IT,45000\n102,Priya,HR,60000\n103,Rahul,Finance,55000\n")
employees = []
with open("employees.txt", "r") as file:
    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        employees.append((emp_id, name, dept, float(salary)))
display_employees(employees)
print("Highest Paid Employee:", highest_paid(employees))
print("Average Salary =", average_salary(employees))
amount = float(input("Enter salary limit: "))
display_employees(above_salary(employees, amount))


print("\n" + "=" * 70 + "\n")

# Program 19: Calculate Student Attendance Percentage

with open("attendance.txt", "w") as file:
    file.write("101,Amit,80,100\n102,Priya,70,100\n103,Rahul,60,90\n")
with open("attendance.txt", "r") as file:
    for line in file:
        roll, name, attended, total = line.strip().split(",")
        percentage = int(attended) / int(total) * 100
        print(name, "Attendance =", round(percentage, 2), "%")
        if percentage < 75:
            print(name, "has attendance below 75%")


print("\n" + "=" * 70 + "\n")

# Program 20: Process Deposit and Withdrawal Transactions

with open("transactions.txt", "w") as file:
    file.write("Deposit,5000\nWithdrawal,1500\nDeposit,3000\nWithdrawal,1000\n")
deposits = withdrawals = largest = 0
with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")
        amount = float(amount)
        if transaction == "Deposit":
            deposits += amount
        else:
            withdrawals += amount
        largest = max(largest, amount)
print("Total Deposits =", deposits)
print("Total Withdrawals =", withdrawals)
print("Final Balance =", deposits - withdrawals)
print("Largest Transaction =", largest)


print("\n" + "=" * 70 + "\n")

# Program 21: Library Book Record Management

books = {}
def save_books():
    with open("books.txt", "w") as file:
        for bid, d in books.items():
            file.write(f"{bid},{d['title']},{d['author']},{d['available']}\n")
def add_book(bid, title, author):
    books[bid] = {"title": title, "author": author, "available": True}
    save_books()
def search_book(bid):
    print(books.get(bid, "Book not found."))
def issue_book(bid):
    if bid in books and books[bid]["available"]:
        books[bid]["available"] = False
        save_books()
        print("Book issued.")
    else:
        print("Book not available.")
def return_book(bid):
    if bid in books:
        books[bid]["available"] = True
        save_books()
        print("Book returned.")
def display_available_books():
    for bid, d in books.items():
        if d["available"]:
            print(bid, d["title"], d["author"])

add_book("B101", "Python Programming", "Amit")
add_book("B102", "Data Structures", "Priya")
search_book("B101")
issue_book("B101")
display_available_books()
return_book("B101")


print("\n" + "=" * 70 + "\n")

# Program 22: Merge Contents of Two Text Files

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
file3 = input("Enter output file name: ")
with open(file1, "r") as f1:
    content1 = f1.read()
with open(file2, "r") as f2:
    content2 = f2.read()
with open(file3, "w") as f3:
    f3.write(content1 + "\n" + content2)
print("Files merged successfully.")


print("\n" + "=" * 70 + "\n")

# Program 23: Compare Two Text Files

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
with open(file1, "r") as f1:
    lines1 = f1.readlines()
with open(file2, "r") as f2:
    lines2 = f2.readlines()
if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")
    for i in range(max(len(lines1), len(lines2))):
        a = lines1[i] if i < len(lines1) else ""
        b = lines2[i] if i < len(lines2) else ""
        if a != b:
            print("First difference found at line", i + 1)
            break
