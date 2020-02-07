import json


class ConfigReader():
    def read_config(self, filename):
        return self._read_config(filename, DbConfigFactory.get_instance())

    def _read_config(self, filename, config_factory):
        try:
            with open(filename, encoding='utf-8') as file:
                config = json.loads(file.read())
            return config_factory.get_config(config)
        except ValueError:
            print('Config is not valid. Check for trailing commas!')
            raise
