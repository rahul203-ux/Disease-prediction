# app.py
import streamlit as st
from disease import diagnose_any_symptom  # your existing code

st.set_page_config(page_title="AI Medical Diagnosis", layout="centered")
st.title("🧠 AI Medical Diagnosis Assistant")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.selectbox("Gender", ["male", "female"])
severity = st.slider("Severity (1–5)", 1, 5)
symptoms = st.text_area("Describe your symptoms here")

if st.button("Analyze"):
    if not symptoms.strip():
        st.warning("Please enter your symptoms!")
    else:
        results = diagnose_any_symptom(symptoms, age=age, gender=gender, severity=severity)

        st.subheader("🧠 AI Diagnosis Result")
        st.write("**Most Probable Disease:**", results[0][0])
        st.write(f"**Confidence Level:** {results[0][1]*100:.2f}%")

        st.write("**Top Possible Diseases:**")
        for disease, score in results[:5]:
            st.write("-", disease)

        st.info("⚠️ This system assists diagnosis. Consult a doctor for confirmation.")
