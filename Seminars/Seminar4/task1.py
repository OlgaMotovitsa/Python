# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

n = input()
def str_text(n):
    a = sorted(n.split())
    max_len = 0
    for el in a:
        if len(el) > max_len:
            max_len = len(el)

    for n, el in enumerate(a, start= 1):
        print(f'{n} {el:>{max_len}}')
        return
    # jmsfkjw fmjwfjwfkjfwl wj