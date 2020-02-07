class ScraperFactory:

    @classmethod
    def get_instance(cls):
        if not ScraperFactory.__INSTANCE:
            ScraperFactory()
        return ScraperFactory.__INSTANCE

    def __init__(self):
        if not ScraperFactory.__INSTANCE:
            ScraperFactory.__INSTANCE = self
        else:
            raise Exception("This class is a singleton! Use get_instance() class method to retrieve an instance")

    def get_scraper(self, site):
        pass
