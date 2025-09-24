import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from models.resume_parser import extract_skills
from models.job_matcher import calculate_match_score
from app.utils import extract_text_from_pdf
from app.gpt_helper import get_gpt_suggestions

st.title("AI Resume Matcher")

# Upload resume as PDF or paste as text
resume_option = st.radio("How would you like to provide your resume?", ["Upload PDF", "Paste Text"])

resume_text = ""
if resume_option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF uploaded and text extracted successfully!")
        with st.expander("View Extracted Resume Text"):
            st.text_area("Extracted Resume Text", resume_text, height=300)
else:
    resume_text = st.text_area("Paste your resume here")

# Job description input
job_text = st.text_area("Paste the job description here")

if st.button("Match Me"):
    if resume_text.strip() and job_text.strip():
        score = calculate_match_score(resume_text, job_text)
        st.success(f"Match Score: {score:.2f}%")

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)
        missing_skills = set(job_skills) - set(resume_skills)

        st.write("Missing Skills:", ", ".join(missing_skills))
    else:
        st.warning("Please provide both resume and job description.")

if st.button("Get GPT Suggestions"):
    if resume_text.strip() and job_text.strip():
        with st.spinner("Generating suggestions from GPT..."):
            suggestions = get_gpt_suggestions(resume_text, job_text)
            st.markdown("### GPT Resume Improvement Suggestions:")
            st.markdown(suggestions)
    else:
        st.warning("Please provide both resume and job description.")

