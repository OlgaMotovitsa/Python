# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

a = 45
b = "qwerty"
c = 3.05
d = True
e = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

data = [a, b, c, d, e]     # start= 1 означает что i ачинается с 1, а не с 0 по дефолту
for n,i in enumerate(data, start= 1): # в n попадет номер порядковый, а в i - наш элемент
    print(n, i, id(i), hash(i), i.__sizeof__())
    if isinstance(i, int): # если хотим проверить все i на целое число
        print("int =", True)
    if isinstance(i, str): # если хотим проверить все i на тип строки
        print("str =", True)



# 1 45 1979891975792 45 28
# int = True
# 2 qwerty 1979893267632 183700552971323527 55
# str = True
# 3 3.05 1979893014864 115292150460684291 24
# 4 True 140717376924520 1 28
# int = True
# 5 None 140717376976888 -9223363242018714753 16

print("\t")
data = [a, b, c, d, e]
for n, i in enumerate(data, start= 1):
    if isinstance(i, int) or isinstance(i, str):
        print(n, i, id(i), hash(i), i.__sizeof__(), True)
    else:
        print(n, i, id(i), hash(i), i.__sizeof__())