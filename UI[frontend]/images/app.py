from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Azure Custom Vision details
PREDICTION_KEY="2ojAfzMubixnhH0hTC4ohIkwHRXIm49T7iOWoUBUB04PGh1N93cSJQQJ99BBACYeBjFXJ3w3AAAIACOG0fds"
PREDICTION_URL = "https://ayishawasteclassification-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/32d76491-8186-418c-b276-db7dc7630d50/classify/iterations/Iteration1/image"

# Dictionary to store disposal tips for only Organic and Recycle
DISPOSAL_TIPS = {
    "Organic": "Compost organic waste or dispose of it in biodegradable bins.",
    "Recycle": "Separate recyclables and drop them in a designated recycling bin."
}

@app.route('/')
def index():
    return send_from_directory('.', 'index1.html')  # Serves the HTML file

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    
    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(PREDICTION_URL, headers=headers, data=image.read())

    # Print the response for debugging
    print("Azure Response Status Code:", response.status_code)
    print("Azure Response Content:", response.text)

    if response.status_code != 200:
        return jsonify({"error": "Classification failed"}), response.status_code

    result = response.json()
    highest_prediction = max(result["predictions"], key=lambda x: x["probability"])
    
    classification = highest_prediction['tagName']
    confidence = highest_prediction['probability'] * 100

    # Get disposal tip only for "Organic" and "Recycle"
    tip = DISPOSAL_TIPS.get(classification, "No tip available for this category.")

    return jsonify({
        "classification": classification,
        "confidence": confidence,
        "tip": tip
    })

if __name__ == '__main__':
    app.run(debug=True)
