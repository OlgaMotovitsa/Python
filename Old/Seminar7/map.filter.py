import random


# map
# filter
# zip
# enumerate
# lambda

# my_list = list(map(func, list)) # на место func мы подставляем какую-то функцию, 
#                                 на место list какой-то список, 
#                                 и эта функция будет применена к каждому элементу  этого списка list 
#                                 и результат будет записан в качестве списка в наш список my_list

my_list = '123456789'
print(my_list)
# 123456789
my_list = list(my_list)
print(my_list)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# for i in range(len(my_list)):    это и есть map
#     my_list[i] = int(my_list[i])

my_list = list(map(int, my_list)) # вместо лист можно положить set tuple главное указать перед мэп какой-то тип данных
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


new_list = list(map(lambda x: x**2, my_list)) # x - это все значения по очереди перебираются
#                                              потом что мы делаем с каждым значением 
                                            # и после запятой - откуда мы их берем
print(new_list)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

new1_list = list(map(lambda x: x == 2, my_list)) 
print(new1_list)
# [False, True, False, False, False, False, False, False, False]

new2_list = list(filter(lambda x: x % 2 == 0, my_list)) # если x % 2 == 0 возвращает труе то этот элемент записываем в новый список
print(new2_list)
# [2, 4, 6, 8]

print(sum(my_list))
# 45


# Вытащить отсюда буквы
my4_list = '1234wjhfhiqjoidjoiqv057dkdnvhd56789'
my4_list = list(my4_list)
print(my4_list)
# ['1', '2', '3', '4', 'w', 'j', 'h', 'f', 'h', 'i', 'q', 'j', 'o', 'i', 'd', 'j', 'o', 'i', 'q', 'v', '0', '5', '7', 'd', 'k', 'd', 'n', 'v', 'h', 'd', '5', '6', '7', '8', '9']

new_list = list(filter(lambda x: x.isdigit(), my4_list))
print(new_list)
# ['1', '2', '3', '4', '0', '5', '7', '5', '6', '7', '8', '9']


# Выписать все гласные из списка my4_list
new_list = list(filter(lambda x: x in 'euioa', my4_list))
print(new_list)
# ['i', 'o', 'i', 'o', 'i']





# 123456789
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# [False, True, False, False, False, False, False, False, False]
# [2, 4, 6, 8]
# 45
# ['1', '2', '3', '4', 'w', 'j', 'h', 'f', 'h', 'i', 'q', 'j', 'o', 'i', 'd', 'j', 'o', 'i', 'q', 'v', '0', '5', '7', 'd', 'k', 'd', 'n', 'v', 'h', 'd', '5', '6', '7', '8', '9']
# ['1', '2', '3', '4', '0', '5', '7', '5', '6', '7', '8', '9']
# ['i', 'o', 'i', 'o', 'i']