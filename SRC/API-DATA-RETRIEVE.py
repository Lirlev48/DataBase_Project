import requests
import pandas as pd
import json
from alive_progress import alive_bar
import pickle


############
# TMDB API #
############
#
# TMDB_API_key = "7850d29af5bf2c21a33f5980cd20a4e7"
#
#
# def insert_to_table_x(movie_id, table_name, table_x, connector_table, keys, connector_id, *args):
#     for line in cur_movie[table_name]:
#         line_id = line[args[0]]
#         # insert to the table
#         if line_id not in keys:
#             keys.add(line_id)
#             for arg in args:
#                 table_x[arg].append(line[arg])
#         # insert connecting table
#         connector_table["movie_id"].append(movie_id)
#         connector_table[connector_id].append(line_id)
#
#
# all_movies_keys = set()
# for i, r in pd.read_csv("movies_to_directors.csv").iterrows():
#     all_movies_keys.add(r["imdb_id"])
#
# movies_keys = set()
# movies_table = {"adult": [], "budget": [], "homepage": [], "id": [], "imdb_id": [], "original_language": [],
#                 "original_title": [], "overview": [], "popularity": [], "release_date": [], "revenue": [],
#                 "runtime": [], "status": [], "tagline": [], "title": [], "vote_average": [], "vote_count": []}
#
# movies_to_genres_table = {"movie_id": [], "genres_id": []}
# genres_table = {"id": [], "name": []}
# genres_keys = set()
#
# movies_to_spoken_languages_table = {"movie_id": [], "spoken_languages_id": []}
# spoken_languages_table = {"english_name": [], "iso_639_1": []}  # id is iso_639_1
# spoken_languages_keys = set()
#
# movies_to_production_countries_table = {"movie_id": [], "production_countries_id": []}
# production_countries_table = {"iso_3166_1": [], "name": []}  # id is iso_3166_1
# production_countries_keys = set()
#
# movies_to_production_companies_table = {"movie_id": [], "production_companies_id": []}
# production_companies_table = {"id": [], "logo_path": [], "name": [], "origin_country": []}
# production_companies_keys = set()
#
# amount = 0
# length = 5000
# while len(movies_keys) < 15000:
#     amount += 1
#     with alive_bar(length) as bar:
#         for i in range((amount - 1) * length, amount * length):
#             bar()
#             try:
#                 res = requests.request("GET", f"https://api.themoviedb.org/3/movie/{i}?api_key={TMDB_API_key}")
#                 cur_movie = json.loads(res.text)
#
#                 cur_movie_id = cur_movie["imdb_id"]
#                 if cur_movie_id not in all_movies_keys:
#                     continue
#                 movies_keys.add(cur_movie_id)
#
#                 # insert movie
#                 for key in movies_table:
#                     movies_table[key].append(cur_movie[key])
#
#                 # insert to genres:
#                 insert_to_table_x(cur_movie_id, "genres", genres_table, movies_to_genres_table,
#                                   genres_keys, "genres_id", "id", "name")
#
#                 # insert to spoken languages:
#                 insert_to_table_x(cur_movie_id, "spoken_languages", spoken_languages_table,
#                                   movies_to_spoken_languages_table, spoken_languages_keys, "spoken_languages_id",
#                                   "iso_639_1", "english_name")
#
#                 # insert to production countries:
#                 insert_to_table_x(cur_movie_id, "production_countries", production_countries_table,
#                                   movies_to_production_countries_table, production_countries_keys,
#                                   "production_countries_id", "iso_3166_1", "name")
#
#                 # insert to production companies:
#                 insert_to_table_x(cur_movie_id, "production_companies", production_companies_table,
#                                   movies_to_production_companies_table, production_companies_keys,
#                                   "production_companies_id", "id", "name", "logo_path", "origin_country")
#
#             except:
#                 pass
#
#     print(len(movies_keys))
#
# # Pickling
# with open("15849.txt", "wb") as fp:
#     pickle.dump(movies_keys, fp)
#
# # saving the tables in a csv format
# for table, name in [(movies_table, "movies"), (movies_to_genres_table, "movies_to_genres"), (genres_table, "genres"),
#                     (movies_to_spoken_languages_table, "movies_to_spoken_languages"),
#                     (spoken_languages_table, "spoken_languages"),
#                     (movies_to_production_countries_table, "movies_to_production_countries"),
#                     (production_countries_table, "production_countries"),
#                     (movies_to_production_companies_table, "movies_to_production_companies"),
#                     (production_companies_table, "production_companies")]:
#     df = pd.DataFrame(table)
#     df.to_csv(name + ".csv")
#
# # tell me when you're done
# print('\a')
#

############
# rapidapi #
############
#
# rapidapi_key = "2e69296398msh2169e50121cc23ep17c546jsnbf1647b8338c"
#
# url = "https://imdb8.p.rapidapi.com/actors/get-all-videos"
#
# querystring = {"nconst":"nm0001667", "region": "US"}
#
# headers = {
#     'x-rapidapi-key': rapidapi_key,
#     'x-rapidapi-host': "imdb8.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(type(response))
#
# html_file = bs(response.text, "html.parser")
#
# print(html_file.prettify())
#

##############
# csv parser #
##############
#
# movies_to_directors_table = {"imdb_id": [], "director_id": []}
# directors_table = {"id": [], "name": []}
# directors_keys = {}
# directors_id = 0
# movies_keys = set()
# validate = 0
#
# # Unpickling
# with open("15849.txt", "rb") as fp:
#     movies_keys = pickle.load(fp)
#
# # load csv file
# df = pd.read_csv("IMDb movies-3.csv", encoding = "ISO-8859-1")
#
# # remove everything but director and imdb_id
# for col in df.copy():
#     if col != "director" and col != "imdb_title_id":
#         df.drop(col, inplace=True, axis=1)
#
# # iterate
# for index, r in df.iterrows():
#     if type(r["director"]) != str:
#         continue
#     d_list = r["director"].split(',')
#     m = r["imdb_title_id"]
#     if m in movies_keys:
#         validate += 1
#         for d in d_list:
#             if d not in directors_keys:
#                 directors_keys[d] = directors_id
#                 directors_id += 1
#                 directors_table["id"].append(directors_keys[d])
#                 directors_table["name"].append(d)
#             movies_to_directors_table["imdb_id"].append(m)
#             movies_to_directors_table["director_id"].append(directors_keys[d])
#
# pd.DataFrame(movies_to_directors_table).to_csv("movies_to_directors.csv")
# pd.DataFrame(directors_table).to_csv("directors.csv")
#
# print(validate)
#

################
# csv to mysql #
################

