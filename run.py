import asyncio
import time
from app.domain.task import Task

if __name__ == '__main__':

    from config import site_config

    if not site_config:
        raise AttributeError("Wrong config!")
    task = Task(site="tutby", start_link=site_config["tutby"])
    start = time.time()
    task.run_async()
    end = time.time()
    print("Async time: ", end - start)
