from datetime import datetime

import pymongo

from app.data_access.storage.abstract_storage import AbstractStorage


class MongoStorage(AbstractStorage):
    def __init__(self, storage_config):
        self.db = pymongo.MongoClient(storage_config.get_uri())[storage_config.database]

    def store(self, model):
        col = self.db[model.MODEL_STORAGE_NAME]
        col.insert_one(model.to_dict())

    def store_many(self, models):
        col_name = models[0].MODEL_STORAGE_NAME
        # self.cleanup(col_name)
        col = self.db[col_name]
        col.insert_many(model.to_dict() for model in models)

    def read(self, column, from_date=None, to_date=None, page=None, page_size=None, site=None):
        if not list(self.db[column].find({})):
            raise AttributeError(f"Data in column {column} was not found")
        return self.__get_data(column, from_date=from_date, to_date=to_date, page=page, page_size=page_size, site=site)

    def __pagination(self, page, column, page_size, find_query, sort_query):
        """returns a set of documents belonging to page number `page`
        where size of each page is `page_size`.
        """
        # Calculate number of documents to skip
        skips = page_size * (page - 1)
        return self.db[column].find(find_query).sort(sort_query).skip(skips).limit(page_size)

    def __get_data(self, column, from_date=None, to_date=None, page=None, page_size=None, site=None):
        if not to_date:
            to_date = datetime.utcnow()
        if not from_date:
            from_date = datetime.min
        if site:
            find_query = {'datePublished': {'$lt': to_date, '$gte': from_date}, 'site': site}
        else:
            find_query = {'datePublished': {'$lt': to_date, '$gte': from_date}}
        sort_query = [("datePublished", -1)]

        # read page by page
        if page and page_size:
            data = self.__pagination(page=page, page_size=page_size, column=column, find_query=find_query,
                                     sort_query=sort_query)
        # read whole data
        else:
            data = self.db[column].find(find_query).sort(sort_query)
        data = list(data)
        for d in data:
            d["_id"] = str(d["_id"])
        return data

    def cleanup(self, col_name):
        self.db[col_name].delete_many({})
