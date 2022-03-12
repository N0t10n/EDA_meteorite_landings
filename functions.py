from wsgiref.util import request_uri
import numpy as np
import streamlit as st
import pandas as pd

class st_functions:

    def __init__(self, DataFrame):
        self.df = DataFrame
    
    def intro(self):
        st.title('EDA METEORITE LANDINGS')
        st.text('By Marcos Alvarez Ots')

        # Image
        st.image('img/namibia-hoba.png')
        st.caption('Namibia, Africa. The Hoba meteorite is the largest known intact meteorite (as a single piece). It is also the most massive naturally occurring piece of iron with an estimated mass at more than 60 tonnes, measuring 2.7×2.7×0.9 m. The name "Hoba" comes from Khoekhoegowab word meaning "gift".')

        st.write("""
        I'm a current Data Science student at [The Bridge](https://www.thebridge.tech/), challenged to build an EDA (Exploratory Data Analysis).
        Therefore, I have decided to analyse data about meteorite landings. 

        Database provided and created by the [NASA](https://www.nasa.gov/) with license: [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)
        """)

        # Video
        st.header('Short introduction to the matter')
        st.video('vid/space_rocks.mp4')
        st.caption('Royal Museums Greenwich, (2016, Jan 27). Space Rocks | What\'s the difference between an asteroid, a meteoroid, a meteorite, and a comet?. Royal Museums Greenwich in UK. [Video]. Youtube. https://www.youtube.com/watch?v=rVdniqc_G_Q')

        # Classification
        st.subheader('Meteorite classification')
        st.text('For further information about classification types, check ')