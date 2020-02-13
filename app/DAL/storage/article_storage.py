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

    def read(self, limit=None):
        return self.storage.read(self.COLUMN_NAME, limit)
