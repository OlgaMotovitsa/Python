# Задача №23. 

# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

import random

my_list = [random.randint(0,10) for i in range(5)]
print(my_list)

count = 0
for i in range(1,len(my_list)):
    if my_list[i] > my_list[i-1]:
        count +=1
print(count)


# my_list = [1,2,3,4,5]
# for i in range(1, len(my_list)):
#     print(i)