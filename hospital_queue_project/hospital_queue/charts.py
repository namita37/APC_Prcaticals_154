import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def show_patient_charts(parent, dataframe):
    if dataframe.empty:
        return False
    departments = dataframe["department"].value_counts().sort_values(ascending=False)
    doctors = dataframe["doctor"].fillna("Unassigned").replace("", "Unassigned").value_counts().sort_values(ascending=False)
    window = tk.Toplevel(parent)
    window.title("Patient counts by department and doctor")
    window.geometry("1050x600")
    figure = Figure(figsize=(10, 5.4), dpi=100, facecolor="white")
    ax_department = figure.add_subplot(1, 2, 1)
    ax_doctor = figure.add_subplot(1, 2, 2)
    departments.plot(kind="bar", ax=ax_department, color="#1677c8")
    doctors.plot(kind="bar", ax=ax_doctor, color="#18a078")
    ax_department.set_title("Patients by Department")
    ax_doctor.set_title("Patients by Doctor")
    for axis in (ax_department, ax_doctor):
        axis.set_ylabel("Number of patients")
        axis.tick_params(axis="x", labelrotation=35)
        axis.grid(axis="y", linestyle="--", alpha=0.3)
        axis.set_axisbelow(True)
    figure.tight_layout()
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=12, pady=12)
    window.protocol("WM_DELETE_WINDOW", lambda: (plt.close(figure), window.destroy()))
    return True
