import asyncio

from app.data_access.storage.storage_factory import StorageFactory
from app.domain.crawler_factory import CrawlerFactory
from app.domain.resource_fetcher.http_fetcher import HTTPFetcher
from app.domain.scraper_factory import ScraperFactory
from app.domain.worker.crawler_worker import CrawlerWorker
from app.domain.worker.scraper_worker import ScraperWorker


class Task:
    def __init__(self, site, start_link):
        self.resource_fetcher = HTTPFetcher()
        self.start_link = start_link
        self.crawler = CrawlerFactory.get_instance().get_crawler(site)
        self.scraper = ScraperFactory.get_instance().get_scraper(site)
        self.scraper_worker = ScraperWorker(scraper=self.scraper, fetcher=self.resource_fetcher)
        self.crawler_worker = CrawlerWorker(crawler=self.crawler, fetcher=self.resource_fetcher)
        self.site = site
        self.article_storage = StorageFactory.get_instance().get_storage().article_storage
        self.link_storage = StorageFactory.get_instance().get_storage().link_storage

    def run(self, is_async=True):
        if is_async:
            self.__run_async()
        else:
            self.__run_sync()

    def __run_sync(self):
        links = self.crawler_worker.work(self.start_link)
        self.link_storage.save_many(links, self.site)
        articles = [self.scraper_worker.work(link) for link in links]
        self.article_storage.save_many(articles)

    def __run_async(self):
        loop = asyncio.get_event_loop()
        links = self.crawler_worker.work(self.start_link)
        results = loop.run_until_complete(asyncio.ensure_future(self.__work_links(links)))
        self.article_storage.save_many(articles=results)

    async def __work_links(self, links):
        if links:
            tasks = [asyncio.ensure_future(self.scraper_worker.work_async(link)) for link in links]
            result = await asyncio.gather(*tasks)
            return [article for article in result if article]
        else:
            return None
