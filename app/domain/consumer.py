import asyncio


class Consumer:
    def __init__(self, queue, scraper_worker):
        self.queue = queue
        self.scraper_worker = scraper_worker

    async def consume(self):
        while True:
            link = await self.queue.get()
            data = await self.scraper_worker.work_async(link)
            self.queue.task_done()
            print(f"consumed {data}")
