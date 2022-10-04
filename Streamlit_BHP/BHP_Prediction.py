import streamlit as st
from PIL import Image
import pickle
import numpy as np
import time
import pandas as pd

model = pickle.load(open('./Model/ML_Model_BHP.pkl', 'rb'))

img1 = Image.open('bang.jpg')
img1 = img1.resize((200,150))
st.image(img1,use_column_width=False)
st.markdown(
         f"""
         <style>
         .stApp {{
            background: url("https://images.unsplash.com/photo-1444791252404-500e5b11f71b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80.jpg");      
		background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.markdown(f'<p style="color:blue;font-size:40px;border-radius:50%;">{"Bangalore House Price Prediction"}</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
    ## House Area in sqft
with col1:
    sqft = st.number_input("House Area in SqFt", min_value=450, step=1)    
    
    ## Number of Bedrooms required
with col2:
    bhk = st.number_input("Number of Bedrooms required?",min_value=1, step=1)  

    ## Number of Bathrooms required
with col3:
    bath = st.number_input("Number of Bathrooms required",min_value=1, step=1)  

    ## Number of Bathrooms required
with col4:
    balcony = st.number_input("Number of Balconies required",value=0) 

def check_input():
    if (not sqft): 
        st.warning("Please enter the Area")
        return False
    elif(not bhk): 
        st.warning("Please enter the value of bhk")
        return False
    elif(not bath): 
        st.warning("Please enter number of bathrooms")
        return False
    elif(not balcony): 
        st.warning("Please enter number of bathrooms")
        return False
    
    if (sqft < 450):
        st.warning("Minimum value of Area is 450 sqft!")
        return False
    elif (bhk < 1):
        st.warning("Minimum value of bhk is 1")
        return False
    elif (bath < 1):
        st.warning("Minimum value of bathrooms is 1")
        return False

    return True
## For Location area of the House in Bangalore
loc_display = ('Bommanahalli','Electronics City','Indira Nagar','Vijayanagar', 'Whitefield', 'JP Nagar')
loc_options = list(range(len(loc_display)))
location = st.selectbox("location",loc_options, format_func=lambda x: loc_display[x])


df = pd.DataFrame([[location,sqft,bhk,bath]],
              columns=['Location','Area in sqft', 'BHK', 'Bathrooms'])

st.markdown(f'<p style="color:blue;font-size:40px;border-radius:50%;">{"Specified Input"}</p>', unsafe_allow_html=True)
st.write(df)
st.write('---')

if st.button("Submit"):
    bar = st.progress(0)
    for i in range(21):
        bar.progress(i * 5)
        time.sleep(0.1)
        
    features = [[sqft, bhk, bath, balcony, location]]
    print(features)
        
    house_price = model.predict(features)
    st.subheader('Predicted House Price :')
    st.subheader('INR'+' '+str(np.round(house_price[0], 2)))
