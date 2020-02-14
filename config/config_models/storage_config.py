class StorageConfig:
    def __init__(self, engine, host, port, username, password, database):
        self.engine = engine
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    @staticmethod
    def from_dict(data):
        engine = data.get('engine', None)
        host = data.get('host', None)
        port = data.get('port', None)
        username = data.get('username', None)
        password = data.get('password', None)
        database = data.get('database', None)
        return StorageConfig(engine=engine, host=host, port=port, username=username, password=password,
                             database=database)

    def get_uri(self):
        if self.username:
            return f"{self.engine}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        else:
            return f"{self.engine}://{self.host}:{self.port}/{self.database}"
