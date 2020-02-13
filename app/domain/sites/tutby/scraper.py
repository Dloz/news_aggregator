from bs4 import BeautifulSoup

from app.domain.scraper.scraper import Scraper


class TutbyScraper(Scraper):
    SITE_NAME = "tutby"

    def scrape(self, html, link):
        soup = BeautifulSoup(html, "html.parser")
        text = self.__get_text(soup)
        title = self.__get_title(soup)
        return {
            "title": title,
            "text": text,
            "link": link,
            "site": self.SITE_NAME
        }

    def __get_title(self, soup):
        return soup.select_one('div.m_header h1').text

    def __get_text(self, soup):
        return '\n'.join([i.text for i in soup.select('div#article_body p')])
