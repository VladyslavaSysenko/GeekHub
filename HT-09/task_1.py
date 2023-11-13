# 1. Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран
# виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора. Кожну 1
# секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка
# така сама як і в звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
#    Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green

import time


def is_int(*args) -> None:
    if not all(isinstance(value, int) for value in args):
        raise TypeError("Seconds for car light must be int.")


def traffic_light(green: int = 5, yellow: int = 1, red: int = 3):
    is_int(green, yellow, red)

    # Calculate and store seconds for each light
    gr_yel = green + yellow
    gr_yel_red = gr_yel + red
    lights = [
        {"car_light": "Green", "ped_light": "Red", "seconds": range(0, green + 1)},
        {"car_light": "Yellow", "ped_light": "Red", "seconds": range(green + 1, gr_yel + 1)},
        {"car_light": "Red", "ped_light": "Green", "seconds": range(gr_yel + 1, gr_yel_red + 1)},
    ]

    while True:
        for second in range(1, sum([green, yellow, red]) + 1):
            for light in lights:
                if second in light["seconds"]:
                    print(f'{light["car_light"]:15}{light["ped_light"]}')
                    time.sleep(1)
                    break


# traffic_light(5, "s", 6)
# traffic_light()
# traffic_light(4, 2, 3)
