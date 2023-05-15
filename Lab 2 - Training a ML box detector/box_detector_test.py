import os
import uuid
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import CustomVisionErrorException
from msrest.authentication import ApiKeyCredentials


ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
prediction_key = "26a33723860043d2be8d686388177f57"
training_key = "26a33723860043d2be8d686388177f57"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

training_credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, training_credentials)

project_id = "20253808-76da-4fa7-9646-5e3c59fd4e2f"

# Get the project by project_id
try:
    iterations = trainer.get_iterations(project_id)
    published_iteration = next(iteration for iteration in iterations if iteration.publish_name)
    publish_iteration_name = published_iteration.publish_name
except StopIteration:
    print("No published iteration found. Please publish an iteration in the Custom Vision portal.")
    exit(1)

base_image_location = os.path.join(os.path.dirname(__file__))

# Open the sample image and get back the prediction results.
with open(os.path.join(base_image_location, "test", "test_box.jpg"), mode="rb") as test_data:
    results = predictor.detect_image(project_id, publish_iteration_name, test_data)

# Set the probability threshold (e.g., 0.8 for 80%)
probability_threshold = 0.8

# Display the results.
# The bounding box values are normalized, which means they are in the range of 0 to 1 relative to the image dimensions. 
# To get the actual pixel coordinates, you can multiply these values by the width and height of the image, respectively.
for prediction in results.predictions:
    if prediction.probability >= probability_threshold:
        print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))


# End of code. See code snippets below for different use cases.

'''
# Code snippet to test multiple images.

import os
from glob import glob

# ...

base_image_location = os.path.join(os.path.dirname(__file__), "Images")

# Get all the image files with .jpg extension in the 'test' subdirectory of 'Images' folder
image_files = glob(os.path.join(base_image_location, "test", "*.jpg"))

for image_file in image_files:
    with open(image_file, mode="rb") as test_data:
        results = predictor.detect_image(project_id, publish_iteration_name, test_data)

    print(f"Image: {os.path.basename(image_file)}")
    
    # Display the results.
    for prediction in results.predictions:
        if prediction.probability * 100 >= threshold:
            print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))


'''

###################

'''
# Code snippet to test images using URLs.
import requests

# ...

# List of image URLs to test
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    # Add more URLs as needed
]

for image_url in image_urls:
    # Download the image data from the URL
    response = requests.get(image_url)
    if response.status_code != 200:
        print(f"Error downloading image from {image_url}: {response.status_code}")
        continue

    image_data = response.content

    results = predictor.detect_image(project_id, publish_iteration_name, image_data)

    print(f"Image: {image_url}")

    # Display the results.
    for prediction in results.predictions:
        if prediction.probability * 100 >= threshold:
            print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))

            '''
