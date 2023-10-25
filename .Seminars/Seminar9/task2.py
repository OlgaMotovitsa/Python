# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию - угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

import random
from functools import wraps


def game_decor(func: callable):
    # def wrapper(*args,**kwargs):
    @wraps(func)
    def wrapper(rnd_num, count_try):

        if not 1 <= rnd_num <= 100:
            rnd_num = random.randint(1,100)
            if not 1 <= count_try <= 10:
                count_try = random.randint(1, 10)
        result = func(rnd_num, count_try)
        return result
    return wrapper


@game_decor
def guess(rnd_num, count_try):
    for i in range(count_try):
        input_num = int(input("введите число: "))
        if input_num > rnd_num:
            print('число должно быть меньше')
        elif input_num < rnd_num:
            print('число должно быть больше')
        else:
            print(rnd_num)
            return 'это загаданное число'
    return 'не угадано'

if __name__ == '__main__':
    guess(101,6)
