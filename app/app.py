from flask import Flask, request, jsonify, render_template_string
import joblib
from notebooks.extract_features import extract_features
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load("models/phishing_model.pkl")

# Simple HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phishing URL Detection</title>
</head>
<body>
    <h1>Phishing URL Detection</h1>
    <form method="post" action="/predict">
        <label for="url">Enter URL:</label><br>
        <input type="text" id="url" name="url" size="50"><br><br>
        <input type="submit" value="Check URL">
    </form>
    {% if result %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form.get("url")
    if not url:
        return render_template_string(HTML_TEMPLATE, result="No URL provided")

    features = extract_features(url)
    X = pd.DataFrame([features])
    pred = model.predict(X)[0]

    result = "phishing" if pred == 1 else "legit"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
