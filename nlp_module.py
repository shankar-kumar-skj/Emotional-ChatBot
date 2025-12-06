"""NLP preprocessing module"""
import re

def preprocess_text(text: str) -> str:
    """
    Minimal preprocessing: strip, normalize whitespace.
    Extend this function if you want tokenization, stopword removal, etc.
    """
    if text is None:
        return ""
    s = text.strip()
    s = re.sub(r"\s+", " ", s)
    return s
