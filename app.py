
import streamlit as st
import pickle
import pandas as pd


# PAGE CONFIG


st.set_page_config(
    page_title="Student Placement Prediction System",
    layout="wide"
)


# CUSTOM CSS


st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

.main-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #CCCCCC;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)


# LOAD MODEL


model = pickle.load(
    open("placement_model.pkl", "rb")
)

scaler = pickle.load(
    open("scaler.pkl", "rb")
)

# TITLE


st.markdown(
    '<p class="main-title"> Student Placement Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning Based Placement Readiness Assessment</p>',
    unsafe_allow_html=True
)

st.write("---")


# INPUTS


col1, col2 = st.columns(2)

with col1:

    ssc_marks = st.slider(
        "SSC Marks",
        0,
        100,
        70
    )

    hsc_marks = st.slider(
        "HSC Marks",
        0,
        100,
        70
    )

    cgpa = st.slider(
        "CGPA",
        0.0,
        10.0,
        7.0
    )

    aptitude = st.slider(
        "Aptitude Test Score",
        0,
        100,
        70
    )

    soft_skills = st.slider(
        "Soft Skills Rating",
        0,
        100,
        70
    )

with col2:

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=10,
        value=2
    )

    internships = st.number_input(
        "Internships",
        min_value=0,
        max_value=10,
        value=1
    )

    certifications = st.number_input(
        "Workshops / Certifications",
        min_value=0,
        max_value=10,
        value=1
    )

    extracurricular = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

    placement_training = st.selectbox(
        "Placement Training",
        ["No", "Yes"]
    )

# CONVERT VALUES

extracurricular_value = (
    1 if extracurricular == "Yes"
    else 0
)

placement_training_value = (
    1 if placement_training == "Yes"
    else 0
)

# PREDICTION BUTTON

if st.button("Predict Placement"):

    sample_data = pd.DataFrame([{
        'SSC_Marks': ssc_marks,
        'HSC_Marks': hsc_marks,
        'CGPA': cgpa,
        'AptitudeTestScore': aptitude,
        'SoftSkillsRating': soft_skills,
        'Projects': projects,
        'Internships': internships,
        'Workshops/Certifications': certifications,
        'ExtracurricularActivities': extracurricular_value,
        'PlacementTraining': placement_training_value
    }])

    sample_scaled = scaler.transform(
        sample_data
    )

    prediction = model.predict(
        sample_scaled
    )

    probability = (
        model.predict_proba(
            sample_scaled
        )[0][1] * 100
    )

    # Readiness Score

    readiness_score = (
        cgpa * 10 * 0.25 +
        aptitude * 0.25 +
        soft_skills * 0.20 +
        projects * 5 +
        internships * 5 +
        certifications * 3 +
        placement_training_value * 10
    )

    readiness_score = min(
        readiness_score,
        100
    )

    st.write("---")

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.success(
            f"Student is likely to get placed with {probability:.2f}% probability"
        )

    else:

        st.error(
            f"Student is less likely to get placed with {probability:.2f}% probability"
        )

    st.info(
        f"Placement Readiness Score: {readiness_score:.2f}/100"
    )

    # Readiness Level

    if readiness_score >= 80:

        st.success(
            "Readiness Level: Excellent"
        )

    elif readiness_score >= 60:

        st.success(
            "Readiness Level: Good"
        )

    elif readiness_score >= 40:

        st.warning(
            "Readiness Level: Average"
        )

    else:

        st.error(
            "Readiness Level: Needs Improvement"
        )

    # Recommendations

    st.subheader(
        "Personalized Recommendations"
    )

    recommendations = []

    if cgpa < 7:
        recommendations.append(
            "Improve CGPA and academic consistency"
        )

    if aptitude < 60:
        recommendations.append(
            "Practice aptitude and reasoning questions"
        )

    if soft_skills < 60:
        recommendations.append(
            "Improve communication and soft skills"
        )

    if internships == 0:
        recommendations.append(
            "Gain internship experience"
        )

    if projects < 2:
        recommendations.append(
            "Build more practical projects"
        )

    if certifications < 2:
        recommendations.append(
            "Complete additional certifications"
        )

    if placement_training_value == 0:
        recommendations.append(
            "Attend placement training sessions"
        )

    if recommendations:

        for item in recommendations:
            st.write("•", item)

    else:

        st.success(
            "Your profile looks strong. Continue interview preparation."
        )
