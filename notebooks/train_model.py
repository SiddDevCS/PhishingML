import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from extract_f import extract_features

# Load phishing URLs
with open("data/phish-data.json", "r") as f:
    data = json.load(f)

df_phish = pd.json_normalize(data)
df_phish["is_phishing"] = 1  # label phishing as 1

# Add legitimate URLs
df_legit = pd.DataFrame({
    "url": [
        "https://www.google.com",
        "https://www.amazon.com",
        "https://www.wikipedia.org",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ],
    "is_phishing": 0  # label legit as 0
})

# Combine datasets
df = pd.concat([df_phish[["url","is_phishing"]], df_legit], ignore_index=True)

# Extract numeric features only
def numeric_features(url: str):
    f = extract_features(url)
    # Remove string features
    f.pop("domain", None)
    f.pop("suffix", None)
    return f

X = pd.DataFrame(list(df["url"].apply(numeric_features)))
y = df["is_phishing"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["legit", "phishing"]))

# Save trained model
joblib.dump(model, "models/phishing_model.pkl")
print("Model saved to models/phishing_model.pkl")
