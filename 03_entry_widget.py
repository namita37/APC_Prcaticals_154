# 03 - Entry Widget - Taking User Input

import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get().strip()
    age  = age_entry.get().strip()
    if not name or not age:
        messagebox.showwarning("Missing Input", "Please enter both name and age.")
        return
    if not age.isdigit():
        messagebox.showerror("Invalid Input", "Age must be a number.")
        return
    result_label.config(text=f"Hello, {name}! You are {age} years old.", fg="#27ae60")

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Entry Widget Demo")
root.geometry("420x320")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="User Input Form", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=15)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(pady=5)

# Name field
tk.Label(frame, text="Name :", font=("Arial", 12), bg="#f8f9fa", width=8, anchor="e").grid(row=0, column=0, pady=8, padx=5)
name_entry = tk.Entry(frame, font=("Arial", 12), width=22, relief="solid", bd=1)
name_entry.grid(row=0, column=1, pady=8)

# Age field
tk.Label(frame, text="Age  :", font=("Arial", 12), bg="#f8f9fa", width=8, anchor="e").grid(row=1, column=0, pady=8, padx=5)
age_entry = tk.Entry(frame, font=("Arial", 12), width=22, relief="solid", bd=1)
age_entry.grid(row=1, column=1, pady=8)

# Buttons
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Greet",  command=greet,        font=("Arial", 11), bg="#3498db", fg="white",
          padx=14, pady=6, relief="flat", cursor="hand2").grid(row=0, column=0, padx=8)
tk.Button(btn_frame, text="Clear",  command=clear_fields, font=("Arial", 11), bg="#95a5a6", fg="white",
          padx=14, pady=6, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)

result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#f8f9fa", fg="#2c3e50")
result_label.pack(pady=10)

root.mainloop()
