import asyncio

from app.DAL import StorageFactory
from app.domain.crawler_factory import CrawlerFactory
from app.domain.resource_fetcher.http_fetcher import HTTPFetcher
from app.domain.scraper_factory import ScraperFactory
from app.domain.worker import Worker


class Task:
    def __init__(self, site, start_link):
        self.resource_fetcher = HTTPFetcher()
        self.start_link = start_link
        self.crawler = CrawlerFactory.get_instance().get_crawler(site)
        self.scraper = ScraperFactory.get_instance().get_scraper(site)
        self.scraper_worker = Worker(directive=self.scraper, fetcher=self.resource_fetcher)
        self.crawler_worker = Worker(directive=self.crawler, fetcher=self.resource_fetcher)
        self.site = site
        self.article_storage = StorageFactory.get_instance().get_storage().article_storage
        self.link_storage = StorageFactory.get_instance().get_storage().link_storage
    
    def run(self, is_async=True):
        if is_async:
            self.run_async()
        else:
            self.run_sync()

    def run_sync(self):
        with self.scraper_worker:
            links = self.crawler_worker.work(self.start_link)
            articles = [self.scraper_worker.work(link) for link in links]
            self.article_storage.save_many(articles)

    def run_async(self):
        loop = asyncio.get_event_loop()
        links = self.crawler_worker.work(self.start_link)
        results = loop.run_until_complete(asyncio.ensure_future(self.__work_links(links)))
        self.article_storage.save_many(articles=results)

    async def __work_links(self, links):
        if links:
            with self.scraper_worker:
                tasks = [asyncio.ensure_future(self.scraper_worker.work_async(link)) for link in links]
                return await asyncio.gather(*tasks)
        else:
            return None
