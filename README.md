# Student Placement Prediction System

## Overview

The Student Placement Prediction System is a Machine Learning project developed to estimate a student's placement chances based on academic performance, aptitude skills, projects, internships, certifications, soft skills, extracurricular activities, and placement training.

The system predicts placement status, placement probability, placement readiness score, and provides personalized recommendations to help students improve their profiles.

---

## Problem Statement

Students often find it difficult to evaluate their placement readiness and identify the areas that need improvement.

The objective of this project is to use Machine Learning techniques to analyze student-related attributes and predict placement outcomes.

---

## Dataset Information

The dataset used in this project contains approximately 10,000 student records and includes information related to academics, skills, training, and placement outcomes.

### Features

- SSC Marks
- HSC Marks
- CGPA
- Aptitude Test Score
- Soft Skills Rating
- Projects
- Internships
- Workshops/Certifications
- Extracurricular Activities
- Placement Training

### Target Variable

- Placement Status

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Pickle

---

## Project Workflow

### 1. Data Collection

The dataset was collected from a publicly available source and loaded using Pandas.

### 2. Data Preprocessing

The following preprocessing steps were performed:

- Checked missing values
- Checked duplicate records
- Label Encoding for categorical features
- Feature selection
- Train-Test Split
- Feature Scaling using StandardScaler

### 3. Exploratory Data Analysis

EDA was performed to understand:

- Data distribution
- Correlation between features
- Placement status distribution
- Feature relationships

Visualization tools such as Matplotlib and Seaborn were used.

### 4. Model Training

Multiple machine learning approaches were explored.

Initially, Logistic Regression was used as a baseline classification model.

Random Forest Classifier was later trained and selected as the final model because it was able to capture feature interactions effectively and also provided feature importance analysis.

---

## Features Used for Training

The final model was trained using the following features:

- SSC_Marks
- HSC_Marks
- CGPA
- AptitudeTestScore
- SoftSkillsRating
- Projects
- Internships
- Workshops/Certifications
- ExtracurricularActivities
- PlacementTraining

Target:

- PlacementStatus

---

## Model Evaluation

The model was evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report
- Cross Validation

These evaluation metrics were used to assess model performance and generalization capability.

---

## Model Outputs

The system provides the following outputs:

### 1. Placement Status

Predicts whether the student is likely to get placed or not.

### 2. Placement Probability

Predicts the probability of placement based on the learned patterns from the dataset.

**Note:**
The placement probability represents the model's prediction and should not be considered as a guaranteed placement outcome.

### 3. Placement Readiness Score

A readiness score is calculated to provide an interpretable assessment of the student's overall profile.

### 4. Personalized Recommendations

The system generates recommendations such as:

- Improve academic performance
- Improve aptitude skills
- Gain internship experience
- Build more projects
- Complete additional certifications
- Attend placement training

---

## Feature Importance Analysis

Feature importance analysis was performed using Random Forest.

This helps identify which features contributed more to the model's predictions.

It is important to note that feature importance values are dependent on the dataset patterns and may not always perfectly match real-world hiring practices.

---

## Model Deployment

The trained model and scaler were saved using Pickle.

A Streamlit web application was developed to provide an interactive interface where users can:

- Enter student details
- Predict placement probability
- View readiness score
- Receive recommendations

---

## Project Limitations

- The project uses a publicly available dataset.
- Real-world hiring decisions depend on additional factors such as interviews, communication skills, company requirements, and market conditions.
- The model predictions are based on patterns learned from the available dataset.

---

## Future Improvements

Possible future enhancements include:

- Using real-world placement datasets
- Comparing additional models such as XGBoost and Gradient Boosting
- Resume analysis integration
- Interview performance assessment
- Explainable AI based recommendation system

---

## Conclusion

This project demonstrates a complete Machine Learning workflow including data preprocessing, model training, evaluation, prediction, and deployment.

The system can help students estimate their placement readiness and understand the factors that influence placement outcomes while also highlighting areas for improvement.
