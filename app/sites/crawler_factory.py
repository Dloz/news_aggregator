from .tutby.crawler import TutbyCrawler


def get_site_name_from_package(crawler):
    return crawler.__module__.split('.')[0]


class CrawlerFactory:
    __INSTANCE = None
    crawlers = {
        get_site_name_from_package(crawler) for crawler in [
            TutbyCrawler,
        ]
    }

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
        pass
