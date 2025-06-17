import streamlit as st
import google.generativeai as genai
import pandas as pd

from prompts import flashcard_prompt
from utils import read_pdf, parse_flashcards

# API setup
# Paste API key is placed directly here.
genai.configure(api_key="Paste your api key here")

# Corrected model name based on your genai.list_models() output 
# You can choose another model from your list if preferred, e.g., "models/gemini-2.5-pro"
model = genai.GenerativeModel("models/gemini-2.5-pro")

st.title("📚 LLM Flashcard Generator")
st.write("Generate flashcards from your study material using Gemini LLM.")

subject = st.selectbox("Select Subject", ["General", "Biology", "History", "Computer Science", "Physics", "Chemistry"])

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
text_input = st.text_area("Or paste text here")

content = ""
if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        content = read_pdf(uploaded_file)
    else:
        content = uploaded_file.read().decode("utf-8")
elif text_input:
    content = text_input

if content and st.button("Generate Flashcards"):
    with st.spinner("Generating flashcards..."):
        prompt = flashcard_prompt(subject, content)
        try:
            response = model.generate_content(prompt)
            flashcard_df = parse_flashcards(response.text)

            st.success("Flashcards Generated!")
            st.dataframe(flashcard_df)

            csv = flashcard_df.to_csv(index=False).encode("utf-8")
            st.download_button("Download as CSV", csv, "flashcards.csv", "text/csv")
        except Exception as e:
            st.error(f"An error occurred while generating flashcards: {e}")
            st.warning("Please ensure the correct model name is used and your content is appropriate for generation.")