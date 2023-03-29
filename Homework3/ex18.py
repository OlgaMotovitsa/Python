# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint

N = int(input('Введите число длины массива '))
print(N)

my_list = [randint(1, 10) for i in range(N)]
print (my_list)

X = int(input ("Введите число, к которому будем искать ближайшее: "))

tempDiff = 0
minDiff = 0
result = 1

for i in range (N):
    if my_list[i] > X:
        tempDiff = (my_list[i] - X)
        minDiff = my_list[i]
    else:
        tempDiff = (X - my_list[i])
        minDiff = my_list[i]
        if tempDiff < minDiff:
            minDiff = tempDiff
            result = my_list[i]
print(result)