from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_questions(resume_text):

    prompt = f"""
    You are an expert AI Interview Coach.

    Analyze the following resume carefully and generate:

    - 6 Technical Interview Questions
    - 2 Project-Based Questions
    - 2 HR/Behavioral Questions

    The questions should:
    - Be personalized according to skills/projects
    - Range from easy to advanced
    - Sound like real interviewer questions
    - Be concise and professional

    Resume:
    {resume_text[:3000]}
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content