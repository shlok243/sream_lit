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
    if 'Alcohol Consumption' in lifestyle_factors:
        specialist_advice.append("Moderate alcohol intake to reduce the risk of eye problems")
    if 'Poor Sleep Quality' in lifestyle_factors:
        recommended_actions.append("Improve sleep habits to reduce eye strain and dryness")
    if 'Poor Work Environment' in lifestyle_factors:
        preventive_measures.append("Optimize workspace ergonomics and lighting")
    if 'Inadequate Hydration' in lifestyle_factors:
        recommended_actions.append("Ensure adequate hydration for eye moisture")
    if 'High Stress Levels' in lifestyle_factors:
        recommended_actions.append("Manage stress to prevent visual symptoms")
    if 'Inadequate Eye Protection' in lifestyle_factors:
        preventive_measures.append("Use appropriate eye protection during hazardous activities")
    if 'Non-Adherence to Vision Correction' in lifestyle_factors:
        recommended_actions.append("Regularly use prescribed glasses or contact lenses")

    return common_issues, recommended_actions, preventive_measures, specialist_advice
