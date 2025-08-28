import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from app.extract_features import extract_features

# Load JSON
with open("data/phish-data.json", "r") as f:
    data = json.load(f)

df = pd.json_normalize(data)

# Features
features = df["url"].apply(extract_features)
X = pd.DataFrame(list(features))

# Encode target labels (if needed)
le = LabelEncoder()
y = le.fit_transform(df["target"])  # Converts strings -> ints

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Saving the model for use later
import joblib
joblib.dump(model, "phishing_model.pkl")

