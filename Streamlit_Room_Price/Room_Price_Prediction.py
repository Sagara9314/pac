import streamlit as st
from PIL import Image
import pickle 
import numpy as np
import pandas as pd
import time

model = pickle.load(open('./Model/ML_Model_Room_Price.pkl', 'rb'))

def run():
    #img1 = Image.open('bank.png')
    #img1 = img1.resize((156,145))
    #st.image(img1,use_column_width=False)
    #st.title("Room Price Prediction using ML Regression Model")

    st.markdown(
         f"""
         <style>
         .stApp {{
            background: url("https://images.pexels.com/photos/4871011/pexels-photo-4871011.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.jpg");      
		background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    st.markdown(f'<p style="color:#F72119;font-size:35px;border-radius:5%;">{"Room Price Prediction using ML"}</p>', unsafe_allow_html=True)

    ## District
    dist_display = ('Manhattan','Brooklyn')
    dist_options = list(range(len(dist_display)))
    dist = st.sidebar.selectbox("District",dist_options, format_func=lambda x: dist_display[x])

    ## Neighborhood
    neigh_display = ('Bath Beach','East Village', 'Harlem', 'Hells Kirchen', 'Upper East Side' 'Upper West Side')
    neigh_options = list(range(len(neigh_display)))
    neigh = st.sidebar.selectbox("Neighborhood",neigh_options, format_func=lambda x: neigh_display[x])

    ## PropertyType
    prop_display = ('Apartment','House', 'Bed & Breakfast', 'Dorm')
    prop_options = list(range(len(dist_display)))
    prop = st.sidebar.selectbox("PropertyType",prop_options, format_func=lambda x: prop_display[x])

    ## CancellationPolicy
    cancel_display = ('strict','moderate', 'flexible')
    cancel_options = list(range(len(cancel_display)))
    cancel = st.sidebar.selectbox("CancellationPolicy",cancel_options, format_func=lambda x: cancel_display[x])

    ## RoomType
    room_display = ('Entire Home/Apt','Private Room', 'Shared Room')
    room_options = list(range(len(room_display)))
    room = st.sidebar.selectbox("RoomType",room_options, format_func=lambda x: room_display[x])

    ## Accomodates
    Accomodates = st.sidebar.slider("Number of people to be accomodated",0,17)    
    
    ## Number of Bedrooms required
    Bedrooms = st.sidebar.slider("Number of Bedrooms required?",0,6)  

    ## Number of Bathrooms required
    Bathrooms = st.sidebar.slider("Number of Bathrooms required",0,6)  

    ## CleaningFee acceptable
    CleaningFee = st.sidebar.slider("Enter the acceptable Cleaning Fees (Max 100)",0,100) 

    ## ReviewRating acceptable
    ReviewRating = st.sidebar.slider("Enter the acceptable Review Rating (Max 100)",0,100) 

    df = pd.DataFrame([[dist,neigh,prop,cancel,room,Accomodates,Bedrooms,Bathrooms,CleaningFee,ReviewRating]],
              columns=['District','Neighborhood', 'PropertyType', 'CancellationPolicy', 'RoomType', 'Accommodates', 'Bedrooms', 'Bathrooms', 'CleaningFee', 'ReviewRating'])

    st.markdown(f'<p style="color:blue;font-size:30px;border-radius:50%;">{"Specified Input"}</p>', unsafe_allow_html=True)
    st.write(df)
    st.write('---')

    if st.button("Submit"):
        bar = st.progress(0)
        for i in range(21):
            bar.progress(i * 5)
            time.sleep(0.1)
        
        features = [[dist, neigh, prop, cancel, room, Accomodates, Bathrooms, Bedrooms, CleaningFee, ReviewRating]]
        print(features)
        
        room_price = model.predict(features)
        st.subheader('Predicted Room Price :')
        st.subheader('$'+ ' '+str(np.round(room_price[0], 2)))

run()