import pandas as pd
import streamlit as st
st.title("Chai Sales Data")
file = st.file_uploader("Upload Your Csv file here",type=["csv"])
if file :
    st.success("File Uploaded")
    df = pd.read_csv(file)
    #st.dataframe(df)
    select_choice = st.selectbox("Select",["Data","Summary"],index=None, placeholder="Select")
    if select_choice == "Data":
        st.subheader("Data Preview")
        st.write(df)
    elif select_choice == "Summary":
        st.subheader("Data Summary")
        st.write(df.describe())