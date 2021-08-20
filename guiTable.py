import streamlit as st
import pandas as pd

#Filter dataframe
import numpy as npdf = pd.read_csv("newsArticleScraping.csv")labels = st.multiselect('Show articles for a label?', df['Label'].unique())

# write dataframe to screen
new_df = df[(df['Label'].isin(clubs))]
st.write(new_df)