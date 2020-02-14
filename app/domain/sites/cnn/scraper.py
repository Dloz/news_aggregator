import dateutil.parser
from bs4 import BeautifulSoup

from app.domain.scraper.scraper import Scraper


class CNNScraper(Scraper):
    SITE_NAME = "cnn"

    def scrape(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return {
            "title": self.__get_title(soup),
            "text": self.__get_text(soup),
            "site": self.SITE_NAME,
            "date": self.__get_date(soup)
        }

    def __get_title(self, soup):
        if soup:
            return soup.find("meta", property="og:title")["content"]
        else:
            return None

    def __get_text(self, soup):
        if soup:
            return '\n'.join([i.text for i in soup.select('section#body-text')])
        else:
            return None

    def __get_date(self, soup):
        if soup:
            date_string = None
            try:
                date_string = soup.select_one('meta[itemprop="datePublished"]') or \
                              soup.select_one('meta[name="pubdate"]')
            except TypeError:
                return None
            return dateutil.parser.parse(date_string["content"])
        else:
            return None
