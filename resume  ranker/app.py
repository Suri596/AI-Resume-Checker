import streamlit as st
import fitz  # PyMuPDF
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Define common skill keywords
COMMON_SKILLS = [
    "python", "sql", "excel", "java", "c++", "data analysis", "data visualization",
    "machine learning", "deep learning", "pandas", "numpy", "scikit-learn", "tensorflow",
    "keras", "power bi", "tableau", "django", "flask", "communication",
    "problem solving", "teamwork", "git", "linux", "cloud", "azure", "aws", "nlp"
]

# Extract raw text from uploaded PDF using PyMuPDF
def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

# Clean and preprocess text using SpaCy
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Extract relevant skills from preprocessed text
def extract_skills(text):
    clean_text = preprocess_text(text)
    found = []
    for skill in COMMON_SKILLS:
        if skill.lower() in clean_text:
            found.append(skill.lower())
    return found

# Rank resumes by number of matched skills
def rank_resumes_by_skills(jd_text, resumes_dict):
    jd_skills = set(extract_skills(jd_text))
    results = []

    for filename, content in resumes_dict.items():
        resume_skills = set(extract_skills(content))
        matched = jd_skills.intersection(resume_skills)
        score = len(matched) / len(jd_skills) if jd_skills else 0
        results.append((filename, score, list(matched)))

    # Sort descending by score
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Streamlit app UI
st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("📄 AI Resume Ranker")
st.write("Upload multiple PDF resumes and paste a job description to rank them by skill match.")

# Job description input
jd_text = st.text_area("📌 Paste the Job Description here:", height=200)

# Resume PDF uploader
uploaded_files = st.file_uploader("📂 Upload Resume PDFs", type="pdf", accept_multiple_files=True)

# Only process when both inputs are provided
if jd_text and uploaded_files:
    st.info("✅ Inputs received. Processing resumes...")
    resume_texts = {}

    # Extract text from each uploaded resume
    for file in uploaded_files:
        resume_texts[file.name] = extract_text_from_pdf(file)

    # Rank resumes by skill match
    results = rank_resumes_by_skills(jd_text, resume_texts)

    # Show results
    st.success("🎉 Resumes ranked successfully!")
    st.table([
        {
            "Rank": i + 1,
            "Resume Name": name,
            "Match Score": f"{score:.2f}",
            "Matched Skills": ", ".join(matches)
        }
        for i, (name, score, matches) in enumerate(results)
    ])
