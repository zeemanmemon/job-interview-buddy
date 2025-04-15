# generator.py

import os

PROMPT_DIR = "prompts"

def get_available_roles():
    files = os.listdir(PROMPT_DIR)
    roles = [os.path.splitext(file)[0].replace("_", " ").title() for file in files if file.endswith(".txt")]
    return roles

def get_questions_for_role(role):
    filename = role.lower().replace(" ", "_") + ".txt"
    path = os.path.join(PROMPT_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            questions = f.read().strip().split("\n")
            return questions
    except FileNotFoundError:
        return ["No questions found for this role."]
