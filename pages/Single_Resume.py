import streamlit as st
from model import extract_text, compute_advanced_scores, highlight_keywords

st.set_page_config(page_title="Single Resume", layout="wide")

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
col1.title("📄 Single Resume Analysis")
if col2.button("⬅ Home"):
    st.switch_page("app.py")

# -------- INPUT -------- #
jd = st.text_area(
    "Job Description",
    height=150,
    placeholder="Enter job requirements..."
)

file = st.file_uploader("Upload Resume")

run = st.button(" Analyze Resume", use_container_width=True)

# -------- OUTPUT -------- #
if run and jd and file:

    text = extract_text(file)
    scores, breakdown = compute_advanced_scores(jd, [text])

    score = float(scores[0])
    info = breakdown[0]

    c1, c2, c3 = st.columns(3)
    c1.metric("Score", f"{score*100:.1f}%")
    c2.metric("Skill Match", info["skill"])
    c3.metric("Experience", f"{info['experience']} yrs")

    st.progress(score)

    st.markdown("### Resume Preview")
    st.markdown(highlight_keywords(text, jd))

elif run:
    st.warning("Provide inputs")
