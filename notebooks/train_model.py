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

# Very large list of legitimate URLs
df_legit = pd.DataFrame({
    "url": [
        "https://www.google.com",
        "https://www.amazon.com",
        "https://www.wikipedia.org",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.linkedin.com",
        "https://www.instagram.com",
        "https://www.reddit.com",
        "https://www.netflix.com",
        "https://www.tesla.com",
        "https://www.paypal.com",
        "https://www.nytimes.com",
        "https://www.bbc.com",
        "https://www.cnn.com",
        "https://www.quora.com",
        "https://www.medium.com",
        "https://www.twitch.tv",
        "https://www.spotify.com",
        "https://www.dropbox.com",
        "https://www.adobe.com",
        "https://www.salesforce.com",
        "https://www.airbnb.com",
        "https://www.booking.com",
        "https://www.udemy.com",
        "https://www.coursera.org",
        "https://www.khanacademy.org",
        "https://www.stackexchange.com",
        "https://www.zoom.us",
        "https://www.slack.com",
        "https://www.wework.com",
        "https://www.nike.com",
        "https://www.etsy.com",
        "https://www.ebay.com",
        "https://www.walmart.com",
        "https://www.target.com",
        "https://www.homedepot.com",
        "https://www.ikea.com",
        "https://www.intuit.com",
        "https://www.oracle.com",
        "https://www.ibm.com",
        "https://www.sap.com",
        "https://www.mozilla.org",
        "https://www.chrome.com",
        "https://www.firefox.com",
        "https://www.yahoo.com",
        "https://www.bing.com",
        "https://www.wikipedia.com",
        "https://www.nationalgeographic.com",
        "https://www.sciencedaily.com",
        "https://www.weather.com",
        "https://www.tripadvisor.com",
        "https://www.imdb.com",
        "https://www.rottentomatoes.com",
        "https://www.kickstarter.com",
        "https://www.patreon.com",
        "https://www.behance.net",
        "https://www.dribbble.com",
        "https://www.chase.com",
        "https://www.bankofamerica.com",
        "https://www.wellsfargo.com",
        "https://www.citigroup.com",
        "https://www.hsbc.com",
        "https://www.barclays.co.uk",
        "https://www.ubank.com",
        "https://www.goldmansachs.com",
        "https://www.morganstanley.com",
        "https://www.nasa.gov",
        "https://www.whitehouse.gov",
        "https://www.fbi.gov",
        "https://www.cia.gov",
        "https://www.nps.gov",
        "https://www.usa.gov",
        "https://www.state.gov",
        "https://www.un.org",
        "https://www.worldbank.org",
        "https://www.imf.org",
        "https://www.harvard.edu",
        "https://www.stanford.edu",
        "https://www.mit.edu",
        "https://www.ox.ac.uk",
        "https://www.cam.ac.uk",
        "https://www.yale.edu",
        "https://www.princeton.edu",
        "https://www.berkeley.edu",
        "https://www.cmu.edu",
        "https://www.duke.edu",
        "https://www.courant.edu",
        "https://www.cnn.com",
        "https://www.foxnews.com",
        "https://www.npr.org",
        "https://www.theguardian.com",
        "https://www.economist.com",
        "https://www.wsj.com",
        "https://www.forbes.com",
        "https://www.techcrunch.com",
        "https://www.wired.com",
        "https://www.engadget.com",
        "https://www.theverge.com",
        "https://www.gizmodo.com",
        "https://www.huffpost.com",
        "https://www.buzzfeed.com",
        "https://www.cnet.com",
        "https://www.digitaltrends.com",
        "https://www.lifehacker.com",
        "https://www.ted.com",
        "https://www.coursera.org",
        "https://www.edx.org",
        "https://www.khanacademy.org",
        "https://www.udacity.com",
        "https://www.skillshare.com",
        "https://www.pluralsight.com",
        "https://www.lynda.com",
        "https://www.codecademy.com"
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
