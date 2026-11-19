import streamlit as st 
from pathlib import Path as P
import streamlit as st
import pandas as pd


# Give the data view more space than the filter controls.
col1,col2 = st.columns([3,1])
# Load the cleaned game-sales data from this script's data folder.
dir = P(__file__).resolve().parent
clean_game_file_path = dir / "data"
df = pd.read_csv(clean_game_file_path / "clean_games.csv")

# Let the user optionally filter the dataset by one column and value.
with col2:
    filter_options = st.selectbox("Select Filter",df.columns,index=None, placeholder="Select")
    if filter_options is not None :
        filter_selected = st.selectbox("Filter Value",df[filter_options].unique() , index=None,placeholder="Filter")
        if filter_selected is not None :
            filtered_df = df[df[filter_options]==filter_selected]
        elif filter_selected is None :
            # Keep all rows until a filter value is selected.
            filtered_df = df
        
    elif filter_options == None :
        filtered_df = df
   
    


# Display either the filtered rows or summary statistics.
with col1:
    st.title("Games Sales Data")
    select_choice = st.selectbox("Select",["Data","Summary"],index=None, placeholder="Select")
    if select_choice == "Data" :
        st.subheader("Data")
        st.dataframe(filtered_df)
    elif select_choice == "Summary":
        st.subheader("Summary")
        st.write(filtered_df.describe())
