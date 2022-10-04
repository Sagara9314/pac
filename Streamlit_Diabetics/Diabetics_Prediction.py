import streamlit as st
import pandas as pd
from PIL import Image
import pickle as pkl
import numpy as np
import streamlit.components.v1 as components
import webbrowser
import time

#st.set_page_config(page_title="Diabetics Predicting Application", layout="wide")

header=st.container()

model = pkl.load(open('./Model/ML_Model_Diabetics.pkl', 'rb'))
img1 = Image.open('diabetes.gif')
img1 = img1.resize((150,110))
st.image(img1,use_column_width=False)

st.markdown(
         f"""
         <style>
         .stApp {{
            background: url("https://images.unsplash.com/photo-1508614999368-9260051292e5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80.jpg");      
		background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.markdown(f'<p style="color:#F72119;font-size:35px;border-radius:5%;">{"Diabetics Classifcation using Machine Learning"}</p>', unsafe_allow_html=True)

url = '1.html'
urls = '2.html'
uri = '3.html'
ure = '4.html'
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('Data Information'):
        webbrowser.open_new_tab(url)
with col2:
    if st.button('Healthy Living'):
        webbrowser.open_new_tab(urls)
with col3:
    if st.button('Medication'):
        webbrowser.open_new_tab(uri)
with col4:
    if st.button('Donate'):
        webbrowser.open_new_tab(ure)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
with col1:
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

with col2:
    Glucose = st.number_input('Glucose Level', min_value=0, step=1)
    
with col3:
    BloodPressure = st.number_input('Blood Pressure', min_value=0, step=1)

with col4:
    SkinThickness = st.number_input('Skin Thickness', min_value=0, step=1)

with col5:
    Insulin = st.number_input('Insulin Level', min_value=0, step=1)

with col6:
    BMI = st.number_input('BMI Value', value=0.0)

with col7:
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', value=0.0)

with col8:
    Age = st.number_input('Age', min_value=20, step=1)


if st.button("Submit"):
	with st.spinner('Wait for it...'):
		time.sleep(2)
		st.success('Done!')

	features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]] 
 
	print(features)
	prediction = model.predict(features)
	lc = [str(i) for i in prediction]
	ans = int("".join(lc))
	if ans == 0:
		st.success(
			'According to ML prediction, the Patient does not have Diabetics'
		)
	else:
		st.error(
			'According to ML Prediction, the Patient has Diabetics'
		)
