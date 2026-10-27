# 01 - Basic Window Creation using Tkinter

import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter Window")

# Set window size (width x height)
root.geometry("400x300")

# Set background color
root.configure(bg="#f0f4f8")

# Add a Label widget
label = tk.Label(
    root,
    text="Welcome to Tkinter GUI!",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
label.pack(pady=60)

# Add a sub-label
sub_label = tk.Label(
    root,
    text="This is your first Python GUI window.",
    font=("Arial", 11),
    bg="#f0f4f8",
    fg="#7f8c8d"
)
sub_label.pack()

# Add a Quit button
quit_btn = tk.Button(
    root,
    text="Close Window",
    command=root.destroy,
    font=("Arial", 11),
    bg="#e74c3c",
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
    cursor="hand2"
)
quit_btn.pack(pady=40)

# Start the event loop
root.mainloop()
