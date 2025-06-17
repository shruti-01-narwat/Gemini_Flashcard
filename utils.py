import fitz  # PyMuPDF
import pandas as pd

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_flashcards(raw_output):
    flashcards = []
    topic = "General"
    for line in raw_output.splitlines():
        line = line.strip()
        if line.startswith("##"):
            topic = line.replace("##", "").strip()
        elif line.startswith("Q:"):
            question = line[2:].strip()
        elif line.startswith("A:"):
            answer = line[2:].strip()
            flashcards.append({"Topic": topic, "Question": question, "Answer": answer})
    return pd.DataFrame(flashcards)
