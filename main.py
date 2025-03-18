import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap
from PIL import Image

# -- Page Configuration --
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="wide")

# -- Custom CSS Styling for a Creative, Modern Look --
st.markdown(
    """
    <style>
    /* Overall background */
    body {
        background: linear-gradient(135deg, #f7f9fc, #e2e8f0);
        font-family: 'Segoe UI', sans-serif;
    }
    /* Main container styling */
    .main-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    /* Sidebar style */
    .css-1d391kg {
        background: linear-gradient(180deg, #2e7bcf, #2e7bcf);
        color: white;
    }
    /* Custom button style */
    .stButton>button {
        background-color: #2e7bcf;
        color: white;
        border: none;
        padding: 0.7em 1.2em;
        font-size: 1em;
        border-radius: 8px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #23609b;
    }
    /* Input elements styling */
    .stTextInput>div>input, .stNumberInput>div>input, .stSelectbox>div>div {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -- Header Banner (Optional) --
# Replace the URL with your own logo/banner image if available
banner = Image.open("https://via.placeholder.com/1200x300.png?text=Customer+Churn+Prediction")
st.image(banner, use_column_width=True)

# -- Main Title and Description --
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.title("Customer Churn Prediction")
st.markdown("Enter customer details below to predict churn and see a local explanation of the model's decision.")
st.markdown("</div>", unsafe_allow_html=True)

# -- Load Model and Explainer (Cache for performance) --
@st.cache(allow_output_mutation=True)
def load_objects():
    # Replace the file paths with your actual model and explainer paths
    model = joblib.load("customer_churn_model.pkl")
    explainer = joblib.load("shap_explainer.pkl")
    return model, explainer

model, explainer = load_objects()

# -- Input Form for Prediction --
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
with st.form("prediction_form"):
    st.subheader("Customer Details")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=120, value=12, step=1)
    with col2:
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, value=70.0, step=0.5)
        contract_type = st.selectbox("Contract Type", options=["Month-to-month", "One year", "Two year"])
    
    # You can add additional inputs here to match your model's features
    submitted = st.form_submit_button("Predict")

if submitted:
    # -- Preprocessing (adjust to match your notebook's pipeline) --
    input_data = pd.DataFrame({
        "age": [age],
        "tenure": [tenure],
        "monthly_charges": [monthly_charges],
        "contract_type": [contract_type]
    })
    # (Make sure to include any encoding/scaling steps as used in your notebook.)

    # -- Make Prediction --
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]  # Adjust index if necessary

    # -- Display Prediction Result --
    result_text = "Churn" if prediction == 1 else "No Churn"
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.subheader("Prediction Result")
    st.write(f"**Outcome:** {result_text}")
    st.write(f"**Probability of Churn:** {probability:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # -- Local Explainability using SHAP --
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.subheader("Local Explanation")
    shap_values = explainer.shap_values(input_data)

    # Create a bar summary plot for the explanation
    fig, ax = plt.subplots(figsize=(10, 3))
    shap.summary_plot(shap_values, input_data, plot_type="bar", show=False)
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)
