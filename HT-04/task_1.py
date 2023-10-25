# 1. Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# a. Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в
# float, а якщо і там ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі
# навчання для цього використати цикл while)
# b. Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і
# виводить відповідне повідомлення


while True:
    # User input
    num_1 = input("Write first number:")
    num_2 = input("Write second number:")
    res_num = []
    for num in [num_1, num_2]:
        # Check if num is int
        try:
            num = int(num)
        except ValueError:
            # Check if num is float
            try:
                num = float(num)
            except ValueError:
                print("Your number(s) is not int or float. Try again!")
                break
        # Save correct nums
        finally:
            res_num.append(num)

    # Divide numbers if both int/float
    if len(res_num) == 2:
        try:
            divis = res_num[0] / res_num[1]
        except ZeroDivisionError as e:
            print("Error!", e)
        else:
            print(f"{res_num[0]} / {res_num[1]} = {divis}")
        finally:
            break
