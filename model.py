import fitz
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_experience(text):
    matches = re.findall(r'(\d+)\s*(years|yrs)', text.lower())
    years = [int(m[0]) for m in matches]
    return max(years) if years else 0

def skill_score(jd, resume):
    skills = ["python","java","sql","machine learning","deep learning","nlp","flask","react"]

    jd_skills = [s for s in skills if s in jd.lower()]
    res_skills = [s for s in skills if s in resume.lower()]

    if not jd_skills:
        return 0

    return len(set(jd_skills) & set(res_skills)) / len(jd_skills)

def highlight_keywords(text, jd):
    words = set(jd.lower().split())
    return " ".join([f"**{w}**" if w.lower() in words else w for w in text.split()][:300])

def compute_advanced_scores(jd, resumes):

    jd_emb = model.encode([jd])
    res_emb = model.encode(resumes)

    semantic_scores = cosine_similarity(jd_emb, res_emb)[0]

    final_scores = []
    breakdown = []

    for i, res in enumerate(resumes):

        skill = skill_score(jd, res)
        exp = extract_experience(res)
        exp_score = min(exp / 10, 1)

        final = 0.6*semantic_scores[i] + 0.25*skill + 0.15*exp_score

        final_scores.append(final)

        breakdown.append({
            "semantic": round(semantic_scores[i],2),
            "skill": round(skill,2),
            "experience": exp
        })

    return final_scores, breakdown