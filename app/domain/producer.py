import asyncio


class Producer:
    def __init__(self, queue, crawler_worker):
        self.queue = queue
        self.crawler_worker = crawler_worker

    async def produce(self, link):
        result = await self.crawler_worker.work_async(link)
        for link in result:
            await self.queue.put(link)
            print(f'produced {link}')
