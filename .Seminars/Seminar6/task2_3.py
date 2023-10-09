"""Задание №2
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь."""


from random import randint
from sys import argv # чтобы из терминала можно было код получить

__all__ = ['random_number']

def random_number(start_num: int, stop_num: int, count_try: int) -> bool:
    random_num = randint(start_num, stop_num)
    for _ in range(count_try): # проходимся по списку количество попыток, но они int и значит пишем range
        input_num = int(input("введите число: "))
        if random_num == input_num:
            return True
        elif random_num > input_num:
            print("нужное число больше ")
        else:
            print("нужное число меньше ")
    return False


if __name__ == '__main__':
    print(random_number(2,8,4))



# Задание №3
# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.

# Ниже - Это нужно для т ого чтобы запускать в терминале argv заложены в терминал принимаются через пробел и находятся в строячном типе
# from sys import argv # чтобы из терминала можно было код получить
# a, *b = argv
# b = list(map(int, b))
# print(random_number(*b))

# (venv) PS C:\Users\Оля\OneDrive\Рабочий стол\Учеба\Python\.Seminars\Seminar6\task1>
# python numbers.py 100 1000 5 - в терминале вводим
# cd..   - вернуться выше по папкам
