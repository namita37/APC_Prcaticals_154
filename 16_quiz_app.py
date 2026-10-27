# 16 - Quiz Application

import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the output of print(type([]))?",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": 1
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["2", "4", "3", "1"],
        "answer": 2
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": ["tuple", "string", "list", "int"],
        "answer": 2
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": 2
    },
]

class QuizApp:
    def __init__(self, root):
        self.root  = root
        self.root.title("Python Quiz")
        self.root.geometry("540x440")
        self.root.configure(bg="#1a252f")
        self.root.resizable(False, False)

        self.index  = 0
        self.score  = 0
        self.selected = tk.IntVar(value=-1)

        # Header
        self.header = tk.Label(root, text="🐍 Python Quiz", font=("Arial", 18, "bold"),
                               bg="#1a252f", fg="#f1c40f")
        self.header.pack(pady=12)

        # Progress
        self.progress_label = tk.Label(root, text="", font=("Arial", 11),
                                       bg="#1a252f", fg="#bdc3c7")
        self.progress_label.pack()

        # Question
        self.q_label = tk.Label(root, text="", font=("Arial", 13),
                                bg="#2c3e50", fg="white", wraplength=480,
                                justify="left", padx=20, pady=20, relief="flat")
        self.q_label.pack(fill="x", padx=30, pady=10)

        # Options frame
        self.opt_frame = tk.Frame(root, bg="#1a252f")
        self.opt_frame.pack(padx=30, fill="x")
        self.option_btns = []
        for i in range(4):
            btn = tk.Radiobutton(self.opt_frame, text="", variable=self.selected,
                                 value=i, font=("Arial", 12), bg="#1a252f", fg="white",
                                 selectcolor="#2c3e50", activebackground="#1a252f",
                                 activeforeground="white", anchor="w", cursor="hand2")
            btn.pack(fill="x", pady=3)
            self.option_btns.append(btn)

        # Feedback
        self.feedback = tk.Label(root, text="", font=("Arial", 11, "bold"),
                                 bg="#1a252f", fg="white")
        self.feedback.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1a252f")
        btn_frame.pack(pady=8)
        self.next_btn = tk.Button(btn_frame, text="Next ➡", command=self.next_question,
                                  font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                                  padx=18, pady=7, relief="flat", cursor="hand2")
        self.next_btn.grid(row=0, column=0, padx=10)

        self.quit_btn = tk.Button(btn_frame, text="Quit", command=root.destroy,
                                  font=("Arial", 12), bg="#e74c3c", fg="white",
                                  padx=18, pady=7, relief="flat", cursor="hand2")
        self.quit_btn.grid(row=0, column=1, padx=10)

        self.load_question()

    def load_question(self):
        self.selected.set(-1)
        self.feedback.config(text="")
        q = questions[self.index]
        self.progress_label.config(text=f"Question {self.index + 1} of {len(questions)}  |  Score: {self.score}")
        self.q_label.config(text=f"Q{self.index+1}. {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.option_btns[i].config(text=f"  {chr(65+i)}.  {opt}", fg="white")
        self.next_btn.config(text="Next ➡" if self.index < len(questions)-1 else "Finish 🏁")

    def next_question(self):
        ans = self.selected.get()
        if ans == -1:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return
        correct = questions[self.index]["answer"]
        if ans == correct:
            self.score += 1
            self.feedback.config(text="✅ Correct!", fg="#2ecc71")
            self.option_btns[ans].config(fg="#2ecc71")
        else:
            self.feedback.config(text=f"❌ Wrong! Correct: {chr(65+correct)}. {questions[self.index]['options'][correct]}", fg="#e74c3c")
            self.option_btns[ans].config(fg="#e74c3c")
            self.option_btns[correct].config(fg="#2ecc71")

        self.root.after(1200, self.advance)

    def advance(self):
        self.index += 1
        if self.index < len(questions):
            self.load_question()
        else:
            pct = (self.score / len(questions)) * 100
            grade = "Excellent! 🏆" if pct >= 80 else "Good! 👍" if pct >= 60 else "Keep Practising! 📚"
            messagebox.showinfo("Quiz Finished",
                                f"Quiz Complete!\n\nScore : {self.score}/{len(questions)}\n"
                                f"Percentage : {pct:.0f}%\nResult : {grade}")
            self.root.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
