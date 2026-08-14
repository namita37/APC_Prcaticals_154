patients = ["Rahul", "Amit", "Pratik", "Sneha"]
patients.append("Neha")
patients.remove("Amit")
name = input("Enter patient name: ")
if name in patients:
    print("Patient found")
else:
    print("Patient not found")
print("All patients:")
for patient in patients:
    print(patient)
print("Total patients:", len(patients))