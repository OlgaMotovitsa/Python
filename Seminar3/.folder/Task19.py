# Задача №19. 

# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

import random

# my_list = [random.randint(0,10) for i in range(10)]
# print(my_list)

# k = int(input('Введите число k '))
# print(k)

# k = [random.randint(0,10) for i in range(k)]
# print(k)

my_list =[i for i in range(10)] 
print(my_list)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k = int(input(' На сколько двигаем вправо '))
for i in range(k):
    temp = my_list.pop() # my_list.pop(len(my_list-1))  -- последний 
    my_list.insert(0, temp)

print(my_list)