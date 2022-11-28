import json
import re

from flask import Flask, request, Response
from flask_cors import CORS

from ArticleDao import ArticleDao, UnknownArticleException
from Article import Article

app = Flask(__name__)

article_dao = ArticleDao('articles.db')

CORS(app)  # Enable CORS for the site to allow a frontend on a different IP/port


def html_sanitise(inp):
    return re.sub(r'<|>|&amp;', '', inp)


@app.route("/article/<article_id>", methods=['GET'])
def get_article(article_id: int):
    """
    Gets article information from id.

    :param article_id: id of the article to get
    :return: A JSON representation of the article
    """
    try:
        article = article_dao.get_article(article_id)

        return Response(json.dumps(article.to_json()), 200, mimetype='application/json')

    except UnknownArticleException:  # Article did not exist
        return Response(json.dumps({
            'status': f'Unknown article id: {article_id}'
        }), 404, mimetype='application/json')  # Return 404 error


@app.route("/article/", methods=['GET'])
def get_articles():
    """
    Get a list of all articles on the site.
    :return: list of all articles on the site
    """
    articles = article_dao.get_articles()

    articles = map(Article.to_json, articles)  # Convert each article to its JSON implementation.

    return Response(json.dumps(list(articles)), 200, mimetype='application/json')


@app.route("/article/", methods=['POST'])
def add_article():
    """
    Upload an article to the page
    :return: A success message (code 201) if the page successfully uploads.
    """
    data = request.json

    article = Article.from_json(data)

    article.title = html_sanitise(article.title)
    article.subtitle = html_sanitise(article.subtitle)
    article.content = html_sanitise(article.content)

    id = article_dao.add_article(article)  # Add the article, return the id of the added article.

    return Response(json.dumps({'success': True, 'id': id}), 201, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
