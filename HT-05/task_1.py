# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде
# повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь). У випадку
# некоректного введеного значення - виводити відповідне повідомлення.


def season(month: int) -> str:
    # Error if month is not int
    if not isinstance(month, int):
        return "Month number must be integer!"
    # Error if month not 1-12
    elif month not in range(1, 13):
        return "Month numbers are 1 - 12"
    # Get season from number
    else:
        if month == 12 or month < 3:
            return "Winter"
        elif month > 2 and month < 6:
            return "Spring"
        elif month > 5 and month < 9:
            return "Summer"
        elif month > 8 and month < 12:
            return "Autumn"


print(season("cat"))
print(season(0))
print(season(1))
print(season(4))
print(season(8))
print(season(10))
