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

    def read(self, column, limit=None):
        try:
            if limit is None:
                data = list(self.db[column].find())
                for d in data:
                    d["_id"] = str(d["_id"])
                return data
            elif limit == 1:
                data = self.db[column].find_one()
                data["_id"] = str(data["_id"])
                return data
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
