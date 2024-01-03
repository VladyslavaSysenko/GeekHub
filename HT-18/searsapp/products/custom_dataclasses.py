from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    link: str
    brand: str
    category: str
    store: str
    current_price: int
    old_price: int
    description: str | None = None


@dataclass
class ScrapingResult:
    success: bool
    message: str | None = None
    product_info: Product | None = None
