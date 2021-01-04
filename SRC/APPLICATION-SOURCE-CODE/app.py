from flask import Flask, render_template, request, json,url_for
import datetime
import generateQueries
app = Flask(__name__)

genere_list = None


@app.route("/")
def home():
        return render_template('x.html') #TODO need to add home page html

@app.route("/q1")
def q1():
    genere_list = generateQueries.renderAllGenres()
    return render_template('q1.html',genres=genere_list)


@app.route("/q1-output", methods=["POST"])
def q1_result():
    genre = request.form.get("genres")
    from_date = request.form.get("from")  ##Y - Date style att todo
    to_date = request.form.get("to")  ##Y - Date style att todo
    limit = request.form.get("limit")
    if (limit == "" or  not limit.isdigit()) or genre =="" or (genre not in genere_list): #TODO need to make sure the genres list is a dropdown and the user can't write what he wants
        return render_template('404page.html') # TODO need to add 404Page
    iter_res = generateQueries.RenderMoviesFromGeneres(genre, from_date, to_date, limit)

    return render_template('query1Format.html', iter_movies=iter_res)


# potential queries

# return movies by genres and limit and range of release dates - DONE Q1
# rank the top langauages that are used in movies with limitation on release dates -DONE Q2
# let user choose a country - for that country for all production companies in that country count the number of movies made for each genre -
# for each production company find the average vote_average for the movies it created for each genre
# full text - let user write a word and find all movies that have that word in the title - return all the directors from those movies
# let user choose a vote_average range and a language and adult film or not and return all movies - return the title and description of the movies
