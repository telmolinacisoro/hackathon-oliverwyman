# Customer Churn Prediction Web App

This repository contains a customer churn prediction web application built using Streamlit. The app allows users to input customer details and predict churn probability while providing local explainability using SHAP. A Tableau dashboard is also included for additional insights.

## Approach

The project follows a structured approach:
1. Data Preprocessing and Exploration: The dataset is cleaned, missing values handled, and exploratory data analysis (EDA) is conducted in the Jupyter Notebook.
2. Feature Engineering and Model Selection: Different models were tested, including logistic regression, random forest, and gradient boosting classifiers.
3. Model Evaluation: The best-performing model was selected based on accuracy, precision, recall, and F1-score.
4. Explainability: SHAP (SHapley Additive exPlanations) is used to interpret the predictions and understand feature importance at both global and local levels.

## Models and Accuracy

Several models were trained and evaluated:
1. Logistic Regression: Accuracy ~ 78%
2. Random Forest: Accuracy ~ 82%
3. Gradient Boosting: Accuracy ~ 85% (Best model)

## Explainability

The SHAP explainability module helps understand the model's decision-making process by:
Showing which features contribute the most to predictions.
Providing individual prediction explanations using SHAP values.
Visualizing the impact of different features on the predicted outcome.
