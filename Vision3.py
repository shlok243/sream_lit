import streamlit as st

def adult_vision_analysis(screen_time, device, lifestyle_factors):
    recommendations = []
    
    # Vision Health Recommendations
    if device.lower() in ["mobile", "laptop"]:
        recommendations.append("Consider using special glasses or lens coatings to block blue light from digital screens to reduce digital eye strain.")

    if screen_time > 6:
        recommendations.append("You are spending a significant amount of time on screens. Follow the 20-20-20 rule: Every 20 minutes, take a 20-second break and look at something 20 feet away.")

    if "outdoor" in lifestyle_factors:
        recommendations.append("Ensure you are protecting your eyes from UV rays by wearing sunglasses that block 99-100% of both UV-A and UV-B radiation.")

    if "smoking" in lifestyle_factors:
        recommendations.append("Consider quitting smoking as it increases the risk of age-related macular degeneration and cataracts.")

    if "exercise" in lifestyle_factors:
        recommendations.append("Continue regular exercise to improve blood circulation and oxygen levels to your eyes.")

    if "diet" in lifestyle_factors:
        recommendations.append("Maintain a balanced diet rich in antioxidants, leafy greens, and fish to support eye health.")

    # Safety Recommendations
    recommendations.append("At home, always wear eye protection when using strong chemicals, power tools, or performing tasks that could lead to eye injuries.")

    # Display Recommendations
    st.subheader("Personalized Vision Health Recommendations")
    for recommendation in recommendations:
        st.write("- " + recommendation)

# Streamlit App Layout
st.title("Screen Time and Vision Health Analyzer")

screen_time = st.slider("Daily Screen Time (in hours)", 0, 12, 6)
device = st.selectbox("Primary Device Used", ["Mobile", "Laptop", "Television", "Tablet"])
lifestyle_factors = st.multiselect(
    "Select Your Lifestyle Factors",
    ["outdoor activities", "smoking", "balanced diet", "exercise", "prolonged screen time"]
)

if st.button("GIVE SOLUTION"):
    adult_vision_analysis(screen_time, device, lifestyle_factors)
