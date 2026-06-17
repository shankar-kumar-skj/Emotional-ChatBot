# Emotional Chatbot Using NLP + Sentiment Analysis + Gemini LLM 🤖

This project is an **emotion-aware chatbot** built using a hybrid approach combining classic Natural Language Processing (NLP) techniques with the power of modern Large Language Models (LLMs).

## Deploy
https://emotional-chatbot-czipakvbe7dgqfhcvp3qwp.streamlit.app/#emotional-chatbot-gemini-nlp-sentiment

It utilizes:

  * **NLP preprocessing** for cleaning user input.
  * **Sentiment analysis (HuggingFace models)** for detecting the overall positive/negative/neutral feeling.
  * **Emotion classification (HuggingFace models)** for detecting specific emotions like 'sadness,' 'joy,' or 'anger.'
  * **Google Gemini LLM** (with a DistilGPT-2 fallback) for generating intelligent, empathetic, and emotionally aligned responses.
  * **Streamlit** for a modern, interactive web UI.

The system takes user input $\to$ processes the input's emotion and intent $\to$ generates an empathetically aligned reply.

-----

# 📌 Project Structure

```
emotional_chatbot/
│── app_streamlit.py           # Main Streamlit UI and orchestration
│── llm_module.py              # Gemini (and Fallback) integration logic
│── nlp_module.py              # Text preprocessing functions
│── sentiment_module.py        # Sentiment and Emotion detection models
│── .env                       # Stores GEMINI_API_KEY
│── requirements.txt           # Project dependencies
│── README.md
```

-----

# 📌 How The System Works (Flow Diagram)

The chatbot operates in a multi-step pipeline, using the outputs of NLP and Sentiment analysis to dynamically inform the final, adaptive response from the LLM.

```
      USER INPUT
          |
          v
 ┌─────────────────┐
 │  NLP Processing │  <- (nlp_module.py)
 └─────────────────┘
          |
          v
 ┌────────────────────────┐
 │ Sentiment Analysis     │
 │ Emotion Classification │ <- (sentiment_module.py)
 └────────────────────────┘
          |
          v
 ┌───────────────────────────────┐
 │ Gemini LLM Prompt Engineering │ <- (llm_module.py)
 └───────────────────────────────┘
          |
          v
 ┌────────────────────────────┐
 │  Generate Response (LLM)   │
 └────────────────────────────┘
          |
          v
    CHATBOT RESPONSE
```

-----

# 📌 Setup Instructions (Step-by-Step)

### **1. Clone or create project folder**

```bash
git clone https://github.com/shankar-kumar-skj/Emotional-ChatBot.git
cd Emotional-ChatBot
```

### **2. Create `.env` file**

Create a file named `.env` in the root directory and add your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### **3. Create `requirements.txt`**

Create a file named `requirements.txt` with the following dependencies:

```
streamlit
google-genai
python-dotenv
transformers
torch
```

### **4. Install required packages**

```bash
pip install -r requirements.txt
```

### **5. Add code files**

Place the four core Python files (`app_streamlit.py`, `llm_module.py`, `nlp_module.py`, and `sentiment_module.py`) into the project directory.

### **6. Run the project**

```bash
streamlit run app_streamlit.py
```

-----

# 📌 Code Explanation (Module-by-Module)

Below is a **clear, simple, block-by-block** explanation of every file.

-----

# 🟦 1. `nlp_module.py` — NLP Preprocessing

### **Purpose:**

To **clean and normalize** the user's raw text input.

### **Main Functions:**

#### **a) `preprocess_text(text)`**

  * Removes extra spaces and leading/trailing whitespace.
  * Ensures the text is in a clean format for subsequent analysis.

### **Flow:**

```
Input text $\to$ strip/normalize whitespace $\to$ cleaned text $\to$ return
```

-----

# 🟩 2. `sentiment_module.py` — Sentiment + Emotion Detection

### **Purpose:**

To identify **how the user feels** by leveraging pre-trained HuggingFace models.

