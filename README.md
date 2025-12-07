Emotional Chatbot Using NLP + Sentiment Analysis + Emotion Detection + Gemini LLM

This project is an emotion-aware conversational AI chatbot built using:

Custom NLP preprocessing

Sentiment analysis (HuggingFace)

Emotion detection (RoBERTa emotional model)

Intent detection using Gemini LLM

Adaptive emotional response generation

Streamlit UI with conversation history

The system takes user input → analyzes emotion/sentiment → detects user intent → generates an emotionally aligned AI response.

📌 Project Structure
emotional_chatbot/
│── app_streamlit.py       # Main Streamlit UI
│── nlp_module.py          # Text preprocessing utilities
│── sentiment_module.py    # Sentiment + emotion detection
│── llm_module.py          # Gemini + GPT-2 fallback LLM interface
│── .env                   # GEMINI_API_KEY stored here
│── requirements.txt
│── README.md

📌 How The System Works (Flow Diagram)
      USER INPUT
          |
          v
 ┌─────────────────┐
 │  NLP Processing │  ← (nlp_module.py)
 └─────────────────┘
          |
          v
 ┌────────────────────────┐
 │ Sentiment Detection    │
 │ Emotion Classification │ ← (sentiment_module.py)
 └────────────────────────┘
          |
          v
 ┌───────────────────────────────┐
 │ Intent Detection (Gemini LLM) │
 └───────────────────────────────┘
          |
          v
 ┌──────────────────────────────────────┐
 │ Emotion-Aware Response Generation    │ ← (llm_module.py)
 └──────────────────────────────────────┘
          |
          v
     STREAMLIT CHATBOT UI

📌 Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/shankar-kumar-skj/Emotional-ChatBot.git
cd Emotional-ChatBot

2. Create .env file

Add your Gemini API key:

GEMINI_API_KEY=your_key_here

3. Install dependencies
pip install -r requirements.txt

4. Run the app
streamlit run app_streamlit.py

🟦 1. nlp_module.py — Text Preprocessing
Purpose

Clean and normalize raw user text before sending to models.

Key Function
preprocess_text(text)

Strips whitespace

Normalizes multiple spaces

Prepares clean text for:

sentiment model

emotion model

LLM

Flow
Raw text → cleaned → returned

🟩 2. sentiment_module.py — Sentiment + Emotion Detection
Purpose

Detect user sentiment and emotion using HuggingFace models.

Models Used

sentiment-analysis (DistilBERT)

j-hartmann/emotion-english-distilroberta-base

Main Functions
detect_sentiment(text)

Returns:

{
  "label": "POSITIVE | NEGATIVE | NEUTRAL",
  "score": 0.85
}

detect_emotion(text)

Returns:

{
  "emotion": "joy | anger | sadness | fear | love | etc.",
  "score": 0.77
}

Flow
Input → HF Pipeline → sentiment + emotion → return

🟨 3. llm_module.py — Gemini LLM + GPT-2 Fallback
Purpose

Generate responses with emotional awareness and intent understanding.

Features

Loads .env for API key

Configures Gemini 2.5 Flash

Adds dynamic system prompts

Injects user intent and emotional context

Includes GPT-2 fallback if Gemini unavailable

Key Function
generate_llm(prompt, model, max_output_tokens, temperature, user_need=None)

Builds system prompt

Adds optional “user need” context

Sends request to Gemini

Falls back to DistilGPT-2 if needed

Flow
(text + sentiment + emotion + intent) → prompt → Gemini → response

🟥 4. app_streamlit.py — Main Frontend Application
Purpose

Provide a clean UI for interacting with the emotional chatbot.

Key Features

Input text area

Optional “What do you need help with?” field

Conversation history sidebar

Emotion-aware tone switching:

empathetic tone if sadness/fear/anger

friendly tone otherwise

Main Steps on “Send” Button

Preprocess text

Detect sentiment

Detect emotion

Detect user's intent via Gemini

Build emotionally adaptive prompt

Generate final chatbot reply

Save conversation to session

Display conversation details:

chatbot reply

detected sentiment

detected emotion

detected intent

Flow
UI input → NLP → sentiment/emotion → intent detection → Gemini response → displayed to user

🎯 Chatbot Workflow Summary
1. User sends a message

⬇️

2. Text is cleaned

⬇️

3. Sentiment & emotion detected

⬇️

4. Intent extracted via Gemini

⬇️

5. Emotion-aware response generated

⬇️

6. Chat history updated

⬇️

7. Response displayed in Streamlit

⬇️

8. User continues conversation
🚀 Possible Future Enhancements

Here are several improvements you can add later:

Memory-enhanced LLM (chat context injection)

Voice input/output

Cloud database logging (Firebase / Supabase / MongoDB)

Animated chat interface

User authentication

Multi-language support

Browser-based speech emotion recognition

If you want, I can generate any of these features, including full code.