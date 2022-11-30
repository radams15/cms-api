from flask import Blueprint, render_template

from API import article_dao

page = Blueprint('frontend', __name__)

@page.route("/")
def index():
    articles = list(article_dao.get_articles())

    return render_template("index.html", articles=articles)


@page.route("/article/read/<article_id>")
def article_read(article_id):
    article = article_dao.get_article(article_id)

    return render_template("read.html", article=article)

@page.route("/article/edit/<article_id>")
def article_edit(article_id):
    article = article_dao.get_article(article_id)

    return render_template("edit.html", article=article)


