from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import pickle as pkl
import streamlit as st
import pandas as pd
import numpy as np

model = pkl.load(open('./Model/ML_Model_Diabetics.pkl', 'rb'))
st.set_page_config(page_title="Diabetes Classification",page_icon="C:/Users/Sagar N/MLDiabetes-main/Imagenes/learning.png")
st.markdown(f'<p style="color:#39FF14;font-size:35px;border-radius:5%;">{"Diabetics Classifcation using Machine Learning"}</p>', unsafe_allow_html=True)
st.write("""
Detect if someone has diabetes using machine learning and python
""")
st.markdown(
         f"""
         <style>
         .stApp {{
            background: url("https://images.unsplash.com/photo-1542789828-6c82d889ed74?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80.jpg");      
		background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
img1 = Image.open('231.jpg')
img1 = img1.resize((550,310))
st.image(img1,use_column_width=False)

df = pd.read_csv('C:/Users/Sagar N/MLDiabetes-main/Data/diabetes.csv')

#Set WebApp subheader
st.subheader('Data information')
#Show data as datatable
st.dataframe(df)
#Show statitstics on the data
#st.write(df.describe())
#Show the data as a chart
#chart = st.bar_chart(df)
#Split the data into independent 'X' and independent 'Y' variables
X = df.iloc[:,0:8].values
Y = df.iloc[:,-1].values
#Split the data set into 75% training and 25% testing
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.25,random_state=0)
#Get the feature input from the user
def get_user_input():
    Pregnancies = st.sidebar.slider('Pregnancies',0,17,3)
    Glucose = st.sidebar.slider('Glucose',0,199,117)
    BloodPressure = st.sidebar.slider('Blood_Pressure',0,122,72)
    SkinThickness =  st.sidebar.slider('SkinThickness',0,99,23)
    Insulin = st.sidebar.slider('Insulin',0.0,846.0,30.5)
    BMI = st.sidebar.slider('BMI',0.0,67.1,32.0)
    DPF = st.sidebar.slider('DPF',0.078,2.42,0.3725)
    Age  = st.sidebar.slider('Age',21,81,29)

    #Store a dictionary into a variable
    user_data = {'Pregnancies' : Pregnancies,
                 'glucose':Glucose,
                 'blood_pressure':BloodPressure,
                 'skin_thikness':SkinThickness,
                 'insulin':Insulin,
                 'BMI':BMI,
                 'DPF':DPF,
                 'Age':Age
                }
    #Transform the data into a data frame 

    features = pd.DataFrame(user_data,index = [0])
    return features
    
#Store the user input into a variable
user_input = get_user_input()

#Set a subheader and display the users input
st.subheader('User input')
st.write(user_input)

#Create and train the model
RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train,Y_train)

#Show the models metrics
#st.subheader('Model Test Accuracy Score: ')
#st.write(str(accuracy_score(Y_test,RandomForestClassifier.predict(X_test)* 100)) + '%')
#Store the models predictions in a variable
prediction =RandomForestClassifier.predict(user_input)
#Set a subheader and display the clasification
st.subheader('Clasification')
st.write(prediction)
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