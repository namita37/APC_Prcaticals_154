import re


def validate_registration(name, age_text, phone, department, doctor, reason):
    name = name.strip()
    age_text = age_text.strip()
    phone = phone.strip()
    reason = reason.strip()
    if not name or not all(character.isalpha() or character == " " for character in name):
        return None, "Name can contain letters and spaces only."
    if not re.fullmatch(r"[0-9]+", age_text) or int(age_text) >= 120:
        return None, "Age must contain digits only and be less than 120."
    if not re.fullmatch(r"[0-9]{10}", phone):
        return None, "Phone number must contain exactly 10 digits (0-9) only."
    if not department or not doctor or not reason:
        return None, "Please complete all fields."
    return (name, int(age_text), phone, department, doctor, reason), None
