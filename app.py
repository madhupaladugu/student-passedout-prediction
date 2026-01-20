import streamlit as st
import pandas as pd
import pickle
import sklearn

# ---------------- CSS FOR BACKGROUND & STYLING ----------------
# ---------------- CSS FOR BACKGROUND & STYLING ----------------
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://i.pinimg.com/736x/04/09/5c/04095cbd2bdd134a6480fdf160fb8694.jpg");
        background-size: cover;
        background-position: center;
    }
    
    /* Heading styling */
    .title {
        color: #ffff;
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Subheading text */
    .subheading {
        color: black;
        font-size: 30px;
        text-align: center;
        text-shadow: 1px 1px 2px #000000;
    }

    /* Buttons styling */
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        height: 50px;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- LOAD MODEL ----------------
with open("model (1).pkl", 'rb') as f:
    model = pickle.load(f)

# ---------------- HEADING ----------------
st.markdown('<h1 class="title">🎓 Student Passed Out Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheading">Enter student details to predict whether the student will pass out or not.</p>', unsafe_allow_html=True)

# ---------------- USER INPUTS (COLUMNS INTERFACE) ----------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    branch = st.selectbox("Branch", ["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT"])
    avg_cgpa = st.number_input("Average CGPA", min_value=0.0, max_value=10.0, step=0.1)
    attendance = st.number_input("Attendance Percentage", min_value=0, max_value=100)

with col2:
    backlogs = st.number_input("Backlogs Count", min_value=0, step=1)
    internship = st.selectbox("Internship Completed", ["Yes", "No"])
    final_project = st.selectbox("Final Year Project Completed", ["Completed", "Not Completed"])
    soft_skills = st.slider("Soft Skills Rating", min_value=1, max_value=10)

# ---------------- PREDICTION BUTTON ----------------
if st.button("🔍 Predict"):
    # Create input dataframe exactly like your original code
    input_data = pd.DataFrame({
        "Gender": [gender],
        "Branch": [branch],
        "Avg_CGPA": [avg_cgpa],
        "Attendance_Percentage": [attendance],
        "Backlogs_Count": [backlogs],
        "Internship_Completed": [internship],
        "Final_Year_Project": [final_project],
        "Soft_Skills_Rating": [soft_skills]
    })

    # Ensure categorical columns are strings (fix isnan error)
    cat_cols = ["Gender", "Branch", "Internship_Completed", "Final_Year_Project"]
    for col in cat_cols:
        input_data[col] = input_data[col].astype(str)

    # Make prediction
    try: 
        prediction = model.predict(input_data)[0]
    except ValueError as e:
        st.error(f"❌ Prediction error: {e}")
        st.info("Make sure your inputs exactly match the categories used during training.")
    else:
        # Show result in a highlighted box
        if prediction == "Yes" or prediction == 1:
            st.success("✅ Student is likely to *PASS OUT*")
        else:
            st.error("❌ Student is *NOT likely to PASS OUT*")