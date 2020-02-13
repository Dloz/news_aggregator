import os
from .config_reader import ConfigReader
from config.config_models.storage_config import StorageConfig

basedir = os.path.abspath(os.path.dirname(__file__))

app_config = None
storage_config = None
site_config = None
try:
    reader = ConfigReader()
    app_config = reader.read_config(basedir + r'/config_files/app_config.json')
    site_config = reader.read_config(basedir + r'/config_files/available_sites.json')
    storage_config = StorageConfig.from_dict(reader.read_config(basedir + r'/config_files/storage_config.json'))

except Exception as e:
    print(e)
