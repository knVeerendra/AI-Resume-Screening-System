import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Single Resume Analysis")

# -------- JOB DESCRIPTION -------- #
job_desc = st.text_area("Enter Job Description")

if st.button("Submit Job Description"):
    res = requests.post(f"{API}/upload_job", params={"desc": job_desc})
    if res.status_code == 200:
        st.success("Job description stored")
    else:
        st.error(res.text)

# -------- FILE UPLOAD -------- #
file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if file:
    if st.button("Analyze Resume"):

        try:
            res = requests.post(
                f"{API}/rank_candidate",
                files={"file": (file.name, file, "application/pdf")}
            )

            # Debug info
            print("STATUS:", res.status_code)
            print("RESPONSE:", res.text)

            if res.status_code == 200:
                data = res.json()

                st.metric("Final Score", f"{data['final_score']}%")
                st.metric("Decision", data["decision"])

                st.subheader("✅ Matched Skills")
                st.write(data["matched_skills"])

                st.subheader("❌ Missing Skills")
                st.write(data["missing_skills"])

            else:
                st.error(f"Backend Error: {res.text}")

        except Exception as e:
            st.error(f"Request Failed: {str(e)}")