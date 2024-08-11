import streamlit as st

def adult_vision_analysis(screen_time, device, lifestyle_factors):
    st.subheader("Vision Health Analysis for Adults (19-40 Years of Age)")
    
    # Protecting Eyes from Digital Strain
    st.write("### Protecting Eyes from Digital Strain")
    st.write("Young adults typically have healthy eyes, but prolonged exposure to digital devices can lead to visual stress. Here are some tips to protect your eyes:")
    st.write("- Use special glasses or lens coatings to block short-wavelength visible light from digital screens.")
    st.write("- Take frequent breaks using the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds.")
    st.write("- Adjust your computer screen's brightness and position it below eye level to reduce strain.")

    # Protecting Eyes from the Sun
    st.write("### Protecting Eyes from the Sun")
    st.write("The sun emits harmful UV rays that can damage your eyes over time. Follow these steps to protect your eyes:")
    st.write("- Wear sunglasses with 99-100% UV-A and UV-B protection.")
    st.write("- Use sunscreen around your eyes and wear a hat for extra protection.")
    
    # Preventing Eye Injuries at Work, Home, and Play
    st.write("### Preventing Eye Injuries")
    st.write("Eye injuries can occur in various settings. Ensure proper eye protection in the following scenarios:")
    st.write("- **At Work:** Wear appropriate safety eyewear to protect against chemical splashes, flying objects, and radiation exposure.")
    st.write("- **At Home:** Use eye protection when handling household chemicals, woodworking, or using power tools.")
    st.write("- **At Play:** Use specialized eyewear for sports activities to prevent injuries.")

    # Dealing with Visual Stress
    st.write("### Dealing with Visual Stress")
    st.write("Long hours of work or study can cause eyestrain. Here are some recommendations to reduce visual stress:")
    st.write("- Adjust your workspace lighting and posture to minimize strain.")
    st.write("- Blink frequently and use artificial tears if necessary.")
    st.write("- Maintain proper posture and take breaks to refresh your eyes.")

    # Routine Eye Exams
    st.write("### Routine Eye Exams")
    st.write("Regular eye exams are essential for maintaining good vision. Consider the following recommendations:")
    st.write("- Schedule an eye exam at least every two years.")
    st.write("- If you have a family history of eye problems, consider more frequent exams.")
    
    # Lifestyle Recommendations
    st.write("### Lifestyle Recommendations")
    st.write("Adopt a healthy lifestyle to support your vision:")
    st.write("- Eat a balanced diet rich in antioxidants.")
    st.write("- Get regular exercise to improve blood circulation and oxygen levels to the eyes.")
    st.write("- Avoid smoking, which increases the risk of macular degeneration and cataracts.")

    # Vision Problems and Treatments
    st.write("### Understanding Vision Problems and Treatments")
    st.write("Be aware of common vision problems such as nearsightedness, farsightedness, astigmatism, and the available treatments:")
    st.write("- Corrective lenses or surgery can help address refractive errors.")
    st.write("- For more serious conditions like cataracts, macular degeneration, and glaucoma, advanced medical and surgical treatments are available.")
    st.write("- Regular eye exams can help detect and manage these conditions early.")

# Example usage in a Streamlit app:
st.title("Screen Time and Vision Health Analysis")

age = st.slider("Select your age", 19, 40, 25)
screen_time = st.number_input("Enter your daily screen time (in hours)", min_value=1.0, max_value=24.0, value=5.0)
device = st.selectbox("Select your primary device", ["Mobile", "Laptop", "Television"])

lifestyle_factors = {
    "smoking": st.checkbox("Do you smoke?"),
    "exercise": st.checkbox("Do you exercise regularly?"),
    "diet": st.checkbox("Do you eat a balanced diet?")
}

# Run analysis
adult_vision_analysis(screen_time, device, lifestyle_factors)
