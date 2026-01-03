<<<<<<< HEAD
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

nltk.download('punkt')

# -------------------------------
# TRAINING DATA (Symptoms + Disease)
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

# NLP Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ML Model
model = MultinomialNB()
model.fit(X, labels)

# -------------------------------
# PATIENT INPUT
# -------------------------------
print("🩺 AI Medical Assistant\n")

age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()
severity = int(input("Severity level (1–5): "))

print("\nDescribe your symptoms:")
patient_text = input().lower()

patient_vector = vectorizer.transform([patient_text])

# -------------------------------
# AI PREDICTION
# -------------------------------
probs = model.predict_proba(patient_vector)[0]
diseases = model.classes_

# -------------------------------
# WEIGHTING LOGIC
# -------------------------------
weighted_scores = {}

for disease, prob in zip(diseases, probs):
    weight = 1.0

    # Age risk
    if age > 60 and disease in ["Heart Attack", "Diabetes", "COVID-19"]:
        weight += 0.3

    # Gender risk
    if gender == "male" and disease == "Heart Attack":
        weight += 0.2
    if gender == "female" and disease == "Migraine":
        weight += 0.2

    # Severity risk
    weight += severity * 0.1

    weighted_scores[disease] = prob * weight

# -------------------------------
# FINAL RESULT
# -------------------------------
sorted_results = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)

print("\n🧠 AI Diagnosis Result")
print("Most Probable Disease:", sorted_results[0][0])
print(f"Confidence Level: {sorted_results[0][1]*100:.2f}%")

print("\nTop Possible Diseases:")
for d, s in sorted_results[:3]:
    print(f"- {d}")
=======
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

nltk.download('punkt')

# -------------------------------
# TRAINING DATA (Symptoms + Disease)
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

# NLP Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ML Model
model = MultinomialNB()
model.fit(X, labels)

# -------------------------------
# PATIENT INPUT
# -------------------------------
print("🩺 AI Medical Assistant\n")

age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()
severity = int(input("Severity level (1–5): "))

print("\nDescribe your symptoms:")
patient_text = input().lower()

patient_vector = vectorizer.transform([patient_text])

# -------------------------------
# AI PREDICTION
# -------------------------------
probs = model.predict_proba(patient_vector)[0]
diseases = model.classes_

# -------------------------------
# WEIGHTING LOGIC
# -------------------------------
weighted_scores = {}

for disease, prob in zip(diseases, probs):
    weight = 1.0

    # Age risk
    if age > 60 and disease in ["Heart Attack", "Diabetes", "COVID-19"]:
        weight += 0.3

    # Gender risk
    if gender == "male" and disease == "Heart Attack":
        weight += 0.2
    if gender == "female" and disease == "Migraine":
        weight += 0.2

    # Severity risk
    weight += severity * 0.1

    weighted_scores[disease] = prob * weight

# -------------------------------
# FINAL RESULT
# -------------------------------
sorted_results = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)

print("\n🧠 AI Diagnosis Result")
print("Most Probable Disease:", sorted_results[0][0])
print(f"Confidence Level: {sorted_results[0][1]*100:.2f}%")

print("\nTop Possible Diseases:")
for d, s in sorted_results[:3]:
    print(f"- {d}")
>>>>>>> ccee7f6 (Initial commit)
