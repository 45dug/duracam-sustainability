import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================
# 1. APP CONFIGURATION
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .header {
        color: #1a5276;
        border-bottom: 2px solid #1a5276;
        padding-bottom: 10px;
    }
    .category-box {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stSlider>div>div>div>div {
        background: #1a5276 !important;
    }
    .st-b7 {
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# 2. BRANDED HEADER
# ======================
st.markdown("<h1 class='header'>DURACAM Sustainability Assessment</h1>", unsafe_allow_html=True)
st.markdown("**Helping companies meet their sustainability goals**")

# ======================
# 3. SIMPLIFIED ASSESSMENT
# ======================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0
    }

with st.form("assessment"):
    st.markdown("### Rate your sustainability performance")
    
    # Carbon Category
    with st.container():
        st.markdown("<div class='category-box'>", unsafe_allow_html=True)
        st.markdown("#### Carbon Management")
        q1 = st.slider(
            "How optimized are your processes for minimal emissions?",
            0, 10, 5,
            key="carbon1"
        )
        q2 = st.slider(
            "Percentage compliant with emission regulations?",
            0, 10, 5,
            key="carbon2"
        )
        st.session_state.scores['Carbon'] = (q1 + q2) / 2
        st.markdown("</div>", unsafe_allow_html=True)

    # Energy Category
    with st.container():
        st.markdown("<div class='category-box'>", unsafe_allow_html=True)
        st.markdown("#### Energy Efficiency")
        q1 = st.slider(
            "Implementation of energy-efficient equipment?",
            0, 10, 5,
            key="energy1"
        )
        q2 = st.slider(
            "Effectiveness of waste diversion programs?",
            0, 10, 5,
            key="energy2"
        )
        st.session_state.scores['Energy'] = (q1 + q2) / 2
        st.markdown("</div>", unsafe_allow_html=True)

    submitted = st.form_submit_button("Calculate Scores", type="primary")

# ======================
# 4. VISUAL RESULTS
# ======================
if submitted:
    st.markdown("---")
    st.header("Assessment Results")
    
    # Convert scores to DataFrame
    scores_df = pd.DataFrame.from_dict(
        st.session_state.scores, 
        orient='index',
        columns=['Score']
    )
    
    # Create two columns layout
    col1, col2 = st.columns([3,2])
    
    with col1:
        # Bar Chart
        fig, ax = plt.subplots(figsize=(8,4))
        scores_df.plot(kind='bar', ax=ax, color=['#1a5276'])
        ax.set_ylim(0, 10)
        ax.set_title("Sustainability Performance")
        ax.set_ylabel("Score (0-10)")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    with col2:
        # Score Summary
        st.markdown("### Score Summary")
        for category, score in st.session_state.scores.items():
            st.metric(label=category, value=f"{score:.1f}/10")
        
        avg_score = sum(st.session_state.scores.values()) / len(st.session_state.scores)
        st.markdown(f"**Overall Average:** {avg_score:.1f}/10")

# ======================
# 5. TOOLKIT SECTION
# ======================
st.markdown("---")
with st.expander("📚 Assessment Toolkit"):
    st.markdown("""
    **How to improve your scores:**
    - Carbon: Implement emission tracking systems
    - Energy: Conduct energy audits quarterly
    - Supply Chain: Develop supplier sustainability criteria
    
    **Industry Benchmarks:**
    - Top performers average 8.5/10
    - Median score: 6.2/10
    """)

# ======================
# 6. PROFESSIONAL FOOTER
# ======================
st.markdown("---")
st.caption("© 2025 DURACAM Sustainability Platform | v2.1")
st.markdown("""
<div style="text-align:center;color:#666;font-size:0.9em;padding:1rem;">
    © 2025 DURACAM Sustainability Pro | <a href="#" style="color:#4e4376;">Privacy Policy</a> | <a href="#" style="color:#4e4376;">Terms of Service</a>
</div>
""", unsafe_allow_html=True)
