# Phishing ML

### Intro

> This is a project I am working on to introduce myself to the world of Machine Learning, using `scikit-learn`.

### What?

I am training a Machine Learning model to predict whether a given URL is a phishing link.

### How?

1. Datasets in `JSON` or `csv`, for the model to be trained on.
2. `tldextract` categorizing/splitting up the link given.
3. Training the ML model.
4. The ML model giving output if the link given is a phishing link or not.

## Project Structure:

```
phishing-detector/
├── data/        # CSV/JSON datasets
├── notebooks/   # Experimentation and feature extraction scripts
├── models/      # Trained ML models
├── app/         # Flask API code
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
