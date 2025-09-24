from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_match_score(resume_text, job_text):
    embeddings = model.encode([resume_text, job_text])
    score = util.cos_sim(embeddings[0], embeddings[1])
    return float(score[0][0]) * 100
