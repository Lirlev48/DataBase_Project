import mysql.connector
from mysql.connector import errorcode
from datetime import date
from datetime import datetime
import queries


def est_connection(query, args=None): # TODO change name of func, variables, prints and details
    details = {
        'user': 'DbMysql08',
        'password': 'lennon',
        'host': 'mysqlsrv1.cs.tau.ac.il',
        'database': 'DbMysql08',
        'port': 3306,
        'raise_on_warnings': True,
    } # add connector details
    cnx = mysql.connector.connect(**details)
    try:
        cnx = mysql.connector.connect(**details)
    except mysql.connector.Error as er:
        if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("There is a mistake in the credentials")
        elif er.errno == errorcode.ER_BAD_DB_ERROR:
            print("The DB you've try to reach does not exist")
        else:
            print(er)
    cur = cnx.cursor(buffered=True)
    if (args != None):
        cur.execute(query, args)
    else:
        cur.execute(query)
    iterator = iter(cur)
    cnx.commit()
    cnx.close()
    return iterator


def RenderMoviesFromGeneres(genre, from_date, to_date, limit): #change name of func and variables
    query_artist_from_gen = queries.choose_artists_according_to_genere()
    genre = '%' + genre + '%' #why %?
    lim = int(limit)
    args = (genre, from_date, to_date, limit,)
    iter = est_connection(get_movies_by_genere_and_date_range, args)
    return iter

def renderAllGenres():
    generate_all_generes = return_all_generes()
    iter = est_connection(generate_all_generes)
    return iter