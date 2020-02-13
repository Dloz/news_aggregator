from bs4 import BeautifulSoup

from app.domain.crawler.crawler import Crawler


class TutbyCrawler(Crawler):
    SITE_NAME = "tutby"

    def crawl(self, link, limit=None):
        html = self.resource_fetcher.fetch(link)
        categories = self.__fetch_categories(html)
        # set used to store unique links
        links = set()
        for category in categories:
            page_links = self.__fetch_article_page_links(self.resource_fetcher.fetch(category))
            links.update(page_links)
        return list(links)

    def __fetch_categories(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return [link['href'] for link in soup.select("ul.b-nav-list li a[href]") if
                'http' in link['href'] and not 'archive' in link[
                    'href']]  # excluded archive links to simplify the project

    def __fetch_article_page_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return [link['href'] for link in soup.select("div.news-entry a[href]")
                if 'http' in link['href']
                and 'tut.by' in link['href']
                and not 'tag' in link['href']
                and not 'kupi.tut.by' in link['href']
                and not 'help.blog.tut.by' in link['href']
                and not 'afisha.tut.by' in link['href']]
