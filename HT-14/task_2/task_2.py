# 2. Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева
#   дати, продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному
#   інтервалі)
# - не забудьте перевірку на валідність введених даних

import requests
import re
from datetime import date, datetime


def currency_rate():
    print("\nОтримання курсу валют по відношенню до гривні за день або за період.", end="\n\n")

    while True:
        code = input("Напишіть код валюти (Натисніть 1 щоб побачити усі доступні): ").upper()
        print("")
        # Show available currencies
        if code == "1":
            currencies = get_available_currencies()
            print("Код: Назва")
            print("-" * 30)
            for code, name in currencies.items():
                print(f"{code}: {name}")
            print("")
            continue
        # Check currency code
        else:
            if not is_available_code(code=code):
                print("Неправильний код валюти", end="\n\n")
                continue

        while True:
            inp = input(
                "Курс за один день: напишіть дату у форматі дд.мм.рррр\n"
                "Курс за кожен день інтервалу: напишіть дату у форматі дд.мм.рррр-дд.мм.рррр\n"
            )
            print("")
            # Get date
            if "-" not in inp:
                try:
                    date_str = re.match(pattern=r"\d{2}.\d{2}.\d{4}$", string=inp)[0]
                    start_date = end_date = datetime.strptime(date_str, "%d.%m.%Y").date()
                except TypeError:
                    print("Дата повинна бути у форматі дд.мм.рррр або дд.мм.рррр-дд.мм.рррр\n")
                    continue
                except ValueError:
                    print("Неправильна дата, перевірте дані.\n")
                    continue

            # Get interval
            else:
                interval_str = re.match(
                    pattern=r"(\d{2}\.\d{2}\.\d{4})-(\d{2}\.\d{2}\.\d{4})$", string=inp
                )
                try:
                    start_date_str, end_date_str = interval_str.groups()
                    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
                    end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()
                except AttributeError:
                    print("Дата повинна бути у форматі дд.мм.рррр або дд.мм.рррр-дд.мм.рррр\n")
                    continue
                except ValueError:
                    print("Неправильна дата, перевірте дані.\n")
                    continue
                if not start_date < end_date:
                    print("Дата початку інтервалу має бути менше дати кінця інтервалу.\n")
                    continue

            # Print rates
            rates = get_date_s_rate(code=code, start_date=start_date, end_date=end_date)
            if not rates:
                print("Немає інформації")
            else:
                print(f"{code}/UAH Дата: Курс")
                for day, rate in rates.items():
                    print(f"  {day}: {rate}")
            break
        break


def get_available_currencies() -> dict[str, str]:
    """Get available currencies in bank.gov.ua. Returns {Code:Name, ...}"""
    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    currencies = {currency["cc"]: currency["txt"] for currency in response.json()}
    return currencies


def is_available_code(code: str) -> bool:
    """Check if available currency code in bank.gov.ua"""
    return code in get_available_currencies()


def get_date_s_rate(code: str, start_date: date, end_date: date = None) -> dict[str, float]:
    """Get rate Code/UAH for date or for each day of interval from bank.gov.ua.
    Returns {'day':rate,...}"""
    start_date = start_date.strftime("%Y%m%d")
    end_date = end_date.strftime("%Y%m%d")
    response = requests.get(
        f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={code}&sort=exchangedate&json"
    ).json()
    return {day["exchangedate"]: day["rate"] for day in response}


currency_rate()
