contacts = {"Amit": "9876543210", "Rahul": "9876501234"}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone number: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 6:
        break

    else:
        print("Invalid choice.")
