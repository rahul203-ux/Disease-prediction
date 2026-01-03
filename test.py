import streamlit as st
import disease   # import the ML/NLP logic

st.title("🧠 AI Medical Diagnosis Assistant")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.selectbox("Gender", ["male", "female"])
severity = st.slider("Severity Level (1–5)", 1, 5)
symptoms = st.text_area("Describe your symptoms")

if st.button("Analyze"):
    if symptoms.strip() == "":
        st.warning("Please enter symptoms")
    else:
        results = disease.diagnose_any_symptom(symptoms, age, gender, severity)
        most_probable = results[0]

        st.subheader("🧠 AI Diagnosis Result")
        st.write("Most Probable Disease:", most_probable[0])
        st.write(f"Confidence Level: {most_probable[1]*100:.2f}%")

        st.write("\nTop Possible Diseases:")
        for d, s in results[:3]:
            st.write("-", d)
        
        st.info("⚠️ This system is for decision support. Consult a doctor for confirmation.")
