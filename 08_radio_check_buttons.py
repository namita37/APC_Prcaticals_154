# 08 - Radiobutton and Checkbutton Widgets

import tkinter as tk
from tkinter import messagebox

def submit():
    gender  = gender_var.get()
    hobbies = [h for h, v in hobby_vars.items() if v.get()]
    if not gender:
        messagebox.showwarning("Missing", "Please select a gender.")
        return
    if not hobbies:
        messagebox.showwarning("Missing", "Please select at least one hobby.")
        return
    result = f"Gender  : {gender}\nHobbies : {', '.join(hobbies)}"
    messagebox.showinfo("Your Selection", result)

root = tk.Tk()
root.title("Radiobutton & Checkbutton")
root.geometry("380x400")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="Select Options", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=15)

# --- Radiobutton (Gender) ---
gender_frame = tk.LabelFrame(root, text=" Gender ", font=("Arial", 12, "bold"),
                              bg="#f8f9fa", fg="#2c3e50", padx=15, pady=10)
gender_frame.pack(fill="x", padx=30, pady=8)
gender_var = tk.StringVar()
for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(gender_frame, text=g, variable=gender_var, value=g,
                   font=("Arial", 12), bg="#f8f9fa", activebackground="#f8f9fa",
                   cursor="hand2").pack(side="left", padx=12)

# --- Checkbutton (Hobbies) ---
hobby_frame = tk.LabelFrame(root, text=" Hobbies ", font=("Arial", 12, "bold"),
                             bg="#f8f9fa", fg="#2c3e50", padx=15, pady=10)
hobby_frame.pack(fill="x", padx=30, pady=8)
hobbies_list = ["Reading", "Gaming", "Cooking", "Travelling", "Music", "Coding"]
hobby_vars = {}
for i, h in enumerate(hobbies_list):
    var = tk.BooleanVar()
    hobby_vars[h] = var
    tk.Checkbutton(hobby_frame, text=h, variable=var,
                   font=("Arial", 11), bg="#f8f9fa", activebackground="#f8f9fa",
                   cursor="hand2").grid(row=i//3, column=i%3, padx=8, pady=4, sticky="w")

# Buttons
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Submit", command=submit, font=("Arial", 12), bg="#27ae60",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Exit",   command=root.destroy, font=("Arial", 12), bg="#e74c3c",
          fg="white", padx=14, pady=7, relief="flat", cursor="hand2").grid(row=0, column=1, padx=10)

root.mainloop()