### **Uses Two Models (HuggingFace Pipelines):**

1.  **Sentiment model:** Detects the overall **Positive** / **Negative** / **Neutral** feeling.
2.  **Emotion model (RoBERTa):** Detects specific, granular emotions (e.g., *sadness*, *joy*, *anger*).

### **Main Functions:**

#### **a) `detect_sentiment(text)`**

  * Uses a standard HuggingFace `sentiment-analysis` pipeline.
  * Returns the dominant sentiment label and its confidence score.

#### **b) `detect_emotion(text)`**

  * Uses the `j-hartmann/emotion-english-distilroberta-base` model.
  * Returns the top-scoring specific emotion label and its confidence score.

### **Flow:**

```
Preprocessed text $\to$ HF pipelines $\to$ sentiment + top emotion $\to$ return
```

-----

# 🟨 3. `llm_module.py` — Gemini LLM Integration + Fallback

### **Purpose:**

To **generate the final, context-aware chatbot reply**. It is responsible for calling the LLM and engineering the prompt based on the detected emotion and intent.

### **Features:**

  * Loads the **`GEMINI_API_KEY`** from the `.env` file for configuration.
  * Targets the **`gemini-2.5-flash`** model by default.
  * Dynamically injects a system prompt (e.g., "You are an **empathetic emotional-support** AI...") and user analysis results (emotion, sentiment, intent) to ensure an appropriate and helpful response.
  * Includes an **automatic fallback** to a HuggingFace **`distilgpt2`** model if the Gemini API is inaccessible.

### **Main Functions:**

#### **a) `generate_llm(...)`**

  * Handles prompt construction and LLM configuration (temperature, max tokens).
  * Prioritizes the Gemini API call.
  * If Gemini fails, it attempts to use the local GPT-2 fallback generator.

### **Flow:**

```
Cleaned text + emotion + sentiment + intent $\to$ System Prompt $\to$ Gemini $\to$ Chatbot Reply
```

-----

# 🟥 4. `app_streamlit.py` — Main Frontend (UI)

### **Purpose:**

To provide the **user interface** and **orchestrate** the flow between the other three modules.

### **Key Components:**

#### **a) Sidebar & Settings**

  * Allows users to configure LLM parameters (`model_name`, `max_tokens`, `temperature`).
  * Displays and allows interaction with the **Conversation History**.

#### **b) Input & Logic**

  * Collects user input and an optional *user need*.
  * On button press, it triggers the full pipeline:
    1.  Calls `nlp_module.preprocess_text()`.
    2.  Calls `sentiment_module` functions.
    3.  Calls `llm_module.generate_llm()` twice: once for **intent detection** (focused) and once for the **main reply** (empathetic/friendly).
  * Stores the comprehensive result (user text, bot reply, sentiment, emotion, intent) in the Streamlit session state.

#### **c) Display**

  * Shows the full conversation turn (input and reply).
  * Displays the **breakdown of analysis** (Sentiment, Detected Emotion, Detected User Need/Intent) for full transparency.

### **Flow:**

```
UI input $\to$ call NLP $\to$ call sentiment $\to$ call Gemini $\to$ output to screen
```

-----

# 🎯 Summary of Chatbot Pipeline

### **1. User sends a message**

⬇️

### **2. Text cleaned** (`nlp_module.py`)

⬇️

### **3. Sentiment + emotion extracted** (`sentiment_module.py`)

⬇️

### **4. User intent and emotional system prompt prepared**

⬇️

### **5. Gemini generates empathetic reply** (`llm_module.py`)

⬇️

### **6. Output displayed on Streamlit UI** (`app_streamlit.py`)

-----

# 🚀 Features You Can Add Next

  * **Chat Memory:** Implement persistent chat memory (e.g., passing a history of interactions to the LLM).
  * **Database Logging:** Log all interactions, sentiment, and emotions to a database for analytics.
  * **Custom Models:** Allow users to specify custom HuggingFace models in the settings.