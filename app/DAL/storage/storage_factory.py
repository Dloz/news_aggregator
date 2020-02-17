from collections import namedtuple

from app.DAL.storage.article_storage import ArticleStorage
from app.DAL.storage.db_storage.mongo_storage import MongoStorage
from app.DAL.storage.link_storage import LinkStorage
from config import storage_config

Storages = namedtuple("Storages", ['article_storage', 'link_storage'])


class StorageFactory:
    __INSTANCE = None
    storages = {  # todo: get storage name from package name
        "mongodb": MongoStorage,
    }

    model_storages = [ArticleStorage, LinkStorage]

    @classmethod
    def get_instance(cls):
        if not StorageFactory.__INSTANCE:
            StorageFactory()
        return StorageFactory.__INSTANCE

    def __init__(self):
        if not StorageFactory.__INSTANCE:
            StorageFactory.__INSTANCE = self
        else:
            raise Exception("This class is a singleton! Use get_instance() class method to retrieve an instance")

    def get_storage(self):
        storage = self.storages[storage_config.engine](storage_config)
        if self.storages[storage_config.engine]:
            return Storages(ArticleStorage(storage), LinkStorage(storage))
        else:
            raise AttributeError("No such storage")
