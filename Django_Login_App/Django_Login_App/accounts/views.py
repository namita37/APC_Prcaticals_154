"""
views.py
========
Handles:
  - register_view  : User registration with regex-validated form
  - login_view     : Login with regex pre-validation + Django auth
  - logout_view    : Session logout
  - dashboard_view : Protected home page (login required)
  - profile_view   : View & update user profile
  - regex_demo_view: Interactive regex tester page
"""

import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistrationForm, LoginForm, ProfileUpdateForm
from .models import UserProfile
from .validators import (
    USERNAME_REGEX, EMAIL_REGEX, PHONE_REGEX, NAME_REGEX,
)


# ─────────────────────────────────────────────────────────────────────────────
# REGISTER
# ─────────────────────────────────────────────────────────────────────────────
def register_view(request):
    """Register a new user with full regex validation."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Create Django User
            user = User.objects.create_user(
                username  = data['username'],
                email     = data['email'],
                password  = data['password'],
                first_name= data['full_name'].split()[0],
                last_name = ' '.join(data['full_name'].split()[1:]),
            )
            # Create profile
            UserProfile.objects.create(
                user      = user,
                full_name = data['full_name'],
                phone     = data.get('phone', ''),
                gender    = data.get('gender', ''),
            )
            messages.success(request, f"Account created for {data['username']}! Please log in.")
            return redirect('login')
        else:
            messages.error(request, 'Please fix the errors below.')

    return render(request, 'accounts/register.html', {'form': form})


# ─────────────────────────────────────────────────────────────────────────────
# LOGIN
# ─────────────────────────────────────────────────────────────────────────────
def login_view(request):
    """Login view with regex pre-validation before authenticating."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Django authentication (checks hashed password in DB)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'accounts/login.html', {'form': form})


# ─────────────────────────────────────────────────────────────────────────────
# LOGOUT
# ─────────────────────────────────────────────────────────────────────────────
def logout_view(request):
    """Log out the current user."""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


# ─────────────────────────────────────────────────────────────────────────────
# DASHBOARD  (login required)
# ─────────────────────────────────────────────────────────────────────────────
@login_required
def dashboard_view(request):
    """Protected dashboard — shows user info and regex patterns used."""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = None

    regex_patterns = [
        {
            'name'   : 'Username',
            'pattern': USERNAME_REGEX,
            'rules'  : 'Starts with letter • Letters/digits/underscore • 3–20 chars',
            'valid'  : 'alice_21, John99',
            'invalid': '1abc, hi, user name!',
        },
        {
            'name'   : 'Email',
            'pattern': EMAIL_REGEX,
            'rules'  : 'local@domain.tld format • Valid characters only',
            'valid'  : 'user@example.com, test.user+tag@mail.org',
            'invalid': 'user@@mail, no-at-sign',
        },
        {
            'name'   : 'Password',
            'pattern': r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#^()])',
            'rules'  : '8+ chars • Uppercase • Lowercase • Digit • Special char',
            'valid'  : 'Pass@1234, Hello#99',
            'invalid': 'password, 12345678, PASSWORD1',
        },
        {
            'name'   : 'Phone',
            'pattern': PHONE_REGEX,
            'rules'  : 'Optional + prefix • 10–13 digits only',
            'valid'  : '9876543210, +919876543210',
            'invalid': '12345, abc1234567, 98765 43210',
        },
        {
            'name'   : 'Full Name',
            'pattern': NAME_REGEX,
            'rules'  : 'Letters and spaces only • 2–50 characters',
            'valid'  : 'Alice Johnson, Raj Kumar',
            'invalid': 'Alice123, A, A!@# Name',
        },
    ]

    context = {
        'user'           : request.user,
        'profile'        : profile,
        'regex_patterns' : regex_patterns,
    }
    return render(request, 'accounts/dashboard.html', context)


# ─────────────────────────────────────────────────────────────────────────────
# PROFILE  (login required)
# ─────────────────────────────────────────────────────────────────────────────
@login_required
def profile_view(request):
    """View and update the current user's profile."""
    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'full_name': request.user.get_full_name() or request.user.username}
    )
    form = ProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix the errors below.')

    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})


# ─────────────────────────────────────────────────────────────────────────────
# REGEX DEMO  (login required)
# ─────────────────────────────────────────────────────────────────────────────
@login_required
def regex_demo_view(request):
    """
    Interactive regex tester.
    The user can type a pattern and test string to see if they match.
    """
    result = None
    pattern_input = ''
    test_input    = ''
    matches       = []
    error_msg     = ''

    if request.method == 'POST':
        pattern_input = request.POST.get('pattern', '').strip()
        test_input    = request.POST.get('test_string', '').strip()
        if pattern_input and test_input:
            try:
                compiled = re.compile(pattern_input)
                full_match = bool(compiled.fullmatch(test_input))
                search_match = compiled.search(test_input)
                matches = compiled.findall(test_input)
                result = {
                    'full_match'  : full_match,
                    'search_match': bool(search_match),
                    'matches'     : matches,
                    'groups'      : search_match.groups() if search_match else [],
                }
            except re.error as e:
                error_msg = f'Invalid regex pattern: {e}'

    preset_patterns = [
        ('Username',      USERNAME_REGEX,         'alice_21'),
        ('Email',         EMAIL_REGEX,             'user@example.com'),
        ('Password',      r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?]).{8,}', 'Hello@123'),
        ('Phone (India)', r'^\+?91?[6-9]\d{9}$',  '+919876543210'),
        ('Full Name',     NAME_REGEX,              'Alice Johnson'),
        ('Date (DD/MM/YYYY)', r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$', '27/10/2026'),
        ('PIN Code',      r'^\d{6}$',              '400001'),
    ]

    context = {
        'result'         : result,
        'pattern_input'  : pattern_input,
        'test_input'     : test_input,
        'error_msg'      : error_msg,
        'preset_patterns': preset_patterns,
    }
    return render(request, 'accounts/regex_demo.html', context)
