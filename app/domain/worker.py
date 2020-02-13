class Worker:
    def __init__(self, directive, fetcher):
        self.scraper = directive
        self.fetcher = fetcher

    def work(self, link):
        html = None
        if link:
            html = self.fetcher.fetch(link)
        if html is not None:
            return self.directive.scrape(html, link)
        else:
            raise Exception("html was not fetched")

    async def work_async(self, link):
        html = None
        if link:
            html = await self.fetcher.fetch_async(link)
        return self.directive.scrape(html=html, link=link)  # todo: scrape or crawl method execution

    def __exit__(self):
        self.fetcher.close()
