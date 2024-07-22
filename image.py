import requests
from PIL import Image
from transformers import pipeline
import json
import requests
from PIL import Image, ImageDraw
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Download an image with cute cats
url = "https://www.marcodalprato.com/event.jpg"
image_data = requests.get(url, stream=True).raw
image = Image.open(image_data)

# Allocate a pipeline for object detection
object_detector = pipeline('object-detection')
detections = object_detector(image)


#print(json.dumps(out, indent=4))

# URL of the image
image_url = "https://www.marcodalprato.com/event.jpg"

# Download the image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Prepare for drawing
fig, ax = plt.subplots(1)
ax.imshow(image)


# Draw bounding boxes and labels
for detection in detections:
    box = detection["box"]
    label = detection["label"]
    score = detection["score"]
    rect = patches.Rectangle((box["xmin"], box["ymin"]), box["xmax"] - box["xmin"], box["ymax"] - box["ymin"], linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.text(box["xmin"], box["ymin"], f'{label}: {score:.2f}', color='white', fontsize=8, backgroundcolor="red")

plt.axis('off')  # Hide the axis
plt.show()  # Display the image with bounding boxes and labels