import streamlit as st
st.title("UI Widgets")
st.subheader("Make your own tea and enjoy")
masala = st.checkbox("Add Masala")
if masala :
     st.write("Masla Added Successfully")
tea_type = st.radio("Choose Tea Base",["Milk","Water","Almond Milk"],index=None)
if tea_type != None:
    st.write(f"You choose {tea_type}.")

flavour = st.selectbox("Select Your flavour",["Adrak","Elaichi","Kesar","Tulsi","Lemon","Ginger","Mint","Honey"],index=None,placeholder="Select Your Flavour")
if flavour != None:
    st.write(f"You choose {flavour}.")

sugar = st.slider("Select Sugar Level(Spoons)", 0, 5, 1,width=150)
if sugar != None:
    st.write(f"You choose {sugar} spoons of sugar.")
cups = st.number_input("Enter number of cups", min_value=1, max_value=10 , step=1,width=150)
if cups != None:
    st.write(f"You choose {cups} cups of tea.")

make_tea = st.button("Make Tea")
if make_tea :
    st.success("Tea is being brewed")
name = st.text_input("Enter Your Name",width=150,placeholder="Enter Your Name")
if name :
    st.write(f"Hello {name}, your tea is ready ")
dob = st.date_input("Enter Your Date of birth",width=150)
if dob:
    st.write(f"Your date of birth is {dob}")

