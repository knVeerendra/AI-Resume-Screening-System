from backend.services.embedding import compute_similarity
import re

# -------- DECISION -------- #
def get_decision(score):
    if score >= 75:
        return "Strong Match"
    elif score >= 50:
        return "Moderate Match"
    return "Weak Match"


# -------- SKILL DICTIONARY -------- #
SKILLS = {
    # Programming
    "python", "java", "c++", "c", "javascript", "typescript",

    # ML / AI
    "machine learning", "deep learning", "nlp", "computer vision",
    "data science", "artificial intelligence",

    # Libraries
    "pytorch", "tensorflow", "scikit-learn", "keras",
    "pandas", "numpy", "matplotlib", "seaborn",

    # Backend
    "flask", "fastapi", "django", "rest api", "api development",

    # Databases
    "mysql", "postgresql", "mongodb", "sqlite",

    # Tools
    "docker", "kubernetes", "git", "github",

    # Cloud
    "aws", "azure", "gcp",

    # Data Engineering
    "spark", "hadoop", "etl",

    # DevOps
    "ci/cd", "jenkins",

    # OS
    "linux", "bash"
}


# -------- CLEAN TEXT -------- #
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


# -------- SKILL EXTRACTION -------- #
def extract_skills(text):
    text = clean_text(text)
    found = set()

    for skill in SKILLS:
        if skill in text:
            found.add(skill)

    return found


# -------- EXPERIENCE ESTIMATION (simple heuristic) -------- #
def estimate_experience(text):
    matches = re.findall(r'(\d+)\+?\s*(years|yrs)', text.lower())
    if matches:
        return max([int(m[0]) for m in matches])
    return 0


# -------- MAIN FUNCTION -------- #
def rank_resume(resume_text, job_desc):

    if not resume_text or not job_desc:
        return {"error": "Missing input"}

    if not resume_text.strip():
        return {"error": "Empty resume text"}

    # -------- Semantic Matching -------- #
    semantic_score = compute_similarity(resume_text, job_desc)

    # -------- Skill Matching -------- #
    job_skills = extract_skills(job_desc)
    resume_skills = extract_skills(resume_text)

    matched = list(job_skills & resume_skills)
    missing = list(job_skills - resume_skills)

    # Stronger skill influence
    skill_score = len(matched) / (len(job_skills) + 1)

    # -------- Experience Matching -------- #
    job_exp = estimate_experience(job_desc)
    resume_exp = estimate_experience(resume_text)

    if job_exp == 0:
        exp_score = 1
    else:
        exp_score = min(resume_exp / job_exp, 1)

    # -------- FINAL SCORE (IMPROVED WEIGHTS) -------- #
    final_score = (
        0.5 * semantic_score +
        0.3 * skill_score +
        0.2 * exp_score
    )

    final_percent = final_score * 100

    return {
        "final_score": float(round(final_percent, 2)),
        "semantic_score": float(round(semantic_score * 100, 2)),
        "skill_score": float(round(skill_score * 100, 2)),
        "experience_score": float(round(exp_score * 100, 2)),
        "decision": get_decision(final_percent),
        "matched_skills": matched,
        "missing_skills": missing
    }