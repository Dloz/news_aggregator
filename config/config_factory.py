from app.PL.api.config import Config
from config.config_reader import ConfigReader
from config import storage_config
from config.config_models.storage_config import StorageConfig


class ConfigFactory:
    __INSTANCE = None
    SITE_PROPERTY = 'site'
    START_LINK_PROPERTY = 'start_link'
    PAUSE_DURATION_PROPERTY = 'pause_duration'
    CHUNK_SIZE_PROPERTY = 'chunk_size'
    config_reader = ConfigReader()

    @classmethod
    def get_instance(cls):
        if not ConfigFactory.__INSTANCE:
            ConfigFactory()
        return ConfigFactory.__INSTANCE

    def __init__(self):
        if not ConfigFactory.__INSTANCE:
            ConfigFactory.__INSTANCE = self
        else:
            raise Exception("This class is a singleton! Use get_instance() class method to retrieve an instance")

    def get_config(self, config):
        site = config.get(self.SITE_PROPERTY, None)
        start_link = config.get(self.START_LINK_PROPERTY, None)
        pause_duration = config.get(self.PAUSE_DURATION_PROPERTY, None)
        chunk_size = config.get(self.CHUNK_SIZE_PROPERTY, None)
        return Config(site, start_link, pause_duration, chunk_size)

    def get_storage_config(self):
        return StorageConfig.from_dict(data=storage_config)
