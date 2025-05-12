import requests

# Replace these with your actual Azure Custom Vision details
prediction_key="2ojAfzMubixnhH0hTC4ohIkwHRXIm49T7iOWoUBUB04PGh1N93cSJQQJ99BBACYeBjFXJ3w3AAAIACOG0fds"
prediction_url = "https://ayishawasteclassification-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/32d76491-8186-418c-b276-db7dc7630d50/classify/iterations/Iteration1/image"

# Recycling tips for waste classification
recycling_tips = {
    "recycle": "Please rinse and clean recyclables before putting them in the recycling bin.",
    "organic": "Organic waste can be composted. Consider setting up a compost bin."
}

def classify_image(image_path):
    # Open the user-provided image
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

    # Find the prediction with the highest probability
    highest_prediction = max(result["predictions"], key=lambda x: x["probability"])
    classification = highest_prediction['tagName'].lower()  # Normalize to lowercase
    confidence = highest_prediction['probability'] * 100

    # Print the classification and recycling tip
    print(f"The image is classified as: {classification} with a confidence of {confidence:.2f}%")
    tip = recycling_tips.get(classification, "No tips available for this classification.")
    print(f"Recycling Tip: {tip}")
    
    # Log the result (Optional: Save to a CSV file for analytics)
    with open("classification_log.csv", "a") as log_file:
        log_file.write(f"{image_path},{classification},{confidence:.2f}%\n")

if __name__ == "__main__":
    # Prompt the user to enter the image path
    image_path = input("Enter the path to the image you want to classify: ")
    try:
        classify_image(image_path)
    except Exception as e:
        print(f"An error occurred: {e}")
