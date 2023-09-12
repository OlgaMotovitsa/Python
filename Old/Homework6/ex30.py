# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



def Progressia (num, step, numbers):
    progressia_array = []
    for i in range (numbers):
        progressia_array.append(num + i * step)
    return progressia_array

num_1 = int(input("Введите первый элемент  "))
numbers_1 = int(input("введите количество элементов   "))
step_1 = int(input("Введите шаг  "))

result = Progressia(num_1, step_1, numbers_1)
print (result)



# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
# print(a1 + i * d)
