# 04 - Simple Calculator

import tkinter as tk
from tkinter import messagebox

def button_click(value):
    current = display_var.get()
    if value == "C":
        display_var.set("")
    elif value == "⌫":
        display_var.set(current[:-1])
    elif value == "=":
        try:
            result = eval(current)
            # Format: remove trailing zeros for floats
            if isinstance(result, float) and result == int(result):
                result = int(result)
            display_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            display_var.set("")
        except Exception:
            messagebox.showerror("Error", "Invalid expression!")
            display_var.set("")
    else:
        display_var.set(current + str(value))

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#2c3e50")
root.resizable(False, False)

display_var = tk.StringVar()

# Display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 22, "bold"),
                   justify="right", bd=0, bg="#34495e", fg="white",
                   insertbackground="white", relief="flat")
display.pack(fill="x", padx=15, pady=(20, 10), ipady=14)

# Button layout
buttons = [
    ["C",  "⌫",  "%",  "/"],
    ["7",  "8",  "9",  "*"],
    ["4",  "5",  "6",  "-"],
    ["1",  "2",  "3",  "+"],
    ["00", "0",  ".",  "="],
]

btn_colors = {
    "=": "#27ae60", "C": "#e74c3c", "⌫": "#e67e22",
    "/": "#8e44ad", "*": "#8e44ad", "-": "#8e44ad", "+": "#8e44ad", "%": "#8e44ad",
}

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(padx=15, pady=5, fill="both", expand=True)

for row_vals in buttons:
    row_frame = tk.Frame(btn_frame, bg="#2c3e50")
    row_frame.pack(fill="x", pady=3)
    for val in row_vals:
        color = btn_colors.get(val, "#ecf0f1")
        fg    = "white" if val in btn_colors else "#2c3e50"
        tk.Button(row_frame, text=val,
                  command=lambda v=val: button_click(v),
                  font=("Arial", 14, "bold"),
                  bg=color, fg=fg,
                  width=5, height=2,
                  relief="flat", cursor="hand2",
                  activebackground="#bdc3c7").pack(side="left", padx=3)

root.mainloop()
