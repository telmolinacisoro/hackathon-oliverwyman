import streamlit as st

# -- Page Configuration --
st.set_page_config(page_title="Tableau Dashboard", page_icon="📈", layout="wide")

# -- Custom CSS Styling --
st.markdown(
    """
    <style>
    /* Overall background */
    body {
        background: linear-gradient(135deg, #f7f9fc, #e2e8f0);
        font-family: 'Segoe UI', sans-serif;
    }
    /* Container styling */
    .dashboard-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    /* Header styling */
    .dashboard-header {
        text-align: center;
        color: #2e7bcf;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -- Header Section --
st.markdown("<div class='dashboard-container'>", unsafe_allow_html=True)
st.markdown("<h1 class='dashboard-header'>Customer Churn Tableau Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explore interactive visualizations and insights on customer churn.</p>", unsafe_allow_html=True)

# -- Embed the Tableau Dashboard --
# Replace with your actual Tableau Public or Server dashboard URL. Ensure embed permissions are enabled.
tableau_url = "https://public.tableau.com/views/YourDashboardName/Sheet1?:embed=y&:display_count=yes"

st.components.v1.html(
    f"""
    <iframe src="{tableau_url}" width="100%" height="800" frameborder="0" style="border: none; border-radius: 15px;" allowfullscreen></iframe>
    """,
    height=820,
    scrolling=True
)
st.markdown("</div>", unsafe_allow_html=True)
