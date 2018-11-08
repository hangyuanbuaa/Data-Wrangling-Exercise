# How to work with HTML files?
# Method 1: saving the HTML file to computer using Requests library
# and reading the file into a BeautifulSoup constructor
# Method 2: reading the HTML response content directly into the BS constructor

#----------------------------------------------------

# Requests > for downloading files programmatic from the Internet
```
import requests
r = requests.get(url)
with open(folder_name + '/' + filename, 'wb') as f:
        f.write(r.content)
```

import requests
import os

# Make directory if it doesn't already exist
folder_name = 'reviews'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

url = 'https://www.rottentomatoes.com/...'
response = requests.get(url)

# Save HTML to file
with open("et_the_extraterrestrial.html", mode='wb') as file:
    file.write(response.content)

# how to download one file to folder?
with open(os.path.join(folder_name,
                        url.split('/')[1]), mode='wb') as file:
    file.write(response.content)
os.listdir(folder_name)  # check


#----------------------------------------------------

# for non-Text requests
# PIL (short for Pillow) library is recommended
```
import requests
from PIL import image
from io import BytesIO

r = requests.get(url)
i = Image.open(BytesIO(r.content))
```

#----------------------------------------------------

# Beautiful Soup: for parsing the HTML files

# 1. making the soup
from bs4 import BeautifulSoup
import os
import pandas as pd
df_list = []
folder = 'rt_html'
for movie_html in os.listdir(folder):
    with open(os.path.join(folder, movie_html)) as file:
        soup = BeautifulSoup(file, 'lxml')
        title = soup.find('title').contents[0][: -len(' - Rotten Tomatoes')]
        audience_score = soup.find('div', class_= 'audience-score meter').find('span').contents[0][:-1]
        num_audience_ratings = soup.find('div', class_='audience-info hidden-xs superPageFontColor').find_all('div')[1].contents[2].strip().replace(',', '')
        # Append to list of dictionaries
        df_list.append({'title': title,'audience_score': int(audience_score),
                            'number_of_audience_ratings': int(num_audience_ratings)})
df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings'])
