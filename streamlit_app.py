import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# ======================================
# 1. PROFESSIONAL UI SETUP
# ======================================
st.set_page_config(
    page_title="DURACAM Sustainability",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .header {
        color: #2E86AB;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 10px;
    }
    .category-box {
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #F8F9FA;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #2E86AB;
        color: white;
        border-radius: 5px;
        padding: 8px 20px;
    }
    .stRadio>div {
        flex-direction: column;
        gap: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ======================================
# 2. BRANDING HEADER
# ======================================
col1, col2 = st.columns([4,1])
with col1:
    st.markdown("<h1 class='header'>DURACAM</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Helping companies meet their sustainability goals</h3>", unsafe_allow_html=True)
with col2:
    st.image("https://via.placeholder.com/100x100/2E86AB/FFFFFF?text=DC", width=80)

# ======================================
# 3. QUESTIONNAIRE (FROM YOUR TABLE)
# ======================================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0,
        'Circular': 0,
        'Profitability Impact': 0
    }

with st.form("assessment"):
    # Carbon Category
    with st.container():
        st.markdown("<div class='category-box'>", unsafe_allow_html=True)
        st.subheader("Carbon Management")
        q1 = st.radio(
            "How optimized are your process choices for emissions reduction?",
            ["Not optimized", "Slightly optimized", "Moderately optimized", "Highly optimized", "Fully optimized"],
            key="carbon1"
        )
        q2 = st.radio(
            "What percentage of operations are emissions-compliant?",
            ["<20%", "20-40%", "40-60%", "60-80%", "80-100%"],
            key="carbon2"
        )
        st.session_state.scores['Carbon'] = (["Not optimized", "Slightly optimized", "Moderately optimized", "Highly optimized", "Fully optimized"].index(q1) + 1) * 2 + \
                                          (["<20%", "20-40%", "40-60%", "60-80%", "80-100%"].index(q2) + 1) * 2
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Category
    with st.container():
        st.markdown("<div class='category-box'>", unsafe_allow_html=True)
        st.subheader("Energy Efficiency")
        q1 = st.radio(
            "Have you implemented equipment upgrades?",
            ["None", "Few upgrades", "Some upgrades", "Many upgrades", "Complete upgrade"],
            key="energy1"
        )
        q2 = st.radio(
            "What's your waste diversion rate?",
            ["<20%", "20-40%", "40-60%", "60-80%", "80-100%"],
            key="energy2"
        )
        st.session_state.scores['Energy'] = (["None", "Few upgrades", "Some upgrades", "Many upgrades", "Complete upgrade"].index(q1) + 1) * 2 + \
                                          (["<20%", "20-40%", "40-60%", "60-80%", "80-100%"].index(q2) + 1) * 2
        st.markdown("</div>", unsafe_allow_html=True)

    # Add all other categories following the same pattern...

    submitted = st.form_submit_button("Calculate Sustainability Score", type="primary")

# ======================================
# 4. RESULTS VISUALIZATION
# ======================================
if submitted:
    st.markdown("---")
    st.header("Sustainability Performance")
    
    # Bar Chart
    fig, ax = plt.subplots(figsize=(10,6))
    categories = list(st.session_state.scores.keys())
    scores = list(st.session_state.scores.values())
    
    colors = ['#2E86AB', '#3DA5D9', '#73BFB8', '#FEC601', '#EA7317']
    bars = ax.bar(categories, scores, color=colors)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}',
                ha='center', va='bottom')
    
    ax.set_ylim(0, 20)
    ax.set_ylabel('Score (out of 20)')
    ax.set_title('Sustainability Performance by Category')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Score Interpretation
    st.markdown("### Key Insights")
    max_category = max(st.session_state.scores, key=st.session_state.scores.get)
    st.success(f"**Strongest Area:** {max_category}")
    
    min_category = min(st.session_state.scores, key=st.session_state.scores.get)
    st.warning(f"**Area Needing Improvement:** {min_category}")

# ======================================
# 5. PROFESSIONAL FOOTER
# ======================================
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666; font-size: 0.9em;'>© 2025 DURACAM Sustainability Assessment Platform</div>", unsafe_allow_html=True)
