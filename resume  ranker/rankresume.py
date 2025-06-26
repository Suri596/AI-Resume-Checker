import os
from extract_text import extract_all_resumes_text
from preprocess import preprocess_text

# ✅ Define a common skill set — expand as needed
COMMON_SKILLS = [
    "python", "sql", "excel", "java", "c++", "data analysis", "data visualization",
    "machine learning", "deep learning", "pandas", "numpy", "scikit-learn", "tensorflow",
    "keras", "power bi", "tableau", "django", "flask", "communication",
    "problem solving", "teamwork", "git", "linux", "cloud", "azure", "aws", "nlp"
]

# ✅ Extract only relevant skills from text
def extract_skills(text):
    clean_text = preprocess_text(text)
    found_skills = []
    for skill in COMMON_SKILLS:
        if skill.lower() in clean_text:
            found_skills.append(skill.lower())
    return found_skills

# ✅ Rank resumes based on skill overlap
def rank_resumes_by_skills(jd_text, resume_texts_dict):
    jd_skills = set(extract_skills(jd_text))
    
    ranking = []
    for filename, text in resume_texts_dict.items():
        resume_skills = set(extract_skills(text))
        matched_skills = jd_skills.intersection(resume_skills)
        score = len(matched_skills) / len(jd_skills) if jd_skills else 0
        ranking.append((filename, score, list(matched_skills)))
    
    # Sort by descending score
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking

# ✅ Main block for testing
if __name__ == "__main__":
    # Load job description text
    with open("job_description.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()
    
    # Load and extract resume texts
    resume_texts = extract_all_resumes_text("resumes")
    
    # Rank them
    results = rank_resumes_by_skills(jd_text, resume_texts)

    # Display the results
    print("\n🔹 Skill-Based Resume Ranking:\n")
    for i, (name, score, skills) in enumerate(results, start=1):
        print(f"{i}. {name} → Score: {score:.2f}")
        print(f"   Matched Skills: {', '.join(skills)}\n")
