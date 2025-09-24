#  AI Resume & Job Match Evaluator

An AI-powered tool that evaluates the match between resumes and job descriptions. It extracts skills and experiences using NLP, calculates match percentages, and suggests personalized bullet points to boost your chances.

> Built for aspiring engineers, data scientists, and analysts navigating the current job market.

---

## Features

 Resume and job spec parsing (PDF, TXT) 
 Skill extraction using NLP (spaCy / BERT) 
 Similarity scoring using sentence embeddings (cosine similarity) 
 AI-generated bullet point suggestions (GPT-based) 
 Streamlit app for interactive use 
 Optional job scraping 
 Dockerized + testable + clean code

---

## Demo Screenshots

| Upload Resume | Match Score | AI Suggestions |
|---------------|-------------|----------------|
| ![](screenshots/upload.png) | ![](screenshots/match.png) | ![](screenshots/suggestions.png) |

🔗 [Live Demo (Streamlit Cloud)](https://your-app-url.streamlit.app)

---

## Tech Stack

- **Python 3.10**
- **spaCy** for NLP
- **Sentence Transformers** for similarity
- **OpenAI GPT-4 API** (optional)
- **Streamlit** for UI
- **Docker** for containerization
- **GitHub Actions** for CI

---

## Project Structure
├── data/ → Sample resumes and job specs
├── models/ → Resume parser and matcher
├── app/ → Streamlit frontend and utils
├── tests/ → Unit tests
├── notebooks/ → EDA and prototyping
├── requirements.txt → Dependencies
├── Dockerfile → Deployment setup

---

## Use Case

- **Candidates**: Check how well your resume matches a job spec
- **Recruiters**: Automate resume screening
- **Career coaches**: Help clients tailor resumes for job specs

---

## Getting Started

###  Installation

```bash
git clone https://github.com/yourusername/ai-resume-matcher.git
cd ai-resume-matcher
pip install -r requirements.txt


