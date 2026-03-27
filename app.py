import streamlit as st
import pandas as pd
import joblib

#making app

model = joblib.load("Fraud_detection_pipeline.pkl")

st.title("Fraud Detection")
st.markdown("Please enter the transaction details and predict the fraud")
st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","CASH_IN"])
amount = st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg= st.number_input("OLd Balance (sender) ",min_value=0.0,value=1000.0)
newbalanceOrig = st.number_input("New Balance (sender)", min_value=0.0,value=1000.0)
oldbalanceDest = st.number_input("Old Balance (reciver)", min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Balance (reciver)", min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount": amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    st.subheader("Result")

    if prediction == 1:
        st.error(f"Fraud Detected (Confidence: {proba:.2%})")
    else:
        st.success(f" Not Fraud (Confidence: {1 - proba:.2%})")

    st.progress(float(proba))

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction does not look like a fraud")