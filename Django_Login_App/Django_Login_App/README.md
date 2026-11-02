# Django Login & Regex Validation Application

This is a complete Django web application demonstrating user authentication (registration, login, logout, profile update) enhanced with strict **Regular Expression (Regex)** validations.

---

## 🚀 Features

1. **User Registration with Regex Validation**:
   - **Username**: Must start with a letter, 3–20 characters, alphanumeric and underscore (`^[a-zA-Z][a-zA-Z0-9_]{2,19}$`).
   - **Email**: Strict RFC-compliant regex validation (`^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$`).
   - **Password Strength**: Lookahead assertions checking for minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character (`(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#^()])`).
   - **Phone Number**: Optional 10–13 digits with optional `+` prefix (`^\+?[0-9]{10,13}$`).
   - **Full Name**: Only letters and spaces, 2–50 characters (`^[A-Za-z\s]{2,50}$`).

2. **Pre-Validation on Login Form**:
   - Rejects malformed usernames and passwords at the form level using regex before database lookup.

3. **User Dashboard & Profile**:
   - Displays authenticated user profile and documentation of regex rules.
   - Allows editing profile with continued regex enforcement.

4. **Interactive Regex Tester**:
   - Test custom patterns with `re.fullmatch`, `re.search`, and `re.findall`.
   - Includes preset patterns for usernames, emails, phone numbers, passwords, dates, and PIN codes.

---

## 🛠️ Setup & Running

### 1. Install Django
If Django is not already installed:
```powershell
pip install -r requirements.txt
# or directly:
pip install django
```

### 2. Apply Migrations
Navigate to the directory and run migrations:
```powershell
cd c:\Users\shiva\Desktop\APC\python\Django_Login_App
python manage.py makemigrations accounts
python manage.py migrate
```

### 3. Create Superuser (Optional)
To access the Django admin panel (`/admin`):
```powershell
python manage.py createsuperuser
```

### 4. Run the Development Server
```powershell
python manage.py runserver
```

Open your browser and visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📂 Project Directory Structure

```text
Django_Login_App/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── login_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── accounts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py         # UserProfile model
    ├── forms.py          # Registration, Login, Profile forms with regex
    ├── validators.py     # Regex validation logic using Python `re`
    ├── views.py          # Register, Login, Logout, Dashboard, Regex demo views
    ├── urls.py           # App routes
    └── templates/accounts/
        ├── base.html
        ├── login.html
        ├── register.html
        ├── dashboard.html
        ├── profile.html
        └── regex_demo.html
```
