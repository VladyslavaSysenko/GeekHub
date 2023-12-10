from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from task_3.dataclasses.extensions_dataclasses import SitemapItem, ExtensionItem
from scrapy.http import Response


class ExtensionsParser:
    BASE_URL = "https://chrome.google.com/webstore/"

    def parse_sitemap(self, response_text: str) -> list[SitemapItem]:
        soup = BeautifulSoup(response_text, "lxml")
        return [SitemapItem(element.text) for element in soup.findAll("loc")]

    def parse_page(self, response: Response) -> ExtensionItem:
        soup = BeautifulSoup(response.text, "lxml")
        id = urlsplit(response.url).path.split("/")[-1]
        name = soup.find("meta", property="og:title").get("content")
        try:
            description = soup.find("meta", property="og:description").get("content")
        except AttributeError:
            description = None
        return ExtensionItem(id=id, name=name, description=description)
