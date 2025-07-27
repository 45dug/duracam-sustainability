import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# -----------------------
# CONFIGURATION
# -----------------------
st.set_page_config(page_title="DURACAM Sustainability Assessment", layout="centered")
PRIMARY_COLOR = "#005f87"

# Custom CSS for branding & WCAG compliance
st.markdown(
    f"""
    <style>
        body {{
            color: #000000;
            background-color: #ffffff;
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-size: 1.1em;
        }}
        .stProgress .st-bo {{
            background-color: {PRIMARY_COLOR};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌱 DURACAM Sustainability Assessment Platform")
st.markdown(
    "Evaluate your company's sustainability performance, view investor-ready insights, "
    "and generate a branded PDF report."
)

# -----------------------
# QUESTIONS & STRUCTURE
# -----------------------
categories = {
    "Carbon": ["Process choices impact", "Emissions tracking effectiveness"],
    "Energy": ["Equipment upgrades", "Waste diversion efforts"],
    "Supply Chain": ["Recycling investment", "Transport footprint management"],
    "Circular": ["Reuse incentives", "Return rate optimization"],
    "Profitability": ["Pricing strategy", "Green marketing initiatives"],
}

responses = {}
total_scores = {}

with st.form("assessment_form"):
    st.subheader("Rate each factor (1 = Very Poor, 5 = Excellent):")

    for category, questions in categories.items():
        st.markdown(f"### {category}")
        cat_scores = []
        for q in questions:
            score = st.radio(q, options=[1, 2, 3, 4, 5], horizontal=True, key=f"{category}_{q}")
            cat_scores.append(score)
        avg = (sum(cat_scores) / len(cat_scores)) * 20  # Convert to 0-100 scale
        total_scores[category] = avg

    submitted = st.form_submit_button("Calculate Results")

# -----------------------
# RESULTS
# -----------------------
if submitted:
    st.success("Assessment completed!")

    df = pd.DataFrame(list(total_scores.items()), columns=["Category", "Score"])
    fig = px.pie(df, names="Category", values="Score", title="Sustainability Score Distribution", color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------
    # PRACTICE RECOMMENDATIONS
    # -----------------------
    st.subheader("Recommended Practices")
    for category, score in total_scores.items():
        if score < 50:
            st.warning(f"**{category}:** Needs major improvements. Focus on foundational practices.")
        elif score < 75:
            st.info(f"**{category}:** Moderate performance. Target advanced optimizations.")
        else:
            st.success(f"**{category}:** Strong sustainability practices in place.")

    # -----------------------
    # ROI & BENCHMARKS
    # -----------------------
    st.subheader("Investor Features")
    avg_score = sum(total_scores.values()) / len(total_scores)
    roi_estimate = round(avg_score * 1.5, 2)
    st.write(f"**Estimated ROI Improvement:** {roi_estimate}%")
    st.write("**Benchmark:** Top industry performers average 80–85% across all categories.")

    st.write("**Case Study Example:** Company X improved its circular economy index by 40%, saving $2M annually.")

    # -----------------------
    # PDF REPORT GENERATION
    # -----------------------
    def generate_pdf(scores: dict, avg: float) -> bytes:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "DURACAM Sustainability Report", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        for cat, sc in scores.items():
            pdf.cell(0, 10, f"{cat}: {sc:.1f}/100", ln=True)
        pdf.cell(0, 10, f"Average Score: {avg:.1f}/100", ln=True)
        pdf.cell(0, 10, f"Estimated ROI Improvement: {roi_estimate}%", ln=True)
        pdf.output("report.pdf")
        with open("report.pdf", "rb") as f:
            return f.read()

    pdf_data = generate_pdf(total_scores, avg_score)
    st.download_button("📥 Download PDF Report", pdf_data, "DURACAM_Sustainability_Report.pdf", "application/pdf")
