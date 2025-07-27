import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.metric_cards import style_metric_cards

# ======================
# 1. APP CONFIGURATION
# ======================
st.set_page_config(
    page_title="DURACAM Sustainability Pro",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium look
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    body {{
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }}
    .header-container {{
        background: linear-gradient(135deg, #0052D9 0%, #4364F7 50%, #6FB1FC 100%);
        padding: 2.5rem;
        border-radius: 0;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .assessment-card {{
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border-left: 4px solid #4364F7;
    }}
    .stSlider>div>div>div>div {{
        background: #0052D9 !important;
    }}
    .st-b7 {{
        font-weight: 600 !important;
    }}
    .toolkit-card {{
        background: #f0f5ff;
        border-radius: 10px;
        padding: 1.2rem;
        margin: 1rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# ======================
# 2. PREMIUM HEADER
# ======================
st.markdown("""
<div class="header-container">
    <div style="display:flex; align-items:center; gap:15px;">
        <h1 style="margin:0; font-size:2.2rem;">DURACAM SUSTAINABILITY INTELLIGENCE</h1>
    </div>
    <p style="margin:0; font-size:1.1rem; opacity:0.9;">Enterprise-grade sustainability assessment and optimization platform</p>
</div>
""", unsafe_allow_html=True)

# ======================
# 3. ASSESSMENT ENGINE
# ======================
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': {"score": 0, "target": 8},
        'Energy': {"score": 0, "target": 7},
        'Supply Chain': {"score": 0, "target": 6},
        'Circularity': {"score": 0, "target": 5},
        'Profit Impact': {"score": 0, "target": 9}
    }

# Initialize session state for form submission
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

with st.form("pro_assessment"):
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Carbon Management
        with st.container():
            st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
            st.markdown("#### 🌱 Carbon Management")
            st.session_state.scores['Carbon']["score"] = st.slider(
                "Process emission optimization (0-10)",
                0, 10, 5,
                key="carbon1",
                help="How optimized are your production processes for minimal emissions?"
            )
            st.session_state.scores['Carbon']["score"] += st.slider(
                "Regulatory compliance score (0-10)",
                0, 10, 5,
                key="carbon2"
            )
            st.session_state.scores['Carbon']["score"] = st.session_state.scores['Carbon']["score"] / 2
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Energy Efficiency
        with st.container():
            st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
            st.markdown("#### ⚡ Energy Efficiency")
            st.session_state.scores['Energy']["score"] = st.slider(
                "Equipment efficiency rating (0-10)",
                0, 10, 5,
                key="energy1"
            )
            st.session_state.scores['Energy']["score"] += st.slider(
                "Waste diversion effectiveness (0-10)",
                0, 10, 5,
                key="energy2"
            )
            st.session_state.scores['Energy']["score"] = st.session_state.scores['Energy']["score"] / 2
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Supply Chain
        with st.container():
            st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
            st.markdown("#### 🚚 Sustainable Supply Chain")
            st.session_state.scores['Supply Chain']["score"] = st.slider(
                "Supplier sustainability (0-10)",
                0, 10, 5,
                key="supply1"
            )
            st.session_state.scores['Supply Chain']["score"] += st.slider(
                "Logistics optimization (0-10)",
                0, 10, 5,
                key="supply2"
            )
            st.session_state.scores['Supply Chain']["score"] = st.session_state.scores['Supply Chain']["score"] / 2
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Profit Impact
        with st.container():
            st.markdown("<div class='assessment-card'>", unsafe_allow_html=True)
            st.markdown("#### 💰 Profitability Impact")
            st.session_state.scores['Profit Impact']["score"] = st.slider(
                "Sustainable revenue contribution (0-10)",
                0, 10, 5,
                key="profit1"
            )
            st.session_state.scores['Profit Impact']["score"] += st.slider(
                "Green marketing effectiveness (0-10)",
                0, 10, 5,
                key="profit2"
            )
            st.session_state.scores['Profit Impact']["score"] = st.session_state.scores['Profit Impact']["score"] / 2
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Form submission
    submitted = st.form_submit_button("🚀 Generate Comprehensive Report", type="primary")
    if submitted:
        st.session_state.submitted = True
        st.rerun()

# ======================
# 4. INTERACTIVE RESULTS DASHBOARD
# ======================
if st.session_state.submitted:
    st.markdown("---")
    st.header("📊 Sustainability Intelligence Dashboard")
    
    # Create metrics row
    total_score = sum(v["score"] for v in st.session_state.scores.values()) / len(st.session_state.scores)
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.metric("Overall Score", f"{total_score:.1f}/10", delta=f"{(total_score - 5):+.1f} vs avg")
    with m2:
        best = max(st.session_state.scores.items(), key=lambda x: x[1]["score"])
        st.metric("Strongest Area", best[0], delta=f"{best[1]['score']:.1f}")
    with m3:
        weak = min(st.session_state.scores.items(), key=lambda x: x[1]["score"])
        st.metric("Improvement Area", weak[0], delta=f"-{(weak[1]['target'] - weak[1]['score']):.1f}")
    with m4:
        st.metric("Benchmark Gap", f"{(total_score - 6.5):+.1f}", "vs industry")
    
    style_metric_cards(border_left_color="#0052D9")
    
    # Create dashboard columns
    dash1, dash2 = st.columns([3, 2])
    
    with dash1:
        # Radar Chart
        st.markdown("### Performance Radar")
        categories = list(st.session_state.scores.keys())
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=[v["score"] for v in st.session_state.scores.values()],
            theta=categories,
            fill='toself',
            name='Your Scores',
            line_color='#4364F7'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=[v["target"] for v in st.session_state.scores.values()],
            theta=categories,
            name='Target Scores',
            line_color='#FF6B6B'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with dash2:
        # Gap Analysis
        st.markdown("### Target Gap Analysis")
        gap_data = {
            "Category": categories,
            "Your Score": [v["score"] for v in st.session_state.scores.values()],
            "Target": [v["target"] for v in st.session_state.scores.values()],
            "Gap": [v["target"] - v["score"] for v in st.session_state.scores.values()]
        }
        
        st.dataframe(
            pd.DataFrame(gap_data).sort_values("Gap", ascending=False),
            hide_index=True,
            use_container_width=True,
            column_config={
                "Gap": st.column_config.ProgressColumn(
                    "Gap",
                    format="%.1f",
                    min_value=0,
                    max_value=5,
                )
            }
        )
        
        # Priority Recommendations
        st.markdown("### 🔍 Priority Recommendations")
        weak_category = min(st.session_state.scores.items(), key=lambda x: x[1]["score"])[0]
        
        if weak_category == "Carbon":
            st.markdown("""
            - Implement real-time emission monitoring
            - Conduct carbon accounting training
            - Explore carbon offset programs
            """)
        elif weak_category == "Energy":
            st.markdown("""
            - Schedule energy efficiency audit
            - Upgrade to smart HVAC systems
            - Implement renewable energy solutions
            """)

# ======================
# 5. EXPANDABLE TOOLKIT
# ======================
with st.expander("🛠️ SUSTAINABILITY TOOLKIT", expanded=False):
    t1, t2, t3 = st.tabs(["Resources", "Benchmarks", "Action Planner"])
    
    with t1:
        st.markdown("""
        **Implementation Guides:**
        - [Carbon Reduction Playbook](#)
        - [Energy Efficiency Handbook](#)
        - [Sustainable Procurement Guide](#)
        
        **Tools & Templates:**
        - [Sustainability Scorecard Template](#)
        - [ROI Calculator](#)
        - [Vendor Assessment Form](#)
        """)
    
    with t2:
        st.markdown("""
        | Category       | Industry Avg | Top Quartile |
        |----------------|-------------:|-------------:|
        | Carbon         | 5.8         | 8.4          |
        | Energy         | 6.2         | 8.7          |
        | Supply Chain   | 4.9         | 7.5          |
        | Profit Impact  | 7.1         | 9.2          |
        """)
    
    with t3:
        st.markdown("""
        **30-Day Action Plan:**
        1. Conduct gap analysis (Week 1)
        2. Prioritize 3 quick wins (Week 2)
        3. Develop roadmap (Week 3-4)
        
        **Stakeholder Engagement:**
        - Executive briefing deck
        - Departmental workshops
        - Vendor alignment sessions
        """)

# ======================
# 6. PROFESSIONAL FOOTER
# ======================
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#64748b; font-size:0.9em; padding:1.5rem;">
    DURACAM Sustainability Intelligence Platform • v3.2 • 
    <a href="#" style="color:#4364F7;">Terms</a> • 
    <a href="#" style="color:#4364F7;">Privacy</a> • 
    <a href="#" style="color:#4364F7;">Contact Support</a>
</div>
""", unsafe_allow_html=True)
