# 💼 AI-Powered Resume Ranker

An AI project to **automatically rank resumes** based on a provided job description using **NLP and keyword matching**.  
Built using **Streamlit**, **Python**, and **PDF processing** tools.

---

## 🚀 How It Works

1. Paste a job description (e.g., "We're hiring a Data Scientist...")
2. Upload multiple PDF resumes.
3. The system extracts text, matches key skills, and gives a score out of 100.
4. Shows:
   - Resume score
   - Matched skills
   - Ranked list of resumes

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: `PyMuPDF`, `re`, `pandas`, `sklearn`
- **File Handling**: PDF parsing with keyword search

---

## 🧪 Features

- Drag-and-drop PDF uploads
- Text extraction from resumes
- Real-time keyword matching
- Resume scoring based on job description
- Results table with matched keywords

---

## 📷 Screenshots

### ✅ Input Section
![Job description input](../screenshots/screenshot1.png)

### 📊 Output Scores
![Ranked resumes](../screenshots/screenshot2.png)

---

## 🧾 Sample Output

| Resume        | Score (%) | Matched Skills                     |
|---------------|------------|------------------------------------|
| `resume1.pdf` | 66.67%     | tensorflow, scikit, pandas, git   |
| `resume2.pdf` | 6.67%      | git                               |

---

## 📂 Folder Structure

