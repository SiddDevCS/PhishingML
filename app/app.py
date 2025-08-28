from flask import Flask, request, jsonify, render_template_string
import joblib
from extract_features import extract_features
import pandas as pd


app = Flask(__name__)

# Load the model
model = joblib.load("models/phishing_model.pkl")

# Simple HTML form template
form_html = """
<!doctype html>
<html>
    <head><title>Phishing URL Detector</title></head>
    <body>
        <h1>Phishing URL Detector</h1>
        <form method="post" action="/predict_url">
            URL: <input type="text" name="url" size="50">
            <input type="submit" value="Check">
        </form>
        {% if prediction %}
            <h2>Result: {{ prediction }}</h2>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(form_html)

@app.route("/predict_url", methods=["POST"])
def predict_url():
    url = request.form.get("url")
    if not url:
        return render_template_string(form_html, prediction="No URL provided!")

    features = extract_features(url)
    X = pd.DataFrame([features])
    pred = model.predict(X)[0]
    result = "phishing" if pred == 1 else "legit"

    return render_template_string(form_html, prediction=result)

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    features = extract_features(url)
    X = pd.DataFrame([features])
    pred = model.predict(X)[0]
    result = "phishing" if pred == 1 else "legit"
    return jsonify({"url": url, "prediction": result})

if __name__ == "__main__":
    app.run(debug=True)