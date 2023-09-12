# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


import random

list_1 = list()
n = int(input("Введите количество элементов в списке  "))
n = range(n)
count = 0

for i in n:
    i = random.randint(1, 10)
    list_1.append(i)
print(list_1)

min_1 = list_1[0]
max_1 = list_1[0]

for i in range(len(list_1)):
    if min_1 > list_1[i]:
        min_1 = list_1[i]
    if max_1 < list_1[1]:
        max_1 = list_1[i]

print(f'{min_1} and {max_1}')

for i in range(len(list_1)):
    if max_1 == list_1[i]:
        list_1[i] = min_1

print(list_1)