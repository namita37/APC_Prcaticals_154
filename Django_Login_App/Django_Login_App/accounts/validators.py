"""
validators.py
=============
All Regular Expression based validators used across the accounts app.
Each function raises ValidationError if the value does not match the pattern.
"""

import re
from django.core.exceptions import ValidationError


# ── USERNAME ──────────────────────────────────────────────────────────────────
USERNAME_REGEX = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
# Rules: starts with a letter, then letters/digits/underscore, total 3-20 chars

def validate_username(value):
    """
    Username Rules (Regex: ^[a-zA-Z][a-zA-Z0-9_]{2,19}$):
      • Must start with a letter
      • Can contain letters, digits, or underscores
      • Length: 3 to 20 characters
    """
    if not re.match(USERNAME_REGEX, value):
        raise ValidationError(
            'Username must start with a letter, be 3–20 characters long, '
            'and contain only letters, digits, or underscores (_).'
        )


# ── EMAIL ─────────────────────────────────────────────────────────────────────
EMAIL_REGEX = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'

def validate_email_regex(value):
    """
    Email Rules (Regex: ^[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,}$):
      • Must have local part @ domain . TLD
      • Local part: letters, digits, dots, %, +, -, _
      • Domain must have valid TLD (2+ letters)
    """
    if not re.match(EMAIL_REGEX, value):
        raise ValidationError('Enter a valid email address (e.g. user@example.com).')


# ── PASSWORD ──────────────────────────────────────────────────────────────────
def validate_password_strength(value):
    """
    Password Rules:
      • At least 8 characters
      • At least one uppercase letter    → (?=.*[A-Z])
      • At least one lowercase letter    → (?=.*[a-z])
      • At least one digit               → (?=.*\\d)
      • At least one special character   → (?=.*[@$!%*?&#^()])
    """
    errors = []

    if len(value) < 8:
        errors.append('at least 8 characters')
    if not re.search(r'[A-Z]', value):
        errors.append('at least one uppercase letter (A-Z)')
    if not re.search(r'[a-z]', value):
        errors.append('at least one lowercase letter (a-z)')
    if not re.search(r'\d', value):
        errors.append('at least one digit (0-9)')
    if not re.search(r'[@$!%*?&#^()]', value):
        errors.append('at least one special character (@$!%*?&#^())')

    if errors:
        raise ValidationError('Password must contain: ' + ', '.join(errors) + '.')


# ── PHONE NUMBER ──────────────────────────────────────────────────────────────
PHONE_REGEX = r'^\+?[0-9]{10,13}$'

def validate_phone(value):
    """
    Phone Rules (Regex: ^\\+?[0-9]{10,13}$):
      • Optional leading +
      • 10 to 13 digits
    """
    if not re.match(PHONE_REGEX, value):
        raise ValidationError(
            'Phone number must be 10–13 digits (optional + prefix). E.g. 9876543210'
        )


# ── FULL NAME ─────────────────────────────────────────────────────────────────
NAME_REGEX = r'^[A-Za-z\s]{2,50}$'

def validate_full_name(value):
    """
    Full Name Rules (Regex: ^[A-Za-z\\s]{2,50}$):
      • Only letters and spaces
      • 2 to 50 characters
    """
    if not re.match(NAME_REGEX, value.strip()):
        raise ValidationError(
            'Full name must contain only letters and spaces (2–50 characters).'
        )
