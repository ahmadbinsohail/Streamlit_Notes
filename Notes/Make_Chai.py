import streamlit as st
st.title("UI Widgets")
st.subheader("Make your own tea and enjoy")
make_tea = st.button("Make Tea")
mt = make_tea
if mt :
    st.success("Tea is being brewed")
masala = st.checkbox("Add Masala")
if masala :
     st.write("Masla Added Successfully")
else :
       st.write("Masla not added yet")
st.write(make_tea)