import datetime

from flask import Flask
from flask_cors import CORS

from API import api
from Frontend import page as frontend
from Article import Article

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(api)
app.register_blueprint(frontend)

# CORS(app)  # Enable CORS for the site to allow a frontend on a different IP/port

from API import article_dao

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    '''article_dao.add_article(Article(
        'Title',
        'SubTitle',
        'Content',
        'https://google.com/',
        datetime.datetime.now()
    ))'''

    '''#print([x.id for x in article_dao.get_articles()])
    print(article_dao.get_article('638dbce734a4992cc02c4436'))

    print(article_dao.update_article(Article(
        'Title 3',
        'SubTitle',
        'Content',
        'https://google.com/',
        datetime.datetime.now(),
        id='638dbce734a4992cc02c4436'
    )))

    print(article_dao.get_article('638dbce734a4992cc02c4436'))'''