import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

st.set_page_config(page_title="DURACAM Sustainability Tool", layout="centered")

# Inject custom CSS for dark blue background and text styling
st.markdown(
    """
    <style>
    body {
        background-color: #003366;
        color: white;
    }
    .stApp {
        background-color: #003366;
        color: white;
    }
    .title h1, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: white;
    }
    .stMarkdown {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
section = st.sidebar.radio("Navigate", ["🏠 Home", "📊 Assessment", "🏗️ ROI Simulator"])

# Main Header
st.title("🌱 DURACAM")
st.subheader("Helping companies meet their sustainability goals")

if section == "🏠 Home":
    st.markdown("""
    Welcome to the **DURACAM Sustainability Assessment Tool**.

    - Evaluate your company’s sustainability across six domains.
    - Visualize results with charts.
    - Export a summary PDF.
    - Simulate ROI with real-time modeling.

    Select **"📊 Assessment"** in the sidebar to begin.
    """)

elif section == "📊 Assessment":
    st.header("📊 Sustainability Assessment")

    st.markdown("Rate your organization from 1 (Poor) to 10 (Excellent) across the following domains:")

    carbon = st.slider("🌍 Carbon Emissions", 1, 10, 5)
    energy = st.slider("⚡ Energy Usage", 1, 10, 5)
    waste = st.slider("🗑️ Waste Management", 1, 10, 5)
    supply_chain = st.slider("🚚 Supply Chain Footprint", 1, 10, 5)
    circular = st.slider("🔁 Circular Economy Practices", 1, 10, 5)
    profit = st.slider("💸 Profitability Impact", 1, 10, 5)

    if st.button("Calculate Score"):
        scores = [carbon, energy, waste, supply_chain, circular, profit]
        labels = [
            "Carbon Emissions", "Energy", "Waste Management",
            "Supply Chain", "Circular Economy", "Profitability"
        ]
        total = sum(scores)
        average = round(total / len(scores), 2)

        st.success(f"🌟 Overall Sustainability Score: **{average}/10**")

        # Pie Chart
        fig, ax = plt.subplots()
        ax.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig, use_container_width=True)

        # Recommendations
        st.markdown("### 📌 Recommendations")
        if average >= 8:
            st.success("Excellent sustainability profile. Keep leading the way! ✅")
        elif average >= 5:
            st.warning("Moderate performance. There’s room to improve on specific areas. ⚠️")
        else:
            st.error("Low sustainability score. Urgent improvements recommended. ❗")

        # PDF Export
        if st.button("📥 Export PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="DURACAM Sustainability Report", ln=True, align='C')
            pdf.ln(10)
            for label, score in zip(labels, scores):
                pdf.cell(200, 10, txt=f"{label}: {score}/10", ln=True)
            pdf.ln(5)
            pdf.cell(200, 10, txt=f"Overall Score: {average}/10", ln=True)
            filename = "duracam_sustainability_report.pdf"
            pdf.output(f"/mnt/data/{filename}")
            st.success("📄 PDF report generated!")
            st.download_button("⬇️ Download Report", data=open(f"/mnt/data/{filename}", "rb"), file_name=filename)

elif section == "🏗️ ROI Simulator":
    st.header("📈 ROI Simulation Tool")
    st.markdown("Use the embedded tool below to **simulate your ROI based on sustainability actions**:")

    # Embed external Streamlit ROI simulator
    st.components.v1.iframe("https://sustainabilitysimulator.streamlit.app/", height=800, scrolling=True)
