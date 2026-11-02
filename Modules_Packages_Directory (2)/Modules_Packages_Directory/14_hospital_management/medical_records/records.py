# medical_records/records.py
_records = {}

def add_record(pid, note):
    if pid not in _records: _records[pid] = []
    _records[pid].append(note)

def get_records(pid):
    return _records.get(pid, ["No records found."])
