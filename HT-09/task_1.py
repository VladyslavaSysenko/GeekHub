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


def print_light(car_light: str, seconds: int):
    # Print car and pedestrian light every 1 second
    for _ in range(0, seconds):
        ped_light = "Green" if car_light == "Red" else "Red"
        print(f"{car_light:15}{ped_light}")
        time.sleep(1)


def traffic_light(green: int = 5, yellow: int = 1, red: int = 3):
    is_int(green, yellow, red)

    # Store order of lights for cars
    lights = [
        {"car_light": "Green", "seconds": green},
        {"car_light": "Yellow", "seconds": yellow},
        {"car_light": "Red", "seconds": red},
        {"car_light": "Yellow", "seconds": yellow},
    ]

    while True:
        for light in lights:
            print_light(light["car_light"], light["seconds"])


# traffic_light(5, "s", 6)
# traffic_light()
# traffic_light(4, 2, 3)
