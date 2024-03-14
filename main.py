from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        """Магический метод"""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __add__(self, another_point: Point) -> str:
        result_x = self.x + another_point.x
        result_y = self.y + another_point.y
        return f"({result_x}, {result_y})"

    def __sub__(self, another_point: Point) -> Point:
        result_x = self.x - another_point.x
        result_y = self.y - another_point.y
        return Point(result_x, result_y)

    def __eq__(self, another_point: Point) -> bool:
        """Если (x1 равен x2) и (y1 равен y2), вернет True, иначе False"""
        return self.x == another_point.x and self.y == another_point.y


# p1 = Point(5, 0)
# p2 = Point(10, 15)
# p4 = Point(5, 0)

# p3 = p1 - p2
# print(p3)

# print(p1 == p4)


class ComplexNumber:
    def __init__(self, real: int, img: int) -> None:
        """Создает 2 аттрибута real: int, img: int"""
        self.real = real
        self.img = img

    def __add__(self, cx: ComplexNumber) -> ComplexNumber:
        """Реальная часть складывается с реальной, воображаемая с воображаемой"""
        return ComplexNumber(self.real + cx.real, self.img + cx.img)

    def __sub__(self, cx: ComplexNumber) -> ComplexNumber:
        """Реальная часть отнимается с реальной, воображаемая с воображаемой"""
        return ComplexNumber(self.real - cx.real, self.img - cx.img)

    def __repr__(self) -> str:
        """Возвращает в формате: 5 + 7j"""
        return f"{self.real} + {self.img}j"

    def __iadd__(self, cx: ComplexNumber) -> ComplexNumber:
        """Добавляет компоненты другого объекта к компонентам объекта self и обновляет self, не создавая новый объект"""
        self.real += cx.real
        self.img += cx.img
        return self

    def __isub__(self, cx: ComplexNumber) -> ComplexNumber:
        """Вычитает компоненты другого объекта из объекта self и обновляет self, не создавая новый объект"""
        self.real -= cx.real
        self.img -= cx.img
        return self

    def __eq__(self, cx: ComplexNumber) -> bool:
        """Если (self.real равен cx.real) и (self.img равен cx.img), вернет True, иначе False"""
        return self.real == cx.real and self.img == cx.img


# __add__ +
# __sub__ -
# __iadd__ +=
# __isub__ -=
# __eq__ ==
    
cn1 = ComplexNumber(3, 5)
cn2 = ComplexNumber(2, 4)

print(cn1 + cn2)
print(cn1 - cn2)

cn1 += cn2
print(cn1)

cn1 -= cn2
print(cn1)

print(cn1 == cn2)