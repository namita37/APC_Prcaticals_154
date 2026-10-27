# 07 - MessageBox and Dialog Demos

import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser, filedialog

root = tk.Tk()
root.title("MessageBox & Dialog Demo")
root.geometry("420x480")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

result_var = tk.StringVar(value="Result will appear here...")

tk.Label(root, text="📦 Dialog Box Examples", font=("Arial", 15, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=15)

def show_info():
    messagebox.showinfo("Information", "This is an Information dialog box.")
    result_var.set("Showed: Info dialog")

def show_warning():
    messagebox.showwarning("Warning", "This is a Warning dialog box!")
    result_var.set("Showed: Warning dialog")

def show_error():
    messagebox.showerror("Error", "This is an Error dialog box!")
    result_var.set("Showed: Error dialog")

def ask_yesno():
    ans = messagebox.askyesno("Question", "Do you like Python?")
    result_var.set(f"Yes/No Answer: {'Yes' if ans else 'No'}")

def ask_okcancel():
    ans = messagebox.askokcancel("Confirm", "Proceed with the action?")
    result_var.set(f"OK/Cancel Answer: {'OK' if ans else 'Cancel'}")

def ask_input():
    val = simpledialog.askstring("Input", "Enter your name:")
    result_var.set(f"Input received: {val}" if val else "Input cancelled")

def pick_color():
    color = colorchooser.askcolor(title="Choose a Color")
    if color[1]:
        result_label.config(bg=color[1])
        result_var.set(f"Color chosen: {color[1]}")

def open_file():
    filepath = filedialog.askopenfilename(title="Open File",
               filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")])
    result_var.set(f"File: {filepath}" if filepath else "No file selected")

# Buttons
btn_cfg = {"font": ("Arial", 11), "fg": "white", "padx": 10, "pady": 6,
           "relief": "flat", "cursor": "hand2", "width": 18}

tk.Button(root, text="ℹ Show Info",       command=show_info,    bg="#3498db", **btn_cfg).pack(pady=4)
tk.Button(root, text="⚠ Show Warning",    command=show_warning, bg="#f39c12", **btn_cfg).pack(pady=4)
tk.Button(root, text="❌ Show Error",      command=show_error,   bg="#e74c3c", **btn_cfg).pack(pady=4)
tk.Button(root, text="✔ Yes / No",         command=ask_yesno,   bg="#27ae60", **btn_cfg).pack(pady=4)
tk.Button(root, text="🔘 OK / Cancel",     command=ask_okcancel, bg="#8e44ad", **btn_cfg).pack(pady=4)
tk.Button(root, text="⌨ Input Dialog",    command=ask_input,    bg="#16a085", **btn_cfg).pack(pady=4)
tk.Button(root, text="🎨 Color Chooser",  command=pick_color,   bg="#d35400", **btn_cfg).pack(pady=4)
tk.Button(root, text="📂 Open File",       command=open_file,   bg="#2980b9", **btn_cfg).pack(pady=4)

result_label = tk.Label(root, textvariable=result_var, font=("Arial", 10, "italic"),
                        bg="#f0f4f8", fg="#2c3e50", wraplength=380)
result_label.pack(pady=12)

root.mainloop()
