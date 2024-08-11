import streamlit as st

# Function to provide recommendations based on device and screen time
def provide_recommendations(age, screen_time, device, apps=None, posture=None):
    recommendations = []
    
    if screen_time > 4:
        recommendations.append("Your screen time is above 4 hours daily. Consider reducing screen time to prevent eye strain.")
    
    if device == "Mobile":
        recommendations.append("You're using a mobile device for most of your screen time.")
        if apps:
            recommendations.append(f"Consider limiting usage of the following apps: {', '.join(apps)}.")
        recommendations.append("Use blue light filters and take breaks to rest your eyes.")
        
    elif device == "Laptop":
        recommendations.append("You're using a laptop for most of your screen time.")
        if posture:
            recommendations.append(f"Ensure that you maintain a correct sitting posture: {posture}.")
        recommendations.append("Use ergonomic furniture and take frequent breaks to stretch.")
        
    elif device == "Television":
        recommendations.append("You're using a television for most of your screen time.")
        recommendations.append("Sit at a proper distance from the screen and ensure proper lighting in the room.")
        recommendations.append("Take breaks to avoid eye fatigue and consider reducing television time.")

    if age < 18:
        recommendations.append("As a young user, it's important to limit screen time to promote healthy development.")
    elif age > 50:
        recommendations.append("Consider using larger fonts and higher contrast settings to reduce eye strain.")

    return recommendations

# Streamlit App
st.title("Screen Time Analyzer and Recommendations")

# Input: Age
age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)

# Input: Daily Screen Time
screen_time = st.number_input("Enter your daily screen time (in hours):", min_value=0, max_value=24, step=1)

# Input: Primary Device Used
device = st.selectbox("Select your primary screen time device:", ["Mobile", "Laptop", "Television"])

# Additional inputs based on device
if device == "Mobile":
    apps = st.multiselect("Which apps do you use most frequently?", ["Social Media", "Streaming", "Gaming", "Browsing", "Other"])
elif device == "Laptop":
    posture = st.radio("Are you maintaining a correct sitting posture?", ["Yes", "No"])
else:
    apps = None
    posture = None

# Button to analyze and provide recommendations
if st.button("Analyze and Get Recommendations"):
    recommendations = provide_recommendations(age, screen_time, device, apps, posture)
    st.write("### Recommendations:")
    for rec in recommendations:
        st.write(f"- {rec}")

st.write("\nUse this tool to better manage your screen time and promote healthier habits!")
