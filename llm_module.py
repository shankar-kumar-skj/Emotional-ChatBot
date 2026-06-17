import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_llm(prompt: str):
    try:
        if not GEMINI_API_KEY:
            return "❌ Missing Gemini API Key"

        genai.configure(api_key=GEMINI_API_KEY)

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "⚠️ Empty response from model"

    except Exception as e:
        return f"LLM Error: {str(e)}"