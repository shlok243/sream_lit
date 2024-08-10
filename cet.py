import streamlit as st

# List of colleges and their respective MHT-CET cutoff scores
colleges = [
    {"name": "College of Engineering, Pune", "cutoff": 175},
    {"name": "Veermata Jijabai Technological Institute, Mumbai", "cutoff": 165},
    {"name": "Sardar Patel Institute of Technology, Mumbai", "cutoff": 160},
    {"name": "Walchand College of Engineering, Sangli", "cutoff": 150},
    {"name": "Vishwakarma Institute of Technology, Pune", "cutoff": 145},
    {"name": "MIT Academy of Engineering, Pune", "cutoff": 140},
    {"name": "K. J. Somaiya College of Engineering, Mumbai", "cutoff": 135},
    {"name": "Sinhgad College of Engineering, Pune", "cutoff": 130},
    {"name": "Rajarambapu Institute of Technology, Sangli", "cutoff": 125},
    {"name": "Yeshwantrao Chavan College of Engineering, Nagpur", "cutoff": 120},
]

def suggest_colleges(score):
    suggested = []
    for college in colleges:
        if score >= college["cutoff"]:
            suggested.append(f"{college['name']} (Cutoff: {college['cutoff']})")
    return suggested

# Streamlit App
st.title("MHT-CET College Selector")

st.write("""
### Enter your MHT-CET score below to find suitable colleges.
""")

# Input score
mht_cet_score = st.number_input("Enter your MHT-CET score:", min_value=0, max_value=200, step=1)

if st.button("Find Colleges"):
    # Suggest colleges based on score
    suitable_colleges = suggest_colleges(mht_cet_score)
    
    if suitable_colleges:
        st.write(f"### Based on your score of {mht_cet_score}, you can consider the following colleges:")
        for college in suitable_colleges:
            st.write(f"- {college}")
    else:
        st.write("No colleges match your score. You may want to consider other options or check for updates in the cutoff list.")

st.write("\nConsider other factors like location, campus facilities, and specializations before making your final decision.")
