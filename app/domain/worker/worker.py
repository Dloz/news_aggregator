from abc import abstractmethod


class Worker:
    def __init__(self, fetcher):
        self.resource_fetcher = fetcher

    @abstractmethod
    def work(self, link):
        pass

    @abstractmethod
    async def work_async(self, link):
        pass
