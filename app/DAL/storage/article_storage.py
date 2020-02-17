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

    def read(self, from_date, to_date=None, page=None, page_size=None, site=None):
        # Handle cases when None passed explicitly
        if to_date is None:
            to_date = datetime.utcnow()
        data = self.storage.read(column=self.COLUMN_NAME,
                                 from_date=from_date,
                                 to_date=to_date,
                                 page=page,
                                 page_size=page_size,
                                 site=site)
        if data:
            return data
        else:
            print("No data")
