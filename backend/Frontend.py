import json

from flask import Blueprint, render_template, Response

from API import article_dao

page = Blueprint('frontend', __name__)

def nav():
    """
    Creates the navbar dynamically.

    :return: Formatted navbar html section.
    """
    articles = list(article_dao.get_articles())

    return render_template("nav.html", articles=articles)

@page.route("/")
def index():
    articles = list(article_dao.get_articles())

    return render_template("index.html", articles=articles, nav=nav())


@page.route("/article/read/<article_id>")
def article_read(article_id):
    try:
        article = article_dao.get_article(article_id)

        return render_template("read.html", article=article, nav=nav())
    except Exception as e:
        print(e)
        return Response(json.dumps({'status': f'Unknown article: {article_id}'}), 404, mimetype='application/json')

@page.route("/article/edit/<article_id>")
def article_edit(article_id):
    try:
        article = article_dao.get_article(article_id)

        return render_template("edit.html", article=article, nav=nav())
    except Exception as e:
        print(e)
        return Response(json.dumps({'status': f'Unknown article: {article_id}'}), 404, mimetype='application/json')


