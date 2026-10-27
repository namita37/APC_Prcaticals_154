# 10 - Menu Bar with Frames (Notepad-like App)

import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont

def new_file():
    text_area.delete("1.0", tk.END)
    root.title("Notepad - New File")

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())
        root.title(f"Notepad - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", f"File saved to {filepath}")
        root.title(f"Notepad - {filepath}")

def cut():   text_area.event_generate("<<Cut>>")
def copy():  text_area.event_generate("<<Copy>>")
def paste(): text_area.event_generate("<<Paste>>")

def select_all():
    text_area.tag_add("sel", "1.0", tk.END)

def increase_font():
    current = text_area.cget("font")
    f = tkfont.Font(font=current)
    f.config(size=f.cget("size") + 2)
    text_area.config(font=f)

def decrease_font():
    current = text_area.cget("font")
    f = tkfont.Font(font=current)
    size = max(8, f.cget("size") - 2)
    f.config(size=size)
    text_area.config(font=f)

def about():
    messagebox.showinfo("About", "Simple Notepad\nBuilt with Python Tkinter")

root = tk.Tk()
root.title("Notepad - New File")
root.geometry("650x480")

# Menu bar
menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New",   command=new_file,   accelerator="Ctrl+N")
file_menu.add_command(label="Open",  command=open_file,  accelerator="Ctrl+O")
file_menu.add_command(label="Save",  command=save_file,  accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit",  command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut",        command=cut,        accelerator="Ctrl+X")
edit_menu.add_command(label="Copy",       command=copy,       accelerator="Ctrl+C")
edit_menu.add_command(label="Paste",      command=paste,      accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
menubar.add_cascade(label="Edit", menu=edit_menu)

view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Increase Font Size", command=increase_font)
view_menu.add_command(label="Decrease Font Size", command=decrease_font)
menubar.add_cascade(label="View", menu=view_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Keyboard shortcuts
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())
root.bind("<Control-a>", lambda e: select_all())

# Text area with scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
text_area = tk.Text(frame, font=("Consolas", 12), wrap=tk.NONE,
                    yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set,
                    undo=True, relief="flat", padx=5, pady=5)
scrollbar_y.config(command=text_area.yview)
scrollbar_x.config(command=text_area.xview)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")
text_area.pack(fill="both", expand=True)

# Status bar
status_bar = tk.Label(root, text="Ready", anchor="w", font=("Arial", 9),
                      bg="#ecf0f1", fg="#7f8c8d", relief="flat", padx=5)
status_bar.pack(fill="x", side="bottom")

def update_status(event=None):
    line, col = text_area.index(tk.INSERT).split(".")
    status_bar.config(text=f"Line: {line}  Column: {int(col)+1}")

text_area.bind("<KeyRelease>", update_status)
text_area.bind("<ButtonRelease>", update_status)

root.mainloop()
