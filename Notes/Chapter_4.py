import pandas as pd
import streamlit as st
col1,col2 = st.columns([3,1])
with col1:
    st.title("Chai Sales Data")
    file = st.file_uploader("Upload Your Csv file here",type=["csv"])
    if file :
        st.success("File Uploaded")
        df = pd.read_csv(file)
        #st.dataframe(df)
        with col2:
            select_city = st.selectbox("Filter for City",df["City"].unique(),index=None,placeholder="City")
            filtered_df = df[df["City"]==select_city]
            st.write("If filter isn't selected , all selected by default")
        select_choice = st.selectbox("Select",["Data","Summary"],index=None, placeholder="Select")
        if select_city:
            preview_df = filtered_df
        else :
            preview_df = df

        if select_choice == "Data":
            st.subheader("Data Preview")
            st.write(preview_df)
        elif select_choice == "Summary":
            st.subheader("Data Summary")
            st.write(preview_df.describe())
    