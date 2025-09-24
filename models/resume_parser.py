import spacy
import subprocess
import sys

def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], check=True)
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

def extract_skills(text):
    doc = nlp(text)
    skills = []
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
            skills.append(token.lemma_.lower())
    return list(set(skills))
