import dateutil.parser
from bs4 import BeautifulSoup

from app.domain.scraper.scraper import Scraper


class TutbyScraper(Scraper):
    SITE_NAME = "tutby"

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
            headline = soup.select_one('h1[itemprop="headline"]')
            if headline:
                return headline.text
            else:
                return None
        else:
            return None

    def __get_text(self, soup):
        if soup:
            return '\n'.join([i.text for i in soup.select('div#article_body p')])
        else:
            return None

    def __get_date(self, soup):
        if soup:
            date_string = None
            try:
                date_string = soup.select_one('time[itemprop="datePublished"]')["datetime"]
            except TypeError:
                return None
            return dateutil.parser.parse(date_string)
        else:
            return None
