from flask import Flask, render_template, request, json, url_for
import datetime
import generateQueries
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html') #TODO need to add home page html

@app.route("/q1")
def q1():
    genre_list =generateQueries.renderAllGenres()
    return render_template('q1.html', genres=genre_list)


@app.route("/q2")
def q2():
    return render_template('q2.html')

@app.route("/q3")
def q3():
    countries_list =generateQueries.renderAllCountries()
    return render_template('q3.html', countries=countries_list)


@app.route("/q1-output", methods=["POST"])
def q1_result():
    genre_list = [t[0] for t in generateQueries.renderAllGenres()]
    genre = request.form.get("genres")
    from_date = request.form.get("from")  ##Y - Date style att todo
    to_date = request.form.get("to")  ##Y - Date style att todo
    limit = request.form.get("limit")
    if (limit == "" or not limit.isdigit()) or genre =="" or (genre not in genre_list): #TODO need to make sure the genres list is a dropdown and the user can't write what he wants
        return render_template('404page.html') # TODO need to add 404Page
    iter_res = generateQueries.RenderMoviesFromGeneres(genre, from_date, to_date, limit)
    return render_template('query1Format.html', iter_movies=iter_res)

@app.route("/q2-output", methods=["POST"])
def q2_result():
    from_date = request.form.get("from")  ##Y - Date style att todo
    to_date = request.form.get("to")  ##Y - Date style att todo
    iter_res = generateQueries.RenderRankTopLanguages(from_date, to_date)
    return render_template('query2Format.html', iter_languages=iter_res)

@app.route("/q3-output", methods=["POST"])
def q3_result():
    country_list = [t[0] for t in generateQueries.renderAllCountries()]
    country = request.form.get("countries")
    if (country == "" or (country not in country_list)):  # TODO need to make sure the genres list is a dropdown and the user can't write what he wants
        return render_template('404page.html')  # TODO need to add 404Page
    iter_res = generateQueries.RenderCountNumberOfMoviesForProductionCompaniesPerCountry(country)
    return render_template('query3Format.html', iter_res=iter_res)


@app.route("/q4-output")
def q4_result():
    iter_res = generateQueries.render_avg_vote_for_company_and_genre()
    return render_template('query4Format.html', iter_companies_genres_votes=iter_res)


@app.route("/q6")
def q6():
    genre_list = generateQueries.renderAllGenres()
    return render_template('q6.html', genres=genre_list)

@app.route("/q6-output", methods=["POST"])
def q6_result():
    minimum_budget = request.form.get("minimum_budget")
    maximum_budget = request.form.get("maximum_budget")
    iter_res = generateQueries.render_num_of_movies_for_language_in_specific_budget_range(minimum_budget, maximum_budget)
    return render_template('query6Format.html', iter_language_and_num_of_movies=iter_res)

if __name__ == '__main__':
    app.run(port="8888", debug=True)


# potential queries

# return movies by genres and limit and range of release dates - DONE Q1
# rank the top langauages that are used in movies with limitation on release dates -DONE Q2
# let user choose a country - for that country for all production companies in that country count the number of movies made for each genre -
# for each production company find the average vote_average for the movies it created for each genre
# full text - let user write a word and find all movies that have that word in the title - return all the directors from those movies
# let user choose a vote_average range and a language and adult film or not and return all movies - return the title and description of the movies
