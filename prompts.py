def flashcard_prompt(subject, content):
    return f"""
You are an expert in {subject}. Generate clear and concise flashcards (Q&A format) from the following content:

--- START OF CONTENT ---
{content}
--- END OF CONTENT ---

Instructions:
- Create at least 10-15 flashcards.
- Each flashcard should include a concise question and a factually correct, self-contained answer.
- Group flashcards under detected topics if possible using headings like ## Topic Name.
Output Format:
## Topic Name
Q: ...
A: ...
Q: ...
A: ...
"""