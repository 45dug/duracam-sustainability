import streamlit as st
import pandas as pd
import plotly.express as px

# Force dark background and high contrast
st.markdown("""
<style>
    body {
        background-color: #2d3436;
        color: #ffffff !important;
        font-family: Arial, sans-serif;
    }
    .stApp {
        background-color: #2d3436;
    }
    .stRadio > div {
        background: #454545;
        padding: 10px;
        border-radius: 10px;
    }
    .stRadio label {
        color: white !important;
        font-size: 18px !important;
    }
    h1, h2, h3 {
        color: #00cec9 !important;
    }
    .stButton button {
        background: #00cec9 !important;
        color: #2d3436 !important;
        font-weight: bold;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize scores
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0,
        'Circular': 0,
        'Profit Impact': 0
    }

# Header with DURACAM branding
st.title("DURACAM Sustainability Pro")
st.markdown("---")

# Assessment Questions
with st.form("assessment"):
    st.header("Assessment Questions")
    
    # Carbon Section
    st.subheader("Carbon Management")
    q1 = st.radio(
        "Process optimization level:",
        ["None", "Basic", "Moderate", "Advanced", "Industry Leader"],
        key="carbon1"
    )
    q2 = st.radio(
        "Emission tracking:",
        ["Not tracked", "Manual records", "Partial automated", "Fully automated", "AI-optimized"],
        key="carbon2"
    )
    st.session_state.scores['Carbon'] = (["None", "Basic", "Moderate", "Advanced", "Industry Leader"].index(q1) + 1) * 10
    
    # Add other sections following same pattern...
    
    if st.form_submit_button("Calculate Scores", type="primary"):
        st.session_state.show_results = True

# Results Section
if hasattr(st.session_state, 'show_results'):
    st.header("Assessment Results")
    
    # Convert scores to DataFrame
    df = pd.DataFrame({
        "Category": st.session_state.scores.keys(),
        "Score": st.session_state.scores.values()
    })
    
    # Create pie chart
    fig = px.pie(
        df,
        names="Category",
        values="Score",
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.Aggrnyl
    )
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        textfont_size=16
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # High-impact recommendations
    st.header("Recommended Actions")
    min_category = min(st.session_state.scores, key=st.session_state.scores.get)
    
    if min_category == "Carbon":
        st.markdown("""
        - Implement real-time emission monitoring (est. $50k/year savings)
        - Conduct carbon accounting training ($15k setup)
        - Explore carbon offset programs
        """)
    elif min_category == "Energy":
        st.markdown("""
        - Schedule energy audit (est. 30% reduction potential)
        - Upgrade to smart HVAC systems
        - Implement solar panel array
        """)

# Footer
st.markdown("---")
st.markdown("DURACAM Sustainability Pro v4.2 | Contact: ceo@duracam.com")
