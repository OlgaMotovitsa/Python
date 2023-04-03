#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint

def CheckValue (arr, mn, mx):
    for i in range (len(arr)):
        if mn <= arr[i] <= mx:
           print (f"Индекс элемента внутри указанных границ: ",i)

len_list = int(input("Введите длину списка: "))
my_list = []
for j in range (len_list):
    my_list.append(randint(0,10))
print (*my_list)

min_value= int(input("введите минимальное число: "))
max_value = int(input("Введите максимальное число: "))

CheckValue (my_list, min_value, max_value)