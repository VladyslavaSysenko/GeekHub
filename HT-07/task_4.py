# 4. Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить
#    декодоване значення (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensetive (на ваш розсуд - велики чи маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не
#       будуть. Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)
#     Приклад:
#     --. . . -.- .... ..- -...   .. ...   .... . .-. .
#     результат: GEEKHUB IS HERE


def is_str(value) -> bool:
    return isinstance(value, str)


# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "SOS": "...---...",
}


def morse_code(row: str) -> str:
    # Check input type
    if not is_str(row):
        return "Morse coded row must be string"

    # Decode row
    result = ""
    words = row.split("   ")
    words_letters = [word.split() for word in words]
    for word in words_letters:
        for morse_letter in word:
            # Search for letter in dict and add to result
            for letter, code in MORSE_CODE_DICT.items():
                if morse_letter == code:
                    result += letter
                    break
            # Error if letter is not in morse code
            else:
                return f"{morse_letter} is not in morse code letters"
        # Add space between words
        result += " "
    return result


print(morse_code(row="--. . . -.- .... ..- -...   .. ...   .... . .-. ."))
print(morse_code(row="--. . . -.- .... ..- -...   .. ...   .... . .-----------. ."))
print(morse_code(row="...---..."))
