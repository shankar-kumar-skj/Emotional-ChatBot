import streamlit as st
from nlp_module import preprocess_text
from sentiment_module import detect_sentiment, detect_emotion
from llm_module import generate_llm
from agents.emotion_agent import get_emotion_context
from agents.memory_agent import MemoryAgent
from agents.rag_agent import RAGAgent

# -------------------------
# INIT AGENTS
# -------------------------
memory = MemoryAgent()
rag = RAGAgent()

# -------------------------
# UI CONFIG
# -------------------------
st.set_page_config("Agentic Emotional AI Assistant", layout="wide")
st.title("🤖 Agentic Emotional AI Assistant (Advanced Version)")

# Debug mode toggle
debug_mode = st.sidebar.checkbox("🧠 Debug Mode (Show Agent Outputs)", value=True)

# -------------------------
# SESSION STATE
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# INPUT
# -------------------------
user_input = st.text_area("Enter your message")
user_need = st.text_input("Optional context")

# -------------------------
# RUN PIPELINE
# -------------------------
if st.button("Send") and user_input.strip():

    # 1. NLP
    text = preprocess_text(user_input)

    # 2. Emotion Agent
    emotion_data = get_emotion_context(text)

    # 3. Sentiment Agent
    sentiment = detect_sentiment(text)

    # 4. Memory Agent
    past_memory = memory.get_memory()

    # 5. RAG Agent
    rag_context = rag.retrieve(text)

    # 6. Prompt Engineering
    prompt = f"""
You are an empathetic AI assistant.

User Input: {text}

Emotion: {emotion_data['emotion']}
Tone: {emotion_data['tone']}
Sentiment: {sentiment['label']}

Memory Context:
{past_memory}

Knowledge Base:
{rag_context}

Respond in a supportive, human-like way.
"""

    # 7. LLM Response
    reply = generate_llm(prompt)

    # 8. Save Memory
    memory.add_memory(text, reply)

    # 9. Store History
    st.session_state.history.append({
        "user": text,
        "bot": reply,
        "emotion_agent": emotion_data,
        "sentiment_agent": sentiment,
        "memory_agent": past_memory,
        "rag_agent": rag_context
    })

# -------------------------
# DISPLAY CHAT
# -------------------------
st.subheader("💬 Conversation History")

for chat in reversed(st.session_state.history):

    st.markdown("### 🧑 User")
    st.info(chat["user"])

    st.markdown("### 🤖 Bot")
    st.success(chat["bot"])

    # -------------------------
    # AGENT OUTPUTS (DEBUG VIEW)
    # -------------------------
    if debug_mode:
        with st.expander("🧠 Agent Outputs (Click to Expand)"):

            st.markdown("#### 🎭 Emotion Agent")
            st.json(chat["emotion_agent"])

            st.markdown("#### 📊 Sentiment Agent")
            st.json(chat["sentiment_agent"])

            st.markdown("#### 💾 Memory Agent")
            st.json(chat["memory_agent"])

            st.markdown("#### 📚 RAG Agent")
            st.json(chat["rag_agent"])

    st.markdown("---")