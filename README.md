Job Interview Buddy 🧠💼
========================

A simple Python desktop app that helps you prepare for interviews by generating role-based questions. Choose your job role from a dropdown or paste your resume — and get instant, relevant questions to practice!

Features
--------

* 🔘 Select a job role and get curated interview questions
* 📝 Paste your resume to auto-detect your role
* 🎯 Personalized question sets by profession
* 💡 Lightweight and works offline (no GPT or internet needed)

Project Structure
-----------------

job-interview-buddy/
├── main.py                 # GUI logic
├── generator.py            # Loads questions by role
├── resume_parser.py        # Detects role from pasted resume
├── prompts/                # Folder with role-based question sets
│   ├── software_engineer.txt
│   ├── data_analyst.txt
│   ├── product_manager.txt
│   └── ...more roles
├── README.md
└── requirements.txt
  

How to Run
----------

1.  **Clone this repo**
2.  (Optional) Create a virtual environment:
    
        python -m venv venv
        source venv/bin/activate  # Windows: venv\Scripts\activate
    
3.  **Install any dependencies**
    
        pip install -r requirements.txt
    
4.  **Run the app**
    
        python main.py
    

Add/Edit Question Sets
----------------------

To add new role-based question sets, simply add new `.txt` files inside the `prompts/` folder.  
**File name format:** `role_name.txt` (use underscores for spaces, lowercase).

Example file: `prompts/project_manager.txt`

How do you prioritize tasks in a project?
How do you manage scope creep?
...
  

Also, update the keyword matcher in `resume_parser.py` to include your new roles.

Credits
-------

Made with ❤️ by Zeeman Memon
