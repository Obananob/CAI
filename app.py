import streamlit as st
import openai
import random
import io
from fpdf import FPDF

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Inspirational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Your education is a dress rehearsal for a life that is yours to lead.",
    "Small progress is still progress. Keep going!",
    "The expert in anything was once a beginner.",
    "Push yourself, because no one else is going to do it for you."
]

# Page config
st.set_page_config(page_title="AI Quiz Maker", page_icon="📝", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #f5f7fa;}
    .stTextArea textarea {border-radius: 10px;}
    .quiz-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .quote {
        font-size: 16px;
        font-style: italic;
        color: #555;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to create PDF
def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split("\n"):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest="S").encode("latin1")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Quiz Generator", " About"])

# HOME PAGE
if page == " Home":
    st.markdown("<h1 style='text-align:center;'>Welcome to AI Quiz Maker </h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Turn your notes into multiple-choice quizzes instantly, powered by AI.</p>", unsafe_allow_html=True)
    st.markdown(f"<div class='quote'>{random.choice(quotes)}</div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1584697964190-6f68b84d0c0f", caption="Learning made easier", use_container_width=True)

# QUIZ GENERATOR PAGE
elif page == " Quiz Generator":
    st.markdown("<h2> AI Quiz Generator</h2>", unsafe_allow_html=True)
    st.write("Paste your notes or topic below, and I'll create a multiple-choice quiz instantly!")
    st.markdown(f"<div class='quote'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

    input_text = st.text_area("Enter your notes or topic:", height=200)

    if st.button("🚀 Generate Quiz"):
        if not input_text.strip():
            st.warning(" Please enter some text or a topic first.")
        else:
            with st.spinner("Generating quiz..."):
                try:
                    prompt = f"""
                    You are an expert teacher. Based on the text below, create 5 multiple-choice questions 
                    with 4 options each, and mark the correct answer with (✔️).
                    Text:
                    {input_text}
                    """
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    quiz = response.choices[0].message.content

                    # Display quiz
                    st.markdown("<div class='quiz-card'>", unsafe_allow_html=True)
                    st.markdown(f"** Your Quiz:**\n\n{quiz}")
                    st.markdown("</div>", unsafe_allow_html=True)

                    # Copyable text
                    st.code(quiz, language="markdown")

                    # Download as PDF
                    pdf_bytes = create_pdf(quiz)
                    st.download_button(
                        label="Download as PDF",
                        data=pdf_bytes,
                        file_name="quiz.pdf",
                        mime="application/pdf"
                    )

                except Exception as e:
                    st.error(f"Error: {e}")

# ABOUT PAGE
elif page == " About":
    st.markdown("<h2> About This App</h2>", unsafe_allow_html=True)
    st.write("""
        **AI Quiz Maker** was built for **Panda Hacks 2025** 🐼 to help students 
        turn their notes into interactive quizzes instantly.  
        
        **Features:**
        - Multiple-choice quiz generation from text  
        - Motivational quotes to keep you inspired  
        - Download quizzes as PDF  
        - Easy to use, no coding required  
        
        **Tech Stack:**
        - Python + Streamlit  
        - OpenAI GPT model  
        - FPDF for PDF generation  
    """)
    st.markdown(f"<div class='quote'> {random.choice(quotes)}</div>", unsafe_allow_html=True)
