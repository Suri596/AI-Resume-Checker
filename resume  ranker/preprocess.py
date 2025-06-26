import spacy

# Load SpaCy's English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if token.is_alpha and not token.is_stop:
            tokens.append(token.lemma_.lower())
    return " ".join(tokens)

# Test preprocessing
if __name__ == "__main__":
    sample_text = """
    Experienced Data Analyst with 5 years in SQL, Python, and data visualization.
    Passionate about uncovering insights and driving decision-making.
    """
    cleaned_text = preprocess_text(sample_text)
    print("Before:\n", sample_text)
    print("\nAfter:\n", cleaned_text)
