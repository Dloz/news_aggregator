from bs4 import BeautifulSoup


class TutbyCrawler:
    SITE_NAME = "tutby"

    def fetch_categories(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return [link['href'] for link in soup.select("ul.b-nav-list li a[href]") if
                'http' in link['href'] and not 'archive' in link[
                    'href']]  # excluded archive links to simplify the project

    def fetch_article_page_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return [link['href'] for link in soup.select("div.news-entry a[href]")
                if 'http' in link['href']
                and 'tut.by' in link['href']
                and not 'tag' in link['href']
                and not 'kupi.tut.by' in link['href']
                and not 'help.blog.tut.by' in link['href']
                and not 'afisha.tut.by' in link['href']]
