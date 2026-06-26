import streamlit as st
from modules.resume_parser import extract_resume_text
from modules.question_generator import generate_questions
from modules.feedback_generator import generate_feedback, generate_voice_feedback
from modules.ats_analyzer import analyze_resume_ats
from modules.jd_matcher import match_resume_with_jd
from streamlit_mic_recorder import speech_to_text
import re
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="PrepWise AI", page_icon="🎯", layout="wide")

# ================= SESSION STATE =================

defaults = {
    "resume_text": "",
    "questions": "",
    "ats_result": "",
    "jd_result": "",
    "technical_scores": [],
    "communication_scores": [],
    "overall_scores": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def save_scores(feedback):
    try:
        technical = int(re.search(r"Technical Score:\s*(\d+)", feedback).group(1))
        communication = int(re.search(r"Communication Score:\s*(\d+)", feedback).group(1))
        overall = int(re.search(r"Overall Score:\s*(\d+)", feedback).group(1))

        st.session_state.technical_scores.append(technical)
        st.session_state.communication_scores.append(communication)
        st.session_state.overall_scores.append(overall)
    except:
        pass


# ================= CSS =================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #031540 0%, #001233 100%);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #00F5FF;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: white;
    margin-bottom: 40px;
}

.upload-box, .question-box, .feedback-box {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    border-left: 5px solid #00F5FF;
    margin-top: 20px;
}

.feedback-box {
    border-left: 5px solid #00FF99;
}

.stButton>button {
    background: linear-gradient(90deg,#00F5FF,#00C2FF);
    color: black;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 12px 20px;
    width: 100%;
}

textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 10px !important;
}

label, .stTextArea label {
    color: white !important;
    font-weight: bold;
}

.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown h1,
.stMarkdown h2, .stMarkdown h3, .stMarkdown strong {
    color: white !important;
}

