def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(days, rate):
    return days * rate

def hospital_final_bill(consultation, laboratory, medicine, room, category):
    total = consultation + laboratory + medicine + room
    if category.lower() == "senior":
        total *= 0.90
    elif category.lower() == "child":
        total *= 0.95
    return total


print(hospital_final_bill(consultation_charges(500), laboratory_charges(1000), medicine_charges(750), room_charges(2, 1200), 'senior'))
