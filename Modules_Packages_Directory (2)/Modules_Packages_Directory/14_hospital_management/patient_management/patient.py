# patient_management/patient.py
_patients = {}

def add_patient(pid, name, age, gender, ailment):
    _patients[pid] = {"name": name, "age": age, "gender": gender, "ailment": ailment}
    print(f"Patient '{name}' (ID:{pid}) admitted.")

def list_patients():
    print("\n=== Patients ===")
    for pid, p in _patients.items():
        print(f"  {pid} | {p['name']} | Age:{p['age']} | {p['gender']} | {p['ailment']}")

def search_patient(pid):
    return _patients.get(pid, None)

def get_patient(pid):
    return _patients.get(pid)
