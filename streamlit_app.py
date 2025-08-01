import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO

# App Styling
st.markdown("""
    <style>
    .main {
        background-color: #003366;
        color: white;
    }
    div.stButton > button {
        background-color: #0057b8;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("DURACAM")
st.subheader("Helping companies meet their sustainability goals")
st.markdown("""<hr style='border: 2px solid white'>""", unsafe_allow_html=True)

st.header("📊 Sustainability Self-Assessment")
st.markdown("Fill in your company's status under each category below.")

# Questionnaire Categories
categories = {
    "Carbon Emissions": ["Very Poor", "Poor", "Average", "Good", "Excellent"],
    "Energy": ["Very Poor", "Poor", "Average", "Good", "Excellent"],
    "Waste Management": ["Very Poor", "Poor", "Average", "Good", "Excellent"],
    "Supply Chain Footprint": ["Very Poor", "Poor", "Average", "Good", "Excellent"],
    "Circular Economy": ["Very Poor", "Poor", "Average", "Good", "Excellent"],
    "Profitability Impact": ["Very Poor", "Poor", "Average", "Good", "Excellent"]
}

score_map = {"Very Poor": 1, "Poor": 2, "Average": 3, "Good": 4, "Excellent": 5}
user_scores = {}

for cat, options in categories.items():
    choice = st.selectbox(f"{cat}", options)
    user_scores[cat] = score_map[choice]

if st.button("Generate Sustainability Report"):
    # Bar Chart Visualization
    fig, ax = plt.subplots()
    ax.bar(user_scores.keys(), user_scores.values(), color='#66b3ff')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Score (1-5)")
    plt.title("Sustainability Domain Scores")
    st.pyplot(fig, use_container_width=True)

    # PDF Report Generation
    report_data = pd.DataFrame.from_dict(user_scores, orient='index', columns=['Score'])
    report_buf = BytesIO()
    report_data.to_csv(report_buf)
    report_buf.seek(0)
    b64 = base64.b64encode(report_buf.read()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="duracam_sustainability_report.csv">📥 Download Sustainability Report</a>'
    st.markdown(href, unsafe_allow_html=True)

st.markdown("""<hr style='border: 2px solid white'>""", unsafe_allow_html=True)

# ROI Simulation Section
st.header("📈 ROI Simulation")

st.markdown("""
Adjust the fields below to simulate potential return on investment (ROI) for your sustainability project.
""")

investment = st.number_input("Investment Cost ($)", min_value=0.0, step=1000.0, format="%.2f")
savings = st.number_input("Estimated Yearly Savings ($)", min_value=0.0, step=500.0, format="%.2f")
period = st.slider("Payback Period (Years)", 1, 10, 5)
impact_score = st.slider("Environmental Benefit Score", 1, 10, 5)

if investment > 0:
    roi = ((savings * period - investment) / investment) * 100
    st.metric("Predicted ROI (%)", f"{roi:.2f}%")

    if roi < 0:
        st.warning("⚠️ Negative ROI. Re-evaluate investment or savings.")
    elif roi < 50:
        st.info("ℹ️ Moderate ROI. Consider increasing impact or savings.")
    else:
        st.success("✅ High ROI! This looks like a solid investment.")

    # ROI Visualization
    fig2, ax2 = plt.subplots()
    ax2.pie([roi, 100 - roi], labels=['ROI', 'Remaining'], autopct='%1.1f%%', startangle=140, colors=['#00cc99', '#d3d3d3'])
    ax2.axis('equal')
    st.pyplot(fig2, use_container_width=True)
else:
    st.info("Enter investment cost to begin simulation.")
