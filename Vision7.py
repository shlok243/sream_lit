import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform diagnosis based on user inputs
def diagnose(screen_time, device, lifestyle_factors):
    # Diagnosis logic (placeholder)
    results = {
        "visual_stress": "Low",
        "eye_strain": "Medium",
        "risk_of_macular_degeneration": "High" if screen_time > 4 else "Low",
        "recommendations": []
    }
    
    if lifestyle_factors['sleep'] < 6:
        results['recommendations'].append("Increase sleep duration to at least 7-8 hours.")
    
    if lifestyle_factors['diet'] < 5:
        results['recommendations'].append("Improve diet with more fruits and vegetables.")
    
    if lifestyle_factors['exercise'] < 30:
        results['recommendations'].append("Increase physical activity to at least 30 minutes a day.")
    
    if device == 'mobile':
        results['recommendations'].append("Consider using blue light filtering glasses.")
    
    return results

# Streamlit UI
st.title('Advanced Vision Diagnosis App')
st.write("This app provides a detailed diagnosis based on your screen time habits and lifestyle factors.")

# Input fields
screen_time = st.slider('Average daily screen time (hours):', min_value=0, max_value=24, value=2)
device = st.selectbox('Primary device used:', ['mobile', 'laptop', 'television'])
age = st.slider('Age:', min_value=0, max_value=100, value=25)

# Lifestyle factors
st.subheader('Lifestyle Factors')
sleep = st.slider('Average sleep duration per night (hours):', min_value=0, max_value=24, value=8)
diet = st.slider('Average servings of fruits and vegetables per day:', min_value=0, max_value=10, value=5)
exercise = st.slider('Average exercise duration per week (minutes):', min_value=0, max_value=600, value=150)

# Perform diagnosis when button is pressed
if st.button('GIVE SOLUTION'):
    lifestyle_factors = {
        'sleep': sleep,
        'diet': diet,
        'exercise': exercise
    }
    diagnosis = diagnose(screen_time, device, lifestyle_factors)
    
    st.write("## Diagnosis Results")
    st.write(f"Visual Stress: {diagnosis['visual_stress']}")
    st.write(f"Eye Strain: {diagnosis['eye_strain']}")
    st.write(f"Risk of Macular Degeneration: {diagnosis['risk_of_macular_degeneration']}")
    
    st.write("## Recommendations")
    for recommendation in diagnosis['recommendations']:
        st.write(f"- {recommendation}")
    
    # Plotting
    fig, ax = plt.subplots()
    sns.barplot(x=list(diagnosis.keys()), y=[1]*len(diagnosis.keys()), ax=ax)
    ax.set_title('Diagnosis Summary')
    ax.set_ylabel('Severity')
    st.pyplot(fig)
