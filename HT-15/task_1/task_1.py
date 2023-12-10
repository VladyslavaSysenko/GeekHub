# 1. Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту
# https://www.sears.com і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані
# (бренд, категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад, якщо категорія
# має ID 12345, то файл буде називатись 12345_products.csv)
# Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184


import csv
import time

import requests
from requests import Response


def get_category_items(id: int) -> None:

    with open(f"{id}_products.csv", "w", encoding="utf-8", newline="") as csvfile:
        fieldnames = ["brand", "name", "old_price", "new_price", "store"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Set items range for one request
        start_index = 1
        end_index = 200

        while True:
            print(f"Getting items from {start_index} to {end_index}")
            response = get_response(start_index=start_index, end_index=end_index, id=id)

            # Check if error
            try:
                response.raise_for_status()
            except Exception as e:
                print(
                    "You have reached the end of the category or something went wrong. Check the"
                    " csv file."
                )
                print(f"Error: {e}")
                break

            # Save items to csv
            category_items = response.json().get("items")
            for item in category_items:
                writer.writerow(
                    {
                        "brand": item.get("brandName"),
                        "name": item.get("name"),
                        "old_price": item.get("additionalAttributes").get("cutPrice"),
                        "new_price": item.get("additionalAttributes").get("displayPrice"),
                        "store": item.get("additionalAttributes").get("storeOrigin")[0],
                    }
                )
            start_index += 200
            end_index += 200
            time.sleep(2)


def get_response(start_index: int, end_index: int, id: int) -> Response:
    headers = {
        "authority": "www.sears.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
        "authorization": "SEARS",
        "content-type": "application/json",
    }
    response = requests.get(
        f"https://www.sears.com/api/sal/v3/products/search?startIndex={start_index}&endIndex={end_index}&searchType=category"
        f"&catalogId=12605&store=Sears&storeId=10153&filterValueLimit=500&catGroupId={id}",
        headers=headers,
    )
    return response


# get_category_items(id=1100113)
get_category_items(id=1021346)
