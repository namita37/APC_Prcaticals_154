# 12 - Student Record Manager (CRUD with Treeview)

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("720x530")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text="🎓 Student Record Manager", font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=10)

# ---- Form ----
form = tk.Frame(root, bg="#f0f4f8")
form.pack(pady=5)

fields  = ["Roll No", "Name", "Branch", "Semester", "Marks"]
entries = {}
for i, field in enumerate(fields):
    tk.Label(form, text=f"{field}:", font=("Arial", 11), bg="#f0f4f8",
             anchor="e", width=10).grid(row=0, column=i*2, padx=5)
    e = tk.Entry(form, font=("Arial", 11), width=10, relief="solid", bd=1)
    e.grid(row=0, column=i*2+1, padx=3)
    entries[field] = e

# ---- Treeview ----
tree_frame = tk.Frame(root)
tree_frame.pack(padx=20, pady=8, fill="both")

cols = ("Roll No", "Name", "Branch", "Semester", "Marks")
tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=12)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=118, anchor="center")

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Style
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
style.configure("Treeview", font=("Arial", 11), rowheight=26)
style.map("Treeview", background=[("selected", "#3498db")])

def get_entries():
    return [entries[f].get().strip() for f in fields]

def clear_entries():
    for e in entries.values():
        e.delete(0, tk.END)

def add_record():
    vals = get_entries()
    if not all(vals):
        messagebox.showwarning("Missing", "Please fill all fields.")
        return
    tree.insert("", tk.END, values=vals)
    clear_entries()

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("None", "Please select a record to delete.")
        return
    if messagebox.askyesno("Confirm", "Delete selected record?"):
        tree.delete(selected[0])

def edit_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("None", "Please select a record to edit.")
        return
    vals = get_entries()
    if not all(vals):
        messagebox.showwarning("Missing", "Please fill all fields with new data.")
        return
    tree.item(selected[0], values=vals)
    clear_entries()

def load_to_form(event):
    selected = tree.selection()
    if not selected:
        return
    vals = tree.item(selected[0])["values"]
    for field, val in zip(fields, vals):
        entries[field].delete(0, tk.END)
        entries[field].insert(0, str(val))

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all records?"):
        tree.delete(*tree.get_children())

tree.bind("<<TreeviewSelect>>", load_to_form)

# Pre-load sample data
samples = [
    ("101", "Amit",   "CS",          "3", "85"),
    ("102", "Priya",  "Electronics", "3", "92"),
    ("103", "Rahul",  "Mechanical",  "4", "78"),
]
for s in samples:
    tree.insert("", tk.END, values=s)

# ---- Buttons ----
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=8)
cfg = {"font": ("Arial", 11), "fg": "white", "padx": 12, "pady": 6, "relief": "flat", "cursor": "hand2"}
tk.Button(btn_frame, text="➕ Add",    command=add_record,   bg="#27ae60", **cfg).grid(row=0, column=0, padx=6)
tk.Button(btn_frame, text="✏ Edit",   command=edit_record,  bg="#f39c12", **cfg).grid(row=0, column=1, padx=6)
tk.Button(btn_frame, text="🗑 Delete", command=delete_record, bg="#e74c3c", **cfg).grid(row=0, column=2, padx=6)
tk.Button(btn_frame, text="🧹 Clear",  command=clear_entries, bg="#95a5a6", **cfg).grid(row=0, column=3, padx=6)
tk.Button(btn_frame, text="❌ Clear All", command=clear_all, bg="#7f8c8d", **cfg).grid(row=0, column=4, padx=6)

root.mainloop()
