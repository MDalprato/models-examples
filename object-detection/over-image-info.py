import requests
from PIL import Image
from transformers import pipeline
import requests
from PIL import Image, ImageDraw
from io import BytesIO
from flask import Flask, request, jsonify
from transformers import pipeline
from flask import send_file

# Initialize Flask app
app = Flask(__name__)

# Define route for sentiment analysis
@app.route('/object-dect', methods=['POST'])
def analyze_sentiment():
    # Extract text from request data
    data = request.json
    imageUrl = data.get('imageUrl')
    image_data = requests.get(imageUrl, stream=True).raw
    image = Image.open(image_data)

    # Allocate a pipeline for object detection
    object_detector = pipeline('object-detection')
    detections = object_detector(image)

    # Prepare for drawing
    image_draw = ImageDraw.Draw(image)

    # Draw bounding boxes and labels
    for detection in detections:
        box = detection["box"]
        label = detection["label"]
        score = detection["score"]
        rect = (box["xmin"], box["ymin"], box["xmax"], box["ymax"])
        image_draw.rectangle(rect, outline='red')
        image_draw.text((box["xmin"], box["ymin"]), f'{label}: {score:.2f}', fill='white', background='red')

    # Save the modified image to a BytesIO object
    image_buffer = BytesIO()
    image.save(image_buffer, format='PNG')
    image_buffer.seek(0)

    # Return the modified image as a response
    return send_file(image_buffer, mimetype='image/png')

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)