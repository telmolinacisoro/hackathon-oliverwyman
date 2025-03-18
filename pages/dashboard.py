import streamlit as st

st.set_page_config(page_title="Tableau Dashboard", layout="wide")

st.title("Customer Churn Tableau Dashboard")
st.markdown("Below is the embedded Tableau dashboard:")

# Replace this URL with your actual Tableau Public or Server dashboard URL.
# Make sure that your dashboard is published with embed permissions.
tableau_url = "https://public.tableau.com/views/YourDashboardName/Sheet1?:embed=y&:display_count=yes"

# Embed the Tableau dashboard using an iframe
st.components.v1.html(
    f"""
    <iframe src="{tableau_url}" width="100%" height="800" frameborder="0" allowfullscreen></iframe>
    """,
    height=800,
    scrolling=True
)
