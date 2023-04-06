import random

rand_list = [random.randint(0, 100) for _ in range(10)]
print(rand_list)
# [16, 94, 65, 59, 38, 40, 32, 51, 1, 29]

for i in range(len(rand_list)):
    print(i)
# проходимся по индексам всех элементов в рандомном массиве и выписываем их
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(len(rand_list)):
    print(i, rand_list[i])
# выводим индексы и рядом их значения
# 0 16
# 1 94
# 2 65
# 3 59
# 4 38
# 5 40
# 6 32
# 7 51
# 8 1
# 9 29

# все это сверху сложно =>
for i in enumerate(rand_list):
    print(i)
# (0, 36)
# (1, 9)
# (2, 54)
# (3, 23)
# (4, 74)
# (5, 49)
# (6, 20)
# (7, 63)
# (8, 13)
# (9, 28)
    
for i, item in enumerate(rand_list):
    print(i, item)
# 0 39
# 1 67
# 2 78
# 3 44
# 4 62
# 5 24
# 6 36
# 7 5
# 8 49
# 9 58

for i, item in enumerate(rand_list, 1):  # список с 1
    print(i, item)

# 1 65
# 2 11
# 3 90
# 4 56
# 5 96
# 6 73
# 7 85
# 8 96
# 9 41
# 10 84

rand_list1 = [random.randint(0, 100) for _ in range(15)]
print(rand_list1)
# [89, 55, 31, 28, 3, 20, 44, 54, 33, 83, 60, 50, 77, 88, 97]

letter_list = list('shfioshf')
print(letter_list)
#['s', 'h', 'f', 'i', 'o', 's', 'h', 'f']

new_list = list(zip(rand_list1, letter_list))
print(new_list)
# [(89, 's'), (55, 'h'), (31, 'f'), (28, 'i'), (3, 'o'), (20, 's'), (44, 'h'), (54, 'f')]