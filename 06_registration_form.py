# 06 - Registration Form

import tkinter as tk
from tkinter import messagebox, ttk

def register():
    name    = name_entry.get().strip()
    email   = email_entry.get().strip()
    phone   = phone_entry.get().strip()
    gender  = gender_var.get()
    course  = course_combo.get()
    password = pass_entry.get().strip()
    confirm  = confirm_entry.get().strip()

    if not all([name, email, phone, gender, course, password, confirm]):
        messagebox.showwarning("Incomplete", "Please fill in all fields.")
        return
    if "@" not in email or "." not in email:
        messagebox.showerror("Invalid", "Please enter a valid email address.")
        return
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Invalid", "Phone must be 10 digits.")
        return
    if password != confirm:
        messagebox.showerror("Mismatch", "Passwords do not match.")
        return

    info = (f"Name   : {name}\nEmail  : {email}\nPhone  : {phone}\n"
            f"Gender : {gender}\nCourse : {course}")
    messagebox.showinfo("Registered!", f"Registration Successful!\n\n{info}")

def clear_form():
    for widget in [name_entry, email_entry, phone_entry, pass_entry, confirm_entry]:
        widget.delete(0, tk.END)
    gender_var.set("")
    course_combo.set("")

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("460x540")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="📋 Student Registration", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=15)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(pady=5)

def make_row(parent, label, row, widget_fn):
    tk.Label(parent, text=label, font=("Arial", 11), bg="#f8f9fa",
             anchor="e", width=14).grid(row=row, column=0, pady=7, padx=5, sticky="e")
    w = widget_fn(parent)
    w.grid(row=row, column=1, pady=7, sticky="w")
    return w

name_entry    = make_row(frame, "Full Name :",    0, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1))
email_entry   = make_row(frame, "Email :",        1, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1))
phone_entry   = make_row(frame, "Phone :",        2, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1))

# Gender (Radio buttons)
tk.Label(frame, text="Gender :", font=("Arial", 11), bg="#f8f9fa",
         anchor="e", width=14).grid(row=3, column=0, pady=7, sticky="e")
gender_var = tk.StringVar()
gender_frame = tk.Frame(frame, bg="#f8f9fa")
gender_frame.grid(row=3, column=1, sticky="w")
for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(gender_frame, text=g, variable=gender_var, value=g,
                   font=("Arial", 11), bg="#f8f9fa").pack(side="left", padx=4)

# Course (Combobox)
tk.Label(frame, text="Course :", font=("Arial", 11), bg="#f8f9fa",
         anchor="e", width=14).grid(row=4, column=0, pady=7, sticky="e")
course_combo = ttk.Combobox(frame, font=("Arial", 11), width=22, state="readonly",
                             values=["B.Sc CS", "BCA", "B.Tech", "MCA", "M.Sc CS"])
course_combo.grid(row=4, column=1, sticky="w")

pass_entry    = make_row(frame, "Password :",     5, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1, show="*"))
confirm_entry = make_row(frame, "Confirm Pass :", 6, lambda p: tk.Entry(p, font=("Arial", 11), width=24, relief="solid", bd=1, show="*"))

# Buttons
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=15)
tk.Button(btn_frame, text="Register", command=register,   font=("Arial", 12), bg="#27ae60",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear",    command=clear_form, font=("Arial", 12), bg="#95a5a6",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Exit",     command=root.destroy, font=("Arial", 12), bg="#e74c3c",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=2, padx=10)

root.mainloop()
