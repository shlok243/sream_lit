import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate recommendations
def get_recommendations(age, screen_time, device, symptoms, lifestyle, stress_level, eye_exam_freq):
    recommendations = []
    
    if age < 40:
        recommendations.append("Focus on protecting eyes from blue light and reducing visual stress.")
    elif age < 60:
        recommendations.append("Consider regular eye exams and managing age-related vision changes.")
    else:
        recommendations.append("Emphasize managing chronic conditions and frequent eye check-ups.")
    
    if screen_time > 4:
        recommendations.append("Limit screen time and take regular breaks.")
    
    if device == 'Mobile':
        recommendations.append("Use blue light filtering apps and maintain proper viewing distance.")
    
    if 'Sore eyes' in symptoms:
        recommendations.append("Ensure proper lighting and take frequent breaks.")
    
    if lifestyle.get('Sun Exposure') == 'High':
        recommendations.append("Wear UV-protective sunglasses and use sunscreen around eyes.")
    
    if lifestyle.get('Smoking') == 'Yes':
        recommendations.append("Quit smoking to reduce risk of AMD and cataracts.")
    
    if stress_level > 7:
        recommendations.append("Consider using anti-reflective lenses and adjust your workspace lighting.")
    
    return recommendations

# Streamlit UI
st.title("Advanced Vision Health Diagnosis")
st.sidebar.header("User Input")

# Collect user inputs
age = st.sidebar.slider("Age", 1, 100, 30)
screen_time = st.sidebar.slider("Daily Screen Time (hours)", 0, 12, 4)
device = st.sidebar.selectbox("Primary Device", ["Mobile", "Laptop", "Television"])
symptoms = st.sidebar.multiselect("Eye Symptoms", ["Sore eyes", "Tired eyes", "Headaches", "Dry eyes", "Sensitivity to light"])
lifestyle = {
    'Sun Exposure': st.sidebar.selectbox("Sun Exposure", ["Low", "Moderate", "High"]),
    'Smoking': st.sidebar.selectbox("Do you smoke?", ["Yes", "No"]),
    'Exercise': st.sidebar.selectbox("Exercise Frequency", ["None", "Rarely", "Regularly"]),
    'Diet': st.sidebar.selectbox("Balanced Diet", ["Yes", "No"])
}
stress_level = st.sidebar.slider("Visual Stress Level (1-10)", 1, 10, 5)
eye_exam_freq = st.sidebar.selectbox("Eye Exam Frequency", ["Annually", "Every 2 years", "Rarely"])

# Generate recommendations
if st.sidebar.button("Get Diagnosis"):
    recommendations = get_recommendations(age, screen_time, device, symptoms, lifestyle, stress_level, eye_exam_freq)
    st.subheader("Your Diagnosis")
    for rec in recommendations:
        st.write(f"- {rec}")

# Plot example (replace with relevant data and charts)
st.subheader("Sample Data Visualization")
data = pd.DataFrame({
    'Age': [25, 35, 45, 55, 65],
    'Screen Time': [2, 4, 6, 8, 10],
    'Visual Stress': [3, 5, 7, 8, 9]
})
fig, ax = plt.subplots()
sns.lineplot(data=data, x='Age', y='Visual Stress', hue='Screen Time', marker='o', ax=ax)
st.pyplot(fig)
