# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде
# повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь). У випадку
# некоректного введеного значення - виводити відповідне повідомлення.


def season(month: int) -> str:
    seasons = {
        "Winter": [12, 1, 2],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11],
    }
    # Error if month is not int
    if not isinstance(month, int):
        return "Month number must be integer!"
    # Error if month not 1-12
    elif month not in range(1, 13):
        return "Month numbers are 1 - 12"
    # Get season from number
    else:
        for season, value in seasons.items():
            if month in value:
                return season


print(season("cat"))
print(season(0))
print(season(1))
print(season(4))
print(season(8))
print(season(10))
