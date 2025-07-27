import streamlit as st
import pandas as pd
import plotly.express as px

# ======================
# 1. INVESTOR-GRADE CONFIG
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability Pro",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium CSS (Fixed Contrast)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    body {{
        font-family: 'Inter', sans-serif;
        background: #f8fafc;
    }}
    .header {{
        background: #005f87;
        color: white;
        padding: 2.5rem;
        margin: -1rem -1rem 2rem -1rem;
    }}
    .card {{
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-left: 4px solid #005f87;
    }}
    .question {{
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #1e293b !important;
        margin-bottom: 0.5rem !important;
    }}
    .stRadio div[role="radiogroup"] label {{
        background: #f1f5f9 !important;
        padding: 12px 16px !important;
        border-radius: 8px !important;
        margin: 8px 0 !important;
        border: 1px solid #e2e8f0 !important;
    }}
    .stButton button {{
        background: #005f87 !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 2. EXECUTIVE HEADER
# ======================
st.markdown("""
<div class="header">
    <h1 style="margin:0;font-weight:700;">DURACAM</h1>
    <h2 style="margin:0;font-weight:600;">Sustainability Intelligence Platform</h2>
    <p style="margin:0.5rem 0 0 0;font-size:1.1rem;opacity:0.9;">
        Investor-Ready Sustainability Assessments
    </p>
</div>
""", unsafe_allow_html=True)

# ======================
# 3. STREAMLINED ASSESSMENT
# ======================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0,
        'Circular': 0,
        'Profit Impact': 0
    }

with st.form("assessment"):
    # Carbon Management
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Carbon Management")
        
        st.markdown('<div class="question">Process optimization for emissions:</div>', unsafe_allow_html=True)
        q1 = st.radio(
            "",
            ["Not optimized", "Basic controls", "Some optimization", "Advanced", "Industry leading"],
            key="carbon1",
            label_visibility="collapsed"
        )
        
        st.markdown('<div class="question">Regulatory compliance status:</div>', unsafe_allow_html=True)
        q2 = st.radio(
            "",
            ["Non-compliant", "Partial", "Compliant", "Exceeds", "Exemplary"],
            key="carbon2",
            label_visibility="collapsed"
        )
        
        st.session_state.scores['Carbon'] = (
            ["Not optimized", "Basic controls", "Some optimization", "Advanced", "Industry leading"].index(q1) * 5 +
            ["Non-compliant", "Partial", "Compliant", "Exceeds", "Exemplary"].index(q2) * 5
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Efficiency
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Energy Efficiency")
        
        st.markdown('<div class="question">Equipment upgrade status:</div>', unsafe_allow_html=True)
        q1 = st.radio(
            "",
            ["No upgrades", "Some", "50% upgraded", "Mostly", "Fully optimized"],
            key="energy1",
            label_visibility="collapsed"
        )
        
        st.markdown('<div class="question">Waste diversion rate:</div>', unsafe_allow_html=True)
        q2 = st.radio(
            "",
            ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"],
            key="energy2",
            label_visibility="collapsed"
        )
        
        st.session_state.scores['Energy'] = (
            ["No upgrades", "Some", "50% upgraded", "Mostly", "Fully optimized"].index(q1) * 5 +
            ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"].index(q2) * 5
        )
        st.markdown("</div>", unsafe_allow_html=True)

    submitted = st.form_submit_button("Generate Report", type="primary")

# ======================
# 4. INVESTOR VISUALIZATION
# ======================
if submitted:
    st.markdown("---")
    st.header("Performance Dashboard")
    
    # Create two columns
    col1, col2 = st.columns([3,1])
    
    with col1:
        # Pie Chart
        fig = px.pie(
            names=list(st.session_state.scores.keys()),
            values=list(st.session_state.scores.values()),
            hole=0.3,
            color_discrete_sequence=px.colors.sequential.Blues_r,
            title="Sustainability Score Distribution"
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=14
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # High-Impact Practices
        st.markdown("### Recommended Actions")
        for category, score in st.session_state.scores.items():
            if score < 15:
                st.markdown(f"""
                <div style="background:#fff4f4;padding:12px;border-radius:8px;margin-bottom:8px;">
                    <b>{category}</b><br>
                    <span style="color:#d33f49;">Priority improvement</span>
                </div>
                """, unsafe_allow_html=True)
            elif score > 35:
                st.markdown(f"""
                <div style="background:#f0f9ff;padding:12px;border-radius:8px;margin-bottom:8px;">
                    <b>{category}</b><br>
                    <span style="color:#0077c8;">Competitive strength</span>
                </div>
                """, unsafe_allow_html=True)

# ======================
# 5. INVESTOR FOOTER
# ======================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#64748b;font-size:0.9em;padding:1.5rem;">
    © 2025 DURACAM | <span style="color:#005f87;">Investor Relations</span> | 
    <span style="color:#005f87;">Contact CEO</span> | <span style="color:#005f87;">Request Demo</span>
</div>
""", unsafe_allow_html=True)
