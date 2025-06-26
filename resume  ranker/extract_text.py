import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_all_resumes_text(resume_folder='resumes'):
    resume_texts = {}
    for filename in os.listdir(resume_folder):
        if filename.endswith('.pdf'):
            path = os.path.join(resume_folder, filename)
            text = extract_text_from_pdf(path)
            resume_texts[filename] = text
    return resume_texts

# Test
if __name__ == "__main__":
    resumes = extract_all_resumes_text()
    for name, content in resumes.items():
        print(f"\n{name}:\n{content[:500]}...\n{'-'*50}")
