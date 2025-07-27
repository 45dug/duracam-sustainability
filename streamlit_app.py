import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Configure page
st.set_page_config(
    page_title="DURACAM Sustainability",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stRadio [role=radiogroup] {
        gap: 10px;
    }
    .stRadio [class^=st-] {
        padding: 12px 20px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    .stRadio [class^=st-]:hover {
        background-color: #f0f7f4;
    }
    .st-emotion-cache-1v0mbdj {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': {'score': 0, 'max': 15},
        'Energy': {'score': 0, 'max': 15},
        'Supply Chain': {'score': 0, 'max': 15}, 
        'Circular': {'score': 0, 'max': 15},
        'Profitability Impact': {'score': 0, 'max': 15}
    }

# MCQ Options (consistent 5-point scale)
OPTIONS = {
    1: {"label": "❌ Not at all", "score": 1},
    2: {"label": "⚠️ Slightly", "score": 2},
    3: {"label": "🟡 Moderately", "score": 3},
    4: {"label": "✅ Significantly", "score": 4},
    5: {"label": "🏆 Extremely", "score": 5}
}

# Assessment Questions
questions = {
    'Carbon': [
        ("Process optimization", "How optimized are your processes for minimal emissions?"),
        ("Regulatory compliance", "Are your operations compliant with emission regulations?"),
        ("Tracking systems", "Do you track CO₂ emissions per production unit?")
    ],
    'Energy': [
        ("Equipment upgrades", "Have you implemented energy-efficient equipment?"),
        ("Renewable usage", "Do you use renewable energy sources?"),
        ("Waste management", "Do you have effective waste diversion programs?")
    ],
    'Supply Chain': [
        ("Sustainable transport", "Do you invest in sustainable transport options?"),
        ("Supplier screening", "Do your suppliers meet sustainability criteria?"),
        ("Delivery methods", "Are your delivery methods sustainable and reliable?")
    ],
    'Circular': [
        ("Reuse incentives", "Do you offer product reuse/recycling incentives?"),
        ("Design approach", "Are your products designed for circularity?"),
        ("Return programs", "Do you have effective product return programs?")
    ],
    'Profitability Impact': [
        ("Pricing strategy", "Does your pricing reflect sustainability investments?"),
        ("Marketing focus", "Is green marketing effective for your business?"),
        ("Revenue sources", "Does revenue come from sustainable products?")
    ]
}

# Assessment Form
with st.form("mcq_assessment"):
    st.header("📝 Sustainability Assessment (MCQ Format)")
    
    for scheme in questions:
        with st.expander(f"### 🌿 {scheme}", expanded=False):
            for i, (kpi, question) in enumerate(questions[scheme]):
                st.markdown(f"**{i+1}. {question}**")
                response = st.radio(
                    label="",
                    options=OPTIONS.keys(),
                    format_func=lambda x: OPTIONS[x]["label"],
                    key=f"{scheme}_{i}",
                    horizontal=True,
                    label_visibility="collapsed"
                )
                st.session_state.scores[scheme]['score'] += OPTIONS[response]["score"]
    
    submitted = st.form_submit_button("📤 Submit Assessment", type="primary")

# Results Visualization
if submitted:
    st.success("✅ Assessment submitted successfully!")
    
    # Calculate scores
    scores_df = pd.DataFrame.from_dict(
        {k: (v['score']/v['max'])*100 for k,v in st.session_state.scores.items()},
        orient='index',
        columns=['Score (%)']
    )
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["📊 Score Summary", "📋 Detailed Breakdown", "💡 Recommendations"])
    
    with tab1:
        st.subheader("Overall Sustainability Performance")
        
        # Score Cards
        cols = st.columns(5)
        for i, (scheme, data) in enumerate(st.session_state.scores.items()):
            with cols[i]:
                score_pct = (data['score']/data['max'])*100
                st.metric(
                    label=scheme,
                    value=f"{data['score']}/{data['max']}",
                    help=f"{score_pct:.0f}% achievement"
                )
                st.progress(score_pct/100)
        
        # Radar Chart
        st.subheader("Performance Comparison")
        fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
        categories = list(scores_df.index)
        N = len(categories)
        angles = [n / float(N) * 2 * 3.14159 for n in range(N)]
        angles += angles[:1]
        ax.set_theta_offset(3.14159 / 2)
        ax.set_theta_direction(-1)
        plt.xticks(angles[:-1], categories)
        values = scores_df['Score (%)'].tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Score")
        ax.fill(angles, values, 'b', alpha=0.1)
        ax.set_rlabel_position(0)
        plt.yticks([20,40,60,80,100], ["20%","40%","60%","80%","100%"], color="grey", size=7)
        plt.ylim(0,100)
        st.pyplot(fig)
    
    with tab2:
        st.subheader("Question-by-Question Analysis")
        for scheme in questions:
            with st.expander(f"**{scheme} Responses**"):
                for i, (kpi, question) in enumerate(questions[scheme]):
                    response_key = f"{scheme}_{i}"
                    if response_key in st.session_state:
                        st.markdown(f"**{question}**")
                        st.info(f"Your response: {OPTIONS[st.session_state[response_key]]['label']}")
    
    with tab3:
        st.subheader("🚀 Improvement Roadmap")
        
        # Get best/worst performing areas
        sorted_schemes = sorted(st.session_state.scores.items(), key=lambda x: x[1]['score'], reverse=True)
        
        st.success("**Your strongest areas:**")
        for scheme, data in sorted_schemes[:2]:
            st.markdown(f"▸ **{scheme}** ({data['score']}/{data['max']})")
        
        st.warning("**Areas needing attention:**")
        for scheme, data in sorted_schemes[-2:]:
            st.markdown(f"▸ **{scheme}** ({data['score']}/{data['max']})")
            with st.expander(f"See {scheme} improvement ideas"):
                if scheme == "Carbon":
                    st.markdown("- Implement carbon accounting software")
                    st.markdown("- Conduct energy audits quarterly")
                elif scheme == "Energy":
                    st.markdown("- Install smart meters in all facilities")
                    st.markdown("- Switch to LED lighting")
                elif scheme == "Supply Chain":
                    st.markdown("- Develop supplier sustainability scorecards")
                    st.markdown("- Optimize delivery routes with AI")
                elif scheme == "Circular":
                    st.markdown("- Launch a product take-back program")
                    st.markdown("- Design for disassembly guidelines")
                else:
                    st.markdown("- Create sustainability premium product lines")
                    st.markdown("- Obtain ECO certification")

# Footer
st.markdown("---")
st.caption("© 2025 DURACAM Sustainability Platform | v3.0 (MCQ Edition)")