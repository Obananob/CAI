# AI Quiz Maker

## About the Project
AI Quiz Maker is a web-based application that transforms your notes into interactive multiple-choice quizzes using AI. It was built to help students, educators, and lifelong learners quickly generate study materials without manual question creation.

### Inspiration
The inspiration came from the challenge of revising large amounts of study notes in limited time. I wanted a tool that could instantly transform my notes into quiz questions, making active recall effortless and engaging.

### What I Learned
- How to integrate OpenAI’s GPT models into a Streamlit application.
- Effective prompt engineering to generate well-structured multiple-choice questions.
- Building responsive and user-friendly interfaces in Streamlit.
- Deployment of AI-powered applications on the cloud.

### How I Built It
1. **Frontend & Backend:** Developed entirely in Python using Streamlit.
2. **AI Model:** Integrated OpenAI GPT API for question generation.
3. **PDF Export:** Used the `fpdf` library to allow users to download quizzes in PDF format.
4. **UI/UX Enhancements:** Applied custom CSS to give a modern and clean interface.
5. **Deployment:** Deployed on Streamlit Cloud with environment variables for API key security.

### Challenges Faced
- **API Quota Limits:** Managing API usage to avoid hitting rate or quota limits.
- **Prompt Optimization:** Ensuring the generated quizzes were relevant and clearly formatted.
- **Deployment Issues:** Resolving missing dependencies and secrets setup during cloud deployment.

---

## Features
- Generate multiple-choice quizzes instantly from your text or notes.
- Download quizzes as a PDF file.
- Motivational quotes for an inspiring user experience.
- Simple, minimal, and mobile-friendly interface.

---

## Tech Stack
- **Python**
- **Streamlit**
- **OpenAI GPT API**
- **FPDF** (for PDF export)
- **CSS** (for styling)

---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/Obananob/CAI.git
cd CAI

## Install Dependencies
pip install -r requirements.txt

## Add API key
add your OpenAI API key to your streamlit cloud secrets or to a .toml file

## Run your app
Streamlit run app.py


