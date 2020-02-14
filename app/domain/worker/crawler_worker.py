import asyncio

from app.domain.worker.worker import Worker


class CrawlerWorker(Worker):
    def __init__(self, crawler, fetcher):
        self.crawler = crawler
        super().__init__(fetcher)

    def work(self, link):
        html = self.resource_fetcher.fetch(link)
        categories = self.crawler.fetch_categories(html)
        # set used to store unique links
        links = set()
        for category in categories:
            page_links = self.crawler.fetch_article_page_links(self.resource_fetcher.fetch(category))
            links.update(page_links)
        return list(links)

    async def work_async(self, link):
        html = await self.resource_fetcher.fetch_async(link)
        categories = self.crawler.fetch_categories(html)
        tasks = []
        for category in categories:
            tasks.append(asyncio.ensure_future(
                self.crawler.fetch_article_page_links(self.resource_fetcher.fetch_async(category))))
        links = await asyncio.gather(*tasks)
        return list(set(links))  # remove duplicates
