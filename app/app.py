from flask import Flask, render_template, request, jsonify
import joblib
from extract_features import extract_features
import pandas as pd
import os

app = Flask(__name__)

# load the trained model
model = joblib.load("models/phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    url = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            features = extract_features(url)
            X = pd.DataFrame([features])
            pred = model.predict(X)[0]
            prediction = "Phishing" if pred == 1 else "Legit"
    return render_template("index.html", prediction=prediction, url=url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)