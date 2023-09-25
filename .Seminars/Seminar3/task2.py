# Задание №3
# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

n = input()
if n.isdigit():
    print(int(n))
if "." in n:
    if "-" in n:
        n = n.replace('-','')
        flag = True
    left, right = n.split('.')
    if left.isdigit() and right.isdigit():
        if flag:
            print(-float(n))
        else:
            print(float(n))
if n != n.lower():
    print(n.lower())
else:
    print(n.upper())

