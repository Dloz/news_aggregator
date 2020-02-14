from app.domain.worker.worker import Worker


class ScraperWorker(Worker):
    def __init__(self, scraper, fetcher):
        self.scraper = scraper
        super().__init__(fetcher)

    def work(self, link):
        html = None
        if link:
            print(f"Requesting: {link}")
            html = self.resource_fetcher.fetch(link)
        if html is not None:
            print(f"Parsing: {link}")
            data = self.scraper.scrape(html)
            data["link"] = link
            return data
        else:
            pass
            #raise Exception("html was not fetched")

    async def work_async(self, link):
        html = None
        if link:
            print(f"Requesting: {link}")
            html = await self.resource_fetcher.fetch_async(link)
        if html is not None:
            print(f"Parsing: {link}")
            data = self.scraper.scrape(html=html)
            data["link"] = link
            return data
        else:
            print("HTML was not fetched")
