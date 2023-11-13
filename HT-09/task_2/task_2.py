# 2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл
# також додайте в репозиторій. На екран повинен вивестись список із трьома блоками - символи з
# початку, із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому
# параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є
# в файлі або, наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на
# місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує.
#    В репозиторій додайте і ті файли, по яким робили тести.
#    Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл,
#    а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість. В разі
#    необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
#    Наприклад:
#    █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
#                      ⏫ центр

#    █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
#                      ⏫ центр


def check_type(file_path: str, num_symbols: int, round_to_top: bool):
    if not isinstance(file_path, str):
        return "File_path must be string."
    elif not isinstance(num_symbols, int):
        return "Num_symbols must be integer."
    elif not isinstance(round_to_top, bool):
        return "Round_to_top must be boolean."
    return False


def correct_length(len_text: int, num_symbols: int) -> bool:
    if num_symbols > len_text:
        return False
    return True


def file_symbols(file_path: str, num_symbols: int, round_to_top: bool = True):
    """
    For cases when amount of symbols in text and amount of needed symbols are one odd and one
    even, you need to use round_to_top argument. For example,
    If round_to_top = True: in text '123456789' and amount of symbols = 2  middle will be '456'
    If round_to_top = False: in text '123456789' and amount of symbols = 2  middle will be '5'
    """

    # Check for correct argument types
    error = check_type(file_path=file_path, num_symbols=num_symbols, round_to_top=round_to_top)
    if error:
        return error

    try:
        with open(file_path) as f:
            text = f.read()
            len_text = len(text)
            # Check if num_symbols is less than text length
            if not correct_length(len_text=len_text, num_symbols=num_symbols):
                return "Num_symbols must be equal or less than text length."
            # Amount of symbols in text and amount of needed symbols are both odd or even
            if (len_text + num_symbols) % 2 == 0:
                mid_sym_idx = num_symbols / 2
            # Amount of symbols in text and amount of needed symbols are one odd and one even
            else:
                mid_sym_idx = (num_symbols + 1) / 2 if round_to_top else (num_symbols - 1) / 2
            mid_el_idx = len_text / 2
            # Get sumbols based on indexes
            result = {
                "Start": text[:num_symbols],
                "Middle": text[int(mid_el_idx - mid_sym_idx) : int(mid_el_idx + mid_sym_idx)],
                "End": text[-num_symbols:],
            }
            return [result["Start"], result["Middle"], result["End"]]
    except FileNotFoundError:
        return f"File with path '{file_path}' not found."


print(file_symbols(file_path="correct.txt", num_symbols=3))
print(file_symbols(file_path="correct_odd.txt", num_symbols="3"))
print(file_symbols(file_path="correct_odd.txt", num_symbols=20))

print(file_symbols(file_path="correct_odd.txt", num_symbols=3))
print(file_symbols(file_path="correct_even.txt", num_symbols=4))
print(file_symbols(file_path="correct_odd.txt", num_symbols=2))
print(file_symbols(file_path="correct_odd.txt", num_symbols=2, round_to_top=False))
print(file_symbols(file_path="correct_even.txt", num_symbols=3))
print(file_symbols(file_path="correct_even.txt", num_symbols=3, round_to_top=False))
