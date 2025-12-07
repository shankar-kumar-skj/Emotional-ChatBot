# Emotional Chatbot Using NLP + Sentiment Analysis + Gemini LLM

This project is an **emotion-aware chatbot** built using:

* **NLP preprocessing**
* **Sentiment analysis (HuggingFace models)**
* **Emotion classification**
* **Google Gemini LLM** for intelligent emotional responses
* **Streamlit** for UI

It takes user input → processes emotion → generates an emotionally aligned reply.

---

# 📌 Project Structure

emotional_chatbot/
│── app_streamlit.py
│── llm_module.py
│── nlp_module.py
│── sentiment_module.py
│── .env
│── requirements.txt
│── README.md

yaml
Copy code

---

# 📌 How The System Works (Flow Diagram)

pgsql
Copy code
  USER INPUT
      |
      v
┌─────────────────┐
│ NLP Processing │ <- (nlp_module.py)
└─────────────────┘
|
v
┌────────────────────────┐
│ Sentiment Analysis │
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
│ Generate Response (LLM) │
└────────────────────────────┘
|
v
CHATBOT RESPONSE

yaml
Copy code

---

# 📌 Setup Instructions (Step-by-Step)

### **1. Clone the repository**

git clone https://github.com/shankar-kumar-skj/Emotional-ChatBot.git
cd Emotional-ChatBot

markdown
Copy code

### **2. Create `.env` file**

GEMINI_API_KEY=your_api_key_here

markdown
Copy code

### **3. Install required packages**

pip install -r requirements.txt

markdown
Copy code

### **4. Run the project**

streamlit run app_streamlit.py

yaml
Copy code

---

# 📌 Code Explanation (Module-by-Module)

Below is a **clear, block-by-block explanation** of every file.

---

# 🟦 1. `nlp_module.py` — NLP Preprocessing

### **Purpose:**
Prepare user's text before sentiment analysis or LLM input.

### **Main Functions:**

#### **a) `preprocess_text(text)`**
* Strips extra spaces
* Normalizes text
* Removes unnecessary characters

### **Flow:**
Input text → cleaned text → return

yaml
Copy code

---

# 🟩 2. `sentiment_module.py` — Sentiment + Emotion Detection

### **Purpose:**
Detect **how the user feels**.

### **Uses Two Models:**
1. **Sentiment model**: Positive / Negative / Neutral
2. **Emotion model**: joy, anger, sadness, fear, love, etc.

### **Main Functions:**

#### **a) `detect_sentiment(text)`**
* Uses HuggingFace DistilBERT
* Returns sentiment label + confidence score

#### **b) `detect_emotion(text)`**
* Uses RoBERTa emotion model
* Returns highest-scored emotion

### **Flow:**
Input text → HF models → sentiment + emotion → return

yaml
Copy code

---

# 🟨 3. `llm_module.py` — Gemini LLM Integration + Fallback

### **Purpose:**
Generate chatbot responses using Gemini LLM.

### **Features:**
* Loads `.env` for GEMINI_API_KEY
* Uses **Gemini 2.5 Flash** model
* Adds emotional context to prompts
* Fallback to GPT-2 if Gemini unavailable

### **Main Steps:**
1. Load key & configure Gemini
2. Build dynamic prompt with system instructions + user input
3. Generate response (Gemini or GPT-2 fallback)

### **Flow:**
cleaned text + emotions → system prompt → Gemini → chatbot reply

markdown
Copy code

---

# 🟥 4. `app_streamlit.py` — Main Frontend (UI)

### **Purpose:**
Provide a user interface for chatbot interaction.

### **Key Components:**
* **Title & layout**: `st.title("Emotional Chatbot — NLP + Sentiment + LLM")`
* **Input box**: `user_text = st.text_area("You:")`
* **Send button flow**:
  1. Preprocess text → `preprocess_text()`
  2. Detect sentiment → `detect_sentiment()`
  3. Detect emotion → `detect_emotion()`
  4. Build LLM prompt → `generate_llm()`
  5. Save conversation to session history
* **Conversation history**: Displays previous messages

### **Flow:**
UI input → NLP → sentiment/emotion detection → LLM → output display

yaml
Copy code

---

# 🎯 Summary of Chatbot Pipeline

1. User sends message  
2. Text preprocessing (`nlp_module.py`)  
3. Sentiment & emotion detection (`sentiment_module.py`)  
4. System prompt prepared  
5. Gemini generates empathetic reply (`llm_module.py`)  
6. Output displayed on Streamlit UI (`app_streamlit.py`)

---

# 🚀 Future Enhancements

* Persistent chat memory
* Voice input (STT)
* Voice output (TTS)
* Database logging
* Animated and interactive UI
* Multi-language support