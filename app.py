from flask import Flask, render_template, request, redirect
from Url import Url
from utils import generateSlug, findUrl

app = Flask(__name__)

urlArr = []


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/url/", methods=["POST"])
def new_url():
    slug = request.form["slug"]
    url = request.form["url"]
    print(url, slug)

    if slug == "":
        slug = generateSlug(6)

    urlArr.append(Url(url, slug))
    return "http://localhost:5000/"+slug


@app.route("/<string:slug>")
def redirectToSlug(slug):
    url = urlArr[findUrl(slug, urlArr)]

    return redirect(url.url, 302)
