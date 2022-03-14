import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

class st_functions:

    def __init__(self, DataFrame):
        self.df = DataFrame
    
    def clean_data(self):
        # Column to count how many types of class there is
        self.df['count'] = pd.Series(np.ones(self.df.shape[0])).astype(int)

        # Turning floats into integers
        self.df['year'] = self.df['year'].fillna(0).apply(lambda x: int(x))
        # Turning mass into kg
        self.df['mass (g)'] = self.df['mass (g)'].apply(lambda x: round(x/1000, 3))
        # Mass == 0 turn to NaN
        self.df['mass (g)'] = self.df['mass (g)'].replace(0, np.nan)

        # Dropping GeoLocation & mass (g)
        self.df.drop(columns=['GeoLocation'], inplace=True)
        # To numeric
        self.df['reclat'].replace(0, np.nan, inplace=True)
        self.df['reclong'].replace(0, np.nan, inplace=True)
        # df[['reclong', 'reclat']].dropna(inplace=True)
        # pd.to_numeric(df['reclong'])
        # pd.to_numeric(df['reclat'])
        # Rename columns
        self.df.rename(
            columns={'mass (g)': 'mass (kg)', 'reclat': 'lat', 'reclong': 'lon'},
            inplace=True
        )
    
    def intro(self):
        st.title('EDA METEORITE LANDINGS')
        st.text('By Marcos Alvarez Ots')

        # Image
        st.image('img/namibia-hoba.png')
        st.caption('Namibia, Africa. The Hoba meteorite is the largest known intact meteorite (as a single piece). It is also the most massive naturally occurring piece of iron with an estimated mass at more than 60 tonnes, measuring 2.7×2.7×0.9 m. The name "Hoba" comes from Khoekhoegowab word meaning "gift".')

        st.write("""
        I'm a current Data Science student at [The Bridge](https://www.thebridge.tech/), challenged to build an EDA (Exploratory Data Analysis).
        Therefore, I have decided to analyse data about meteorite landings. 

        Database provided and created by the [NASA](https://www.nasa.gov/) with license: [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
        """)

        # Video
        st.header('Short introduction to the matter')
        st.video('vid/space_rocks.mp4', start_time=0)
        st.caption('Royal Museums Greenwich, (2016, Jan 27). Space Rocks | What\'s the difference between an asteroid, a meteoroid, a meteorite, and a comet?. Royal Museums Greenwich in UK. [Video]. Youtube. https://www.youtube.com/watch?v=rVdniqc_G_Q')

        # Classification
        st.subheader('Meteorite classification')
        st.image('img/meteoritefamilytree.gif')
        st.caption('Image obtained from [Nature History Museum](https://www.nhm.ac.uk/).')
        st.write('For further information about classification, visit [The Catalogue of Meteorites](https://www.nhm.ac.uk/our-science/data/metcat/search/bgmettypes.dsml) of Nature History Museum.')

    def data(self):
        # MAPPLOT
        # st.map(self.df[['lon', 'lat']].dropna())

        # BOXPLOT
        st.subheader('Understanding data collection')
        st.write('''
        A few entries in the original databse contain date information that was incorrectly parsed into the NASA database.
        As a spot check: any date that is before 860 CE or after 2016 are incorrect; these should actually be BCE years.

        So in order to focus in relevant information I have proceeded to remove them for this plot.
        ''')
        df_1 = self.df[(self.df['year']!=0) & (self.df['year']<2100)]
        fig = px.box(df_1, y='year', height=1000, color='fall')
        fig.update_layout(title='Meteorites fall by year')
        st.plotly_chart(fig, use_container_width=True)

        # BARPLOT
        st.subheader('Classifying meteorites by it\'s mass')
        switch = st.radio(
            "Choose and option to display in y axis:",
            ('Mean', 'Standard deviation', 'Max'),
            )
        if switch == 'Mean':
            c = 'mean'
        elif switch == 'Standard deviation':
            c = 'std'
        else:
            c = 'max'

        sort = st.radio(
            "Sort by:",
            ('Count', 'Mean', 'Standard deviation', 'Max'),
            )
        if sort == 'Count':
            s = 'count'
        elif sort == 'Mean':
            s = 'mean'
        elif sort == 'Standard deviation':
            s = 'std'
        else:
            s = 'max'
        
        # recclass slider
        start, end = st.select_slider(
        'Select a range of recclass length:',
        options=list(np.arange(0, 388, 10)),
        value=(0, 100))

        df_2 = self.df.dropna().groupby('recclass')[['mass (kg)']].describe()
        df_2 = df_2['mass (kg)'].sort_values(by=s, ascending=False)
        df_2 = df_2[start:end]
        
        fig = px.bar(
            df_2,
            x=df_2.index,
            y=c,
            hover_data=['mean', 'std'],
            color='count',
            color_continuous_scale='Blugrn',
            title='Amount rank of each meteorite property classified by a given input',
            height=600,
            text='count'
        )
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True)