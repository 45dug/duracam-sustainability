import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================
# 1. APP CONFIGURATION
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability",
    page_icon="🌍",
    layout="centered"
)

# Sky blue background
st.markdown("""
<style>
    body {
        background-color: #e6f7ff;
    }
    .assessment-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1 {
        color: #005b96;
    }
    h2 {
        color: #003d66;
    }
    .stButton>button {
        background-color: #005b96;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# 2. HEADER
# ======================
st.markdown("<h1 style='text-align:center;'>DURACAM Sustainability Assessment</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#003d66;'>Simple, actionable sustainability insights</h3>", unsafe_allow_html=True)

# ======================
# 3. ASSESSMENT QUESTIONS (FROM YOUR TABLE)
# ======================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0,
        'Circular': 0,
        'Profitability Impact': 0
    }

with st.form("assessment"):
    # Carbon Management
    with st.container():
        st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
        st.markdown("#### Carbon Management")
        q1 = st.radio(
            "How would you rate your process choices for reducing emissions?",
            ["Poor", "Below Average", "Average", "Good", "Excellent"],
            key="carbon1"
        )
        q2 = st.radio(
            "What is your regulatory compliance status?",
            ["Non-compliant", "Partially compliant", "Fully compliant", "Exceeds requirements"],
            key="carbon2"
        )
        st.session_state.scores['Carbon'] = (["Poor", "Below Average", "Average", "Good", "Excellent"].index(q1) + 1) * 2 + \
                                          (["Non-compliant", "Partially compliant", "Fully compliant", "Exceeds requirements"].index(q2) + 1) * 2
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Efficiency
    with st.container():
        st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
        st.markdown("#### Energy Efficiency")
        q1 = st.radio(
            "How effective are your equipment upgrades?",
            ["Not effective", "Slightly effective", "Moderately effective", "Very effective", "Extremely effective"],
            key="energy1"
        )
        q2 = st.radio(
            "What is your waste diversion rate?",
            ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"],
            key="energy2"
        )
        st.session_state.scores['Energy'] = (["Not effective", "Slightly effective", "Moderately effective", "Very effective", "Extremely effective"].index(q1) + 1) * 2 + \
                                          (["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"].index(q2) + 1) * 2
        st.markdown("</div>", unsafe_allow_html=True)

    # Add other categories following the same pattern...

    submitted = st.form_submit_button("Calculate Results", type="primary")

# ======================
# 4. PIE CHART RESULTS
# ======================
if submitted:
    st.markdown("---")
    st.header("Sustainability Performance")
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(8,8))
    categories = list(st.session_state.scores.keys())
    scores = list(st.session_state.scores.values())
    
    colors = ['#005b96', '#0088cc', '#00aaff', '#66c2ff', '#b3e0ff']
    wedges, texts, autotexts = ax.pie(
        scores,
        labels=categories,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1}
    )
    
    # Equal aspect ratio ensures pie is drawn as a circle
    ax.axis('equal')  
    plt.setp(autotexts, size=10, weight="bold", color="white")
    st.pyplot(fig)
    
    # Score Summary
    st.markdown("### Score Distribution")
    for category, score in st.session_state.scores.items():
        st.markdown(f"- **{category}**: {score}/20")

# ======================
# 5. FOOTER
# ======================
st.markdown("---")
st.markdown("<div style='text-align:center;color:#666;font-size:0.9em;'>© 2025 DURACAM Sustainability Assessment</div>", unsafe_allow_html=True)
