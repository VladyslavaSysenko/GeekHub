# 2. Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/"
# (з ним будьте обережні), і парсите список  доменів. Всі отримані значення зберігти в CSV файл.


import csv
import random
import time

import requests
from bs4 import BeautifulSoup
from requests import Response


def get_domains() -> None:
    domain_num = 0

    with open("domains.csv", "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["domain_name"])

        while True:
            print(f"Get domain names from {domain_num} to {domain_num + 25}")
            response = get_response(domain_num=domain_num)
            soup = BeautifulSoup(response.text, "lxml")

            if not soup.select_one(".field_domain"):
                print("You have reached the end or you were blocked. Check the csv file")
                break

            domains = soup.select(".field_domain")
            writer.writerows([[domain.text] for domain in domains])
            domain_num += 25
            time.sleep(random.uniform(5, 15))


def get_response(domain_num: int) -> Response:
    headers = {
        "authority": "www.expireddomains.net",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent": (
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like"
            " Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        ),
    }
    params = {"start": domain_num}
    response = requests.get(
        "https://www.expireddomains.net/expired-domains/", params=params, headers=headers
    )
    return response


get_domains()
