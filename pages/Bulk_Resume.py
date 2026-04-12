import streamlit as st
import pandas as pd
from model import extract_text, compute_advanced_scores, highlight_keywords

st.set_page_config(page_title="Bulk Resume", layout="wide")

# -------- STYLE -------- #
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}

textarea {
    background-color:#f8fafc !important;
    border-radius:10px !important;
}

[data-testid="stFileUploader"] {
    background:#f8fafc;
    padding:10px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# -------- HEADER -------- #
col1, col2 = st.columns([6,1])
col1.title("📂 Bulk Resume Screening")
if col2.button("⬅ Home"):
    st.switch_page("app.py")

# -------- INPUT -------- #
jd = st.text_area(
    "Job Description",
    height=150,
    placeholder="Enter job requirements..."
)

files = st.file_uploader(
    "Upload Resumes",
    accept_multiple_files=True
)

top_n = st.slider("Top Candidates", 1, 20, 5)

run = st.button("🚀 Analyze Candidates", use_container_width=True)

# -------- OUTPUT -------- #
if run and jd and files:

    resumes = [extract_text(f) for f in files]
    scores, breakdown = compute_advanced_scores(jd, resumes)

    results = sorted(
        zip(files, resumes, scores, breakdown),
        key=lambda x: x[2],
        reverse=True
    )[:top_n]

    df = pd.DataFrame({
        "Candidate":[f.name for f,_,_,_ in results],
        "Score":[float(s) for _,_,s,_ in results]
    })

    st.bar_chart(df.set_index("Candidate"))

    for i,(file,text,score,info) in enumerate(results):

        score = float(score)

        if i == 0:
            st.markdown("### 🏆 Best Candidate")

        st.write(f"**{file.name}**")

        c1,c2,c3 = st.columns(3)
        c1.metric("Score", f"{score*100:.1f}%")
        c2.metric("Skill Match", info["skill"])
        c3.metric("Experience", f"{info['experience']} yrs")

        st.progress(score)
        st.markdown(highlight_keywords(text, jd))

elif run:
    st.warning("Provide inputs")