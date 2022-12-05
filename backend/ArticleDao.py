import sqlite3
import pymongo
from os import path

from bson import ObjectId

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


class InvalidArticleException(Exception):
    """
    Raised to indicate an article that has failed the validity check.
    """

    def __init__(self, article):
        super().__init__(f"Invalid article: {article.title}")


class ArticleDao:
    """
    Database manager for the Article table.

    Allows selecting from and inserting into the table.

    If the database file does not exist then the file and table are created.
    """

    def __init__(self, url):
        self.client = pymongo.MongoClient(url)

        # if 'Article' not in self.client.list_database_names():  # DB did not exist so create the table.
        #    pass

        self.db = self.client['Article']

        self.articles = self.db['Article']

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

    def add_article(self, article: Article) -> int:
        if not article.valid():
            raise InvalidArticleException(article)

        self._wait_lock()

        try:
            self._locked = True

            to_insert = article.to_json()

            res = self.articles.insert_one(to_insert)

            return res.inserted_id

        except Exception as e:
            raise e

        finally:
            self._locked = False

    def get_article(self, id: str) -> Article:
        self._wait_lock()

        try:
            self._locked = True

            query = {'_id': ObjectId(id)}

            article_json = self.articles.find_one(query)

            article = Article.from_json(article_json)

            return article

        except Exception as e:
            raise e

        finally:
            self._locked = False  # Unlock table to prevent deadlock

    def update_article(self, article):
        self._wait_lock()

        try:
            self._locked = True

            to_insert = article.to_json()

            query = {'_id': ObjectId(article.id)}
            new_values = {'$set': article.to_json()}

            self.articles.update_one(query, new_values)

        except Exception as e:
            raise e

        finally:
            self._locked = False

    def get_articles(self) -> iter:
        self._wait_lock()

        try:
            self._locked = True

            return map(Article.from_json, self.articles.find())

        except:
            return iter([])  # Prentend there were no articles, return empty iterator.

        finally:
            self._locked = False  # Unlock table to prevent deadlock
