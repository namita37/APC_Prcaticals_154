"""Main Tkinter window and receptionist/patient workflows."""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from .config import AVERAGE_MINUTES
from .database import (call_next, complete_patient, dataframe_for_charts,
                       dataframe_for_export, get_patient_status, get_patients,
                       register_patient)
from .dialogs import LoginDialog, PatientDialog
from .charts import show_patient_charts


class HospitalQueueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Queue Management")
        self.geometry("1060x680")
        self.minsize(820, 540)
        self.configure(bg="#f3f6fb")
        self.receptionist_authenticated = False
        self._style()
        self._build()
        self.refresh_queue()

    def _style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#f3f6fb")
        style.configure("Card.TFrame", background="white")
        style.configure("TLabel", background="#f3f6fb", foreground="#1c2b3a", font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="#17324d")
        style.configure("Sub.TLabel", font=("Segoe UI", 10), foreground="#60758a")
        style.configure("TButton", font=("Segoe UI", 10), padding=(10, 7))
        style.configure("Treeview", font=("Segoe UI", 9), rowheight=28)
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))

    def _build(self):
        outer = ttk.Frame(self, padding=22)
        outer.pack(fill="both", expand=True)
        header = ttk.Frame(outer)
        header.pack(fill="x")
        ttk.Label(header, text="Hospital Queue Management", style="Title.TLabel").pack(side="left")
        ttk.Button(header, text="Log out", command=self.logout).pack(side="right")
        ttk.Label(outer, text="Reception desk and patient queue", style="Sub.TLabel").pack(anchor="w", pady=(3, 14))
        self.tabs = ttk.Notebook(outer)
        self.tabs.pack(fill="both", expand=True)
        self.reception = ttk.Frame(self.tabs, padding=16)
        self.patient = ttk.Frame(self.tabs, padding=16)
        self.tabs.add(self.reception, text="Receptionist")
        self.tabs.add(self.patient, text="Patient")
        self._build_receptionist()
        self._build_patient()

    def open_for_role(self, role):
        if role == "Patient":
            if not self.receptionist_authenticated and str(self.reception) in self.tabs.tabs():
                self.tabs.forget(self.reception)
            self.tabs.select(self.patient)
        else:
            if str(self.reception) not in self.tabs.tabs():
                self.tabs.insert(0, self.reception, text="Receptionist")
            self.tabs.select(self.reception)
        self.deiconify()

    def receptionist_access(self):
        if self.receptionist_authenticated:
            self.open_for_role("Receptionist")
        else:
            LoginDialog(self, allow_patient=False, cancel_destroys_app=False)

    def logout(self):
        self.receptionist_authenticated = False
        if str(self.reception) in self.tabs.tabs():
            self.tabs.forget(self.reception)
        self.tabs.select(self.patient)
        LoginDialog(self, allow_patient=True, cancel_destroys_app=False)

    def _build_receptionist(self):
        bar = ttk.Frame(self.reception)
        bar.pack(fill="x", pady=(0, 12))
        ttk.Label(bar, text="Receptionist dashboard", font=("Segoe UI", 15, "bold")).pack(side="left")
        ttk.Button(bar, text="View charts", command=self.show_charts).pack(side="right", padx=5)
        ttk.Button(bar, text="Export queue", command=self.export_queue).pack(side="right", padx=5)
        ttk.Button(bar, text="Refresh", command=self.refresh_queue).pack(side="right", padx=5)
        ttk.Button(bar, text="Register patient", command=self.register_patient).pack(side="right", padx=5)
        cols = ("token", "name", "age", "phone", "department", "doctor", "status", "registered")
        self.tree = ttk.Treeview(self.reception, columns=cols, show="headings", selectmode="browse")
        labels = {"token":"Queue token", "name":"Patient", "age":"Age", "phone":"Phone", "department":"Department", "doctor":"Doctor", "status":"Status", "registered":"Registered"}
        widths = {"token":130, "name":125, "age":40, "phone":105, "department":125, "doctor":130, "status":115, "registered":130}
        for col in cols:
            self.tree.heading(col, text=labels[col])
            self.tree.column(col, width=widths[col], anchor="w")
        self.tree.pack(fill="both", expand=True)
        actions = ttk.Frame(self.reception)
        actions.pack(fill="x", pady=(12, 0))
        ttk.Button(actions, text="Call next patient", command=self.call_next_patient).pack(side="left")
        ttk.Button(actions, text="Mark selected completed", command=self.complete_selected).pack(side="left", padx=8)

    def _build_patient(self):
        card = ttk.Frame(self.patient, style="Card.TFrame", padding=22)
        card.pack(fill="x", pady=(0, 16))
        ttk.Label(card, text="Patient services", font=("Segoe UI", 16, "bold"), background="white").pack(anchor="w")
        ttk.Label(card, text="Register for a visit or check your queue status.", background="white", style="Sub.TLabel").pack(anchor="w", pady=(4, 12))
        buttons = ttk.Frame(card, style="Card.TFrame")
        buttons.pack(fill="x")
        ttk.Button(buttons, text="Register and get a token", command=self.register_patient).pack(side="left")
        ttk.Button(buttons, text="Open Receptionist", command=self.receptionist_access).pack(side="left", padx=8)
        status = ttk.Frame(self.patient, style="Card.TFrame", padding=22)
        status.pack(fill="x")
        ttk.Label(status, text="Check queue status", font=("Segoe UI", 14, "bold"), background="white").pack(anchor="w")
        ttk.Label(status, text="Approximate wait is based on typical appointment time and patients ahead for the same doctor.", background="white", style="Sub.TLabel").pack(anchor="w", pady=(5, 0))
        row = ttk.Frame(status, style="Card.TFrame")
        row.pack(fill="x", pady=(14, 8))
        ttk.Label(row, text="Queue token:", background="white").pack(side="left")
        self.token_entry = ttk.Entry(row, width=30)
        self.token_entry.pack(side="left", padx=10)
        ttk.Button(row, text="Check status", command=self.check_status).pack(side="left")
        self.status_result = ttk.Label(status, text="Enter the token printed during registration.", background="white", style="Sub.TLabel")
        self.status_result.pack(anchor="w", pady=(8, 0))

    def register_patient(self):
        dialog = PatientDialog(self)
        self.wait_window(dialog)
        if not dialog.result:
            return
        token = register_patient(*dialog.result)
        self.refresh_queue()
        self.token_entry.delete(0, "end")
        self.token_entry.insert(0, token)
        self.check_status()
        messagebox.showinfo("Registration complete", f"Patient registered successfully.\n\nQueue token: {token}", parent=self)
        self.tabs.select(self.patient)

    def refresh_queue(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in get_patients():
            self.tree.insert("", "end", iid=row["token"], values=(row["token"], row["name"], row["age"], row["phone"], row["department"], row["doctor"], row["status"], row["registered_at"].replace("T", " ")))

    def call_next_patient(self):
        row = call_next()
        if row:
            messagebox.showinfo("Calling patient", f"Now calling {row['token']} — {row['name']}\nDepartment: {row['department']}", parent=self)
        else:
            messagebox.showinfo("Queue empty", "There are no patients waiting.", parent=self)
        self.refresh_queue()

    def complete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select a patient", "Select a patient from the queue first.", parent=self)
        elif complete_patient(selected[0]):
            messagebox.showinfo("Completed", f"{selected[0]} marked as completed.", parent=self)
        else:
            messagebox.showwarning("Cannot complete", "Only a patient in consultation can be completed.", parent=self)
        self.refresh_queue()

    def check_status(self):
        token = self.token_entry.get().strip().upper()
        if not token:
            messagebox.showwarning("Token required", "Enter your queue token.", parent=self)
            return
        patient, ahead = get_patient_status(token)
        if not patient:
            self.status_result.configure(text="Token not found. Please check it and try again.", foreground="#b42318")
            return
        text = f"{patient['token']} · {patient['name']} · {patient['department']} · {patient['doctor']} — {patient['status']}"
        if patient["status"] == "Waiting":
            wait = ahead * AVERAGE_MINUTES.get(patient["department"], 20)
            text += f" · {ahead} ahead · Approx. wait: {wait} min"
        elif patient["status"] == "In Consultation":
            text += " · Please go to the consultation room."
        else:
            text += " · Visit complete. Thank you."
        self.status_result.configure(text=text, foreground="#167044")

    def show_charts(self):
        if not show_patient_charts(self, dataframe_for_charts()):
            messagebox.showinfo("No queue data", "Register patients before viewing charts.", parent=self)

    def export_queue(self):
        path = filedialog.asksaveasfilename(parent=self, title="Export patient queue", defaultextension=".xlsx", initialfile="hospital_queue.xlsx", filetypes=[("Excel workbook", "*.xlsx"), ("CSV file", "*.csv")])
        if not path:
            return
        try:
            df = dataframe_for_export()
            if path.lower().endswith(".csv"):
                df.to_csv(path, index=False, encoding="utf-8-sig")
            else:
                df.to_excel(path, index=False, sheet_name="Patient Queue")
        except Exception as exc:
            messagebox.showerror("Export failed", f"Could not save the queue:\n{exc}", parent=self)
            return
        messagebox.showinfo("Export complete", f"Queue exported to:\n{path}", parent=self)


def run():
    from .database import initialize
    initialize()
    app = HospitalQueueApp()
    app.open_for_role("Patient")
    LoginDialog(app)
    app.mainloop()
