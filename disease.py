# -------------------------------
# disease.py
# -------------------------------

import nltk
nltk.download('punkt', quiet=True)

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -------------------------------
# TRAINING DATA
# -------------------------------
training_data = [
    ("fever cough headache fatigue body pain", "Flu"),
    ("fever cough loss of taste breathing problem fatigue", "COVID-19"),
    ("fever chills sweating vomiting headache", "Malaria"),
    ("high fever joint pain rash headache", "Dengue"),
    ("chest pain shortness of breath sweating nausea", "Heart Attack"),
    ("frequent urination increased thirst weight loss fatigue", "Diabetes"),
    ("headache nausea light sensitivity", "Migraine"),
    ("breathing problem wheezing chest tightness cough", "Asthma"),
]

texts = [t[0] for t in training_data]
labels = [t[1] for t in training_data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# -------------------------------
# FUNCTION USED BY STREAMLIT
# -------------------------------
def diagnose_any_symptom(symptoms, age=30, gender="male", severity=3):
    symptoms = symptoms.lower()
    X_test = vectorizer.transform([symptoms])

    probs = model.predict_proba(X_test)[0]
    diseases = model.classes_

    weighted = {}
    for d, p in zip(diseases, probs):
        weight = 1.0

        if age > 60 and d in ["Heart Attack", "Diabetes", "COVID-19"]:
            weight += 0.3
        if gender == "male" and d == "Heart Attack":
            weight += 0.2
        if gender == "female" and d == "Migraine":
            weight += 0.2

        weight += severity * 0.1
        weighted[d] = p * weight

    ranked = sorted(weighted.items(), key=lambda x: x[1], reverse=True)
    return "general", [d for d, _ in ranked[:3]]
