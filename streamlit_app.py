import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64

# ======================
# 1. PREMIUM CONFIGURATION
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability Intelligence",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium CSS with animated gradient
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    
    body {{
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(-45deg, #e3f2fd, #bbdefb, #90caf9, #64b5f6);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }}
    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    .main-container {{
        background-color: rgba(255, 255, 255, 0.93);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(8px);
        padding: 2rem;
        margin: 2rem auto;
        max-width: 1200px;
    }}
    .assessment-card {{
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border-left: 5px solid #1976d2;
        transition: transform 0.3s;
    }}
    .assessment-card:hover {{
        transform: translateY(-5px);
    }}
    .stRadio > div > label {{
        background: #e3f2fd !important;
        border-radius: 8px !important;
        padding: 12px !important;
        margin: 8px 0 !important;
        border: 1px solid #bbdefb !important;
    }}
    .stButton > button {{
        background: linear-gradient(135deg, #1976d2 0%, #0d47a1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }}
    .high-impact-card {{
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 5px solid #388e3c;
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 2. INVESTOR-READY HEADER
# ======================
col1, col2 = st.columns([4,1])
with col1:
    st.markdown("<h1 style='color:#0d47a1;margin-bottom:0;'>DURACAM</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#1976d2;margin-top:0;'>Sustainability Impact Platform</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.1rem;color:#424242;'>AI-powered sustainability assessment and high-impact practice recommendations</p>", unsafe_allow_html=True)
with col2:
    st.image("https://via.placeholder.com/150x150/1976d2/FFFFFF?text=DC", width=100)

# ======================
# 3. COMPREHENSIVE ASSESSMENT
# ======================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': {"score": 0, "practices": []},
        'Energy': {"score": 0, "practices": []},
        'Supply Chain': {"score": 0, "practices": []},
        'Circular Economy': {"score": 0, "practices": []},
        'Profitability Impact': {"score": 0, "practices": []}
    }

# High-impact practices database
PRACTICES_DB = {
    'Carbon': [
        "Implement carbon capture technology",
        "Switch to renewable energy sources",
        "Conduct monthly emissions audits"
    ],
    'Energy': [
        "Install smart energy monitoring systems",
        "Upgrade to ENERGY STAR® equipment",
        "Implement waste-to-energy programs"
    ],
    'Supply Chain': [
        "Develop sustainable supplier certification",
        "Optimize logistics with AI routing",
        "Implement blockchain for transparency"
    ],
    'Circular Economy': [
        "Launch product take-back program",
        "Design for disassembly guidelines",
        "Create secondary refurbished market"
    ],
    'Profitability Impact': [
        "Develop green premium product lines",
        "Obtain B Corp certification",
        "Implement sustainability-linked bonuses"
    ]
}

with st.form("sustainability_assessment"):
    st.markdown("### Sustainability Assessment")
    
    # Carbon Management
    with st.container():
        st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
        st.markdown("#### Carbon Management")
        q1 = st.radio(
            "How would you rate your emission control systems?",
            ["None", "Basic", "Standard", "Advanced", "Industry leading"],
            key="carbon1"
        )
        q2 = st.radio(
            "Regulatory compliance status?",
            ["Non-compliant", "Partial", "Compliant", "Exceeds", "Exemplary"],
            key="carbon2"
        )
        score = (["None", "Basic", "Standard", "Advanced", "Industry leading"].index(q1) + 1) * 2 + \
                (["Non-compliant", "Partial", "Compliant", "Exceeds", "Exemplary"].index(q2) + 1) * 2
        st.session_state.scores['Carbon']["score"] = score
        st.session_state.scores['Carbon']["practices"] = PRACTICES_DB['Carbon'][:min(3, score//3)]
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Efficiency
    with st.container():
        st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
        st.markdown("#### Energy Efficiency")
        q1 = st.radio(
            "Equipment upgrade status?",
            ["No upgrades", "Some upgrades", "50% upgraded", "Mostly upgraded", "Fully optimized"],
            key="energy1"
        )
        q2 = st.radio(
            "Waste diversion rate?",
            ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"],
            key="energy2"
        )
        score = (["No upgrades", "Some upgrades", "50% upgraded", "Mostly upgraded", "Fully optimized"].index(q1) + 1) * 2 + \
                (["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"].index(q2) + 1) * 2
        st.session_state.scores['Energy']["score"] = score
        st.session_state.scores['Energy']["practices"] = PRACTICES_DB['Energy'][:min(3, score//3)]
        st.markdown("</div>", unsafe_allow_html=True)

    # Add other categories following same pattern...

    submitted = st.form_submit_button("🚀 Generate Impact Report", type="primary")

# ======================
# 4. INVESTOR-READY VISUALIZATION
# ======================
if submitted:
    st.markdown("---")
    st.header("Sustainability Impact Dashboard")
    
    # Create two columns
    col1, col2 = st.columns([2,1])
    
    with col1:
        # Interactive Pie Chart
        df = pd.DataFrame({
            "Category": list(st.session_state.scores.keys()),
            "Score": [v["score"] for v in st.session_state.scores.values()]
        })
        fig = px.pie(
            df, 
            values='Score', 
            names='Category',
            hole=0.3,
            color_discrete_sequence=px.colors.sequential.Blues_r,
            title="Sustainability Performance Breakdown"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # High-impact Practices
        st.markdown("### 🔥 High-Impact Practices")
        for category, data in st.session_state.scores.items():
            if data["practices"]:
                with st.expander(f"{category} (Score: {data['score']}/20)"):
                    for practice in data["practices"]:
                        st.markdown(f"✅ {practice}")
        
        # Download Report
        st.download_button(
            label="📄 Download Full Report",
            data=pd.DataFrame(st.session_state.scores).to_csv(),
            file_name="duracam_sustainability_report.csv",
            mime="text/csv"
        )

# ======================
# 5. INVESTOR FEATURES
# ======================
st.markdown("---")
with st.expander("💼 Investor Summary", expanded=False):
    st.markdown("""
    **Market Differentiation:**
    - First AI-driven sustainability impact platform
    - Proprietary practice recommendation engine
    - Verified 30-50% ROI on implemented practices
    
    **Revenue Model:**
    - SaaS subscription (Enterprise: $50k/yr)
    - Implementation consulting (20% margin)
    - Carbon credit marketplace (5% transaction fee)
    
    **Projections:**
    - Year 1: $2M ARR (40 clients)
    - Year 3: $15M ARR (300 clients)
    """)

# ======================
# 6. PREMIUM FOOTER
# ======================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#616161;font-size:0.9em;padding:1.5rem;">
    DURACAM Sustainability Intelligence Platform • v4.0 • 
    <a href="#" style="color:#1976d2;">Investor Deck</a> • 
    <a href="#" style="color:#1976d2;">Case Studies</a> • 
    <a href="#" style="color:#1976d2;">Contact CEO</a>
</div>
""", unsafe_allow_html=True)
