# Command 1 to run the web app : streamlit run C:\Users\Soubhik\OneDrive\Documents\Form-1.py
# Command 2 to run the web app : python -m streamlit run C:\Users\Soubhik\OneDrive\Documents\Form-1.py

import streamlit as st
import numpy as np
import datetime

st.title("FORM-1")
st.write("\n\n")
st.write("\n\n")
st.subheader('1. Name')
user_name = st.text_input("Enter your name:")
st.write("Hello, Your Name : " + user_name)
st.write("\n\n")
st.subheader('2. Gender')
gender = st.radio('Select your gender:', options=('Male', 'Female', 'Other'), help='Choose One', horizontal=True)
st.write("Gender :", gender)
st.write("\n\n")
st.subheader('3. Date Of Birth')
selected_date = st.date_input("Select Your Date Of Birth:", datetime.date.today())
st.write("Date Of Birth :", selected_date)
st.write("\n\n")
st.subheader('3. Field Of Interest')
career_options = ["Artificial Intelligence", "Azure And Microservices", "Big Data", "Business Analyst", "Cloud Computing Engineer", "Cybersecurity Engineer", "Data Analytics", "Databases", "Data Science", "Deep Learning", "DevOps", "Frontend Developper", "Full Stack Developper", "Game Design", "Information Security", "Internet of Things", "Machine Learning", "MERN Stack Developper", "MEAN Stack Developper", "Mobile App Developer", "Natural Language Processing", "Robotics", "Software Ingineer", "Software Developper", "UX & UI Designer", "Web Designer"]
selected_career = st.selectbox("Select your Field Of Interest:", career_options)
st.write("Selected Career:", selected_career)
st.write("\n\n")
st.subheader('4. Age')
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=30)
st.write("Your age:", age)
st.write("\n\n")
st.subheader('5. Color Picker')
color = st.color_picker('Select your favourite color:', '#DC1D07')
st.write("You've selected", color, 'color')
st.write("\n\n")
st.subheader('6. Feedback')
user_comment = st.text_area("Provide your feedback:")
st.write("Your feedback:", user_comment)
st.write("\n\n")
st.button('Submit your Response')