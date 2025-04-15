# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from generator import get_available_roles, get_questions_for_role
from resume_parser import detect_role_from_resume


class InterviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Interview Buddy")
        self.root.geometry("700x600")

        # Heading
        heading = tk.Label(root, text="Job Interview Buddy", font=("Arial", 18, "bold"))
        heading.pack(pady=10)

        # Role Selection Section
        self.role_var = tk.StringVar()
        role_label = tk.Label(root, text="🔘 Option 1: Select a role")
        role_label.pack()
        self.role_dropdown = ttk.Combobox(root, textvariable=self.role_var, state="readonly")
        self.role_dropdown['values'] = get_available_roles()
        self.role_dropdown.pack(pady=5)

        generate_button = tk.Button(root, text="Generate Questions (From Role)",
                                    command=self.generate_questions_from_role)
        generate_button.pack(pady=5)

        # Separator
        separator = ttk.Separator(root, orient='horizontal')
        separator.pack(fill='x', pady=10)

        # Resume Paste Mode
        resume_label = tk.Label(root, text="📝 Option 2: Paste your resume text")
        resume_label.pack()
        self.resume_text = tk.Text(root, height=10, wrap='word')
        self.resume_text.pack(padx=10, pady=5, fill=tk.X)

        resume_button = tk.Button(root, text="Detect Role & Generate Questions", command=self.generate_from_resume)
        resume_button.pack(pady=5)

        # Another Separator
        separator2 = ttk.Separator(root, orient='horizontal')
        separator2.pack(fill='x', pady=10)

        # Output Text Box
        output_label = tk.Label(root, text="🎯 Interview Questions")
        output_label.pack()
        self.text_box = tk.Text(root, wrap="word", height=15)
        self.text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def generate_questions_from_role(self):
        selected_role = self.role_var.get()
        if not selected_role:
            messagebox.showwarning("No role selected", "Please select a role first.")
            return
        self.display_questions(selected_role)

    def generate_from_resume(self):
        resume_input = self.resume_text.get("1.0", tk.END).strip()
        if not resume_input:
            messagebox.showwarning("No resume input", "Please paste your resume first.")
            return
        detected_role = detect_role_from_resume(resume_input)
        if not detected_role:
            messagebox.showinfo("No match", "Could not detect a role from your resume.")
            return
        messagebox.showinfo("Role Detected", f"We detected your role as: {detected_role}")
        self.display_questions(detected_role)

    def display_questions(self, role):
        questions = get_questions_for_role(role)
        self.text_box.delete("1.0", tk.END)
        for i, q in enumerate(questions, 1):
            self.text_box.insert(tk.END, f"{i}. {q}\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterviewApp(root)
    root.mainloop()
