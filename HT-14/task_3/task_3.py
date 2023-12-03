# 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про
#    записи: цитата, автор, інфа про автора тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл


import csv

import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/"
quotes = []
authors_info = {}


def get_quotes():
    page = 1

    with open("quotes.csv", "w", encoding="utf-8", newline="") as csvfile:
        fieldnames = [
            "text",
            "author_name",
            "tags",
            "author_born_date",
            "author_born_location",
            "author_description",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Inspect all pages
        while True:
            response = requests.get(f"{URL}/page/{page}/")
            soup = BeautifulSoup(response.text, "lxml")
            soup_quotes = soup.select(".quote")

            # Save quotes from this page
            for quote in soup_quotes:
                text = quote.select_one(".text").text
                author_name = quote.select_one(".author").text
                href = quote.select_one("a")["href"]
                author_info = get_author_info(name=author_name, href=href)
                tags = [tag.text for tag in quote.select(".tag")]
                writer.writerow(
                    {
                        "text": text,
                        "author_name": author_name,
                        "tags": tags,
                        "author_born_date": author_info["born_date"],
                        "author_born_location": author_info["born_location"],
                        "author_description": author_info["description"],
                    }
                )
            print(page)
            page += 1

            # Stop if last page
            if not soup.select_one(".next"):
                break


def get_author_info(name: str, href: str):
    # Save author info if not in the dict
    author = authors_info.get(name)
    if not author:
        response = requests.get(f"{URL}/{href}")
        soup = BeautifulSoup(response.text, "lxml")

        born_date = soup.select_one(".author-born-date").text
        born_location = soup.select_one(".author-born-location").text
        description = soup.select_one(".author-description").text

        author = {
            "name": name,
            "born_date": born_date,
            "born_location": born_location,
            "description": description.strip(),
        }
        authors_info.update({name: author})
    return author


get_quotes()
