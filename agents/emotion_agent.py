from sentiment_module import detect_emotion

def get_emotion_context(text):
    result = detect_emotion(text)

    emotion = result["emotion"]

    tone_map = {
        "joy": "positive",
        "sadness": "empathetic",
        "anger": "calm-down",
        "fear": "supportive",
        "neutral": "friendly"
    }

    return {
        "emotion": emotion,
        "tone": tone_map.get(emotion, "neutral"),
        "confidence": result["score"]
    }