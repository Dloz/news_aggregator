from abc import abstractmethod


class Worker:
    def __init__(self, fetcher):
        self.resource_fetcher = fetcher

    def __enter__(self):
        pass

    @abstractmethod
    def work(self, link):
        pass

    @abstractmethod
    async def work_async(self, link):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resource_fetcher.__exit__()
