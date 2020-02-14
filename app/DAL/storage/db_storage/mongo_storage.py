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

    def pagination(self, page, col_name, page_size=5, from_date=None, to_date=None):  # todo: remove page_size hardcode
        """returns a set of documents belonging to page number `page`
        where size of each page is `page_size`.
        """
        date_query = {'datePublished': {'$lt': to_date, '$gte': from_date}}
        date_sort_query = [("date", -1)]
        # Calculate number of documents to skip
        skips = page_size * (page - 1)
        if from_date and to_date:
            cursor = self.db[col_name].find(date_query).sort(date_sort_query).skip(skips).limit(page_size)
        else:
            # Skip and limit
            cursor = self.db[col_name].find().sort(date_sort_query).skip(skips).limit(page_size)
        data = []
        for x in cursor:
            x["_id"] = str(x["_id"])
            data.append(x)
        # Return documents
        return data

    def read(self, column, limit=None, from_date=None, to_date=None):
        date_query = {'datePublished': {'$lt': to_date, '$gte': from_date}}
        date_sort_query = [("datePublished", -1)]
        try:
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
        except KeyError:
            print("Column provided was not found")
            raise

    def cleanup(self, col_name):
        self.db[col_name].delete_many({})
