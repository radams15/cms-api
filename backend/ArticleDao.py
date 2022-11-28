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

        c.close()

        self._locked = False

    def get_article(self, id: int) -> Article:
        self._wait_lock()

        self._locked = True

        c = self.db.cursor()
        c.execute('SELECT * FROM Article WHERE id IS ?', (id,))

        article_data = c.fetchone()

        article = Article(
            *article_data[1:],
            article_data[0]
        )

        c.close()

        self._locked = False

        return article
