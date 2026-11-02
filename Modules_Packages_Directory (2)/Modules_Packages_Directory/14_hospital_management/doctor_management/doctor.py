# doctor_management/doctor.py
from patient_management.patient import get_patient

_doctors = {}

def add_doctor(did, name, specialty):
    _doctors[did] = {"name": name, "specialty": specialty}
    print(f"Doctor '{name}' (ID:{did}) added.")

def list_doctors():
    print("\n=== Doctors ===")
    for did, d in _doctors.items():
        print(f"  {did} | {d['name']} | {d['specialty']}")

def assign_doctor(pid, did):
    patient = get_patient(pid)
    doctor  = _doctors.get(did)
    if not patient: return f"Patient {pid} not found."
    if not doctor:  return f"Doctor {did} not found."
    patient["doctor"] = did
    return f"Dr. {doctor['name']} assigned to {patient['name']}."
