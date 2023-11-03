import os
import sys


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


def test_width():
    r = Rectangle(width=5)
    assert r.width == 5


def test_height():
    r = Rectangle(width=3, height=4)
    assert r.height == 4


def test_perimeter():
    r = Rectangle(width=5)
    assert r.perimeter() == 20


def test_area():
    r = Rectangle(width=3, height=4)
    assert r.area() == 12


def test_addition():
    r1 = Rectangle(width=5)
    r2 = Rectangle(width=3, height=4)
    r3 = r1 + r2
    assert r3.width == 8
    assert r3.height == 9.0


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(width=-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(width=5, height=-4)


def test_set_width():
    r = Rectangle(width=5)
    r.width = 10
    assert r.width == 10


def test_set_negative_width():
    r = Rectangle(width=5)
    with pytest.raises(NegativeValueError):
        r.width = -10


def test_set_height():
    r = Rectangle(width=5)
    r.height = 6
    assert r.height == 6


def test_set_negative_height():
    r = Rectangle(width=5)
    with pytest.raises(NegativeValueError):
        r.height = -6


def test_subtraction():
    r1 = Rectangle(width=10)
    r2 = Rectangle(width=3, height=4)
    r3 = r1 - r2
    assert r3.width == 7
    assert r3.height == 6.0


def test_subtraction_negative_result():
    r2 = Rectangle(width=10)
    r1 = Rectangle(width=3, height=4)
    with pytest.raises(NegativeValueError):
        r1 - r2


def test_subtraction_same_perimeter():
    r1 = Rectangle(width=5)
    r2 = Rectangle(width=3, height=4)
    r3 = r1 - r2
    assert r3.width == 2
    assert r3.height == 1.0

    pytest.main(["--no-header", '-q', "--durations=0", new_filename])

import warnings

warnings.filterwarnings('ignore')


# Введите ваше решение ниже
import pytest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


def test_width():
    r = Rectangle(width=5)
    assert r.width == 5


def test_height():
    r = Rectangle(width=3, height=4)
    assert r.height == 4


def test_perimeter():
    r = Rectangle(width=5)
    assert r.perimeter() == 20


def test_area():
    r = Rectangle(width=3, height=4)
    assert r.area() == 12


def test_addition():
    r1 = Rectangle(width=5)
    r2 = Rectangle(width=3, height=4)
    r3 = r1 + r2
    assert r3.width == 8
    assert r3.height == 9.0


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(width=-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(width=5, height=-4)


def test_set_width():
    r = Rectangle(width=5)
    r.width = 10
    assert r.width == 10


def test_set_negative_width():
    r = Rectangle(width=5)
    with pytest.raises(NegativeValueError):
        r.width = -10


def test_set_height():
    r = Rectangle(width=5)
    r.height = 6
    assert r.height == 6


def test_set_negative_height():
    r = Rectangle(width=5)
    with pytest.raises(NegativeValueError):
        r.height = -6


def test_subtraction():
    r1 = Rectangle(width=10)
    r2 = Rectangle(width=3, height=4)
    r3 = r1 - r2
    assert r3.width == 7
    assert r3.height == 6.0


def test_subtraction_negative_result():
    r2 = Rectangle(width=10)
    r1 = Rectangle(width=3, height=4)
    with pytest.raises(NegativeValueError):
        r1 - r2


def test_subtraction_same_perimeter():
    r1 = Rectangle(width=5)
    r2 = Rectangle(width=3, height=4)
    r3 = r1 - r2
    assert r3.width == 2
    assert r3.height == 1.0




