import streamlit as st

# Run the app with:
# streamlit run Day_1.py

# App title and intro section
st.title("Day 1 of learning Streamlit")
st.subheader("This is a subheader for the app")

# User can pick a skill level for the app experience
st.selectbox("Choose your level", ["Beginner", "Advanced", "Intermediate"],index=None, placeholder="Level")

# A second title to make the page look more engaging
st.title("Art of forcing ")

# Let the user select their favorite person from a list
fvrt_person = st.selectbox(
    "Your Favorite Person ",
    ["Ahmad", "Ahmad Raza", "Ahmad Raza Sohail", "Ahmad Raza Sohail Ahmad"],index=None, placeholder="Favorite Person"
)

# Show a congratulatory message only when a valid name is selected
if fvrt_person != None :
    st.write(f"You choose {fvrt_person}. Well done")
