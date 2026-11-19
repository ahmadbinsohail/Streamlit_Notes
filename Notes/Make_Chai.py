import streamlit as st
st.title("UI Widgets")
st.subheader("Make your own tea and enjoy")
masala = st.checkbox("Add Masala")
if masala :
     st.write("Masla Added Successfully")
tea_type = st.radio("Choose Tea Base",["Milk","Water","Almond Milk"],index=None)
make_tea = st.button("Make Tea")
if make_tea :
    st.success("Tea is being brewed")
st.selectbox("Select Your flavour",["masala", "lemon", "green", "ginger"], index=None, placeholder="flavour")