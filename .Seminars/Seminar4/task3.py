# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def func(a: str) -> dict[str, int]:
    new_dict = {}
    a = a.split()
    for i in range(int(a[0]),int(a[1]) ):
        new_dict[chr(i)] = i
    return new_dict

a = "110 223"
print((func(a)))

# def func(a: str) -> dict[str, int]:
#     new_dict = {}
# start, stop = map(int, a.split())
# for i in range(start, stop):
#     new_dict[chr(i)] = i
# return new_dict
#
#
# a = "110 123"
# print(func(a))