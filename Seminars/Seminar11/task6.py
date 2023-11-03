# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self, other: "Rect"):
        return self.sq() == other.sq()

    def __gt__(self, other: "Rect"):
        return self.sq() > other.sq()

    def __lt__(self, other: "Rect"):
        return self.sq() < other.sq()

    def __repr__(self) -> str:
        return f"Rect({self.lenght}, {self.width})"


x1 = Rect(3, 2)
x2 = Rect(3, 2)
print(x1)
print(x2)
print(x1.per(), x1.sq())
print(x2.per(), x2.sq())
a = x1 - x2
print(a)
one = Rect(3)
two = Rect(4)
print(one == two)
print(one > two)
print(one < two)







