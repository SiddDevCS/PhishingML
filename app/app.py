from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os
import sys

# Add the app directory to the Python path
sys.path.append(os.path.dirname(__file__))
from extract_features import extract_features

app = Flask(__name__, static_folder='static', static_url_path='/static')

# load the trained model with proper path handling
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "phishing_model.pkl")
model = joblib.load(model_path)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    url = ""
    error = None
    
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                features = extract_features(url)
                X = pd.DataFrame([features])
                pred = model.predict(X)[0]
                prediction = "Phishing" if pred == 1 else "Legit"
            except Exception as e:
                error = f"Error processing URL: {str(e)}"
    
    return render_template("index.html", prediction=prediction, url=url, error=error)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "message": "Phishing detector is running"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)