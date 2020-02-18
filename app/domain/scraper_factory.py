from app.domain import get_site_name_from_package
from app.domain.sites.cnn.scraper import CNNScraper
from app.domain.sites.tutby.scraper import TutbyScraper


class ScraperFactory:
    __INSTANCE = None
    scrapers = {
        get_site_name_from_package(scraper): scraper for scraper in [
            TutbyScraper,
            CNNScraper
        ]
    }

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
        if self.scrapers[site]:
            return self.scrapers[site]()
        else:
            raise ValueError("No such site")
