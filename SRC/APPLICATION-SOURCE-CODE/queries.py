def get_movies_by_genre_and_date_range():
    return ("SELECT movies.original_title "
            "FROM movies, movies_to_genres, genres "
            "WHERE movies.imdb_id = movies_to_genres.imdb_id "
            "AND movies_to_genres.genres_id = genres.id "
            "AND genres.genre = %s "
            "AND movies.release_date BETWEEN DATE (%s) AND DATE (%s) "
            "ORDER BY  movies.release_date DESC "
            "LIMIT %s")


def return_all_generes():
    return ("SELECT DISTINCT genres.genre "
            "FROM genres ORDER BY genres.genre")


def return_all_languages():
    return ("SELECT DISTINCT spoken_languages.english_name "
            "FROM spoken_languages ORDER BY spoken_languages.english_name")


def generate_all_countries():
    return ("SELECT DISTINCT production_countries.name "
            "FROM production_countries ORDER BY production_countries.name")


def rank_top_languages():
    return (" SELECT spoken_languages.english_name, count(Distinct spoken_tbl.imdb_id) AS count_movies_per_language"
            " FROM movies,movies_to_spoken_languages AS spoken_tbl, spoken_languages "
            " Where movies.imdb_id = spoken_tbl.imdb_id "
            " AND spoken_languages.id = spoken_tbl.spoken_languages_id "
            " And movies.release_date BETWEEN DATE (%s) AND DATE (%s) "
            " GROUP BY  spoken_languages.english_name "
            " ORDER BY count_movies_per_language desc")


def return_the_specialization_genre_of_companies():
    return ("SELECT tlb.pname as company, tlb.gname as genre "
            "FROM "
            "(SELECT production_companies.name as pname, genres.genre as gname, "
            "count(distinct movies.imdb_id) as count_movies_per_genre "
            "FROM movies, production_countries, production_companies, movies_to_genres, "
            "genres, movies_to_production_companies "
            "Where production_companies.origin_country = production_countries.id "
            "AND movies_to_genres.genres_id = genres.id AND movies.imdb_id = movies_to_genres.imdb_id "
            "AND movies_to_production_companies.imdb_id =  movies.imdb_id "
            "AND movies_to_production_companies.production_companies_id =  production_companies.id "
            "AND production_countries.name = '%s' "
            "GROUP BY production_companies.name, genres.genre) as tlb "
            "WHERE tlb.count_movies_per_genre >= ALL(SELECT "
            "count(distinct movies.imdb_id) as count_movies_per_genre "
            "FROM movies, production_countries, production_companies, movies_to_genres, "
            "genres, movies_to_production_companies "
            "Where production_companies.origin_country = production_countries.id "
            "AND movies_to_genres.genres_id = genres.id AND movies.imdb_id = movies_to_genres.imdb_id "
            "AND movies_to_production_companies.imdb_id =  movies.imdb_id "
            "AND movies_to_production_companies.production_companies_id =  production_companies.id "
            "AND production_countries.name = '%s' "
            "AND tlb.pname =production_companies.name "
            "GROUP BY production_companies.name, genres.genre)"
            "order by company,genre"
            )


def production_company_and_genre_average_vote():
    return ("Select production_companies.name, genres.genre, AVG(movies.vote_average) as Average_vote "
            "From production_companies, movies, movies_to_genres as mtg, genres, "
            "movies_to_production_companies as mtpc "
            "Where production_companies.id = mtpc.production_companies_id and mtpc.imdb_id = movies.imdb_id "
            "and mtg.imdb_id = movies.imdb_id and mtg.genres_id = genres.id "
            "group by production_companies.name, genres.genre "
            "Order by Average_vote DESC, production_companies.name, genres.genre "
            "LIMIT %s")


def movies_from_text():
    return ("select title, overview "
            "from movies where match(title, overview) "
            "against(%s IN BOOLEAN MODE) "
            "AND movies.release_date BETWEEN DATE (%s) AND DATE (%s)")


def num_of_movies_for_language_in_specific_budget_range():
    return ("SELECT spoken_languages.english_name, Count(Distinct movies.imdb_id) as count "
            "from movies, movies_to_spoken_languages as msl, spoken_languages "
            "where movies.imdb_id = msl.imdb_id and msl.spoken_languages_id = spoken_languages.id "
            "and movies.budget >= %s and movies.budget <= %s "
            "group by spoken_languages.english_name "
            "order by count DESC")


def movie_recommendation():
    return ("SELECT movies.title, movies.vote_average, movies.runtime "
            "from movies, movies_to_genres, genres,movies_to_spoken_languages as mtsl, spoken_languages " 
            "where movies.imdb_id = movies_to_genres.imdb_id and movies_to_genres.genres_id = genres.id "
            "and mtsl.spoken_languages_id = spoken_languages.id and mtsl.imdb_id = movies.imdb_id "
            "and movies.runtime >= %s and movies.runtime <= %s and genres.genre = %s "
            "and spoken_languages.english_name in (%s, %s) "
            "order by movies.vote_average DESC ")
