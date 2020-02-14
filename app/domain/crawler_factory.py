from app.DAL import StorageFactory
from app.domain import get_site_name_from_package
from app.domain.sites.cnn.crawler import CNNCrawler
from app.domain.sites.tutby.crawler import TutbyCrawler


class CrawlerFactory:
    __INSTANCE = None
    crawlers = {
        get_site_name_from_package(crawler): crawler for crawler in [
            TutbyCrawler,
            CNNCrawler
        ]
    }
    storage_factory = StorageFactory.get_instance()

    @classmethod
    def get_instance(cls):
        if not CrawlerFactory.__INSTANCE:
            CrawlerFactory()
        return CrawlerFactory.__INSTANCE

    def __init__(self):
        if not CrawlerFactory.__INSTANCE:
            CrawlerFactory.__INSTANCE = self
        else:
            raise Exception("This class is a singleton! Use get_instance() class method to retrieve an instance")

    def get_crawler(self, site):
        if self.crawlers[site]:
            return self.crawlers[site]()
        else:
            raise AttributeError("No such site")
