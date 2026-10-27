# 09 - Listbox Widget Demo

import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get().strip()
    if not item:
        messagebox.showwarning("Empty", "Please type an item to add.")
        return
    listbox.insert(tk.END, item)
    entry.delete(0, tk.END)

def delete_item():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("None Selected", "Please select an item to delete.")
        return
    listbox.delete(selected[0])

def clear_all():
    listbox.delete(0, tk.END)

def show_selected():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Selection", "No item selected.")
        return
    item = listbox.get(selected[0])
    messagebox.showinfo("Selected Item", f"You selected: {item}")

def move_up():
    selected = listbox.curselection()
    if not selected or selected[0] == 0:
        return
    idx  = selected[0]
    item = listbox.get(idx)
    listbox.delete(idx)
    listbox.insert(idx - 1, item)
    listbox.select_set(idx - 1)

def move_down():
    selected = listbox.curselection()
    if not selected or selected[0] == listbox.size() - 1:
        return
    idx  = selected[0]
    item = listbox.get(idx)
    listbox.delete(idx)
    listbox.insert(idx + 1, item)
    listbox.select_set(idx + 1)

root = tk.Tk()
root.title("Listbox Demo")
root.geometry("420x460")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text="📋 Listbox Widget", font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=12)

# Entry + Add
top_frame = tk.Frame(root, bg="#f0f4f8")
top_frame.pack(pady=5)
entry = tk.Entry(top_frame, font=("Arial", 12), width=22, relief="solid", bd=1)
entry.pack(side="left", padx=5)
tk.Button(top_frame, text="Add", command=add_item, font=("Arial", 11),
          bg="#27ae60", fg="white", padx=10, pady=4, relief="flat", cursor="hand2").pack(side="left")

# Listbox with scrollbar
lb_frame = tk.Frame(root, bg="#f0f4f8")
lb_frame.pack(pady=10)
scrollbar = tk.Scrollbar(lb_frame, orient=tk.VERTICAL)
listbox = tk.Listbox(lb_frame, font=("Arial", 12), width=28, height=10,
                     yscrollcommand=scrollbar.set, relief="solid", bd=1,
                     selectbackground="#3498db", selectforeground="white", activestyle="none")
scrollbar.config(command=listbox.yview)
listbox.pack(side="left")
scrollbar.pack(side="right", fill="y")

# Pre-fill items
for item in ["Python", "Java", "C++", "JavaScript", "Go", "Rust", "Kotlin"]:
    listbox.insert(tk.END, item)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)
cfg = {"font": ("Arial", 10), "fg": "white", "padx": 8, "pady": 5, "relief": "flat", "cursor": "hand2"}
tk.Button(btn_frame, text="Show",       command=show_selected, bg="#3498db", **cfg).grid(row=0, column=0, padx=4)
tk.Button(btn_frame, text="Delete",     command=delete_item,   bg="#e74c3c", **cfg).grid(row=0, column=1, padx=4)
tk.Button(btn_frame, text="Clear All",  command=clear_all,     bg="#95a5a6", **cfg).grid(row=0, column=2, padx=4)
tk.Button(btn_frame, text="Move Up",    command=move_up,       bg="#9b59b6", **cfg).grid(row=0, column=3, padx=4)
tk.Button(btn_frame, text="Move Down",  command=move_down,     bg="#e67e22", **cfg).grid(row=0, column=4, padx=4)

tk.Label(root, text="Tip: Click an item to select it first.", font=("Arial", 9, "italic"),
         bg="#f0f4f8", fg="#95a5a6").pack()

root.mainloop()
