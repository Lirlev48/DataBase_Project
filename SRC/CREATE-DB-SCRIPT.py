import pandas as pd
from sshtunnel import SSHTunnelForwarder
import mysql.connector


# ###############
# csv to mysql #
# ###############
#
# tunnel = SSHTunnelForwarder(('nova.cs.tau.ac.il', 22),
#                             ssh_username=input("insert your moodle username: "),
#                             ssh_password=input("insert your moodle password: "),
#                             remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306))
# tunnel.start()
#
# details = {
#     'user': 'DbMysql02',
#     'password': 'DbMysql02',
#     'host': '127.0.0.1',
#     'database': 'DbMysql02',
#     'port': tunnel.local_bind_port,
#     'raise_on_warnings': True,
# }
#
# cnx = mysql.connector.connect(**details)
#
# cursor = cnx.cursor()
# df = pd.read_csv("movies_to_spoken_languages.csv")
# for index, row in df.iterrows():
#
#     # for movies_to_table #
#
#     try:
#         sql_q = ("INSERT INTO movies_to_spoken_languages (imdb_id, spoken_languages_id) "
#                  "values ('{}', '{}')".format(row["movie_id"], row["spoken_languages_id"]))
#         cursor.execute(sql_q)
#         emp_no = cursor.lastrowid
#
#         # Make sure data is committed to the database
#         cnx.commit()
#     except Exception as e:
#         if e.args[0] != 1062:
#             print(e)
#             print(sql_q)
#
#     # for movies table and the other tables have the same idea #
#
#     row["title"] = row["title"].translate(str.maketrans({'"': "'"}))
#     if len(row["title"]) > 100:
#         row["title"] = row["title"][:90] + "..."
#     row["original_title"] = row["original_title"].translate(str.maketrans({'"': "'"}))
#     if len(row["original_title"]) > 100:
#         row["original_title"] = row["original_title"][:90] + "..."
#     if not pd.isna(row["homepage"]) and len(row["homepage"]) > 500:
#         row["homepage"] = ""
#     if not pd.isna(row["overview"]):
#         if len(row["overview"]) > 1000:
#             row["overview"] = row["overview"][:990] + "..."
#         row["overview"] = row["overview"].translate(str.maketrans({'"': "'"}))
#     if not pd.isna(row["tagline"]):
#         if len(row["tagline"]) > 1000:
#             row["tagline"] = row["tagline"][:990] + "..."
#         row["tagline"] = row["tagline"].translate(str.maketrans({'"': "'"}))
#     if row["adult"]:
#         row["adult"] = 1
#     else:
#         row["adult"] = 0
#
#     try:
#         sql_q = ('INSERT INTO movies (imdb_id, adult, budget, homepage, original_language, original_title,'
#                      'overview, popularity, release_date, revenue, runtime, status, tagline, title, vote_average,'
#                      'vote_count) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}",'
#                      '"{}", "{}", "{}")'.format(row["imdb_id"], row["adult"], row["budget"], row["homepage"],
#                                                 row["original_language"], row["original_title"], row["overview"],
#                                                 row["popularity"], row["release_date"], row["revenue"], row["runtime"],
#                                                 row["status"], row["tagline"], row["title"], row["vote_average"],
#                                                 row["vote_count"]))
#
#         cursor.execute(sql_q)
#         emp_no = cursor.lastrowid
#
#         # Make sure data is committed to the database
#         cnx.commit()
#     except Exception as e:
#         if e.args[0] != 1062:
#             print(e)
#             print(sql_q)
#             try:
#                 sql_q = ("INSERT INTO movies (imdb_id, adult, budget, homepage, original_language, original_title,"
#                      "overview, popularity, release_date, revenue, runtime, status, tagline, title, vote_average,"
#                      "vote_count) values ('{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', "
#                      "'{}', '{}', '{}')".format(row["imdb_id"], row["adult"], row["budget"], row["homepage"],
#                                                 row["original_language"], row["original_title"], row["overview"],
#                                                 row["popularity"], row["release_date"], row["revenue"], row["runtime"],
#                                                 row["status"], row["tagline"], row["title"], row["vote_average"],
#                                                 row["vote_count"]))
#                 # Insert new employee
#                 cursor.execute(sql_q)
#                 emp_no = cursor.lastrowid
#
#                 # Make sure data is committed to the database
#                 cnx.commit()
#             except Exception as e:
#                 if e.args[0] != 1062:
#                     print(e)
#                     print(sql_q)
#
# cursor.close()
# cnx.close()
#
# print('done')
#
