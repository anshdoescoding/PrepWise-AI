from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def match_resume_with_jd(resume_text, job_description):

    prompt = f"""
You are an expert ATS and recruitment analyst.

Compare the resume with the job description.

Provide your response in this format:

Job Match Score: XX/100

Matched Skills:
- skill 1
- skill 2

Missing Skills:
- skill 1
- skill 2

Experience Gaps:
- gap 1
- gap 2

Resume Improvement Suggestions:
- suggestion 1
- suggestion 2

Final Recommendation:
Short recommendation for the candidate.

Resume:
{resume_text[:3000]}

Job Description:
{job_description[:3000]}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content