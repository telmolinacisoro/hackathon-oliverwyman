# Customer Churn Prediction - HackatOW Challenge

## Project Overview
In the following code, I applied a structured approach to explore, predict, and understand the data. The process began by properly connecting and merging the CSV files into a unified DataFrame. This allowed for a thorough exploratory data analysis, where I examined the statistical properties of the dataset, studied feature distributions, and visualized correlations using a heatmap.

## Model Training and Evaluation
Next, I trained multiple machine learning models to predict customer churn. Although several architectures were tested (including logistic regression, tree-based models, neural networks, and even model stacking) none showed significant improvements in performance. I also implemented GridSearchCV for hyperparameter tuning, but the gains were marginal, meaning that model architecture alone was not enough to push accuracy further.

## Future Improvements
Given these results, a logical next step would be to enhance the dataset. This could be achieved by augmenting the existing data through web scraping, external APIs, or other sources that provide complementary customer behavior or market context. More data variety could lead to richer features and better predictions.

## Explainable AI with SHAP
As part of the understand phase, I intended to incorporate Explainable AI techniques using SHAP (SHapley Additive Explanations) to gain both global and local interpretability of the predictions. Although this wasn't fully implemented in the final version of the code, the plan was to use SHAP to show which features contributed most to an individual customer’s churn prediction.

## BI Dashboard & Streamlit App
In addition, my original vision included a Tableau dashboard to extract actionable insights and support BI. The dashboard would be embedded in a Streamlit application (by posting it to the Tableau Server), which would also feature a simple UI allowing users to input customer attributes, receive a churn probability prediction, and view local explainability results from SHAP. 

## Final Thoughts & Future Directions
To take things even further, I also considered integrating open-source LLMs via Hugging Face to automatically generate weekly customer reports, helping to understand ongoing trends and changes in customer behavior.

Overall, this has been an exciting opportunity to explore new projects and I very much look forward to exploring these ideas further!!
