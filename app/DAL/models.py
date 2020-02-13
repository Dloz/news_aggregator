import json


class Article:
    """
    Represents article content
    """
    # Model storage is a content storage of specific db type
    # (for SQL databases - Table, for NoSQl - column, key-value etc.)
    MODEL_STORAGE_NAME = 'article'

    def __init__(self, site, title, text, link):
        self.site = site
        self.title = title
        self.text = text
        self.link = link

    @staticmethod
    def from_dict(article):
        return Article(site=article["site"], title=article["title"], text=article["text"], link=article["link"])

    def to_dict(self):
        return {
            "site": self.site,
            "title": self.title,
            "text": self.text,
            "link": self.link
        }


class Link:
    """
    Represents navigation, pages, categories and other links
    """
    # Model storage is a content storage of specific db type
    # (for SQL databases - Table, for NoSQl - column, document etc.)
    MODEL_STORAGE_NAME = 'link'

    def __init__(self, site, link):
        self.site = site
        self.link = link

    @staticmethod
    def from_dict(link):
        return Link(site=link["site"], link=link["link"])

    def to_dict(self):
        return {
            "site": self.site,
            "link": self.link
        }
