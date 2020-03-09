from bs4 import BeautifulSoup


class CNNCrawler:
    SITE_NAME = "cnn"
    ROOT_LINK = "https://edition.cnn.com"

    def fetch_categories(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return [self.ROOT_LINK + link["href"] for link in
                soup.select("ul.nav-linksstyles__NavLinkList-sc-1tike8v-2.jJWZwe li a[href]")]

    def fetch_article_page_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # base_uri = soup.find("meta", property="og:url")["content"]
        # for link in soup.select("article a[href]"):
        #     l = base_uri + link['href']
        return [self.ROOT_LINK + link['href'] if 'http' not in link['href'] else link['href']
                for link in soup.select("article a[href]") if 'index.html' in link['href']]
