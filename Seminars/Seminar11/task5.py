# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №2 из прошлого семинара
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rect:
    def __init__(self, lenght, width=None):
        self.lenght = lenght
        if width:
            self.width = width
        else:
            self.width = lenght

    def per(self):
        return 2 * (self.lenght + self.width)

    def sq(self):
        return self.lenght * self.width

    def __add__(self, other: "Rect"):
        if self.width == other.width:
            sum_per = self.per() + other.per()
            new_len = sum_per/2 - self.width
            return Rect(new_len, self.width)
        else:
            raise ValueError

    def __sub__(self, other: "Rect"):
        if self.width == other.width:
            sum_per = self.per() - other.per()
            new_len = sum_per/2 - self.width
            return Rect(new_len, self.width)
        else:
            raise ValueError

    def __repr__(self) -> str:
        return f"Rect({self.lenght}, {self.width})"


x1 = Rect(3, 2)
x2 = Rect(3, 2)
print(x1)
print(x2)

a = x1 - x2
print(a)








