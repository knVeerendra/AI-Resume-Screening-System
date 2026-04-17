import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Bulk Resume Screening")

# -------- JOB DESCRIPTION -------- #
job_desc = st.text_area("Enter Job Description")

if st.button("Submit Job Description"):
    res = requests.post(f"{API}/upload_job", params={"desc": job_desc})
    if res.status_code == 200:
        st.success("Job description stored")
    else:
        st.error(res.text)

# -------- MULTIPLE FILE UPLOAD -------- #
files = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if files:
    if st.button("Rank Candidates"):

        try:
            upload_files = [
                ("files", (f.name, f, "application/pdf")) for f in files
            ]

            res = requests.post(f"{API}/rank_multiple", files=upload_files)

            # Debug info
            print("STATUS:", res.status_code)
            print("RESPONSE:", res.text)

            if res.status_code == 200:
                data = res.json()["ranked_candidates"]

                df = pd.DataFrame(data)

                st.subheader("🏆 Ranked Candidates")
                st.dataframe(df, use_container_width=True)

                if not df.empty:
                    top = df.iloc[0]
                    st.success(f"Top Candidate: {top['name']} ({top['final_score']}%)")

            else:
                st.error(f"Backend Error: {res.text}")

        except Exception as e:
            st.error(f"Request Failed: {str(e)}")