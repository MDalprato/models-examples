from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Define route for sentiment analysis
@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    # Extract text from request data
    data = request.json
    text = data.get('text')
    
    # Check if text is provided
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Analyze sentiment
    result = sentiment_pipeline(text)
    
    # Return result as JSON
    return jsonify(result)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)