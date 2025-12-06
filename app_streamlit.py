import streamlit as st
from nlp_module import preprocess_text
from sentiment_module import detect_sentiment, detect_emotion
from llm_module import generate_llm

# -------------------------
# Page Config
# -------------------------
st.set_page_config("Emotional Chatbot (Gemini)", layout="wide")
st.title("Emotional Chatbot — Gemini + NLP + Sentiment")

# -------------------------
# Session State
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []  # Each entry: {user, bot, emotion, sentiment, intent}
if "selected_index" not in st.session_state:
    st.session_state.selected_index = None

# -------------------------
# Sidebar: Settings + History
# -------------------------
with st.sidebar:
    st.header("Settings")
    model_name = st.text_input("Gemini model", value="gemini-2.5-flash")
    max_tokens = st.slider("Max output tokens", 50, 1024, 250)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    # Style sidebar buttons like first version
    st.markdown(
        """
        <style>
        button[kind="secondary"] {
            width: 200px !important;
            height: 40px !important;
            text-align: left !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.header("Conversation History")
    if st.session_state.history:
        for i, turn in enumerate(reversed(st.session_state.history)):
            idx = len(st.session_state.history) - 1 - i
            if st.button(f"{turn['user'][:30]}...", key=f"hist_{idx}"):
                st.session_state.selected_index = idx
    else:
        st.info("No previous conversation.")

# -------------------------
# Main Input Area
# -------------------------
st.subheader("New Message")
user_input = st.text_area("You:", height=150)
st.markdown("### Optional: Help us understand your need")
user_need = st.text_input("What would you like help with? (optional)")

# -------------------------
# Send Button
# -------------------------
if st.button("Send") and user_input.strip():
    # Preprocess input
    text = preprocess_text(user_input)

    # Sentiment and emotion detection
    sentiment = detect_sentiment(text)
    emotion_res = detect_emotion(text)
    emotion = emotion_res.get("emotion", "neutral")

    # Detect user intent
    intent_prompt = f"Determine the user's main need or intent from: '{text}'"
    if user_need:
        intent_prompt += f" User additionally says: '{user_need}'"
    user_intent = generate_llm(
        intent_prompt,
        model=model_name,
        max_output_tokens=150,
        temperature=0.5,
        user_need=user_need
    )

    # Build adaptive LLM response
    tone = "empathetic" if emotion in ["sadness", "fear", "anger"] else "friendly"
    explanation_prompt = (
        f"You are a {tone} AI assistant.\n"
        f"Explain the input '{text}' in short points.\n"
        f"Detected emotion: {emotion}\n"
        f"Sentiment: {sentiment['label']} (score {sentiment['score']:.2f})\n"
        f"User intent/need: {user_intent}\n"
        f"Provide a helpful, human-like response considering user emotion and intent."
    )

    # Generate LLM reply
    reply = generate_llm(
        explanation_prompt,
        model=model_name,
        max_output_tokens=max_tokens,
        temperature=temperature,
        user_need=user_need
    )

    # Save conversation
    st.session_state.history.append({
        "user": text,
        "bot": reply,
        "emotion": emotion,
        "sentiment": sentiment,
        "intent": user_intent
    })
    st.session_state.selected_index = len(st.session_state.history) - 1

# -------------------------
# Display Conversation
# -------------------------
if st.session_state.selected_index is not None:
    turn = st.session_state.history[st.session_state.selected_index]

    st.subheader("Conversation Details")

    # Explanation
    st.markdown("### 📝 Explanation")
    st.info(turn['bot'])

    # Sentiment
    st.markdown("### 🙂 Sentiment")
    st.success(f"{turn['sentiment']['label']} (score {turn['sentiment']['score']:.2f})")

    # Emotion
    st.markdown("### 😐 Detected Emotion")
    st.warning(turn['emotion'])

    # User Intent
    st.markdown("### 🎯 Detected User Need / Intent")
    st.info(turn['intent'])
else:
    st.info("Send a message or select a conversation from history.")
