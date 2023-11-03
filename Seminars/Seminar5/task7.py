# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

import typing

def simple_n(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# n = 100
# for i in range(2, n):
#     if simple_n(i):
#         print(i)

# или так ->

def gen_simple(n: int) -> typing.Generator:
    for i in range(2, n):
        if simple_n(i):
            yield i


# если хотим вывести 5 чисел
for i in gen_simple(100):
    print(i)

result = gen_simple(100)
for i in range(5):
    print(next(result))