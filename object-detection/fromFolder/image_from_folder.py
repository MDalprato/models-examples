# getting objects from local images and storing them in MongoDB
import os
from PIL import Image
from transformers import pipeline
import pymongo

# Get the path of the images folder
folder_path = './camera02'

# List all the image files in the folder
image_files = os.listdir(folder_path)

# Iterate over each image file
for image_file in image_files:
    # Construct the full path of the image file
    image_path = os.path.join(folder_path, image_file)
    
    # Check if the file ends with .jpg
    if image_file.endswith('.jpg'):
        # Open the image file
        image = Image.open(image_path)
        
        # Allocate a pipeline for object detection
        object_detector = pipeline('object-detection')
        
        # Perform object detection on the image
        detections = object_detector(image)

        # Convert detections to a dictionary
        detections_dict = {"detections": detections}

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        # Access the "detection" collection
        db = client["your_database_name"]
        collection = db["detection"]

        # Insert the detections into the collection
        collection.insert_one(detections_dict)

        print("Detections inserted into MongoDB")

print("Done")