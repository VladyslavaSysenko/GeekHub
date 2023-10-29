# 4. Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k
# 5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)


import string


def work_with_row(row: str) -> str:
    # Return sum of all numbers and row with only letters
    if len(row) < 30:
        # Replace non number characters with space e.g. "0f12g.g1.5p -5.0k!" -> "0 12  . 1.5 -5.0  "
        str_num = "".join((ch if ch in "0123456789-." else " ") for ch in row)
        # Split string and save only numbers (e.g. skip only ".")
        list_num = []
        for i in str_num.split():
            try:
                list_num.append(float(i))
            except ValueError:
                pass
        # Delete non letters
        str_ltr = "".join((ch if ch.isalpha() else "") for ch in row)
        return f"sum = {sum(list_num)}    {str_ltr}"

    # Return len of row, amount of letters and digits
    if 29 < len(row) < 51:
        # Calculate amount of letters and digits
        letters = digits = 0
        for ch in row:
            if ch.isdigit():
                digits += 1
            elif ch.isalpha():
                letters += 1
        return f"length = {len(row)}, amount of letters = {letters} and amount of digits = {digits}"

    # Return digits or letters that are not in the row
    if len(row) > 50:
        alphabet = list(string.ascii_lowercase)
        digits = list("0123456789")
        row = row.lower()
        not_found_ltr, not_found_dgt = [], []
        # Find not used letters
        for el in alphabet:
            if row.find(el) == -1:
                not_found_ltr.append(el)
        # Find not used digits
        for el in digits:
            if row.find(el) == -1:
                not_found_dgt.append(el)
        # Return result
        letter = ", ".join(not_found_ltr) if len(not_found_ltr) != 0 else "all used!"
        digit = ", ".join(not_found_dgt) if len(not_found_dgt) != 0 else "all used!"
        return f"Not used letters: {letter}, not used digits: {digit}"


print(work_with_row(row="0f12g.gl*1.5p -5.0k!"))

print(work_with_row(row="0f12g.gl*1.5p -5.0k!g15erg50*fw/"))

print(work_with_row(row="0F1bCuV2I.gl*1.5p -5.0k!g1Zt5erg893  kskdnflkanf 8815030 50*fw/"))
print(work_with_row(row="0F1bCuV2I.gl*1.5p -5.0k!g1Zt5erg893  kskdnflkanf 815030 50*fw/467"))
print(work_with_row(row="0F1bCuV2I.gl*1.5p -5.0k!g1Zt5erg893  kskdnflkanf 815030 50*fw/hjmoqxy"))
print(work_with_row(row="0F1bCuV2I.gl*1.5p -5.0k!g1Zt5erg893  kskdnflkanf 815030 50*fw/hjmoqxy467"))
