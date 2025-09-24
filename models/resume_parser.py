import spacy
import os

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = []
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
            skills.append(token.lemma_.lower())
    return list(set(skills))
