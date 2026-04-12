import streamlit as st

st.set_page_config(page_title="AI Resume Screening", layout="wide")

# -------- SESSION STATE -------- #
if "started" not in st.session_state:
    st.session_state.started = False

# -------- STYLE -------- #
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}

.hero {
    text-align: center;
    margin-top: 60px;
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    color: #1e293b;
}

.hero-sub {
    font-size: 18px;
    color: gray;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    height: 45px;
    font-weight: 600;
    border: none;
}

/* CARD */
.card {
    background: #ffffff;
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    transition: 0.3s;
    margin-bottom: 10px;
}

.card:hover {
    transform: translateY(-5px);
}

/* SECTION TITLE */
.section-title {
    text-align: center;
    font-size: 28px;
    margin-top: 40px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------- HERO -------- #
st.markdown("""
<div class="hero">
    <div class="hero-title"> AI Resume Screening</div>
    <div class="hero-sub">Smart AI-powered candidate ranking system</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------- STEP 1 -------- #
if not st.session_state.started:

    center = st.columns([1,2,1])[1]

    with center:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.started = True
            st.rerun()

# -------- STEP 2 -------- #
else:

    st.markdown('<div class="section-title">Select Workflow</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    # -------- SINGLE -------- #
    with col1:
        st.markdown("""
        <div class="card">
            <h3>📄 Individual Resume Evaluation</h3>
            <p>Perform detailed analysis on a single candidate profile.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Start Individual Analysis", use_container_width=True):
            st.switch_page("pages/Single_Resume.py")

    # -------- BULK -------- #
    with col2:
        st.markdown("""
        <div class="card">
            <h3>📂 Bulk Candidate Screening</h3>
            <p>Process multiple resumes and generate ranked insights.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Initiate Bulk Screening", use_container_width=True):
            st.switch_page("pages/Bulk_Resume.py")