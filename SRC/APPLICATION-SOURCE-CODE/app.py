from flask import Flask, render_template, request, json,url_for
import datetime
import queryGenCode
app = Flask(__name__)

genere_list = ["Drama","Crime","Comedy","Action","Thriller","Adventure","Science Fiction","Animation","Family,Romance","Mystery","Horror","Fantasy","War",
               "Music","Western","History","Documentary","TV Movie"]
@app.route("/")
def home():
        return render_template('x.html') #call the home page html

@app.route("/q1")
def q1():
        return render_template('q1.html',genres=genere_list)


@app.route("/q1-output", methods=["POST"])
def q1_result():
    gen = request.form.get("genres")
    from_date = request.form.get("from")  ##Y - Date style att todo
    to_date = request.form.get("to")  ##Y - Date style att todo
    lim = request.form.get("limit")
    if (lim == "" or  not lim.isdigit()) or gen =="" or (gen not in dict.genres):
        return render_template('404page.html')
    iter_res = queryGenCode.RendArtFromGen(gen, from_date, to_date, lim)

    return render_template('query1Layout.html', art_from_gen_iter=iter_res)
