import datetime

from flask import Flask, request

from ArticleDao import ArticleDao
from Article import Article

article_dao = ArticleDao('articles.db')

'''article_dao.add_article(Article(
    'Title 1',
    'A subtitle',
    'Some content',
    'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    datetime.datetime.now()
))'''

print(article_dao.get_article(1))

article_dao.close()

'''app = Flask(__name__)

@app.route("/article/<article_id>", methods=['GET'])
def get_article(article_id: int):
    return f"<p>Got article: {article_id}"


@app.route("/article/", methods=['POST'])
def add_article():
    data = request.json

    print(data['title'])
    return f"<p>Got article: {data['title']}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
'''