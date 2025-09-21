from transformers import pipeline
from functools import lru_cache

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@lru_cache(maxsize=100)
def analyze_sentiment(text: str) -> dict:
    try:
        result = sentiment_pipeline(text)[0]  
        return {"label": result["label"], "score": result["score"]}
    except Exception as e:
        return {"label": "ERROR", "score": 0, "detail": str(e)}