"""Sentiment and Emotion detection module"""
from transformers import pipeline

# Initialize pipelines
try:
    # Sentiment analysis
    sentiment_analyzer = pipeline("sentiment-analysis")
except Exception as e:
    print("Sentiment pipeline init error:", e)
    sentiment_analyzer = None

try:
    # Emotion detection
    emotion_analyzer = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )
except Exception as e:
    print("Emotion pipeline init error:", e)
    emotion_analyzer = None

# -------------------------
# Sentiment Detection
# -------------------------
def detect_sentiment(text):
    if not sentiment_analyzer:
        return {"label": "neutral", "score": 0.0}
    try:
        result = sentiment_analyzer(text)[0]
        return {"label": result["label"], "score": float(result["score"])}
    except Exception as e:
        print("Sentiment error:", e)
        return {"label": "neutral", "score": 0.0}

# -------------------------
# Emotion Detection
# -------------------------
def detect_emotion(text):
    if not emotion_analyzer:
        return {"emotion": "neutral", "score": 0.0}
    try:
        result = emotion_analyzer(text)[0]
        # pick top emotion
        top = max(result, key=lambda x: x['score'])
        return {"emotion": top['label'], "score": float(top['score'])}
    except Exception as e:
        print("Emotion error:", e)
        return {"emotion": "neutral", "score": 0.0}
