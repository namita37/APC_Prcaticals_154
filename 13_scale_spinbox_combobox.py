# 13 - Scale, Spinbox and Combobox Widgets

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Scale, Spinbox & Combobox")
root.geometry("440x480")
root.configure(bg="#f8f9fa")
root.resizable(False, False)

tk.Label(root, text="Widget Showcase", font=("Arial", 16, "bold"),
         bg="#f8f9fa", fg="#2c3e50").pack(pady=12)

frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(padx=30, pady=5, fill="x")

# --- Scale (Slider) ---
scale_frame = tk.LabelFrame(frame, text=" Scale (Slider) ", font=("Arial", 11, "bold"),
                             bg="#f8f9fa", fg="#2c3e50", padx=10, pady=8)
scale_frame.pack(fill="x", pady=6)

age_var = tk.IntVar(value=20)
tk.Label(scale_frame, text="Select Age:", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
scale = tk.Scale(scale_frame, from_=1, to=100, orient=tk.HORIZONTAL,
                 variable=age_var, length=340, font=("Arial", 10),
                 bg="#f8f9fa", troughcolor="#3498db", activebackground="#2980b9",
                 highlightthickness=0, cursor="hand2")
scale.pack(fill="x")
age_label = tk.Label(scale_frame, textvariable=age_var, font=("Arial", 12, "bold"),
                     bg="#f8f9fa", fg="#e74c3c")
age_label.pack()

# --- Spinbox ---
spin_frame = tk.LabelFrame(frame, text=" Spinbox ", font=("Arial", 11, "bold"),
                            bg="#f8f9fa", fg="#2c3e50", padx=10, pady=8)
spin_frame.pack(fill="x", pady=6)

tk.Label(spin_frame, text="Select Semester:", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
spinbox = tk.Spinbox(spin_frame, from_=1, to=8, width=5, font=("Arial", 14, "bold"),
                     justify="center", relief="solid", bd=1)
spinbox.pack(anchor="w", pady=4)

tk.Label(spin_frame, text="Select Score (Step 5):", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
spinbox2 = tk.Spinbox(spin_frame, from_=0, to=100, increment=5, width=6, font=("Arial", 13),
                      justify="center", relief="solid", bd=1)
spinbox2.pack(anchor="w", pady=4)

# --- Combobox ---
combo_frame = tk.LabelFrame(frame, text=" Combobox (Dropdown) ", font=("Arial", 11, "bold"),
                             bg="#f8f9fa", fg="#2c3e50", padx=10, pady=8)
combo_frame.pack(fill="x", pady=6)

tk.Label(combo_frame, text="Select Branch:", font=("Arial", 11), bg="#f8f9fa").pack(anchor="w")
branch_combo = ttk.Combobox(combo_frame, font=("Arial", 11), state="readonly", width=30,
                             values=["Computer Science", "Electronics", "Mechanical",
                                     "Civil", "Information Technology", "BCA", "MCA"])
branch_combo.set("Computer Science")
branch_combo.pack(anchor="w", pady=4)

# Submit
def show_values():
    info = (f"Age      : {age_var.get()}\n"
            f"Semester : {spinbox.get()}\n"
            f"Score    : {spinbox2.get()}\n"
            f"Branch   : {branch_combo.get()}")
    messagebox.showinfo("Selected Values", info)

tk.Button(root, text="Show Selected Values", command=show_values,
          font=("Arial", 12), bg="#3498db", fg="white",
          padx=14, pady=7, relief="flat", cursor="hand2").pack(pady=12)

root.mainloop()
