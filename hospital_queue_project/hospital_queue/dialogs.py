"""Tkinter registration and login dialogs."""
import tkinter as tk
from tkinter import messagebox, ttk
from .config import DEPARTMENTS, RECEPTIONIST_USERNAME, RECEPTIONIST_PASSWORD
from .database import check_patient_login
from .validation import validate_registration


class PatientDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Register patient")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.result = None
        body = ttk.Frame(self, padding=22)
        body.pack(fill="both", expand=True)
        ttk.Label(body, text="Patient registration", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))
        self.fields = {}
        for row, (label, key) in enumerate((("Name", "name"), ("Age", "age"), ("Phone number", "phone")), start=1):
            ttk.Label(body, text=label).grid(row=row, column=0, sticky="w", padx=(0, 14), pady=6)
            entry = ttk.Entry(body, width=36)
            entry.grid(row=row, column=1, sticky="ew", pady=6)
            self.fields[key] = entry
        ttk.Label(body, text="Department").grid(row=4, column=0, sticky="w", padx=(0, 14), pady=6)
        self.department = ttk.Combobox(body, values=list(DEPARTMENTS), state="readonly", width=33)
        self.department.grid(row=4, column=1, sticky="ew", pady=6)
        self.department.set(list(DEPARTMENTS)[0])
        self.department.bind("<<ComboboxSelected>>", self.update_doctors)
        ttk.Label(body, text="Doctor").grid(row=5, column=0, sticky="w", padx=(0, 14), pady=6)
        self.doctor = ttk.Combobox(body, state="readonly", width=33)
        self.doctor.grid(row=5, column=1, sticky="ew", pady=6)
        self.update_doctors()
        ttk.Label(body, text="Reason for visit").grid(row=6, column=0, sticky="w", padx=(0, 14), pady=6)
        self.fields["reason"] = ttk.Entry(body, width=36)
        self.fields["reason"].grid(row=6, column=1, sticky="ew", pady=6)
        buttons = ttk.Frame(body)
        buttons.grid(row=7, column=0, columnspan=2, sticky="e", pady=(16, 0))
        ttk.Button(buttons, text="Cancel", command=self.destroy).pack(side="right")
        ttk.Button(buttons, text="Register", command=self.submit).pack(side="right", padx=8)
        body.columnconfigure(1, weight=1)
        self.fields["name"].focus_set()

    def update_doctors(self, _event=None):
        doctors = DEPARTMENTS.get(self.department.get(), [])
        self.doctor["values"] = doctors
        self.doctor.set(doctors[0] if doctors else "")

    def submit(self):
        values, error = validate_registration(
            self.fields["name"].get(), self.fields["age"].get(), self.fields["phone"].get(),
            self.department.get(), self.doctor.get(), self.fields["reason"].get(),
        )
        if error:
            messagebox.showerror("Invalid registration", error, parent=self)
            return
        self.result = values
        self.destroy()


class LoginDialog(tk.Toplevel):
    def __init__(self, app, allow_patient=True, cancel_destroys_app=True):
        super().__init__(app)
        self.app = app
        self.allow_patient = allow_patient
        self.cancel_destroys_app = cancel_destroys_app
        self.title("Hospital Queue Login")
        self.resizable(False, False)
        self.transient(app)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.grab_set()
        self.lift()
        self.focus_force()
        body = ttk.Frame(self, padding=26)
        body.pack(fill="both", expand=True)
        ttk.Label(body, text="Receptionist sign-in", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))
        ttk.Label(body, text="Username").grid(row=1, column=0, sticky="w", pady=6, padx=(0, 14))
        self.username = ttk.Entry(body, width=34)
        self.username.grid(row=1, column=1, pady=6)
        ttk.Label(body, text="Password").grid(row=2, column=0, sticky="w", pady=6, padx=(0, 14))
        self.password = ttk.Entry(body, width=34, show="•")
        self.password.grid(row=2, column=1, pady=6)
        ttk.Label(body, text="Demo: receptionist / admin123").grid(row=3, column=0, columnspan=2, sticky="w", pady=8)
        buttons = ttk.Frame(body)
        buttons.grid(row=4, column=0, columnspan=2, sticky="e", pady=(10, 0))
        if allow_patient:
            ttk.Button(buttons, text="Continue as Patient", command=self.continue_patient).pack(side="left", padx=(0, 8))
        ttk.Button(buttons, text="Sign in", command=self.login).pack(side="left")
        self.bind("<Return>", lambda _event: self.login())
        self.username.focus_set()

    def login(self):
        if self.username.get().strip() != RECEPTIONIST_USERNAME or self.password.get().strip() != RECEPTIONIST_PASSWORD:
            messagebox.showerror("Sign-in failed", "Incorrect receptionist username or password.", parent=self)
            return
        self.app.receptionist_authenticated = True
        self.app.open_for_role("Receptionist")
        self.destroy()

    def continue_patient(self):
        self.app.open_for_role("Patient")
        self.destroy()

    def cancel(self):
        if self.cancel_destroys_app:
            self.app.destroy()
        else:
            self.destroy()
