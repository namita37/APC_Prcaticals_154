# 05 - Login Form with Validation

import tkinter as tk
from tkinter import messagebox

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    username = user_entry.get().strip()
    password = pass_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Empty Fields", "Please enter both username and password.")
        return
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {username}! Login successful.")
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        pass_entry.delete(0, tk.END)

def toggle_password():
    if pass_entry.cget("show") == "*":
        pass_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        pass_entry.config(show="*")
        show_btn.config(text="Show")

def clear_form():
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Login Form")
root.geometry("380x380")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

# Header
tk.Label(root, text="🔐 Login", font=("Arial", 20, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=25)

# Form frame
frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

# Username
tk.Label(frame, text="Username:", font=("Arial", 12), bg="#f0f4f8", anchor="w",
         width=10).grid(row=0, column=0, pady=10, sticky="w")
user_entry = tk.Entry(frame, font=("Arial", 12), width=20, relief="solid", bd=1)
user_entry.grid(row=0, column=1, columnspan=2, pady=10)

# Password
tk.Label(frame, text="Password:", font=("Arial", 12), bg="#f0f4f8", anchor="w",
         width=10).grid(row=1, column=0, pady=10, sticky="w")
pass_entry = tk.Entry(frame, font=("Arial", 12), width=15, relief="solid", bd=1, show="*")
pass_entry.grid(row=1, column=1, pady=10)
show_btn = tk.Button(frame, text="Show", command=toggle_password, font=("Arial", 9),
                     bg="#bdc3c7", relief="flat", cursor="hand2", width=5)
show_btn.grid(row=1, column=2, padx=5)

# Hint
tk.Label(root, text="Hint: admin / 1234", font=("Arial", 9, "italic"),
         bg="#f0f4f8", fg="#95a5a6").pack()

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Login",  command=login,      font=("Arial", 12), bg="#27ae60",
          fg="white", padx=16, pady=7, relief="flat", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear",  command=clear_form, font=("Arial", 12), bg="#95a5a6",
          fg="white", padx=16, pady=7, relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Cancel", command=root.destroy, font=("Arial", 12), bg="#e74c3c",
          fg="white", padx=16, pady=7, relief="flat", cursor="hand2").grid(row=0, column=2, padx=10)

user_entry.focus()
root.mainloop()
