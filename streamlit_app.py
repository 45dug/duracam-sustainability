import streamlit as st
import pandas as pd
import plotly.express as px

# ======================
# 1. HIGH-CONTRAST CONFIG
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability",
    page_icon="♻️",
    layout="wide"
)

# Accessibility-focused CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
    
    body {{
        font-family: 'Open Sans', sans-serif;
        background-color: #ffffff;
    }}
    .header {{
        background: #005f87;
        color: white;
        padding: 2rem;
        margin-bottom: 2rem;
    }}
    .assessment-card {{
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #005f87;
    }}
    .stRadio > div > div > label {{
        font-size: 1rem !important;
        color: #333333 !important;
        padding: 12px 16px !important;
        background: #f8f9fa !important;
        border-radius: 8px !important;
        margin: 8px 0 !important;
    }}
    .stRadio > div > div > label:hover {{
        background: #e9ecef !important;
    }}
    h1, h2, h3 {{
        color: #005f87 !important;
    }}
    .stButton > button {{
        background: #005f87 !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
    }}
    .high-impact {{
        background: #e6f7ff;
        border-left: 4px solid #0088cc;
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 2. HIGH-VISIBILITY HEADER
# ======================
st.markdown("""
<div class="header">
    <h1 style="margin:0;font-weight:700;">DURACAM</h1>
    <h2 style="margin:0;font-weight:600;">Sustainability Impact Platform</h2>
    <p style="margin:0.5rem 0 0 0;font-size:1.1rem;">Clear, actionable sustainability assessments</p>
</div>
""", unsafe_allow_html=True)

# ======================
# 3. HIGH-CONTRAST ASSESSMENT
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
    st.markdown("### Sustainability Assessment")
    
    # Carbon Management - Bold Questions
    with st.container():
        st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
        st.markdown("#### <span style='color:#005f87;'>Carbon Management</span>", unsafe_allow_html=True)
        q1 = st.radio(
            "**How effective are your emission controls?**",
            ["❌ Not implemented", "⚠️ Basic systems", "🟡 Moderate controls", 
             "✅ Effective systems", "🏆 Industry leading"],
            key="carbon1"
        )
        q2 = st.radio(
            "**Regulatory compliance status?**",
            ["❌ Non-compliant", "⚠️ Partial compliance", "🟡 Fully compliant", 
             "✅ Exceeds requirements", "🏆 Exemplary performance"],
            key="carbon2"
        )
        st.session_state.scores['Carbon'] = (
            ["❌ Not implemented", "⚠️ Basic systems", "🟡 Moderate controls", 
             "✅ Effective systems", "🏆 Industry leading"].index(q1) * 5 +
            ["❌ Non-compliant", "⚠️ Partial compliance", "🟡 Fully compliant", 
             "✅ Exceeds requirements", "🏆 Exemplary performance"].index(q2) * 5
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Efficiency - Bold Questions
    with st.container():
        st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
        st.markdown("#### <span style='color:#005f87;'>Energy Efficiency</span>", unsafe_allow_html=True)
        q1 = st.radio(
            "**Equipment upgrade status?**",
            ["❌ No upgrades", "⚠️ Some upgrades", "🟡 50% upgraded", 
             "✅ Mostly upgraded", "🏆 Fully optimized"],
            key="energy1"
        )
        q2 = st.radio(
            "**Waste diversion rate?**",
            ["❌ 0-20%", "⚠️ 20-40%", "🟡 40-60%", 
             "✅ 60-80%", "🏆 80-100%"],
            key="energy2"
        )
        st.session_state.scores['Energy'] = (
            ["❌ No upgrades", "⚠️ Some upgrades", "🟡 50% upgraded", 
             "✅ Mostly upgraded", "🏆 Fully optimized"].index(q1) * 5 +
            ["❌ 0-20%", "⚠️ 20-40%", "🟡 40-60%", 
             "✅ 60-80%", "🏆 80-100%"].index(q2) * 5
        )
        st.markdown("</div>", unsafe_allow_html=True)

    submitted = st.form_submit_button("📊 Generate Results", type="primary")

# ======================
# 4. ULTRA-READABLE RESULTS
# ======================
if submitted:
    st.markdown("---")
    st.header("Assessment Results")
    
    # Two-column layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # High-contrast bar chart
        df = pd.DataFrame({
            "Category": list(st.session_state.scores.keys()),
            "Score": list(st.session_state.scores.values())
        })
        fig = px.bar(
            df,
            x="Category",
            y="Score",
            color="Category",
            color_discrete_sequence=["#005f87", "#0088cc", "#00aaff", "#73c2ff", "#b3e0ff"],
            text="Score",
            title="<b>Performance by Category</b>"
        )
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=14),
            yaxis_range=[0,50]
        )
        fig.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # High-impact practices
        st.markdown("### 🚀 Recommended Actions")
        for category, score in st.session_state.scores.items():
            if score < 15:
                st.markdown(f"<div class='assessment-card high-impact'><b>{category}</b><br>Priority improvement area</div>", 
                           unsafe_allow_html=True)
            elif score > 35:
                st.markdown(f"<div class='assessment-card'><b>{category}</b><br>Strength to leverage</div>", 
                           unsafe_allow_html=True)

# ======================
# 5. CLEAN FOOTER
# ======================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#666;font-size:0.9em;padding:1rem;">
    © 2025 DURACAM | <span style="color:#005f87;">Contact</span> | 
    <span style="color:#005f87;">Privacy</span> | <span style="color:#005f87;">Terms</span>
</div>
""", unsafe_allow_html=True)