.footer {
    text-align:center;
    color: #A0A0A0;
    margin-top:50px;
}
</style>
""", unsafe_allow_html=True)


# ================= HEADER =================

st.markdown("<div class='title'>🎯 PrepWise AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-Powered Resume & Interview Intelligence Platform</div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.05);padding:25px;border-radius:20px;border:1px solid #00F5FF;text-align:center;height:220px;">
        <h2 style="color:#00F5FF;">🤖 AI Questions</h2>
        <p style="color:white;font-size:18px;">Generate personalized interview questions using AI.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.05);padding:25px;border-radius:20px;border:1px solid #00F5FF;text-align:center;height:220px;">
        <h2 style="color:#00F5FF;">🎤 Voice Interview</h2>
        <p style="color:white;font-size:18px;">Practice real-time interviews with voice input.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.05);padding:25px;border-radius:20px;border:1px solid #00F5FF;text-align:center;height:220px;">
        <h2 style="color:#00F5FF;">📊 AI Feedback</h2>
        <p style="color:white;font-size:18px;">Receive intelligent feedback and interview scores instantly.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)


# ================= RESUME UPLOAD =================

st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
st.markdown("<h3 style='color:white;'>📄 Upload Your Resume</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["pdf"], key="resume_uploader")

st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file:
    st.session_state.resume_text = extract_resume_text(uploaded_file)
    st.success("✅ Resume Uploaded Successfully!")

resume_text = st.session_state.resume_text


# ================= MAIN APP =================

if resume_text:

    st.markdown("<h1 style='color:white;'>📑 Extracted Resume Text</h1>", unsafe_allow_html=True)
    st.text_area("Resume Content", resume_text, height=300)

    st.markdown("<br>", unsafe_allow_html=True)

    # ATS ANALYSIS
    if st.button("📄 Analyze Resume ATS Score"):
        with st.spinner("Analyzing Resume for ATS Score..."):
            st.session_state.ats_result = analyze_resume_ats(resume_text)

    if st.session_state.ats_result:
        st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:white;'>📄 ATS Resume Analysis</h2>", unsafe_allow_html=True)
        st.markdown(st.session_state.ats_result)
        st.markdown("</div>", unsafe_allow_html=True)

    # JD MATCHING
    st.markdown("---")
    st.markdown("<h2 style='color:white;'>🎯 Job Description Matchmaking</h2>", unsafe_allow_html=True)

    job_description = st.text_area(
        "Paste the Job Description here:",
        height=220,
        key="job_description_box"
    )

    if st.button("🎯 Match Resume with Job Description"):
        if job_description.strip() == "":
            st.warning("Please paste a job description first.")
        else:
            with st.spinner("Matching resume with job description..."):
                st.session_state.jd_result = match_resume_with_jd(resume_text, job_description)

    if st.session_state.jd_result:
        st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:white;'>🎯 Job Match Analysis</h2>", unsafe_allow_html=True)
        st.markdown(st.session_state.jd_result)
        st.markdown("</div>", unsafe_allow_html=True)

    # QUESTION GENERATION
    if st.button("🚀 Generate Interview Questions"):
        with st.spinner("Generating AI Questions..."):
            st.session_state.questions = generate_questions(resume_text)

        st.success("✅ Interview questions generated successfully!")

    if st.session_state.questions:

        st.markdown("<div class='question-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:white;'>🤖 AI Generated Questions</h2>", unsafe_allow_html=True)
        st.markdown(st.session_state.questions)
        st.markdown("</div>", unsafe_allow_html=True)

        questions_list = [
            q.strip()
            for q in st.session_state.questions.split("\n")
            if q.strip()
        ]

        text_tab, voice_tab = st.tabs(["✍️ Text Interview", "🎤 Voice Interview"])

        # TEXT INTERVIEW
        with text_tab:

            st.markdown("<h2 style='color:white;'>✍️ Text Answer Practice</h2>", unsafe_allow_html=True)

            selected_question = st.selectbox(
                "Choose a question to answer:",
                questions_list,
                key="selected_text_question"
            )

            answer = st.text_area(
                "Write your answer below:",
                height=200,
                key="answer_box"
            )

            if st.button("📊 Generate AI Feedback", key="text_feedback_btn"):

                if answer.strip() == "":
                    st.warning("Please write an answer first.")

                else:
                    with st.spinner("Analyzing your answer..."):
                        feedback = generate_feedback(selected_question, answer)
                        save_scores(feedback)

                    st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
                    st.markdown("<h2 style='color:white;'>📈 AI Feedback & Score</h2>", unsafe_allow_html=True)
                    st.markdown(feedback)
                    st.markdown("</div>", unsafe_allow_html=True)

        # VOICE INTERVIEW
        with voice_tab:

            st.markdown("<h2 style='color:white;'>🎤 Voice Interview Practice</h2>", unsafe_allow_html=True)

            selected_voice_question = st.selectbox(
                "Choose a question for voice answer:",
                questions_list,
                key="selected_voice_question"
            )

            st.markdown(f"### Question: {selected_voice_question}")

            spoken_text = speech_to_text(
                language="en",
                start_prompt="🎙️ Start Recording",
                stop_prompt="⏹️ Stop Recording",
                key="voice_interview"
            )

            if spoken_text:

                st.success("✅ Speech Captured Successfully")

                st.text_area(
                    "Transcribed Answer",
                    spoken_text,
                    height=200,
                    key="voice_transcript"
                )

                if st.button("📊 Analyze Spoken Answer", key="voice_feedback_btn"):

                    with st.spinner("Analyzing Voice Response..."):
                        feedback = generate_voice_feedback(spoken_text)
                        save_scores(feedback)

                    st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
                    st.markdown("<h2 style='color:white;'>📈 Voice Feedback & Score</h2>", unsafe_allow_html=True)
                    st.markdown(feedback)
                    st.markdown("</div>", unsafe_allow_html=True)


# ================= DASHBOARD =================

if len(st.session_state.overall_scores) > 0:

    st.markdown("---")
    st.markdown("<h1 style='color:white;'>📊 Interview Performance Dashboard</h1>", unsafe_allow_html=True)

    avg_tech = round(sum(st.session_state.technical_scores) / len(st.session_state.technical_scores), 1)
    avg_comm = round(sum(st.session_state.communication_scores) / len(st.session_state.communication_scores), 1)
    avg_overall = round(sum(st.session_state.overall_scores) / len(st.session_state.overall_scores), 1)

    col1, col2, col3 = st.columns(3)

    col1.metric("Technical Score", avg_tech)
    col2.metric("Communication Score", avg_comm)
    col3.metric("Overall Score", avg_overall)

    df = pd.DataFrame({
        "Category": ["Technical", "Communication", "Overall"],
        "Score": [avg_tech, avg_comm, avg_overall]
    })

    fig = px.bar(
        df,
        x="Category",
        y="Score",
        title="Interview Score Breakdown",
        range_y=[0, 100]
    )

    st.plotly_chart(fig, use_container_width=True)

    progress_df = pd.DataFrame({
        "Attempt": list(range(1, len(st.session_state.overall_scores) + 1)),
        "Overall Score": st.session_state.overall_scores
    })

    fig2 = px.line(
        progress_df,
        x="Attempt",
        y="Overall Score",
        markers=True,
        title="Interview Progress Over Attempts"
    )

    st.plotly_chart(fig2, use_container_width=True)


# ================= FOOTER =================

st.markdown(
    "<div class='footer'>Built with ❤️ using Python, Streamlit & AI</div>",
    unsafe_allow_html=True
)
