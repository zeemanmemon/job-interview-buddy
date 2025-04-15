# resume_parser.py

ROLE_KEYWORDS = {
    "Software Engineer": ["python", "java", "c++", "git", "api", "backend", "frontend", "oop"],
    "Data Analyst": ["excel", "sql", "python", "tableau", "power bi", "data cleaning", "visualization"],
    "Product Manager": ["roadmap", "stakeholders", "user stories", "sprint", "agile", "prioritize", "product"],
    "Project Manager": ["pmi", "project", "timeline", "budget", "milestones", "agile", "risk", "scrum"],
    "Cybersecurity Analyst": ["firewall", "network", "threat", "malware", "vulnerability", "security", "incident", "splunk"],
    "Ux Designer": ["wireframe", "prototype", "figma", "sketch", "design system", "usability", "user testing", "ui"]
}


def detect_role_from_resume(resume_text):
    text = resume_text.lower()
    scores = {}

    for role, keywords in ROLE_KEYWORDS.items():
        match_count = sum(1 for keyword in keywords if keyword in text)
        scores[role] = match_count

    # Sort by match count and return highest if found
    best_match = max(scores, key=scores.get)
    if scores[best_match] == 0:
        return None
    return best_match
