# 3. Використовуючи Scrapy, заходите на "https://chrome.google.com/webstore/sitemap", переходите на
# кожен лінк з тегів <loc>, з кожного лінка берете посилання на сторінки екстеншенів, парсите їх і
# зберігаєте в CSV файл ID, назву та короткий опис кожного екстеншена (пошукайте уважно де його можна взяти)

from urllib.parse import urljoin

import scrapy
from scrapy.http import Response, Request
from task_3.parsers.extensions_parser import ExtensionsParser


class ExtensionsSpider(scrapy.Spider):
    parser = ExtensionsParser()

    name = "extensions"
    start_urls = [urljoin(parser.BASE_URL, "sitemap")]

    def parse(self, response: Response):
        sitemap_items = self.parser.parse_sitemap(response_text=response.text)
        for item in sitemap_items:
            yield Request(url=item.url, callback=self.parse_location)

    def parse_location(self, response: Response):
        sitemap_items = self.parser.parse_sitemap(response_text=response.text)
        for item in sitemap_items:
            yield Request(url=item.url, callback=self.parse_extension_page)

    def parse_extension_page(self, response: Response):
        extension_info = self.parser.parse_page(response=response)
        yield {
            "id": extension_info.id,
            "name": extension_info.name,
            "description": extension_info.description,
        }
