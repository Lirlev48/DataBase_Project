from flask import Flask, render_template, request
import generateQueries

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/q1")
def q1():
    genre_list = generateQueries.render_all_genres()
    return render_template('q1.html', genres=genre_list)


@app.route("/q2")
def q2():
    return render_template('q2.html')


@app.route("/q3")
def q3():
    countries_list = generateQueries.render_all_countries()
    return render_template('q3.html', countries=countries_list)


@app.route("/q4")
def q4():
    return render_template('q4.html')


@app.route("/q5")
def q5():
    return render_template('q5.html')


@app.route("/q6")
def q6():
    return render_template('q6.html')


@app.route("/q7")
def q7():
    genre_list = generateQueries.render_all_genres()
    language_list = generateQueries.render_all_languages()
    return render_template('q7.html', genres=genre_list, languages=language_list)


@app.route("/q1-output", methods=["POST"])
def q1_result():
    genre_list = [t[0] for t in generateQueries.render_all_genres()]
    genre = request.form.get("genres")
    from_date = request.form.get("from")
    to_date = request.form.get("to")
    limit = request.form.get("limit")
    if limit == "" or not limit.isdigit() or genre == "" or genre not in genre_list:
        return render_template('404.html')
    iter_res = generateQueries.render_movies_from_generes(genre, from_date, to_date, limit)
    return render_template('query1Format.html', iter_movies=iter_res)


@app.route("/q2-output", methods=["POST"])
def q2_result():
    from_date = request.form.get("from")
    to_date = request.form.get("to")
    iter_res = generateQueries.render_rank_top_languages(from_date, to_date)
    return render_template('query2Format.html', iter_languages=iter_res)


@app.route("/q3-output", methods=["POST"])
def q3_result():
    country_list = [t[0] for t in generateQueries.render_all_countries()]
    country = request.form.get("countries")
    if country == "" or country not in country_list:
        return render_template('404.html')
    iter_res = generateQueries.render_return_the_specialization_genre_of_companies(country)
    return render_template('query3Format.html', iter_res=iter_res)


@app.route("/q4-output", methods=["POST"])
def q4_result():
    limit = request.form.get("limit")
    if limit == "" or not limit.isdigit():
        return render_template('404.html')
    iter_res = generateQueries.render_avg_vote_for_company_and_genre(limit)
    return render_template('query4Format.html', iter_companies_genres_votes=iter_res)


@app.route("/q5-output", methods=["POST"])
def q5_result():
    from_date = request.form.get("from")
    to_date = request.form.get("to")
    fulltext_in = request.form.get("fulltext_in")
    fulltext_out = request.form.get("fulltext_out")
    if fulltext_in == "" or fulltext_out == "":
        return render_template('404.html')
    iter_res = generateQueries.render_movies_from_text(f"+{fulltext_in}* -{fulltext_out}*", from_date, to_date)
    return render_template('query5Format.html', iter_title_and_overview=iter_res)


@app.route("/q6-output", methods=["POST"])
def q6_result():
    minimum_budget = request.form.get("minimum_budget")
    maximum_budget = request.form.get("maximum_budget")
    if maximum_budget == "" or not maximum_budget.isdigit()\
            or minimum_budget == "" or not minimum_budget.isdigit():
        return render_template('404.html')
    iter_res = generateQueries.render_num_of_movies_for_language_in_specific_budget_range(minimum_budget, maximum_budget)
    return render_template('query6Format.html', iter_language_and_num_of_movies=iter_res)


@app.route("/q7-output", methods=["POST"])
def q7_result():
    genre_list = [t[0] for t in generateQueries.render_all_genres()]
    language_list = [t[0] for t in generateQueries.render_all_languages()]
    genre = request.form.get("genres")
    runtime_from = request.form.get("runtime_from")
    runtime_to = request.form.get("runtime_to")
    language1 = request.form.get("language1")
    language2 = request.form.get("language2")
    if runtime_from == "" or not runtime_from.isdigit() \
            or runtime_to == "" or not runtime_to.isdigit() \
            or genre == "" or genre not in genre_list \
            or language1 not in language_list or language2 not in language_list \
            or language1 == "" or language2 == "":
        return render_template('404.html')
    iter_res = generateQueries.runtime_genre_languages(runtime_from, runtime_to, genre, language1, language2)
    return render_template('query7Format.html', iter_movies=iter_res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="40043", debug=True)
