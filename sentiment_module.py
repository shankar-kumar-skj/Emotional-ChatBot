from transformers import pipeline

try:
    sentiment = pipeline("sentiment-analysis")
except:
    sentiment = None

try:
    emotion = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )
except:
    emotion = None


def detect_sentiment(text):
    if not sentiment:
        return {"label": "neutral", "score": 0.0}

    res = sentiment(text)[0]
    return {"label": res["label"], "score": float(res["score"])}


def detect_emotion(text):
    res = emotion(text)

    # always unwrap first level
    res = res[0] if isinstance(res[0], list) else res[0]

    top = max(res, key=lambda x: x["score"])

    return {
        "emotion": top["label"],
        "score": float(top["score"])
    }