import argparse
import asyncio
import logging
import time

from app.domain.task import Task

LOG_FILE_PATH = '/home/INTEXSOFT/dmitry.lozovik/PycharmProjects/news_aggregator/news.log'


def work_site(site):
    loop = asyncio.get_event_loop()
    logging.info("Start")
    task = Task(site=site, start_link=site_config[site])
    start = time.time()
    task.run()
    end = time.time()
    logging.info(f"Async time: {end - start}")
    print(f"Async time: {end - start}")


if __name__ == '__main__':
    from config import site_config

    with open(LOG_FILE_PATH, 'w'):
        pass

    logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO,
                        format='[%(asctime)s] [%(levelname)s] - %(message)s')
    parser = argparse.ArgumentParser()
    parser.add_argument('site')
    args = parser.parse_args()
    site = args.site
    if args:
        if site in site_config.keys():
            work_site(site)
    else:
        if not site_config:
            raise ValueError("Wrong config!")

        for site in site_config.keys():
            work_site(site)
