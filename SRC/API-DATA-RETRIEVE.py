# connection  to server details


# my_sql_connector


# definitions on how to insert different data to DB


# retrieve data from API

# insert data to DB

import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://imdb8.p.rapidapi.com/actors/get-all-videos"

querystring = {"nconst":"nm0001667", "region": "US"}

headers = {
    'x-rapidapi-key': "2e69296398msh2169e50121cc23ep17c546jsnbf1647b8338c",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(type(response))

html_file = BeautifulSoup(response.text, "html.parser")

print(html_file.prettify())
# d = pd.read_json()
# df = pd.DataFrame(response)#r'C:\Users\sahar gavriely\Desktop\pop.txt')
# print(df)
# df.to_csv(r'C:\Users\sahar gavriely\Desktop\pap.csv', index=None)
