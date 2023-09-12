# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил 
# купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз 
# потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


# from random import randint

# n = int(input('Введите кол-во арбузов для сравнения: '))
# max_arbus = 10
# min_arbus = 30

# while n != 0:
#     ves = (randint(10, 30))
#     print(ves, end =" ")
#     if ves > max_arbus:
#         max_arbus = ves
#     if ves < min_arbus:
#         min_arbus = ves
#     n -= 1

# print()
# print(f' Самый тяжелый арбуз весит {max_arbus} кг')
# print(f' Самый легкий арбуз весит {min_arbus} кг')

from random import randint
count = int(input('Введите кол арбузов: '))

min_weight = 30
max_weight = 10

for _ in range(count):  # _ - это значит неважная переменная range(0, 10 например и 10 не включительно, 1- это шаг) 10 арбузов 10 сравнений по циклу _ - это индексы!!!
    current_weight = randint(10, 30)
    print(current_weight, end = ' ')  # энд пишем чтобы все значения писались в строчку
    if min_weight > current_weight:
        min_weight = current_weight
    if max_weight < current_weight:
        max_weight = current_weight

print()
print(f'Себе {max_weight} кг, ф теще {min_weight} кг')