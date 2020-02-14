import pymongo

from app.DAL.storage.abstract_storage import AbstractStorage


class MongoStorage(AbstractStorage):
    def __init__(self, storage_config):
        self.db = pymongo.MongoClient(storage_config.get_uri())[storage_config.database]

    def store(self, model):
        col = self.db[model.MODEL_STORAGE_NAME]
        col.insert_one(model.to_dict())

    def store_many(self, models):
        col_name = models[0].MODEL_STORAGE_NAME
        self.cleanup(col_name)
        col = self.db[col_name]
        col.insert_many(model.to_dict() for model in models)

    def read(self, column, limit=None, from_date=None, to_date=None, page=None, page_size=None):
        if not list(self.db[column].find({})):
            raise AttributeError(f"Data in column {column} was not found")
        return self.__get_data(column, from_date, to_date, page, page_size, limit)

    def __pagination(self, page, column, page_size, from_date=None, to_date=None):
        """returns a set of documents belonging to page number `page`
        where size of each page is `page_size`.
        """
        date_query = {'datePublished': {'$lt': to_date, '$gte': from_date}}
        date_sort_query = [("datePublished", -1)]
        # Calculate number of documents to skip
        skips = page_size * (page - 1)
        if from_date and to_date:
            cursor = self.db[column].find(date_query).sort(date_sort_query).skip(skips).limit(page_size)
        else:
            # Skip and limit
            cursor = self.db[column].find().sort(date_sort_query).skip(skips).limit(page_size)
        data = []
        for x in cursor:
            x["_id"] = str(x["_id"])
            data.append(x)
        # Return documents
        return data

    def __get_data(self, column, from_date=None, to_date=None, page=None, page_size=None, limit=None):
        date_query = {'datePublished': {'$lt': to_date, '$gte': from_date}}
        date_sort_query = [("datePublished", -1)]

        # read page by page
        if page and page_size:
            return self.__pagination(page=page, page_size=page_size, column=column, from_date=from_date, to_date=to_date)
        # read whole data
        else:
            if limit is None:
                if from_date and to_date:
                    data = list(self.db[column].find(date_query).sort(date_sort_query))
                else:
                    data = list(self.db[column].find().sort(date_sort_query))
                for d in data:
                    d["_id"] = str(d["_id"])
                return data
            elif limit == 1:
                if from_date and to_date:
                    data = self.db[column].find_one(date_query)
                else:
                    data = self.db[column].find_one()
                data["_id"] = str(data["_id"])
                return data
            else:
                if from_date and to_date:
                    data = list(self.db[column].find(date_query))
                else:
                    data = list(self.db[column].find().limit(limit))
                for d in data:
                    d["_id"] = str(d["_id"])
                return data

    def cleanup(self, col_name):
        self.db[col_name].delete_many({})
