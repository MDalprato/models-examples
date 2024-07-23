# from transformers import pipeline
# unmasker = pipeline('fill-mask', model='distilroberta-base')
# out = unmasker("During a <mask> day the temperature drops and the wind increases.")
# print(out);


from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load sentiment analysis pipeline
mask_pipeline = pipeline('fill-mask', model='distilroberta-base')

# Define route for sentiment analysis
@app.route('/mask', methods=['POST'])
def analyze_sentiment():
    # Extract text from request data
    data = request.json
    text = data.get('text')
    
    # Check if text is provided
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Analyze sentiment
    result = mask_pipeline(text)
    
    # Return result as JSON
    return jsonify(result)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)