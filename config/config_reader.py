import json


class ConfigReader:
    def read_config(self, filename):
        return self._read_config(filename)

    def _read_config(self, filename):
        try:
            with open(filename, encoding='utf-8') as file:
                return json.loads(file.read())
        except ValueError:
            print('Config is not valid. Check for trailing commas!')
            raise
