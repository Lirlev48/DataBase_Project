import mysql.connector
from mysql.connector import errorcode
import queries
from sshtunnel import SSHTunnelForwarder


def est_connection(query, args=None):
    # tunnel = SSHTunnelForwarder(('nova.cs.tau.ac.il', 22),
    #                             ssh_username='saharg',
    #                             ssh_password='',
    #                             remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306))
    # tunnel.start()
    details = {
        'user': 'DbMysql02',
        'password': 'DbMysql02',
        'host': 'mysqlsrv1.cs.tau.ac.il',    # '127.0.0.1',
        'database': 'DbMysql02',
        'port': '3306',     # tunnel.local_bind_port,
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
    if args is not None:
        cur.execute(query, args)
    else:
        cur.execute(query)
    iterator = list(cur)
    cnx.commit()
    cnx.close()
    return iterator


def render_rank_top_languages(from_date, to_date):
    args = (from_date, to_date)
    return est_connection(queries.rank_top_languages(), args)


def render_return_the_specialization_genre_of_companies(country_name):
    args = (country_name)
    return est_connection(queries.return_the_specialization_genre_of_companies(), args)


def render_all_genres():
    generate_all_generes = queries.return_all_generes()
    return est_connection(generate_all_generes)


def render_all_languages():
    generate_all_language = queries.return_all_languages()
    return est_connection(generate_all_language)


def runtime_genre_languages(runtime_from, runtime_to, genre, language1, language2):
    args = (int(runtime_from), int(runtime_to), genre, language1, language2,)
    return est_connection(queries.movie_recommendation(), args)


def render_all_countries():
    generate_all_countries = queries.generate_all_countries()
    return est_connection(generate_all_countries)


def render_movies_from_generes(genre, from_date, to_date, limit):
    genre = genre
    limit = int(limit)
    args = (genre, from_date, to_date, limit,)
    return est_connection(queries.get_movies_by_genre_and_date_range(), args)


def render_movies_from_text(fulltext, from_date, to_date):
    args = (fulltext, from_date, to_date,)
    return est_connection(queries.movies_from_text(), args)


def render_avg_vote_for_company_and_genre(limit):
    args = (int(limit),)
    return est_connection(queries.production_company_and_genre_average_vote(), args)


def render_num_of_movies_for_language_in_specific_budget_range(minimum_budget, maximum_budget):
    args = (int(minimum_budget), int(maximum_budget),)
    return est_connection(queries.num_of_movies_for_language_in_specific_budget_range(), args)
