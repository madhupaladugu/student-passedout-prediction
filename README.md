.

🎓 Student Passed Out Prediction App

A Machine Learning–powered Streamlit web application that predicts whether a student is likely to pass out (graduate successfully) based on academic performance, attendance, internships, and skill-related factors.

🚀 Project Overview

This application uses a pre-trained Scikit-learn model to analyze student data and provide instant predictions through an interactive and visually appealing web interface built with Streamlit.

✨ Features

📊 Real-time student pass-out prediction

🖥️ Interactive Streamlit user interface

🎨 Custom background and UI styling using CSS

🧠 Machine Learning model integration

✅ Clear and user-friendly prediction results

🧾 Input Parameters

The following student details are required for prediction:

Gender (Male / Female)

Branch (CSE, ECE, EEE, MECH, CIVIL, IT)

Average CGPA

Attendance Percentage

Backlogs Count

Internship Completed (Yes / No)

Final Year Project Status (Completed / Not Completed)

Soft Skills Rating (1–10)

🛠️ Tech Stack

Python

Streamlit

Pandas

Scikit-learn

Pickle

HTML & CSS

📂 Project Structure
├── app.py
├── model (1).pkl
├── requirements.txt
└── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-passout-prediction.git
cd student-passout-prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

📌 Prediction Output

✅ PASS OUT – Student is likely to graduate successfully

❌ NOT PASS OUT – Student may not graduate successfully

🔮 Future Enhancements

Add model performance metrics (accuracy, confusion matrix)

Support multiple machine learning algorithms

Deploy on Streamlit Cloud

Store predictions in a database

👤 Author

Madhu Paladugu
B.Tech | Python & Machine Learning Enthusiast
