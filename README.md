# 🎯 PrepWise AI

> **An AI-Powered Resume & Interview Intelligence Platform built with Python, Streamlit, and Large Language Models.**

PrepWise AI helps job seekers improve their resumes, analyze ATS compatibility, compare resumes with job descriptions, practice technical interviews through text and voice, and receive AI-powered feedback with performance analytics.

---

## 🚀 Demo

🎥 **Project Demo:** *https://youtu.be/RVkFQZSEczY*

🌐 **Live Website:** *(Add your deployed website link here after deployment)*

---

# ✨ Features

### 📄 Resume Parsing
- Upload PDF resumes
- Extracts resume text automatically
- Displays parsed content for review

### 📊 ATS Resume Analysis
- AI-powered ATS evaluation
- Resume strengths
- Missing keywords
- Resume improvement suggestions

### 🎯 Job Description Matching
- Compare resume with any job description
- Resume-job match score
- Matched skills
- Missing skills
- Experience gap analysis
- Personalized recommendations

### 🤖 AI Interview Question Generator
- Generates 10+ personalized interview questions
- Tailored according to uploaded resume
- Covers technical, project-based and behavioral questions

### ✍️ Text Interview Mode
- Practice interview questions
- Receive AI-generated feedback
- Technical Score
- Communication Score
- Overall Interview Score

### 🎤 Voice Interview Mode
- Speech-to-text interview practice
- AI evaluates spoken responses
- Confidence and communication analysis

### 📈 Performance Dashboard
- Interview score tracking
- Technical score visualization
- Communication score visualization
- Overall performance trends

---

# 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI
- OpenRouter API
- GPT OSS 20B

### Libraries
- PyPDF2
- Plotly
- Pandas
- SpeechRecognition
- streamlit-mic-recorder
- python-dotenv

---

# 📂 Project Structure

```
PrepWise-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── resume_parser.py
│   ├── ats_analyzer.py
│   ├── jd_matcher.py
│   ├── question_generator.py
│   └── feedback_generator.py
│
└── screenshots/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/PrepWise-AI.git
```

Navigate into the project

```bash
cd PrepWise-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENROUTER_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

> *(Add screenshots here after uploading them.)*

### 🏠 Home

![Home](screenshots/home.png)

---

### 📄 ATS Resume Analysis

![ATS](screenshots/ats.png)

---

### 🎯 Job Description Matching

![JD](screenshots/jd_match.png)

---

### 🤖 AI Interview Questions

![Questions](screenshots/questions.png)

---

### 📊 Interview Dashboard

![Dashboard](screenshots/dashboard.png)

---

# 🔥 Future Improvements

- 📥 Download interview reports as PDF
- 🌍 Multi-language interview support
- 📹 Webcam-based mock interviews
- 📅 Interview history and progress tracking
- 🎯 AI-generated resume rewriting
- 💼 LinkedIn profile analysis
- ☁️ Cloud deployment

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ansh Kaushik**

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

It helps others discover the project and motivates further improvements.

---

## 🙌 Acknowledgements

- Streamlit
- OpenRouter
- GPT OSS 20B
- Python Open Source Community
