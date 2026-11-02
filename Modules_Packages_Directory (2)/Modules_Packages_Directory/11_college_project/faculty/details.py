# faculty/details.py - Faculty details
def get_faculty_details(name, fid, department, designation):
    return {"name": name, "id": fid, "department": department, "designation": designation}

def display_faculty(faculty):
    print(f"  Name       : {faculty['name']}")
    print(f"  Faculty ID : {faculty['id']}")
    print(f"  Department : {faculty['department']}")
    print(f"  Designation: {faculty['designation']}")
