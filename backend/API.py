import json

from flask import Blueprint, request, Response

from ArticleDao import ArticleDao, UnknownArticleException, InvalidArticleException
from Article import Article

api = Blueprint('api', __name__)

article_dao = ArticleDao('articles.db')

def html_sanitise(inp):
    return inp
    #return str(Markup.escape(inp))

@api.route("/api/v1/article/<article_id>", methods=['GET'])
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


@api.route("/api/v1/article/", methods=['GET'])
def get_articles():
    """
    Get a list of all articles on the site.
    :return: list of all articles on the site
    """
    articles = article_dao.get_articles()

    articles = map(Article.to_json, articles)  # Convert each article to its JSON implementation.

    return Response(json.dumps(list(articles)), 200, mimetype='application/json')


@api.route("/api/v1/article/", methods=['POST'])
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

    try:
        id = article_dao.add_article(article)  # Add the article, return the id of the added article.
        return Response(json.dumps({'success': True, 'id': id}), 201, mimetype='application/json')
    except InvalidArticleException:
        return Response(json.dumps({'success': False}), 400, mimetype='application/json')


@api.route("/api/v1/article/", methods=['PUT'])
def update_article():
    """
    Change an existing article
    :return: A success message (code 201) if the page successfully uploads.
    """
    data = request.json

    article = Article.from_json(data)

    article.title = html_sanitise(article.title)
    article.subtitle = html_sanitise(article.subtitle)
    article.content = html_sanitise(article.content)

    article_dao.update_article(article)  # Add the article, return the id of the added article.

    return Response(json.dumps({'success': True, 'id': article.id}), 201, mimetype='application/json')
