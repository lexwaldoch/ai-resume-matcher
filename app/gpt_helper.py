import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_suggestions(resume_text, job_description):
    prompt = f"""
    You are a career coach. Given the following resume and job description, suggest 3-5 improved bullet points to help the candidate better match the job.

    Resume:
    \"\"\"{resume_text}\"\"\"

    Job Description:
    \"\"\"{job_description}\"\"\"

    Provide clear, concise bullet points the candidate can add or rephrase in their resume.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=400,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

