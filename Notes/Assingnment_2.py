import streamlit as st 
import datetime as dt
current_date = dt.date.today()
st.title("Age Calculator")
dob = st.date_input("Enter Your Date of Birth",min_value= dt.date(1973,1,1),max_value=current_date)
st.write(":green[If dropdown not going back than 20 years , **Type manually or select oldest to get more**]")
if dob is not None :
    st.write(f"Selected : {dob}")
age = current_date.year - dob.year -((current_date.month,current_date.day)<(dob.month,dob.day))
st.write(f"Your age is {age}")