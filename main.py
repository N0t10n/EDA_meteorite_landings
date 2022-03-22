from functions import st_functions
import streamlit as st
import pandas as pd

# Importing data
df = pd.read_csv('data/Meteorite_Landings.csv')

ml = st_functions(df) # Calling class object
ml.clean_data() # Cleaning it's data

# Browser tab configuration
st.set_page_config(page_title='EDA Meteorite Landings', layout='wide', page_icon='🌍')

# Adding a side bar
index = st.sidebar.selectbox(
    'INDEX',
    ('A brief introduction', 'Exploring data')
)

# Running functions
if index == 'A brief introduction':
    ml.intro()
else: # index == 'Exploring data'
    ml.data()