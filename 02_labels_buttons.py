# 02 - Labels and Buttons Demo

import tkinter as tk

def change_text():
    label.config(text="Button was Clicked!", fg="#27ae60")

def reset_text():
    label.config(text="Hello, Tkinter!", fg="#2c3e50")

def change_color():
    current = root.cget("bg")
    root.configure(bg="#dfe6e9" if current == "#f0f4f8" else "#f0f4f8")
    label.configure(bg=root.cget("bg"))
    btn_frame.configure(bg=root.cget("bg"))

root = tk.Tk()
root.title("Labels and Buttons")
root.geometry("420x300")
root.configure(bg="#f0f4f8")

# Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20, "bold"),
                 bg="#f0f4f8", fg="#2c3e50", pady=30)
label.pack()

# Button frame
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Click Me",    command=change_text,  font=("Arial", 11),
          bg="#3498db", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").grid(row=0, column=0, padx=8)

tk.Button(btn_frame, text="Reset",       command=reset_text,   font=("Arial", 11),
          bg="#95a5a6", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)

tk.Button(btn_frame, text="Toggle BG",   command=change_color, font=("Arial", 11),
          bg="#9b59b6", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").grid(row=0, column=2, padx=8)

tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 11),
          bg="#e74c3c", fg="white", padx=12, pady=6, relief="flat", cursor="hand2").pack(pady=20)

root.mainloop()
