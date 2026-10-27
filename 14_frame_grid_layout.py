# 14 - Frame and Grid Layout Demo

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Frame & Grid Layout")
root.geometry("500x520")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

tk.Label(root, text="📐 Layout Demo with Frames", font=("Arial", 15, "bold"),
         bg="#ecf0f1", fg="#2c3e50").pack(pady=10)

# ---- TOP FRAME - personal info ----
top_frame = tk.LabelFrame(root, text=" Personal Information ", font=("Arial", 11, "bold"),
                           bg="#ecf0f1", fg="#2c3e50", padx=15, pady=10)
top_frame.pack(fill="x", padx=20, pady=5)

labels_entries = [
    ("First Name:",  0, 0), ("Last Name:",   0, 2),
    ("Email:",       1, 0), ("Phone:",       1, 2),
    ("City:",        2, 0), ("Country:",     2, 2),
]
entry_widgets = {}
for text, row, col in labels_entries:
    tk.Label(top_frame, text=text, font=("Arial", 11), bg="#ecf0f1",
             anchor="e", width=12).grid(row=row, column=col, padx=5, pady=6, sticky="e")
    e = tk.Entry(top_frame, font=("Arial", 11), width=15, relief="solid", bd=1)
    e.grid(row=row, column=col+1, padx=5, pady=6)
    entry_widgets[text] = e

# ---- MIDDLE FRAME - academic info ----
mid_frame = tk.LabelFrame(root, text=" Academic Information ", font=("Arial", 11, "bold"),
                           bg="#ecf0f1", fg="#2c3e50", padx=15, pady=10)
mid_frame.pack(fill="x", padx=20, pady=5)

acad_fields = [("Roll No:", 0, 0), ("Course:", 0, 2), ("Year:", 1, 0), ("CGPA:", 1, 2)]
for text, row, col in acad_fields:
    tk.Label(mid_frame, text=text, font=("Arial", 11), bg="#ecf0f1",
             anchor="e", width=12).grid(row=row, column=col, padx=5, pady=6, sticky="e")
    e = tk.Entry(mid_frame, font=("Arial", 11), width=15, relief="solid", bd=1)
    e.grid(row=row, column=col+1, padx=5, pady=6)
    entry_widgets[text] = e

# ---- BOTTOM FRAME - buttons ----
bottom_frame = tk.Frame(root, bg="#ecf0f1")
bottom_frame.pack(pady=12)

def submit_form():
    filled = {k: v.get().strip() for k, v in entry_widgets.items()}
    empty  = [k for k, v in filled.items() if not v]
    if empty:
        messagebox.showwarning("Incomplete", f"Please fill: {', '.join(empty)}")
        return
    result = "\n".join(f"{k:<14} {v}" for k, v in filled.items())
    messagebox.showinfo("Form Data", result)

def clear_form():
    for e in entry_widgets.values():
        e.delete(0, tk.END)

cfg = {"font": ("Arial", 12), "fg": "white", "padx": 14, "pady": 7, "relief": "flat", "cursor": "hand2"}
tk.Button(bottom_frame, text="Submit", command=submit_form, bg="#27ae60", **cfg).grid(row=0, column=0, padx=10)
tk.Button(bottom_frame, text="Clear",  command=clear_form,  bg="#95a5a6", **cfg).grid(row=0, column=1, padx=10)
tk.Button(bottom_frame, text="Exit",   command=root.destroy, bg="#e74c3c", **cfg).grid(row=0, column=2, padx=10)

root.mainloop()
