# members/register.py
_members = {}

def add_member(member_id, name):
    _members[member_id] = {"name": name, "issued_books": []}
    print(f"Member '{name}' registered.")

def list_members():
    for mid, m in _members.items():
        print(f"  ID:{mid} | {m['name']} | Books: {m['issued_books']}")

def get_member(member_id):
    return _members.get(member_id)
