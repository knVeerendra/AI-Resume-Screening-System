# 🤖 AI-Powered Semantic Resume Screening & Candidate Ranking System

## 📌 Overview

This project is an **AI-driven Resume Screening System** that ranks candidates based on their relevance to a given **Job Description**.

Unlike traditional keyword-based systems, this application uses:

* **Semantic similarity (SBERT)**
* **Skill matching**
* **Experience estimation**

to provide **accurate, explainable, and dynamic candidate ranking**.

---

## 🚀 Key Features

### 🔹 Semantic Matching (Core AI)

* Uses **Sentence-BERT (all-MiniLM-L6-v2)**
* Captures contextual similarity between resume and job description
* Not limited to exact keyword matches

---

### 🔹 Skill-Based Ranking

* Extracts relevant skills from job description
* Compares them with candidate resumes
* Provides:

  * ✅ Matched Skills
  * ❌ Missing Skills

---

### 🔹 Experience Evaluation

* Detects years of experience from resumes
* Compares with job requirements
* Adds weighted contribution to final score

---

### 🔹 Explainable Scoring System

Each candidate is evaluated using:

```
Final Score =
  50% Semantic Similarity +
  30% Skill Match +
  20% Experience Match
```

---

### 🔹 Bulk Resume Screening

* Upload multiple resumes
* Automatically ranks candidates
* Displays top candidate

---

### 🔹 Clean UI (Streamlit)

* Simple and interactive interface
* Supports:

  * Resume upload
  * Ranking visualization
  * Built-in table controls

---

## 🏗️ Project Structure

```
AI-Resume-Screening/
│
├── backend/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── embedding.py
│   │   ├── ranking.py
│   │   └── resume_parser.py
│   ├── models/
│   │   └── schema.py
│
├── frontend/
│   ├── app.py
│   └── pages/
│       ├── Single_Resume.py
│       └── Bulk_Resume.py
│
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **ML/NLP:** Sentence Transformers (SBERT)
* **Libraries:**

  * scikit-learn
  * PyMuPDF
  * pandas, numpy

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 2️⃣ Start Backend

```
python -m uvicorn backend.main:app --reload
```

---

### 3️⃣ Start Frontend

```
cd frontend
streamlit run app.py
```

---

### 4️⃣ Open in Browser

```
http://localhost:8501
```

---



## 🎯 Use Cases

* HR Resume Screening
* Candidate Ranking Systems
* AI-based Recruitment Tools
* Resume Filtering Automation

---



---

## 👨‍💻 Author

Developed as a **Machine Learning + Backend System Design Project**
focusing on **real-world recruitment automation**.

---

## ⭐ Final Note

This project demonstrates:

* Applied Machine Learning
* Backend architecture
* Real-world problem solving

👉 Designed to simulate a **production-level AI recruitment system**
