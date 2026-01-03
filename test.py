import streamlit as st
import disease   # <-- your existing file

st.title("🧠 AI Medical Diagnosis Assistant")

age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["male", "female"])
severity = st.slider("Severity (1–5)", 1, 5)

symptoms = st.text_area("Describe your symptoms")

if st.button("Analyze"):
    if symptoms.strip() == "":
        st.warning("Please enter symptoms")
    else:
        system, diseases = disease.diagnose_any_symptom(symptoms)

        st.subheader("🧠 AI Analysis Result")
        st.write("**Affected Body System:**", system.capitalize())
        st.write("**Possible Diseases:**")
        for d in diseases:
            st.write("-", d)

        st.info("⚠️ This system assists diagnosis. Consult a doctor for confirmation.")
