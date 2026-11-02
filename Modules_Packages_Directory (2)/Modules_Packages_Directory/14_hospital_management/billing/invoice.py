# billing/invoice.py
from patient_management.patient import get_patient

_bills = {}
_bill_counter = [1]

def generate_bill(pid, consultation=0, medicine=0, tests=0):
    patient = get_patient(pid)
    total   = consultation + medicine + tests
    bill_id = f"BILL{_bill_counter[0]:03d}"
    _bill_counter[0] += 1
    _bills[bill_id] = {
        "patient": patient["name"] if patient else pid,
        "consultation": consultation,
        "medicine": medicine,
        "tests": tests,
        "total": total,
    }
    return bill_id

def display_bill(bill_id):
    b = _bills.get(bill_id)
    if not b:
        print("Bill not found.")
        return
    print(f"\n=== Bill {bill_id} for {b['patient']} ===")
    print(f"  Consultation : {b['consultation']}")
    print(f"  Medicine     : {b['medicine']}")
    print(f"  Tests        : {b['tests']}")
    print(f"  Total        : {b['total']}")
