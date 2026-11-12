import streamlit as st
st.title("Assignment 1: Streamlit App")
st.subheader("Favroite Programing Language Selector")
fvrt_lang =st.selectbox("Choose your favorite programming language", ["Python", "JavaScript", "Java", "C++", "C#", "Ruby"], index=None, placeholder="Select a language")
if fvrt_lang != None:
    st.write(f"You chose {fvrt_lang}. Great choice!")
