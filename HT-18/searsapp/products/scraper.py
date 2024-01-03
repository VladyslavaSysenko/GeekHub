import requests
from requests import Response

from .custom_dataclasses import Product, ScrapingResult


class ProductScraper:
    """Class for scraping product from https://www.sears.com/ using product id"""

    def __init__(self, id: str) -> None:
        self.id = id

    def get_product_details(self) -> ScrapingResult:
        response = self.__get_product_page()

        # Check if error
        try:
            response.raise_for_status()
        except Exception as e:
            return ScrapingResult(success=False, message=f"{e}")

        # Get item from response
        item = response.json().get("productDetail").get("softhardProductdetails")[0]
        product = Product(
            id=item.get("partNum"),
            name=item.get("descriptionName"),
            link="https://www.sears.com" + item.get("seoUrl"),
            brand=item.get("brandName"),
            category=item.get("hierarchies").get("specificHierarchy")[-1].get("name"),
            store=(
                item.get("defaultSeller").get("soldBy") if item.get("defaultSeller") else "Sears"
            ),
            current_price=item.get("salePrice"),
            old_price=item.get("regularPrice"),
            description=item.get("shortDescription"),
        )
        return ScrapingResult(
            success=True, message="Product details successfully scraped.", product_info=product
        )

    def __get_product_page(self) -> Response:
        headers = {
            "authority": "www.sears.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
            "authorization": "SEARS",
            "content-type": "application/json",
        }

        params = {"storeName": "Sears"}

        response = requests.get(
            f"https://www.sears.com/api/sal/v3/products/details/{self.id}",
            params=params,
            headers=headers,
        )
        return response
