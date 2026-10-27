# 17 - Digital Clock and Stopwatch

import tkinter as tk
import time

root = tk.Tk()
root.title("Clock & Stopwatch")
root.geometry("440x380")
root.configure(bg="#1a252f")
root.resizable(False, False)

# ---- DIGITAL CLOCK ----
clock_frame = tk.LabelFrame(root, text=" 🕐 Digital Clock ", font=("Arial", 11, "bold"),
                             bg="#1a252f", fg="#f1c40f", padx=10, pady=10)
clock_frame.pack(fill="x", padx=20, pady=12)

time_label = tk.Label(clock_frame, text="", font=("Courier", 38, "bold"),
                      bg="#1a252f", fg="#2ecc71")
time_label.pack()

date_label = tk.Label(clock_frame, text="", font=("Arial", 13),
                      bg="#1a252f", fg="#bdc3c7")
date_label.pack()

def update_clock():
    now = time.localtime()
    time_label.config(text=time.strftime("%H : %M : %S", now))
    date_label.config(text=time.strftime("%A, %d %B %Y", now))
    root.after(1000, update_clock)

update_clock()

# ---- STOPWATCH ----
sw_frame = tk.LabelFrame(root, text=" ⏱ Stopwatch ", font=("Arial", 11, "bold"),
                          bg="#1a252f", fg="#f1c40f", padx=10, pady=10)
sw_frame.pack(fill="x", padx=20, pady=5)

sw_running    = False
sw_elapsed    = 0.0
sw_start_time = 0.0

sw_display = tk.Label(sw_frame, text="00 : 00 . 00", font=("Courier", 30, "bold"),
                      bg="#1a252f", fg="#e74c3c")
sw_display.pack()

def format_time(elapsed):
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    centiseconds = int((elapsed % 1) * 100)
    return f"{minutes:02d} : {seconds:02d} . {centiseconds:02d}"

def update_stopwatch():
    if sw_running:
        elapsed = sw_elapsed + (time.time() - sw_start_time)
        sw_display.config(text=format_time(elapsed))
        root.after(10, update_stopwatch)

def start_stop():
    global sw_running, sw_start_time, sw_elapsed
    if not sw_running:
        sw_start_time = time.time()
        sw_running = True
        start_btn.config(text="⏸ Pause", bg="#e67e22")
        update_stopwatch()
    else:
        sw_elapsed += time.time() - sw_start_time
        sw_running = False
        start_btn.config(text="▶ Start", bg="#27ae60")

def reset_sw():
    global sw_running, sw_elapsed
    sw_running = False
    sw_elapsed = 0.0
    start_btn.config(text="▶ Start", bg="#27ae60")
    sw_display.config(text="00 : 00 . 00")

sw_btn_frame = tk.Frame(sw_frame, bg="#1a252f")
sw_btn_frame.pack(pady=8)
start_btn = tk.Button(sw_btn_frame, text="▶ Start", command=start_stop,
                      font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                      padx=14, pady=6, relief="flat", cursor="hand2")
start_btn.grid(row=0, column=0, padx=8)

tk.Button(sw_btn_frame, text="↺ Reset", command=reset_sw,
          font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
          padx=14, pady=6, relief="flat", cursor="hand2").grid(row=0, column=1, padx=8)

root.mainloop()
