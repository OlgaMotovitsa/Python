# Задача №39. Решение в группах
# Даны два списка чисел. Требуется вывести те элементы
# первого списка (в том порядке, в каком они идут в первом
# списке), которых нет во втором списке. Пользователь вводит 
# число N - количество элементов в первом списке, затем N
# чисел - элементы списке. Затем число M - количество
# элементов во втором списке. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


import random

# list_1 = list()
# n = int(input("Введите количество элементов в списке: "))
# n = range(n)
# count = 0

# for i in n:
#     i = random.randint(1, 10)
#     list_1.append(i)
# print(list_1)

# list_2 = list()
# n = int(input("Введите количество элементов в списке: "))
# n = range(n)
# count = 0

# for i in n:
#     i = random.randint(1, 10)
#     list_2.append(i)
# print(list_2)






# def gen_list(n):
#     list_1 = [random.randint(0, 20) for i in range(n)]
#     return list_1

# a = int (input("Введите количество элементов в списке 1: "))
# list_1 = gen_list(a)
# print(list_1)

# b = int (input("Введите количество элементов в списке 2: "))
# list_2 = gen_list(b)
# print(list_2)

# for i in list_1:
#     for j in list_2:
#         if i != j:
#             list_3 = list()
#             list_3.append(i)
# print(list_3)

import random

list_1 = [random.randint(1, 20) for _ in range(int (input("Введите количество элементов в списке 1: ")))]
list_2 = [random.randint(1, 20) for _ in range(int (input("Введите количество элементов в списке 2: ")))]
print(list_1)
print(list_2)

final_list = []

for item in list_1:
    if not item in list_2:
        final_list.append(item)

print(final_list)