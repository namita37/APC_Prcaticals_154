# 18 - To-Do List Application

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("460x540")
        self.root.configure(bg="#f8f9fa")
        self.root.resizable(False, False)

        self.tasks = []

        # Header
        tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"),
                 bg="#f8f9fa", fg="#2c3e50").pack(pady=12)

        # Input frame
        input_frame = tk.Frame(root, bg="#f8f9fa")
        input_frame.pack(padx=20, fill="x")

        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), relief="solid", bd=1)
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        tk.Button(input_frame, text="Add", command=self.add_task,
                  font=("Arial", 11, "bold"), bg="#27ae60", fg="white",
                  padx=12, pady=6, relief="flat", cursor="hand2").pack(side="left")

        # Task listbox with scrollbar
        lb_frame = tk.Frame(root, bg="#f8f9fa")
        lb_frame.pack(padx=20, pady=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(lb_frame)
        self.listbox = tk.Listbox(lb_frame, font=("Arial", 12), relief="solid", bd=1,
                                  yscrollcommand=scrollbar.set, height=14,
                                  selectbackground="#3498db", selectforeground="white",
                                  activestyle="none")
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.listbox.bind("<Double-Button-1>", lambda e: self.toggle_done())

        # Status bar
        self.status_var = tk.StringVar(value="0 tasks")
        tk.Label(root, textvariable=self.status_var, font=("Arial", 10, "italic"),
                 bg="#f8f9fa", fg="#7f8c8d").pack()

        # Buttons
        btn_frame = tk.Frame(root, bg="#f8f9fa")
        btn_frame.pack(pady=10)
        cfg = {"font": ("Arial", 11), "fg": "white", "padx": 10, "pady": 6, "relief": "flat", "cursor": "hand2"}
        tk.Button(btn_frame, text="✔ Done",    command=self.toggle_done,  bg="#3498db", **cfg).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="✏ Edit",    command=self.edit_task,    bg="#f39c12", **cfg).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🗑 Delete",  command=self.delete_task,  bg="#e74c3c", **cfg).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="🧹 Clear All", command=self.clear_all, bg="#95a5a6", **cfg).grid(row=0, column=3, padx=5)

        # Sample tasks
        for t in ["Buy groceries", "Study Python Tkinter", "Complete assignment", "Read a book"]:
            self.add_task(t)

    def add_task(self, text=None):
        task = text if text else self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Empty", "Please enter a task.")
            return
        self.tasks.append({"text": task, "done": False})
        self.listbox.insert(tk.END, f"  ○  {task}")
        self.task_entry.delete(0, tk.END)
        self.update_status()

    def toggle_done(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        idx = selected[0]
        task = self.tasks[idx]
        task["done"] = not task["done"]
        if task["done"]:
            self.listbox.itemconfig(idx, fg="#27ae60")
            self.listbox.delete(idx)
            self.listbox.insert(idx, f"  ✔  {task['text']}")
            self.listbox.itemconfig(idx, fg="#27ae60")
        else:
            self.listbox.delete(idx)
            self.listbox.insert(idx, f"  ○  {task['text']}")
            self.listbox.itemconfig(idx, fg="black")
        self.update_status()

    def edit_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("None", "Select a task to edit.")
            return
        idx = selected[0]
        old = self.tasks[idx]["text"]
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, old)
        self.tasks.pop(idx)
        self.listbox.delete(idx)
        self.update_status()

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("None", "Select a task to delete.")
            return
        idx = selected[0]
        if messagebox.askyesno("Confirm", f"Delete '{self.tasks[idx]['text']}'?"):
            self.tasks.pop(idx)
            self.listbox.delete(idx)
            self.update_status()

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Clear all tasks?"):
            self.tasks.clear()
            self.listbox.delete(0, tk.END)
            self.update_status()

    def update_status(self):
        done  = sum(1 for t in self.tasks if t["done"])
        total = len(self.tasks)
        self.status_var.set(f"{total} tasks  |  {done} completed  |  {total-done} pending")

root = tk.Tk()
app  = TodoApp(root)
root.mainloop()
