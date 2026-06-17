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
    # If the first element is a list, unwrap it; otherwise res itself is the list of dicts
    if isinstance(res[0], list):
        scores = res[0]
    else:
        scores = res
    top = max(scores, key=lambda x: x["score"])
    return {"emotion": top["label"], "score": float(top["score"])}