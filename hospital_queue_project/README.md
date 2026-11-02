# Hospital Queue Management (Modular Python GUI)

## Requirements
- Python 3.10 or later
- Tkinter (included with standard Windows Python installer)

## Install packages
Open Command Prompt in this folder and run:

```bat
py -m pip install -r requirements.txt
```

## Start the application

```bat
py main.py
```

The app creates `hospital_queue.db` automatically beside `main.py` the first time it runs. Patient records are stored locally in that database. The database is intentionally not included in the source ZIP.

## Demo login
- Receptionist username: `receptionist`
- Receptionist password: `admin123`
- Patients can choose **Continue as Patient** and do not need a login.
- Receptionist access remains active until **Log out** is selected. From a patient session choose **Open Receptionist**; sign in once, then switching screens does not ask for the password again.

## Modules
- `hospital_queue/app.py` — main Tkinter application and workflows
- `hospital_queue/database.py` — SQLite setup, patient records, queue operations, pandas dataframes
- `hospital_queue/dialogs.py` — registration and login dialogs
- `hospital_queue/charts.py` — matplotlib department and doctor charts
- `hospital_queue/config.py` — doctor list, departments, wait estimates, demo credentials
- `hospital_queue/validation.py` — registration input validation
- `main.py` — app launcher

## Features
Patient registration, department and doctor dropdowns, receptionist queue management, patient status and approximate wait, CSV/Excel export, and department/doctor charts.

Registration validation: name letters and spaces only; age digits only and less than 120; phone exactly 10 digits (0–9).

This is a learning project. The sample receptionist password is hard-coded and is not appropriate for a real hospital system.
