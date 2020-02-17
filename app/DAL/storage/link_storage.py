from app.DAL.models import Link


class LinkStorage:
    COLUMN_NAME = "link"

    def __init__(self, storage):
        self.storage = storage

    def save(self, link, site):
        if site and link:
            self.storage.store(Link(site=site, link=link))
        else:
            raise AttributeError("Wrong data")

    def save_many(self, links, site):
        if links and site:
            self.storage.store_many([Link(site=site, link=link) for link in links])
        else:
            raise AttributeError("Wrong data")

    def read(self):
        return self.storage.read(self.COLUMN_NAME)
