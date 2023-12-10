from dataclasses import dataclass


@dataclass
class SitemapItem:
    url: str


@dataclass
class ExtensionItem:
    id: str
    name: str
    description: str | None
