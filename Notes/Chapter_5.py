import streamlit as st 
from pathlib import Path as P
import streamlit as st
import pandas as pd


col1,col2 = st.columns([3,1])
dir = P(__file__).resolve().parent
clean_game_file_path = dir / "data"
df = pd.read_csv(clean_game_file_path / "clean_games.csv")
with col2:
    filter_options = st.selectbox("Select Filter",df.columns,index=None, placeholder="Select")
    if filter_options is not None :
        filter_selected = st.selectbox("Filter Value",df[filter_options].unique() , index=None,placeholder="Filter")
        if filter_selected is not None :
            filtered_df = df[df[filter_options]==filter_selected]
        elif filter_selected is None :
            filtered_df = df
        
    elif filter_options == None :
        filtered_df = df
   
    


with col1:
    st.title("Games Sales Data")
    select_choice = st.selectbox("Select",["Data","Summary"],index=None, placeholder="Select")
    if select_choice == "Data" :
        st.subheader("Data")
        st.dataframe(filtered_df)
    elif select_choice == "Summary":
        st.subheader("Summary")
        st.write(filtered_df.describe())
