# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
# які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession (його
# не має інсувати під час ініціалізації).


class Person:
    def __init__(self, *, name=None, age=None) -> None:
        self.age = age
        self.name = name

    def show_age(self) -> None:
        print(f"age: {self.age}")

    def show_name(self) -> None:
        print(f"name: {self.name}")

    def show_all_information(self) -> None:
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


student1 = Person(name="Kate", age=20)
student1.profession = "Chemist"
student1.show_age()
student1.show_name()
student1.show_all_information()

student1 = Person(name="Bob", age=43)
student1.profession = "Artist"
student1.show_age()
student1.show_name()
student1.show_all_information()
