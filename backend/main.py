import json

from flask import Flask, request, Response

from ArticleDao import ArticleDao
from Article import Article

article_dao = ArticleDao('articles.db')

app = Flask(__name__)


@app.route("/article/<article_id>", methods=['GET'])
def get_article(article_id: int):
    article = article_dao.get_article(article_id)

    return Response(json.dumps(article.to_json()), 200, mimetype='application/json')


@app.route("/article/", methods=['POST'])
def add_article():
    data = request.json

    article = Article.from_json(data)

    id = article_dao.add_article(article)

    return Response(json.dumps({'success': True, 'id': id}), 201, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
