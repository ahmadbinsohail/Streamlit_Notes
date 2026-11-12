import streamlit as st
"streamlit run day_1.py"

st.title("Day 1 of learning Streamlit")
st.subheader("Choose your level")
st.selectbox(" ",["Beginner","Advanced","Intermediate"])
st.title("Art of forcing ")
fvrt_person = st.selectbox("Your Favorite Person ",["NAME","Ahmad","Ahmad Raza","Ahmad Raza Sohail", "Ahmad Raza Sohail Ahmad"])
if fvrt_person != "NAME":
    st.write(f"You choose {fvrt_person}. Well done")
