'''Задание №4
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.

Задание №5
� Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.

Задание №6
� Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение'''
__all__ = ['mystery_launch', 'show_res', 'mystery']

_result = {} # 5


def mystery (mys:str, answer: list[str], count: int)-> int:
    for i in range(1, count + 1):
        user_input = input("Ответ : ")
        if user_input in answer:
            _arhive(mys, i) # 5
            return i
    _arhive(mys, 0) # 5
    return 0


def mystery_launch(count):
    mystery_box = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
                   'Не лает, не кусает, в дом не пускает': ['замок'],
                   'Сидит дед во сто шуб одет': ['лук', 'луковица'],}

    for key, value in mystery_box.items():
        print(key)
        print(mystery(key, value , count))


def _arhive(mys:str, count: int): #5
    global _result
    _result[mys] = count


def show_res():       #5
    global _result    #5
    print(_result)    #5


if __name__ == '__main__':
    count = 3
    mystery_launch(count)
    show_res()        #5

