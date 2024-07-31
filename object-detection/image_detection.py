# Description: This script defines a Flask app that performs object detection on an image.
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

# Define route 
@app.route('/object-dect', methods=['POST'])
def analyze_image():
    # Extract text from request data
    data = request.json
    imageUrl = data.get('imageUrl')
    image_data = requests.get(imageUrl, stream=True).raw
    image = Image.open(image_data)

    # Allocate a pipeline for object detection
    object_detector = pipeline('object-detection')
    detections = object_detector(image)

    # Return the modified image as a response
    return jsonify(detections)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)