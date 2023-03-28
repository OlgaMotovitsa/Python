# Задача №17.
# 
#  Решение в группах
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

import random

my_list = [random.randint(0,10) for i in range(9)]

# my_list = []
# for i in range(9):
#     my_list.append(random.randint(0, 10))

print(my_list)

           # i записывается квадратом проходя по списку значений
# my_list = [i**2 for i in range(9)]
# print(my_list)  

print(set(my_list))  # показывает уникальные значения
print(len(set(my_list)))

# [2, 7, 1, 7, 9, 0, 5, 4, 6]
# {0, 1, 2, 4, 5, 6, 7, 9}
# 8


# ответ в одну строку:
# print(len(set([random.randint(0, 10) for i in range(9)])))