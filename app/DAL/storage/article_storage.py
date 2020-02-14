from datetime import datetime

from app.DAL.models import Article


class ArticleStorage:
    COLUMN_NAME = "article"

    def __init__(self, storage):
        self.storage = storage

    def save(self, article):
        if article:
            self.storage.store(Article.from_dict(article))
        else:
            raise AttributeError("Wrong data")

    def save_many(self, articles):
        if articles:
            self.storage.store_many([Article.from_dict(article) for article in articles])
        else:
            raise AttributeError("Wrong data")

    def pagination(self, page):
        if page:
            return self.storage.pagination(page=page, col_name=self.COLUMN_NAME)
        else:
            raise AttributeError("Wrong page")

    def read(self, from_date, to_date=datetime.utcnow(), limit=None):
        return self.storage.read(column=self.COLUMN_NAME, limit=limit, from_date=from_date, to_date=to_date)
