import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap

# Set page config
st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

# ----- Custom CSS for Visual Appeal -----
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf, #2e7bcf);
        color: white;
    }
    .stButton>button {
        background-color: #2e7bcf;
        color: white;
        border: none;
        padding: 0.6em 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Customer Churn Prediction")
st.markdown("Enter the customer details below to predict churn:")

# ----- Load your pre-trained model and any additional objects (like a SHAP explainer) -----
@st.cache(allow_output_mutation=True)
def load_objects():
    # Replace with your actual model and explainer filenames
    model = joblib.load("customer_churn_model.pkl")
    explainer = joblib.load("shap_explainer.pkl")
    return model, explainer

model, explainer = load_objects()

# ----- Input Form for Prediction -----
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=120, value=12)
    with col2:
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=500.0, value=70.0)
        contract_type = st.selectbox("Contract Type", options=["Month-to-month", "One year", "Two year"])
    
    # Add more input fields as needed matching your model’s features
    
    submitted = st.form_submit_button("Predict")

if submitted:
    # ----- Preprocess inputs -----
    # Here you should match your notebook’s preprocessing steps
    input_data = pd.DataFrame({
        "age": [age],
        "tenure": [tenure],
        "monthly_charges": [monthly_charges],
        "contract_type": [contract_type]
    })
    # (For categorical variables, ensure you perform the same encoding/scaling as in your notebook.)

    # ----- Predict Outcome -----
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]  # assuming probability for churn is the second column
    
    result_text = "Churn" if prediction == 1 else "No Churn"
    st.subheader(f"Prediction: {result_text}")
    st.write(f"**Probability of churn:** {probability:.2f}")

    # ----- Local Explainability using SHAP -----
    st.subheader("Local Explanation")
    # Compute SHAP values for the single input
    shap_values = explainer.shap_values(input_data)
    
    # Create a bar summary plot for the explanation
    fig, ax = plt.subplots(figsize=(10, 3))
    shap.summary_plot(shap_values, input_data, plot_type="bar", show=False)
    st.pyplot(fig)
