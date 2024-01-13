import re
import subprocess
import time
from sys import stderr, stdin, stdout

from .models import Product, ScrapingTask
from .scraper import ProductScraper


def save_scraped_products(task_id: int) -> None:
    command = (
        'python manage.py shell --command="from products.services import'
        f" _save_products_details; _save_products_details({task_id})"
    )
    subprocess.run(
        command, shell=True, check=True, stdin=stdin, stdout=stdout, stderr=stderr
    )


def _save_products_details(task_id: int) -> None:
    task = ScrapingTask.objects.get(pk=task_id)
    product_ids = task.product_ids.split(",")
    for product_id in product_ids:
        scraping_result = ProductScraper(product_id).get_product_details()
        if scraping_result.success:
            product = scraping_result.product_info

            # Save product to db
            Product.objects.create(
                site_id=product.id,
                name=product.name,
                link=product.link,
                brand=product.brand,
                category=product.category,
                store=product.store,
                current_price=product.current_price,
                old_price=product.old_price,
                description=product.description,
            )
            print(f"Product {product_id} is successfully added.")
        else:
            print(
                f"Product {product_id} is not added. Error: {scraping_result.message}"
            )

        # Give time for site so that it won't block other requests
        time.sleep(0.5)

    # Delete task from db
    task.delete()


def is_valid_ids(ids: list[str]) -> bool:
    pattern = re.compile(r"^[A-Za-z0-9]+(?:,[A-Za-z0-9]+)*$")
    return bool(pattern.match(ids))
