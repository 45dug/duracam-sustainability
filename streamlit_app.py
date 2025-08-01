import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="DURACAM Sustainability App", layout="wide")

# App title
st.title("🌿 DURACAM Sustainability Assessment Platform")

# Sidebar navigation
section = st.sidebar.radio("Navigate", ["🏠 Home", "📊 Assessment", "🏗️ ROI Simulator", "📄 Download Report"])

# Function to calculate total score
def calculate_score(inputs):
    return sum(inputs)

# Function to generate pie chart
def plot_pie(scores, categories):
    fig, ax = plt.subplots()
    ax.pie(scores, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    return fig

# Section: Home
if section == "🏠 Home":
    st.header("Welcome to DURACAM Sustainability Tool")
    st.markdown("""
    This tool helps you evaluate your organization’s sustainability across multiple areas
    and simulate ROI improvement opportunities.

    Use the sidebar to begin your assessment or explore the ROI simulation tool.
    """)

# Section: Assessment
elif section == "📊 Assessment":
    st.header("📊 Sustainability Assessment")

    categories = [
        "Environmental Impact", "Social Responsibility", "Economic Viability",
        "Energy Efficiency", "Waste Management", "Innovation & Technology"
    ]

    scores = []
    for category in categories:
        score = st.slider(f"{category} Score (0–10)", 0, 10, 5)
        scores.append(score)

    total_score = calculate_score(scores)

    st.subheader(f"🔢 Total Sustainability Score: `{total_score} / 60`")
    st.pyplot(plot_pie(scores, categories))

    # Save scores to session state for later use
    st.session_state["assessment_scores"] = scores
    st.session_state["total_score"] = total_score

# Section: ROI Simulator (external link)
elif section == "🏗️ ROI Simulator":
    st.header("📈 ROI Simulation Tool")
    st.markdown("""
    Due to security and platform limitations, the ROI simulator cannot be embedded directly here.

    👉 **Click the button below to launch the ROI Simulator in a new tab.**
    """)
    st.link_button("🔗 Open Sustainability ROI Simulator", "https://sustainabilitysimulator.streamlit.app/")

# Section: Downloadable Report
elif section == "📄 Download Report":
    st.header("📄 Your Sustainability Report")

    if "assessment_scores" not in st.session_state:
        st.warning("⚠️ Please complete the assessment first.")
    else:
        st.subheader("🧾 Summary")
        for i, category in enumerate(categories):
            st.write(f"- **{category}**: {st.session_state['assessment_scores'][i]} / 10")

        st.write(f"**Total Score:** `{st.session_state['total_score']} / 60`")

        # Generate downloadable text report
        report_text = "DURACAM Sustainability Assessment Report\n\n"
        for i, category in enumerate(categories):
            report_text += f"{category}: {st.session_state['assessment_scores'][i]} / 10\n"
        report_text += f"\nTotal Score: {st.session_state['total_score']} / 60"

        st.download_button(
            label="📥 Download Report as TXT",
            data=report_text,
            file_name="sustainability_report.txt",
            mime="text/plain"
        )

