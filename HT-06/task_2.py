# 2. Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі
# <a> одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується
# на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються
# відсотки). Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%). Функція
# повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок).


def check_type(money: float, years: int, percents: float) -> bool:
    if not (
        isinstance(money, (int, float))
        and isinstance(years, int)
        and isinstance(percents, (int, float))
    ):
        print("Money and percents must be int or float. Years must be only int")
        return False
    if percents <= 0:
        print("Percents must be positive")
        return False
    return True


def bank(money: float, years: int, percents: float = 10) -> float:
    # Check input type
    if check_type(money=money, years=years, percents=percents):
        # Calculate money
        for _ in range(years):
            money += money * percents / 100
        print(money)
        return round(money, 2)


bank(money="ds", years=3, percents=3)
bank(money=100, years=3.3, percents=3)
bank(money=100, years=3, percents=-3)
bank(money=100, years=3, percents=3)
bank(money=100, years=3)
