import time

from app.domain.task import Task

if __name__ == '__main__':
    import sys
    from config import site_config

    args = sys.argv[1:]
    if args:
        for site in site_config.keys():
            if site in args:
                task = Task(site=site, start_link=site_config[site])
                start = time.time()
                task.run()
                end = time.time()
                print("Async time: ", end - start)
    else:
        if not site_config:
            raise AttributeError("Wrong config!")

        for site in site_config.keys():
            task = Task(site=site, start_link=site_config[site])
            start = time.time()
            task.run()
            end = time.time()
            print("Async time: ", end - start)
