# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# 2 пособа

def sort_list(list_: list[int]):
    for i in range(len(list_)):
        for j in range(len(list_)-1):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]

list_ = [12, 23, 44]
sort_list(list_)
print(list_)

# [44, 23, 12]


def sort_list(list_ : list[int]):
    for i in range(len(list_)):
        for j in range(i, len(list_)):
            if list_[i]>list_[j]:
                list_[i], list_[j] = list_[j] , list_[i]

list_ = [12, 23, 44]
sort_list(list_)
print(list_)

# [12, 23, 44]