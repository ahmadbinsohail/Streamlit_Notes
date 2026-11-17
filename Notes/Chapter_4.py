import pandas as pd
import streamlit as st
st.title("Chai Sales Data")
file = st.file_uploader("Upload Your Csv file here",type=["csv"])
if file :
    st.success("File Uploaded")
    df = pd.read_csv(file)
    st.dataframe(df)