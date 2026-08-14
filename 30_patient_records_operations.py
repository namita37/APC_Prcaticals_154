patients = (
    (101, "Amit", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Rahul", 40, "O+"),
    (104, "Pooja", 28, "A+")
)


print("All Patient Records:")
for patient in patients:
    print("ID:", patient[0], "Name:", patient[1], "Age:", patient[2], "Blood Group:", patient[3])


patient_id = int(input("\nEnter patient ID to search: "))
found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:")
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found.")


print("Total patients:", len(patients))


blood_group = input("Enter blood group to search: ")

print("Patients with blood group", blood_group + ":")
for patient in patients:
    if patient[3].upper() == blood_group.upper():
        print(patient)
