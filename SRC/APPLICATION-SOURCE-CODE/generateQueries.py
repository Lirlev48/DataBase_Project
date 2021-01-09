import mysql.connector
from mysql.connector import errorcode
from datetime import date
from datetime import datetime
import queries
from sshtunnel import SSHTunnelForwarder


def est_connection(query, args=None): # TODO change name of func, variables, prints and details
    tunnel = SSHTunnelForwarder(('nova.cs.tau.ac.il', 22),
                                                                                                              ssh_username= 'yuvalishay', # input("insert your moodle username: "),
                                                                                                              ssh_password= 'Thxeu123', # input("insert your moodle password: "),
                                remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306))
    tunnel.start()
    details = {
        'user': 'DbMysql02',
        'password': 'DbMysql02',
        'host': '127.0.0.1',
        'database': 'DbMysql02',
        'port': tunnel.local_bind_port,
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
    iterator = list(cur)
    cnx.commit()
    cnx.close()
    return iterator


def RenderMoviesFromGeneres(genre, from_date, to_date, limit): #change name of func and variables
    genre = genre
    limit = int(limit)
    args = (genre, from_date, to_date, limit,)
    iter = est_connection(queries.get_movies_by_genre_and_date_range(), args)
    return iter

def renderAllGenres():
    generate_all_generes = queries.return_all_generes()
    iter = est_connection(generate_all_generes)

    return iter


#@@UPDATE HERE
def render_avg_vote_for_company_and_genre():
    iter = est_connection(queries.production_company_and_genre_average_vote())
    return iter

#@@UPDATE HERE
def render_num_of_movies_for_language_in_specific_budget_range(minimum_budget, maximum_budget):
    args = (float(minimum_budget), float(maximum_budget),)
    iter = est_connection(queries.num_of_movies_for_language_in_specific_budget_range(), args)
    return iter