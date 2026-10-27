# 11 - Canvas Drawing Shapes

import tkinter as tk

root = tk.Tk()
root.title("Canvas - Drawing Shapes")
root.geometry("600x500")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

tk.Label(root, text="🎨 Canvas Drawing Demo", font=("Arial", 15, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=8)

# Canvas
canvas = tk.Canvas(root, width=560, height=370, bg="white",
                   relief="solid", bd=1, highlightthickness=0)
canvas.pack(padx=20, pady=5)

def draw_all():
    canvas.delete("all")

    # Rectangle
    canvas.create_rectangle(30, 30, 160, 110, fill="#3498db", outline="#2980b9", width=2)
    canvas.create_text(95, 70, text="Rectangle", fill="white", font=("Arial", 11, "bold"))

    # Oval
    canvas.create_oval(200, 30, 360, 120, fill="#e74c3c", outline="#c0392b", width=2)
    canvas.create_text(280, 75, text="Oval", fill="white", font=("Arial", 11, "bold"))

    # Triangle (Polygon)
    canvas.create_polygon(420, 115, 480, 25, 540, 115, fill="#27ae60", outline="#1e8449", width=2)
    canvas.create_text(480, 85, text="Triangle", fill="white", font=("Arial", 10, "bold"))

    # Line
    canvas.create_line(30, 160, 180, 160, fill="#8e44ad", width=4, arrow=tk.LAST)
    canvas.create_text(105, 145, text="Arrow Line", fill="#8e44ad", font=("Arial", 10, "bold"))

    # Arc
    canvas.create_arc(200, 140, 360, 220, start=0, extent=270,
                      fill="#f39c12", outline="#d68910", width=2)
    canvas.create_text(280, 185, text="Arc", fill="white", font=("Arial", 10, "bold"))

    # Star (Polygon)
    import math
    cx, cy, r_outer, r_inner, points = 480, 185, 45, 20, 5
    coords = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        angle = math.pi / points * i - math.pi / 2
        coords += [cx + r * math.cos(angle), cy + r * math.sin(angle)]
    canvas.create_polygon(coords, fill="#e67e22", outline="#d35400", width=2)
    canvas.create_text(480, 185, text="★", fill="white", font=("Arial", 14, "bold"))

    # Text
    canvas.create_text(95, 260, text="Hello, Canvas!", fill="#2c3e50",
                       font=("Arial", 14, "bold italic"))

    # Circle (filled)
    canvas.create_oval(200, 235, 300, 310, fill="#16a085", outline="#0e6655", width=2)
    canvas.create_text(250, 272, text="Circle", fill="white", font=("Arial", 10, "bold"))

    # Dashed Rectangle
    canvas.create_rectangle(330, 235, 545, 310, dash=(8, 4),
                             outline="#e74c3c", width=2)
    canvas.create_text(437, 272, text="Dashed Border", fill="#e74c3c", font=("Arial", 10, "bold"))

    # Grid lines
    for x in range(0, 561, 70):
        canvas.create_line(x, 340, x, 370, fill="#bdc3c7", width=1)
    for y in range(340, 371, 15):
        canvas.create_line(0, y, 560, y, fill="#bdc3c7", width=1)
    canvas.create_text(280, 355, text="Grid Pattern", fill="#7f8c8d", font=("Arial", 9))

draw_all()

btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Redraw", command=draw_all, font=("Arial", 11),
          bg="#3498db", fg="white", padx=14, pady=5, relief="flat", cursor="hand2").grid(row=0, column=0, padx=8)
tk.Button(btn_frame, text="Clear",  command=lambda: canvas.delete("all"), font=("Arial", 11),
          bg="#95a5a6", fg="white", padx=14, pady=5, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)
tk.Button(btn_frame, text="Exit",   command=root.destroy, font=("Arial", 11),
          bg="#e74c3c", fg="white", padx=14, pady=5, relief="flat", cursor="hand2").grid(row=0, column=2, padx=8)

root.mainloop()
