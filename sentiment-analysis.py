from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you", "my cat is sick"]
sentiment_pipeline(data)

print(sentiment_pipeline(data))