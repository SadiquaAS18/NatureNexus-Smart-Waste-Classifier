#import requests

# Replace with your Custom Vision Prediction Key and URL
#prediction_key="2ojAfzMubixnhH0hTC4ohIkwHRXIm49T7iOWoUBUB04PGh1N93cSJQQJ99BBACYeBjFXJ3w3AAAIACOG0fds"
#prediction_url = "https://ayishawasteclassification-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/32d76491-8186-418c-b276-db7dc7630d50/classify/iterations/Iteration1/image"
# Open an image file to send for prediction
#image_path = "/Users/ayishakhanmj/Desktop/aimodel/images.jpeg"
#with open(image_path, "rb") as image_file:
    #image_data = image_file.read()

# Set headers for the request
#headers = {
 #   "Prediction-Key": prediction_key,
  #  "Content-Type": "application/octet-stream"
#}

# Send the image to the Custom Vision endpoint
#response = requests.post(prediction_url, headers=headers, data=image_data)
#result = response.json()

# Print the classification result
#print("Prediction:", result)
import requests

# Replace these with your actual values
prediction_key="2ojAfzMubixnhH0hTC4ohIkwHRXIm49T7iOWoUBUB04PGh1N93cSJQQJ99BBACYeBjFXJ3w3AAAIACOG0fds"
prediction_url = "https://ayishawasteclassification-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/32d76491-8186-418c-b276-db7dc7630d50/classify/iterations/Iteration1/image"
# Open an image file to send for prediction
image_path = "/Users/ayishakhanmj/Desktop/aimodel/backend/images/a-Sustainable-Way-to-Manage-Organic-Waste.jpg"
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Set headers for the request
headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/octet-stream"
}

# Send the image to the Custom Vision endpoint
response = requests.post(prediction_url, headers=headers, data=image_data)
result = response.json()

# Find the highest probability prediction
highest_prediction = max(result["predictions"], key=lambda x: x["probability"])

# Print the result
print(f"The image is classified as: {highest_prediction['tagName']} with a confidence of {highest_prediction['probability'] * 100:.2f}%")
