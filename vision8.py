import streamlit as st

# Function to generate diagnosis based on input parameters
def get_diagnosis(age, screen_time, device, eye_issues, lifestyle_factors):
    common_issues = []
    recommended_actions = []
    preventive_measures = []
    specialist_advice = []

    # Age-based recommendations
    if age in range(19, 31):
        common_issues.append("Digital Eye Strain, UV Damage")
        recommended_actions.append("Use the 20-20-20 rule, Wear UV-protective sunglasses")
    elif age in range(31, 41):
        common_issues.append("Beginning Presbyopia, Ongoing Digital Strain")
        recommended_actions.append("Consider reading glasses, Continue 20-20-20 rule")
    elif age in range(41, 51):
        common_issues.append("Progressive Presbyopia, Risk of Dry Eye, Glaucoma")
        recommended_actions.append("Get annual eye exams, Use moisturizing eye drops")
    elif age in range(51, 61):
        common_issues.append("Advanced Presbyopia, Risk of Cataracts and Glaucoma")
        recommended_actions.append("Consult for cataract surgery if needed, Monitor for glaucoma")
    elif age in range(61, 71):
        common_issues.append("Cataracts, Risk of AMD, Diabetic Retinopathy")
        recommended_actions.append("Consider cataract surgery, Regular AMD screening")
    elif age in range(71, 81):
        common_issues.append("Advanced AMD, Ongoing Glaucoma Management")
        recommended_actions.append("Manage AMD with available treatments, Continue glaucoma management")
    elif age in range(81, 91):
        common_issues.append("Complex Cataract Surgery Needs, Severe AMD")
        recommended_actions.append("Explore advanced cataract surgery options, Use low-vision aids")
    elif age in range(91, 101):
        common_issues.append("Multiple Age-Related Conditions")
        recommended_actions.append("Focus on comfort and quality of life, Frequent eye exams")

    # Screen time-based recommendations
    if screen_time == '<1 hour':
        preventive_measures.append("Minimal risk from screen time")
    elif screen_time == '1-3 hours':
        preventive_measures.append("Regular breaks recommended")
    elif screen_time == '4-6 hours':
        preventive_measures.append("Increase frequency of breaks, Use anti-glare screens")
    elif screen_time == '>6 hours':
        preventive_measures.append("Consider blue light blocking glasses, Schedule frequent eye exams")

    # Device-based recommendations
    if device == 'Mobile':
        preventive_measures.append("Use night mode on devices, Maintain proper distance")
    elif device == 'Laptop':
        preventive_measures.append("Adjust screen brightness and contrast, Use ergonomically designed chairs")
    elif device == 'Television':
        preventive_measures.append("Maintain proper viewing distance, Use appropriate room lighting")

    # Eye issues-based recommendations
    if 'Dry Eyes' in eye_issues:
        recommended_actions.append("Use lubricating eye drops, Avoid dry environments")
    if 'Blurred Vision' in eye_issues:
        recommended_actions.append("Consider a comprehensive eye exam for refractive errors")
    if 'Headaches' in eye_issues:
        recommended_actions.append("Check for visual stress and adjust screen settings")

    # Lifestyle factors-based recommendations
    if 'Smoking' in lifestyle_factors:
        specialist_advice.append("Seek advice on quitting smoking, as it affects eye health")
    if 'Poor Diet' in lifestyle_factors:
        recommended_actions.append("Increase intake of fruits and vegetables rich in antioxidants")
    if 'Lack of Exercise' in lifestyle_factors:
        recommended_actions.append("Incorporate regular exercise to improve circulation")
    if 'High Stress' in lifestyle_factors:
        recommended_actions.append("Practice stress management techniques like mindfulness and relaxation exercises")
    if 'Excessive Alcohol Consumption' in lifestyle_factors:
        specialist_advice.append("Moderate alcohol consumption as it can impact overall health and vision")

    return common_issues, recommended_actions, preventive_measures, specialist_advice

# Streamlit UI setup
st.title("Virtual Eye Specialist")

# Input fields
age = st.slider("Select your age", 0, 100, 25)
screen_time = st.selectbox("Screen Time", ["<1 hour", "1-3 hours", "4-6 hours", ">6 hours"])
device = st.selectbox("Primary Device", ["Mobile", "Laptop", "Television"])
eye_issues = st.multiselect("Eye Issues", ["Dry Eyes", "Blurred Vision", "Headaches", "None"])
lifestyle_factors = st.multiselect("Lifestyle Factors", [
    "Smoking",
    "Poor Diet",
    "Lack of Exercise",
    "High Stress",
    "Excessive Alcohol Consumption",
    "None"
])

# Button to get diagnosis
if st.button("Get Diagnosis"):
    common_issues, recommended_actions, preventive_measures, specialist_advice = get_diagnosis(age, screen_time, device, eye_issues, lifestyle_factors)

    st.subheader("Diagnosis Summary")
    st.write("### Common Issues")
    st.write(", ".join(common_issues) if common_issues else "No common issues detected.")

    st.write("### Recommended Actions")
    st.write(", ".join(recommended_actions) if recommended_actions else "No specific actions needed.")

    st.write("### Preventive Measures")
    st.write(", ".join(preventive_measures) if preventive_measures else "No additional preventive measures required.")

    st.write("### Specialist Advice")
    st.write(", ".join(specialist_advice) if specialist_advice else "No specialist advice required.")
