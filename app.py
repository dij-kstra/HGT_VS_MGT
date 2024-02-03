# app.py
import streamlit as st
from logistic_regression import predict_logistic_regression
#from dummy import predict_dummy

st.title("Text Classification Application")
st.write('HGT VS MGT')

# User input
text_input = st.text_area("Enter your text here:", "")

#Model selection
model_option = st.sidebar.selectbox("Select Model", ["Logistic Regression", "Dummy Model"])

# Prediction
if st.button("Predict"):
    if model_option == "Logistic Regression":
        prediction = predict_logistic_regression(text_input)
    # elif model_option == "Dummy Model":
    #     prediction = predict_dummy(text_input)
    else:
        st.error("Invalid model selection")

    st.success(f"Prediction: {prediction}")
