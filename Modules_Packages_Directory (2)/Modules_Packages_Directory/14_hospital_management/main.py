# main.py - Hospital Management System
from patient_management.patient import add_patient, list_patients, search_patient
from doctor_management.doctor import add_doctor, list_doctors, assign_doctor
from billing.invoice import generate_bill, display_bill
from medical_records.records import add_record, get_records

# Patients
add_patient("P001", "Alice", 30, "Female", "Fever")
add_patient("P002", "Bob",   45, "Male",   "Fracture")
list_patients()

# Doctors
add_doctor("D001", "Dr. Sharma", "General Medicine")
add_doctor("D002", "Dr. Patel",  "Orthopedics")
list_doctors()

# Assign
print(assign_doctor("P001", "D001"))
print(assign_doctor("P002", "D002"))

# Medical Records
add_record("P001", "Prescribed Paracetamol 500mg twice daily.")
add_record("P002", "X-ray done. Plaster applied.")
print(get_records("P001"))

# Billing
bill_id = generate_bill("P001", consultation=500, medicine=300, tests=200)
display_bill(bill_id)
