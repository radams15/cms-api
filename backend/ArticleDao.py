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
    """
    Raised to indicate an article that does not exist but was requested.
    """

    def __init__(self, id):
        super().__init__(f"Unknown article: {id}")


class ArticleDao:
    """
    Database manager for the Article table.

    Allows selecting from and inserting into the table.

    If the database file does not exist then the file and table are created.
    """

    def __init__(self, db_file):
        init_table = False
        if not path.exists(db_file):
            init_table = True

        self.db = sqlite3.connect(db_file, check_same_thread=False)

        if init_table:  # DB did not exist so create the table.
            c = self.db.cursor()
            c.execute(DB_TABLE_STMT)
            c.close()

        self._locked = False

    def _wait_lock(self):
        """
        Wait until the table is no longer locked.
        """
        while self._locked: continue

    def close(self):
        """
        Save and close the database.

        Sets db to None to prevent re-use.
        :return:
        """
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

        if not article_data:  # Article id did not exist, fail
            self._locked = False  # Unlock table to prevent deadlock
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
            if not article_data:  # Article id did not exist, fail
                self._locked = False  # Unlock table to prevent deadlock
                raise UnknownArticleException(id)

            yield Article(
                *article_data[1:],
                article_data[0]
            )

        c.close()

        self._locked = False
