# 9. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки
# в цьому проміжку (границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100,
# а також якщо він кратний 400.

# User input
first_year = int(input("First year:"))
last_year = int(input("Last year:"))

# Get leap years
print(f"Leap years from {first_year} to {last_year}:")
for year in range(first_year, last_year + 1):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(year)
