# Phishing ML

---

### Intro

This is a project I am working on to introduce myself to the world of Machine Learning, using `scikit-learn`.

> NOTE: This project is still in progress.

---

### What?

I am training a Machine Learning model to predict whether a given URL is a phishing link.

---

# Get started

1. Clone the repo:
```shell
git clone https://github.com/SiddDevCS/PhishingML.git
```

2. Go to the project folder:
```shell
cd phishing-ml/
```

3. Set up venv (virtual environment)
```shell
python3 -m venv venv
source venv/bin/activate
```

4. Install libraries
```shell
pip install -r requirements.txt
```

5. Load model into models/ directory
```shell
python3 notebooks/train_model.py
```

6. Finally set up the Flask web app
```shell
python3 app/app.py
```

7. Visit the web app in your browser at: http://127.0.0.1:5000/

---

### Workflow

1. Datasets in `JSON`, for the model to be trained on.
2. `tldextract` categorizing/splitting up the link given.
3. Training the ML model.
4. The ML model giving output if the link given is a phishing link or not.

---

## Project Structure:

```
phishing-detector/
├── data/
├────── fetch.py                # Script to fetch phishing datasets (make sure to use VPN, to not get blocked)
├────── phish-data.json         # JSON datasets
├── notebooks/              
├────── load_data.py            # loads JSON into dataframe
├────── train_model.py          # trains/creates model in models/ dir
├── models/      
├────── phishing_model.pkl      # Trained ML model
├── app/
├────── app.py
├────── extract_features.py     # tldextract splitting up link
├────── static/
├───────────── style.css        # UI
├────── templates/
├───────────── index.html       # UI
├── README.md
└── requirements.txt
```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
