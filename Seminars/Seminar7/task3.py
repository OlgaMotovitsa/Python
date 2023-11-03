# Задание №3
# 1 ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# 2 ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# 3 ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# 4 ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# 5 ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# 6 ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from task1 import rnd_num
from task2 import rnd_name_in_file


def same_len_list(list1, list2):         # 6 ✔   # 5 ✔
    if len(list2) > len(list1):          # уравняли списки разной длины
        temp = len(list1)               # в короткий список добавили элементы чтобы длины списков были равнры
        for i in range(len(list2)):
            if i > len(list1) - 1:
                list1.append(list1[i % temp])

    elif len(list2) < len(list1):
        temp = len(list2)
        for i in range(len(list1)):
            if i > len(list2) - 1:
                list2.append(list2[i % temp])

    return list1, list2


def open_file(file_names, file_numbers, output):
    with (
        open(file_names, 'r') as a,
        open(file_numbers, 'r') as b,
        open(output, 'w') as c      # 2 ✔
    ):
        names = a.read().split('\n')
        numbers = b.read().split('\n')
        for i, j in zip(*same_len_list(names, numbers)): # i отвечает за документ нэймз, а j за намберс
            if j == '':
                continue
            first, second = map(float, j.split('|')) # -606 /534.9075576751452 эти 2 числа привели к флоту и разделили строку на эти 2 числа
            mult = first * second # 2 ✔
            if mult < 0:
                c.write(f'{i.lower()} {abs(mult)}\n')   # 3 ✔
            elif mult > 0:
                c.write(f'{i.upper()} {int(mult)}\n')   # 4 ✔


if __name__ == '__main__':
    # list2 = [1,5,6]
    # list1 = [1,2,3,4,5,6,7,8,9,9]
    # print(same_len_list(list1, list2))
    rnd_num(10, 'numbers1.txt')
    rnd_name_in_file(5, 'names1.txt')
    open_file('names1.txt', 'numbers1.txt', 'output') # 2 ✔
