# 📚 LLM-Powered Flashcard Generator

A Streamlit application designed to automatically generate question-and-answer flashcards from various educational materials using Google's Gemini Large Language Models (LLMs). This tool provides a simple, intuitive interface for students and educators to quickly transform notes, textbook excerpts, or pasted text into effective study aids.

---

## ✨ Features

### 📥 Content Ingestion:
- Upload `.pdf` or `.txt` files directly.
- Paste raw text into a dedicated input area.

### 🎯 Subject-Contextual Generation:
- Select a subject (e.g., Biology, History, Computer Science) to guide the LLM in generating more relevant and accurate flashcards.

### 🧠 Automatic Flashcard Creation:
- Generates a minimum of 10–15 concise Q&A flashcards per input submission.

### 🗂 Topic Grouping (Bonus):
- Flashcards are intelligently grouped under detected topic headers, enhancing organization and study flow.

### 💬 Interactive Display:
- View generated flashcards within a clean, tabular format in the Streamlit interface.

### ⬇️ Export Functionality:
- Easily download generated flashcards as a `.csv` file.

### ⚠️ Robust Error Handling:
- Includes clear messages for common API issues (e.g., model not found, quota exceeded).

---

## 🛠️ Setup

### ✅ Prerequisites
- Python 3.8+
- `pip` (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/shruti-01-narwat/Gemini_Flashcard.git
cd Gemini_Flashcard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Your Google Gemini API Key

#### Access Google AI Studio:
- Visit: https://ai.google.dev/aistudio
- Sign in with your Google account

#### Create an API Key:
- Click "Get API key" / "API keys"
- Select or create a Google Cloud Project
- Copy and save the generated API key securely

### 4. Enable Generative Language API in Google Cloud

- Go to: https://console.cloud.google.com/
- Select the **same Google Cloud Project**
- Navigate to **"APIs & Services" > "Enabled APIs & Services"**
- Click `+ ENABLE APIS AND SERVICES`
- Search for `Generative Language API` and **enable** it

### 5. Configure Your Project

Open `main.py` and set your API key + model name:

```python
# API setup
genai.configure(api_key="YOUR_API_KEY_GOES_HERE")

# Choose your model
model = genai.GenerativeModel("models/gemini-1.5-pro")
```

---

## 🚀 Run the Application

```bash
streamlit run main.py
```

---

## 📂 Project Structure

```
Gemini_Flashcard/
├── main.py             # Main Streamlit app
├── prompts.py          # Prompt logic for Gemini
├── utils.py            # Helper functions
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🧩 Troubleshooting

### ❌ 404 models/gemini-pro not found
- Ensure you use a model returned by `genai.list_models()`
- Ensure "Generative Language API" is enabled in Google Cloud

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
```

### ❌ 429 Too many requests / Quota exceeded
- Wait a while before retrying
- Check quotas and billing in Google Cloud Console
  - https://console.cloud.google.com/billing

---

## 🤝 Contribution

Fork the repo, open issues, or submit PRs to improve the project.

> Developed as an internship assignment demonstrating LLM integration.
