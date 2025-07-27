import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# -----------------------
# CONFIGURATION & THEME
# -----------------------
st.set_page_config(page_title="DURACAM Sustainability Assessment", layout="centered")
PRIMARY_COLOR = "#005f87"
BACKGROUND_COLOR = "#f1f5f9"  # Light, professional background

# Custom CSS
st.markdown(
    f"""
    <style>
        body {{
            background-color: #005f87;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }}
        .stApp {{
            background-color: #005f87;
        }}
        h1, h2, h3, h4, h5, h6, p, label {{
            color: #ffffff !important;
        }}
        .stButton>button {{
            background-color: #ffffff;
            color: #005f87;
            border: none;
            border-radius: 6px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.2s ease-in-out;
        }}
        .stButton>button:hover {{
            background-color: #f0f0f0;
            color: #003f5c;
            transform: scale(1.05);
        }}
        .stRadio>div {{
            background-color: #ffffff;
            color: #000000;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
        }}
        .block-container {{
            max-width: 700px;
            padding-top: 2rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)



# -----------------------
# HEADER
# -----------------------
st.image(
    "https://via.placeholder.com/600x100.png?text=DURACAM+Sustainability+Assessment",
    use_container_width=True
)
st.title("🌱 DURACAM")
st.markdown("**Helping companies meet their sustainability goals**")

# -----------------------
# QUESTIONS
# -----------------------
categories = {
    "Carbon Emissions": ["Process choices impact", "Emissions tracking effectiveness"],
    "Energy": ["Equipment upgrades", "Waste diversion efforts"],
    "Waste Management": ["Recycling investment", "Waste reduction policies"],
    "Supply Chain Footprint": ["Transport emissions", "Delivery reliability"],
    "Circular Economy": ["Reuse incentives", "Product return rates"],
    "Profitability Impact": ["Pricing strategy", "Green marketing initiatives"],
}

scores = {}

with st.form("assessment_form"):
    st.subheader("🔍 Please rate each factor (1 = Very Poor, 5 = Excellent):")

    for category, questions in categories.items():
        st.markdown(f"### {category}")
        category_scores = []
        for q in questions:
            score = st.radio(
                f"{q}",
                options=[1, 2, 3, 4, 5],
                horizontal=True,
                key=f"{category}_{q}"
            )
            category_scores.append(score)
        scores[category] = (sum(category_scores) / len(category_scores)) * 20  # Convert to 0-100

    submitted = st.form_submit_button("Calculate My Sustainability Score")

# -----------------------
# RESULTS
# -----------------------
if submitted:
    st.success("✅ Assessment completed! See your results below.")

    df = pd.DataFrame(list(scores.items()), columns=["Category", "Score"])

    fig = px.pie(
        df,
        names="Category",
        values="Score",
        title="Your Sustainability Score Breakdown",
        color_discrete_sequence=px.colors.sequential.Blues
    )
    fig.update_traces(textinfo='percent+label', pull=[0.05]*len(scores))
    st.plotly_chart(fig, use_container_width=True)

    avg_score = sum(scores.values()) / len(scores)
    st.metric("🌟 Average Sustainability Score", f"{avg_score:.1f} / 100")

    # Recommendations
    st.subheader("📌 Recommendations")
    for category, score in scores.items():
        if score < 50:
            st.warning(f"**{category}:** Needs significant improvement. Start with basic sustainability actions.")
        elif score < 75:
            st.info(f"**{category}:** Decent progress. Focus on optimizing your strategies.")
        else:
            st.success(f"**{category}:** Excellent! Keep maintaining strong practices.")

    # -----------------------
    # PDF Report
    # -----------------------
    def generate_pdf(data: dict, avg: float) -> bytes:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 18)
        pdf.set_text_color(0, 95, 135)
        pdf.cell(0, 10, "DURACAM Sustainability Report", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(10)
        for cat, sc in data.items():
            pdf.cell(0, 10, f"{cat}: {sc:.1f}/100", ln=True)
        pdf.cell(0, 10, f"Average Score: {avg:.1f}/100", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 10, "Thank you for using the DURACAM Sustainability Assessment. This report reflects your current performance and highlights areas for improvement.")
        pdf.output("duracam_report.pdf")
        with open("duracam_report.pdf", "rb") as f:
            return f.read()

    pdf_file = generate_pdf(scores, avg_score)
    st.download_button("📥 Download Your PDF Report", pdf_file, "DURACAM_Sustainability_Report.pdf", "application/pdf")

