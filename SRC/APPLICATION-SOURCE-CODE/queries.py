def get_movies_by_genere_and_date_range():
    return (" SELECT movies.original_title " 
            " FROM movies, movies_to_genres, genres " 
            " movies.imdb_id = movies_to_genres.movie_id AND "
			" movies_to_genres.genres_id = genres.id AND "
            " genres.name LIKE %s "
            " AND movies.release_date BETWEEN DATE (%s) AND DATE (%s) "
            " ORDER BY  movies.release_date DESC "
            " LIMIT %s ")


def return_all_generes():
    return (" SELECT genres.name " 
            " FROM genres " )

def rank_top_languages():
    return(" SELECT spoken_languages.english_name, count(spoken_tbl.movie_id) AS count_movies_per_language" 
            " FROM movies,movies_to_spoken_languages AS spoken_tbl,spoken_languages " 
            " movies.imdb_id = movies_to_spoken_languages.movie_id AND "
            "spoken_languages.iso_639_1 = movies_to_spoken_languages.spoken_languages_id"
            " movies.release_date BETWEEN DATE (%s) AND DATE (%s) "
            " GROUP BY  spoken_languages.english_name "
            " ORDER BY count_movies_per_language desc"
       )

def count_number_of_movies_for_production_companies_per_country():
    return (
            " SELECT name, max(count_movies_per_gener)"
            " FROM"
            " ("
            "SELECT production_company.name,genre, count(distinct imdb_id) as count_movies_per_gener "
            " FROM production_countries,production_companies,movies_to_production_companies "
            " production_companies.origin_country = production_countries.iso_3166_1 AND"
            " movies_to_production_companies.production_companies_id =  production_companies.id"
            " AND production_countries.name == '(%s)' "
            " GROUP BY production_company.name,genre"
            ")"
            " GROUP BY name"
            )