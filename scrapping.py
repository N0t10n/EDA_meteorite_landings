from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np

pages = np.arange(1,2)
count = 1
ms_data = []

for page in pages:
    URL = 'https://www.lpi.usra.edu/meteor/metbull.php?sea=&sfor=names&ants=&nwas=&falls=&valids=&stype=contains&lrec=50&map=ge&browse=&country=All&srt=name&categ=All&mblist=107&rect=&phot=&strewn=&snew=0&pnt=Normal%20table&dr=&page=' + str(page)

    r = requests.get(URL)
    soup = bs(r.text, "lxml")
    types_grid = soup.find_all('a', href='metbullclass.php?sea=L3')

    count_type = 1

    for type in types_grid:

        URL_type = 'https://www.lpi.usra.edu/meteor/' + type.text
        r = requests.get(URL_type)
        soup_type = bs(r.text, 'lxml')

        # Title
        title = soup_type.find('h1').text

        # Rating
        try:
            rating = float(soup_type.find('span', class_='').text)
        except:
            rating = None
        
        data = {
            'id': id_cerv,
        }

        count += 1
        count_type += 1

        ms_data.append(data)