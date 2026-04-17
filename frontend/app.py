import streamlit as st

st.set_page_config(page_title="AI Resume Screening", layout="wide")

st.title("AI Resume Screening System")

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Single Resume Analysis", use_container_width=True):
        st.switch_page("pages/Single_Resume.py")

with col2:
    if st.button("📂 Bulk Resume Screening", use_container_width=True):
        st.switch_page("pages/Bulk_Resume.py")