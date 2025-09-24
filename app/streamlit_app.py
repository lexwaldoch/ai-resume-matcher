import streamlit as st
from models.resume_parser import extract_skills
from models.job_matcher import calculate_match_score

st.title("AI Resume Matcher")

resume_text = st.text_area("Paste your resume here")
job_text = st.text_area("Paste the job description here")

if st.button("Match Me"):
    if resume_text and job_text:
        score = calculate_match_score(resume_text, job_text)
        st.success(f"Match Score: {score:.2f}%")

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)
        missing_skills = set(job_skills) - set(resume_skills)

        st.write("Missing Skills:", ", ".join(missing_skills))
    else:
        st.warning("Please enter both resume and job description.")
