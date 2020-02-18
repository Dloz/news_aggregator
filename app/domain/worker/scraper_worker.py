import logging
from app.domain.worker.worker import Worker


class ScraperWorker(Worker):
    def __init__(self, scraper, fetcher):
        self.scraper = scraper
        super().__init__(fetcher)

    def work(self, link):
        html = None
        if link:
            logging.info(f"Requesting: {link}")
            html = self.resource_fetcher.fetch(link)
        if html is not None:
            logging.info(f"Parsing: {link}")
            data = self.scraper.scrape(html)
            data["link"] = link
            return data
        else:
            logging.info("HTML was not fetched")

    async def work_async(self, link):
        html = None
        if link:
            logging.info(f"Requesting: {link}")
            html = await self.resource_fetcher.fetch_async(link)
        if html is not None:
            logging.info(f"Parsing: {link}")
            data = self.scraper.scrape(html=html)
            data["link"] = link
            logging.info(f"Got {data}")
            return data
        else:
            logging.info("HTML was not fetched")
            return None
