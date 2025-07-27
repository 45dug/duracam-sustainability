import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from PIL import Image

# ======================
# 1. APP CONFIGURATION
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability Pro",
    page_icon="🌿",
    layout="wide"
)

# Custom CSS for modern UI
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
    
    body {{
        font-family: 'Montserrat', sans-serif;
        background-color: #f9fbfa;
    }}
    .header {{
        background: linear-gradient(135deg, #2b5876 0%, #4e4376 100%);
        color: white;
        padding: 2rem;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }}
    .category-card {{
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-left: 4px solid #4e4376;
    }}
    .stRadio > div > label {{
        background: #f0f4f8 !important;
        padding: 10px 15px !important;
        border-radius: 8px !important;
        margin: 5px 0 !important;
    }}
    .stButton > button {{
        background: linear-gradient(135deg, #2b5876 0%, #4e4376 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
    }}
    .toolkit-card {{
        background: #f0f5ff;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 2. BRANDED HEADER
# ======================
st.markdown("""
<div class="header">
    <h1 style="margin:0;font-weight:600;">DURACAM SUSTAINABILITY PRO</h1>
    <p style="margin:0;font-size:1.1rem;">Helping companies meet their sustainability goals with precision</p>
</div>
""", unsafe_allow_html=True)

# ======================
# 3. ASSESSMENT TOOLKIT
# ======================
def show_toolkit():
    with st.expander("📚 Assessment Toolkit Resources", expanded=False):
        st.markdown("""
        <div class="toolkit-card">
            <h4>📋 Assessment Guide</h4>
            <p>How to complete this evaluation:</p>
            <ol>
                <li>Answer all questions honestly</li>
                <li>Choose the option that best reflects your current status</li>
                <li>Submit to get your sustainability score</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="toolkit-card">
            <h4>📊 Benchmarking Data</h4>
            <p>Industry average scores:</p>
            <ul>
                <li>Carbon Management: 12/20</li>
                <li>Energy Efficiency: 14/20</li>
                <li>Supply Chain: 10/20</li>
                <li>Circular Economy: 8/20</li>
                <li>Profitability Impact: 16/20</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

show_toolkit()

# ======================
# 4. SIMPLIFIED ASSESSMENT
# ======================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0,
        'Circular': 0,
        'Profitability Impact': 0
    }

with st.form("simple_assessment"):
    # Carbon Management
    with st.container():
        st.markdown("<div class='category-card'>", unsafe_allow_html=True)
        st.subheader("Carbon Management")
        q1 = st.radio(
            "Process emission controls:",
            ["None", "Basic controls", "Some optimization", "Advanced systems", "Industry leading"],
            key="carbon_q1"
        )
        q2 = st.radio(
            "Regulatory compliance:",
            ["Non-compliant", "Partially compliant", "Mostly compliant", "Fully compliant", "Exceeds requirements"],
            key="carbon_q2"
        )
        st.session_state.scores['Carbon'] = (["None", "Basic controls", "Some optimization", "Advanced systems", "Industry leading"].index(q1) * 2 + \
                                          (["Non-compliant", "Partially compliant", "Mostly compliant", "Fully compliant", "Exceeds requirements"].index(q2) * 2)
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Efficiency
    with st.container():
        st.markdown("<div class='category-card'>", unsafe_allow_html=True)
        st.subheader("Energy Efficiency")
        q1 = st.radio(
            "Equipment efficiency:",
            ["All outdated", "Some upgrades", "50% modern", "Mostly modern", "100% optimized"],
            key="energy_q1"
        )
        q2 = st.radio(
            "Waste management:",
            ["No program", "Basic recycling", "Some reduction", "Advanced systems", "Zero waste"],
            key="energy_q2"
        )
        st.session_state.scores['Energy'] = (["All outdated", "Some upgrades", "50% modern", "Mostly modern", "100% optimized"].index(q1) * 2 + \
                                          (["No program", "Basic recycling", "Some reduction", "Advanced systems", "Zero waste"].index(q2) * 2))
        st.markdown("</div>", unsafe_allow_html=True)

    # Add other categories following same pattern...

    submitted = st.form_submit_button("📊 Generate Sustainability Report")

# ======================
# 5. VISUAL RESULTS
# ======================
if submitted:
    st.markdown("---")
    st.header("Sustainability Assessment Results")
    
    # Create two columns
    col1, col2 = st.columns([2,1])
    
    with col1:
        # Horizontal Bar Chart
        fig, ax = plt.subplots(figsize=(10,6))
        categories = list(st.session_state.scores.keys())
        scores = list(st.session_state.scores.values())
        
        colors = ['#2b5876', '#3a7bd5', '#00d2ff', '#4e4376', '#a8c0ff']
        bars = ax.barh(categories, scores, color=colors)
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                    f'{width}/20',
                    va='center', ha='left', fontsize=10)
        
        ax.set_xlim(0, 20)
        ax.set_xlabel('Score (out of 20)')
        ax.set_title('Sustainability Performance', pad=20)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)
    
    with col2:
        # Score Summary
        st.markdown("""
        <div style="background:#f9fbfa;padding:1.5rem;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color:#2b5876;margin-top:0;">Overall Score</h3>
            <h1 style="color:#4e4376;text-align:center;">{}/100</h1>
            <p style="text-align:center;">{}</p>
            <hr style="border-color:#eee;">
            <h4 style="color:#2b5876;">Top Recommendation</h4>
            <p>{}</p>
        </div>
        """.format(
            sum(st.session_state.scores.values()),
            "Meeting Industry Standards" if sum(st.session_state.scores.values()) >= 60 else "Needs Improvement",
            "Implement advanced carbon tracking systems" if min(st.session_state.scores, key=st.session_state.scores.get) == "Carbon" else
            "Upgrade energy infrastructure" if min(st.session_state.scores, key=st.session_state.scores.get) == "Energy" else
            "Optimize supply chain logistics"
        ), unsafe_allow_html=True)

# ======================
# 6. PROFESSIONAL FOOTER
# ======================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#666;font-size:0.9em;padding:1rem;">
    © 2025 DURACAM Sustainability Pro | <a href="#" style="color:#4e4376;">Privacy Policy</a> | <a href="#" style="color:#4e4376;">Terms of Service</a>
</div>
""", unsafe_allow_html=True)
