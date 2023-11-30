# 1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим
# значенням white і метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат»
# (Square) містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.


class Figure:
    def __init__(self, color="white") -> None:
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Oval(Figure):
    def __init__(self, small_radius: float, big_radius: float) -> None:
        super().__init__()
        self.small_radius = small_radius
        self.big_radius = big_radius


class Square(Figure):
    def __init__(self, side: float) -> None:
        super().__init__()
        self.side = side


f = Figure()
print(f.color)

oval = Oval(5, 10)
oval.color = "fff"
print(oval.small_radius, oval.big_radius, oval.color)

square = Square(6)
print(square.side, square.color)
square.color = "black"
print(square.color)
