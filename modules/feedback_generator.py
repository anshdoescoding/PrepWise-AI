from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# =====================================
# TEXT INTERVIEW FEEDBACK
# =====================================

def generate_feedback(question, answer):

    prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate's answer.

Interview Question:
{question}

Candidate Answer:
{answer}

Analyze the answer and provide.

IMPORTANT:
Provide your response in EXACTLY this format:

Technical Score: XX
Communication Score: XX
Overall Score: XX

Strengths:
- Point 1
- Point 2

Weaknesses:
- Point 1
- Point 2

Suggestions:
- Point 1
- Point 2

Keep the feedback concise and professional.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

# =====================================
# VOICE INTERVIEW FEEDBACK
# =====================================

def generate_voice_feedback(answer):

    prompt = f"""
You are an expert interview evaluator.

The following answer was given during a voice interview.

Candidate Answer:
{answer}

Analyze the answer and provide.

IMPORTANT:
Provide your response in EXACTLY this format:

Technical Score: XX
Communication Score: XX
Overall Score: XX

Strengths:
- Point 1
- Point 2

Weaknesses:
- Point 1
- Point 2

Suggestions:
- Point 1
- Point 2

Keep the feedback concise and professional.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
