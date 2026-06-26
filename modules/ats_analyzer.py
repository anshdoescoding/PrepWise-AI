from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_resume_ats(resume_text):

    prompt = f"""
You are an ATS resume expert.

Analyze this resume and provide:

ATS Score: XX

Missing Keywords:
- keyword 1
- keyword 2

Strong Skills Found:
- skill 1
- skill 2

Weak Areas:
- area 1
- area 2

Resume Improvement Suggestions:
- suggestion 1
- suggestion 2

Resume:
{resume_text[:3000]}

Keep it concise and professional.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content