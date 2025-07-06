import tkinter as tk
import string

def check_password(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters.")
    if not any(c.islower() for c in password):
        feedback.append("Add at least one lowercase letter.")
    if not any(c.isupper() for c in password):
        feedback.append("Add at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        feedback.append("Add at least one digit.")
    if not any(c in string.punctuation for c in password):
        feedback.append("Add at least one special character (e.g., !, @, #, etc.).")
    if not feedback:
        return "Strong password!", "green"
    else:
        return "\n".join(feedback), "red"

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()
entry.bind("<Return>", lambda event: show_feedback())

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

def show_feedback(event=None):
    pwd = entry.get()
    result, color = check_password(pwd)
    feedback_label.config(text=result, fg=color)

tk.Button(root, text="Check Strength", command=show_feedback, font=("Arial", 12)).pack(pady=10)

root.mainloop()