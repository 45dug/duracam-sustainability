import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title and description
st.title("DURACAM Sustainability Assessment Platform")
st.markdown("""
Plan, justify and implement sustainability practices with precision for your company.
""")

# Initialize session state for scores if not exists
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'Carbon': 0,
        'Energy': 0,
        'Supply Chain': 0,
        'Circular': 0,
        'Profitability Impact': 0
    }

# Assessment questions for each scheme
questions = {
    'Carbon': [
        "How optimized are your process choices for minimal emissions?",
        "What percentage of your operations are compliant with emission regulations?",
        "Do you track CO₂ emissions per production unit?"
    ],
    'Energy': [
        "Have you implemented energy-efficient equipment upgrades?",
        "What percentage of your energy comes from renewable sources?",
        "How effective is your waste diversion program?"
    ],
    'Supply Chain': [
        "How much have you invested in sustainable transport options?",
        "What percentage of your suppliers meet sustainability criteria?",
        "How reliable are your sustainable delivery methods?"
    ],
    'Circular': [
        "What incentives do you offer for product reuse/recycling?",
        "What percentage of your products are designed for circularity?",
        "How effective is your product return/reuse program?"
    ],
    'Profitability Impact': [
        "How does your pricing strategy reflect sustainability investments?",
        "How effective is your green marketing?",
        "What percentage of revenue comes from sustainable products?"
    ]
}

# Assessment form
with st.form("sustainability_assessment"):
    st.header("Sustainability Assessment")
    
    # Create sliders for each question
    for scheme in questions:
        st.subheader(scheme)
        for i, question in enumerate(questions[scheme]):
            response = st.slider(
                question,
                min_value=0,
                max_value=10,
                value=5,
                key=f"{scheme}_{i}"
            )
            st.session_state.scores[scheme] += response
    
    submitted = st.form_submit_button("Submit Assessment")
    
    if submitted:
        st.success("Assessment submitted successfully!")
        st.session_state.assessment_done = True

# Display results if assessment done
if 'assessment_done' in st.session_state and st.session_state.assessment_done:
    st.header("Assessment Results")
    
    # Create DataFrame for scores
    scores_df = pd.DataFrame.from_dict(
        st.session_state.scores, 
        orient='index', 
        columns=['Score']
    )
    
    # Display scores table
    st.subheader("Performance by Sustainability Scheme")
    st.dataframe(scores_df.style.highlight_max(axis=0))
    
    # Create pie chart
    st.subheader("Sustainability Performance Distribution")
    fig, ax = plt.subplots()
    ax.pie(
        scores_df['Score'], 
        labels=scores_df.index,
        autopct='%1.1f%%',
        startangle=90
    )
    ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
    st.pyplot(fig)
    
    # High impact recommendations
    st.subheader("High Impact Recommendations")
    max_scheme = max(st.session_state.scores, key=st.session_state.scores.get)
    st.write(f"Your strongest area is **{max_scheme}**. Consider these high-impact practices:")
    
    recommendations = {
        'Carbon': "Implement carbon capture technologies and transition to renewable energy sources.",
        'Energy': "Upgrade to smart energy systems and implement waste-to-energy programs.",
        'Supply Chain': "Develop a supplier sustainability program and optimize logistics routes.",
        'Circular': "Launch a product take-back program and design for disassembly.",
        'Profitability Impact': "Develop premium sustainable product lines and enhance green branding."
    }
    
    st.write(recommendations[max_scheme])