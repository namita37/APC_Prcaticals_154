# 15 - Simple Paint / Drawing App using Canvas

import tkinter as tk
from tkinter import colorchooser, messagebox

root = tk.Tk()
root.title("🎨 Simple Paint App")
root.geometry("700x540")
root.configure(bg="#2c3e50")
root.resizable(False, False)

# Drawing state
draw_color  = "#000000"
brush_size  = 5
last_x = last_y = None
draw_mode   = tk.StringVar(value="pen")

def get_color():
    global draw_color
    color = colorchooser.askcolor(title="Pick Color", color=draw_color)
    if color[1]:
        draw_color = color[1]
        color_btn.config(bg=draw_color)

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    mode = draw_mode.get()
    size = brush_size_scale.get()

    if mode == "pen":
        canvas.create_line(last_x, last_y, event.x, event.y,
                           fill=draw_color, width=size, capstyle=tk.ROUND, smooth=True)
        last_x, last_y = event.x, event.y
    elif mode == "eraser":
        canvas.create_oval(event.x - size, event.y - size,
                           event.x + size, event.y + size,
                           fill="white", outline="white")
        last_x, last_y = event.x, event.y

def draw_shape(event):
    global last_x, last_y
    mode = draw_mode.get()
    size = brush_size_scale.get()
    if mode == "circle":
        canvas.create_oval(event.x - size*3, event.y - size*3,
                           event.x + size*3, event.y + size*3,
                           outline=draw_color, width=2)
    elif mode == "rect":
        canvas.create_rectangle(last_x, last_y, event.x, event.y,
                                 outline=draw_color, width=2)

def clear_canvas():
    canvas.delete("all")

def fill_bg():
    canvas.configure(bg=draw_color)

# ---- Toolbar ----
toolbar = tk.Frame(root, bg="#34495e", pady=5)
toolbar.pack(fill="x")

tk.Label(toolbar, text="Mode:", font=("Arial", 10), bg="#34495e", fg="white").pack(side="left", padx=8)
modes = [("Pen", "pen"), ("Eraser", "eraser"), ("Circle", "circle"), ("Rectangle", "rect")]
for label, val in modes:
    tk.Radiobutton(toolbar, text=label, variable=draw_mode, value=val,
                   font=("Arial", 10), bg="#34495e", fg="white",
                   selectcolor="#2c3e50", activebackground="#34495e",
                   activeforeground="white", cursor="hand2").pack(side="left", padx=5)

tk.Label(toolbar, text="  Size:", font=("Arial", 10), bg="#34495e", fg="white").pack(side="left", padx=5)
brush_size_scale = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL,
                             bg="#34495e", fg="white", troughcolor="#3498db",
                             highlightthickness=0, length=100)
brush_size_scale.set(5)
brush_size_scale.pack(side="left")

color_btn = tk.Button(toolbar, text="  Color  ", command=get_color,
                      bg=draw_color, fg="white", font=("Arial", 10, "bold"),
                      relief="flat", padx=6, cursor="hand2")
color_btn.pack(side="left", padx=10)

tk.Button(toolbar, text="Clear", command=clear_canvas,
          bg="#e74c3c", fg="white", font=("Arial", 10),
          relief="flat", padx=8, cursor="hand2").pack(side="left", padx=4)

tk.Button(toolbar, text="Fill BG", command=fill_bg,
          bg="#8e44ad", fg="white", font=("Arial", 10),
          relief="flat", padx=8, cursor="hand2").pack(side="left", padx=4)

# ---- Canvas ----
canvas = tk.Canvas(root, bg="white", cursor="crosshair",
                   highlightthickness=0)
canvas.pack(fill="both", expand=True, padx=10, pady=8)

canvas.bind("<ButtonPress-1>",  start_draw)
canvas.bind("<B1-Motion>",      draw)
canvas.bind("<ButtonRelease-1>", draw_shape)

# Status bar
status = tk.Label(root, text="Draw on the canvas. Use toolbar to switch modes.",
                  font=("Arial", 9), bg="#2c3e50", fg="#bdc3c7", anchor="w", padx=10)
status.pack(fill="x")

def update_status(event):
    status.config(text=f"X: {event.x}  Y: {event.y}  | Mode: {draw_mode.get()} | Size: {brush_size_scale.get()}")

canvas.bind("<Motion>", update_status)

root.mainloop()
