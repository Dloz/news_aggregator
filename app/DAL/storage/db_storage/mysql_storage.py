import mysql.connector

from app.DAL.storage.abstract_storage import AbstractStorage


class MysqlStorage(AbstractStorage):

    def __init__(self, storage_config):
        self.db = mysql.connector.connect(
            host=storage_config.host,
            port=storage_config.port,
            user=storage_config.user,
            password=storage_config.password,
            database=storage_config.database
        )

    def store(self, model):
        pass

    def store_many(self, models):
        pass

    def __pagination(self, page, page_size, col_name):
        pass

    def cleanup(self, col_name):
        pass
