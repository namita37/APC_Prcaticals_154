"""
forms.py
========
Django forms with full Regex-based validation for:
  - User Registration
  - User Login
  - Profile Update
"""

import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile
from .validators import (
    validate_username,
    validate_email_regex,
    validate_password_strength,
    validate_phone,
    validate_full_name,
)


# ─────────────────────────────────────────────────────────────────────────────
# REGISTRATION FORM
# ─────────────────────────────────────────────────────────────────────────────
class RegistrationForm(forms.Form):
    """
    Registration form with regex validation on every field.
    Demonstrates how re module patterns are applied via validators.
    """

    full_name = forms.CharField(
        max_length=50,
        label='Full Name',
        validators=[validate_full_name],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. Alice Johnson',
            'autocomplete': 'off',
        }),
        help_text='Letters and spaces only, 2–50 characters.',
    )

    username = forms.CharField(
        max_length=20,
        label='Username',
        validators=[validate_username],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. alice_21',
            'autocomplete': 'off',
        }),
        help_text='Starts with a letter, 3–20 chars, letters/digits/underscore.',
    )

    email = forms.EmailField(
        label='Email Address',
        validators=[validate_email_regex],
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. alice@example.com',
        }),
        help_text='Must be a valid email: user@domain.com',
    )

    phone = forms.CharField(
        max_length=15,
        label='Phone Number',
        validators=[validate_phone],
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. 9876543210',
        }),
        help_text='10–13 digits, optional + prefix.',
    )

    gender = forms.ChoiceField(
        label='Gender',
        choices=[('', '-- Select --'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-input'}),
    )

    password = forms.CharField(
        label='Password',
        validators=[validate_password_strength],
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Min 8 chars, upper, lower, digit, special',
            'id': 'id_password',
        }),
        help_text='Min 8 chars • Uppercase • Lowercase • Digit • Special char (@$!%*?&#^())',
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Repeat your password',
        }),
    )

    # ── Cross-field validation ────────────────────────────────────────────────
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError('This username is already taken. Please choose another.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('An account with this email already exists.')
        return email

    def clean(self):
        cleaned = super().clean()
        pw  = cleaned.get('password')
        cpw = cleaned.get('confirm_password')
        if pw and cpw and pw != cpw:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned


# ─────────────────────────────────────────────────────────────────────────────
# LOGIN FORM
# ─────────────────────────────────────────────────────────────────────────────
class LoginForm(forms.Form):
    """
    Login form with regex-based field validation before hitting the database.
    """

    username = forms.CharField(
        max_length=20,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your username',
            'autocomplete': 'off',
            'autofocus': True,
        }),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your password',
        }),
    )

    # Regex validation at form level (before auth check)
    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        # Reject obviously invalid usernames immediately
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
            raise ValidationError(
                'Username must be 3–20 characters: letters, digits, or underscores only.'
            )
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters.')
        return password


# ─────────────────────────────────────────────────────────────────────────────
# PROFILE UPDATE FORM
# ─────────────────────────────────────────────────────────────────────────────
class ProfileUpdateForm(forms.ModelForm):
    """Form to update UserProfile fields."""

    class Meta:
        model  = UserProfile
        fields = ['full_name', 'phone', 'gender', 'bio']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone':     forms.TextInput(attrs={'class': 'form-input'}),
            'gender':    forms.Select(attrs={'class': 'form-input'}),
            'bio':       forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }
