import sqlite3
from os import path

from Article import Article

DB_TABLE_STMT = '''
CREATE TABLE "Article" (
    "id"	INTEGER NOT NULL UNIQUE,
    "title"	TEXT,
    "subtitle"	TEXT,
    "content"	TEXT NOT NULL,
    "header_img"	TEXT NOT NULL,
    "published"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);'''


class UnknownArticleException(Exception):
    def __init__(self, id):
        super().__init__(f"Unknown article: {id}")


class ArticleDao:

    def __init__(self, db_file):
        init_table = False
        if not path.exists(db_file):
            init_table = True

        self.db = sqlite3.connect(db_file, check_same_thread=False)

        if init_table:
            c = self.db.cursor()
            c.execute(DB_TABLE_STMT)
            c.close()

        self._locked = False

    def _wait_lock(self):
        while self._locked: continue

    def close(self):
        self.db.commit()
        self.db.close()
        self.db = None

    def add_article(self, article: Article):
        self._wait_lock()

        self._locked = True
        c = self.db.cursor()
        c.execute(
            'INSERT INTO Article VALUES (null, ?, ?, ?, ?, ?)', (
                article.title,
                article.subtitle,
                article.content,
                article.header_img,
                article.published.timestamp()
            )
        )

        c.execute('SELECT id from Article order by ROWID DESC limit 1')
        id = c.fetchone()

        c.close()
        self.db.commit()

        self._locked = False

        return id[0]

    def get_article(self, id: int) -> Article:
        self._wait_lock()

        self._locked = True

        c = self.db.cursor()
        c.execute('SELECT * FROM Article WHERE id IS ?', (id,))

        article_data = c.fetchone()

        if article_data == None:
            self._locked = False
            raise UnknownArticleException(id)

        article = Article(
            *article_data[1:],
            article_data[0]
        )

        c.close()

        self._locked = False

        return article

    def get_articles(self) -> iter:
        self._wait_lock()

        self._locked = True

        c = self.db.cursor()
        c.execute('SELECT * FROM Article')

        article_data_list = c.fetchall()

        for article_data in article_data_list:
            if article_data == None:
                self._locked = False
                raise UnknownArticleException(id)

            yield Article(
                *article_data[1:],
                article_data[0]
            )

        c.close()

        self._locked = False