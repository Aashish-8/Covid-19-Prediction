import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load("icu_predict_model.pkl")

st.title("🧠 COVID-19 ICU Prediction App")

st.markdown("Fill in the patient info to predict ICU requirement.")

# Feature input form
USMER = st.selectbox("🧪 USMER Medical Unit", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
MEDICAL_UNIT = st.slider("🏥 Medical Unit", 1, 20)
SEX = st.selectbox("🧑 Sex", [1, 2], format_func=lambda x: "Male" if x == 1 else "Female")
PATIENT_TYPE = st.selectbox("🏨 Patient Type", [1, 2], format_func=lambda x: "Outpatient" if x == 1 else "Hospitalized")
DATE_DIED = st.slider("📅 Date Died (days since Jan 1)", 1, 366)
INTUBED = st.selectbox("🫁 Intubed", [0, 1, 97, 98, 99], format_func=lambda x: {0: "No", 1: "Yes", 97: "Unknown", 98: "Not Applied", 99: "Not Known"}.get(x, str(x)))
PNEUMONIA = st.selectbox("🦠 Pneumonia", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
AGE = st.slider("🎂 Age", 0, 120)
PREGNANT = st.selectbox("🤰 Pregnant", [0, 1, 97, 98, 99], format_func=lambda x: {0: "No", 1: "Yes", 97: "Unknown", 98: "Not Applied", 99: "Not Known"}.get(x, str(x)))
DIABETES = st.selectbox("🍬 Diabetes", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
COPD = st.selectbox("💨 COPD", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
ASTHMA = st.selectbox("🌬 Asthma", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
INMSUPR = st.selectbox("🛡 Immunosuppressed", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
HIPERTENSION = st.selectbox("🩸 Hypertension", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
OTHER_DISEASE = st.selectbox("🧬 Other Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
CARDIOVASCULAR = st.selectbox("❤️ Cardiovascular Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
OBESITY = st.selectbox("⚖ Obesity", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
RENAL_CHRONIC = st.selectbox("🧫 Chronic Renal Failure", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
TOBACCO = st.selectbox("🚬 Tobacco Use", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
CLASIFFICATION_FINAL = st.selectbox("📊 Final Classification", [1, 2, 3], format_func=lambda x: f"Class {x}")

# Predict button
if st.button("🔍 Predict ICU Need"):
    input_data = np.array([
        USMER, MEDICAL_UNIT, SEX, PATIENT_TYPE, DATE_DIED,
        INTUBED, PNEUMONIA, AGE, PREGNANT, DIABETES,
        COPD, ASTHMA, INMSUPR, HIPERTENSION, OTHER_DISEASE,
        CARDIOVASCULAR, OBESITY, RENAL_CHRONIC, TOBACCO, CLASIFFICATION_FINAL
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 The patient is likely to need ICU care.")
    else:
        st.success("✅ The patient is not likely to need ICU care.")
