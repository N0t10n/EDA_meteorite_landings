from functions import st_functions as stf
import pandas as pd
import streamlit as st
import numpy as np

# Importing data
df = pd.read_csv('data/Meteorite_Landings.csv')

## CREATING & CLEANING
# Column to count how many types of class there is
df['count'] = pd.Series(np.ones(df.shape[0])).astype(int)
# Turning floats into integers
df['year'] = df['year'].fillna(0).apply(lambda x: int(x)).replace(0, np.nan)
# Dropping GeoLocation
df.drop(columns='GeoLocation', inplace=True)
# Turning mass into kg
df['mass (g)'] = df['mass (g)'].apply(lambda x: round(x/1000, 3))
# Rename columns
df.rename(
    columns={'mass (g)': 'mass (kg)'},
    inplace=True
)

# Calling class object
ml = stf(df)

# Browser tab configuration
st.set_page_config(page_title='EDA Meteorite Landings', layout='wide', page_icon='🌍')

# Adding a side bar
index = st.sidebar.selectbox(
    'INDEX',
    ('A brief introduction', 'Exploring data', 'Conclusions')
)

# Running functions
if index == 'A brief introduction':
    ml.intro()
elif index == 'Exploring data':
    # ml.data()
    pass
else:
    # ml.conclude()
    pass