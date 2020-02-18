from app.data_access.storage.storage_factory import StorageFactory

article_storage = StorageFactory.get_instance().get_storage().article_storage

