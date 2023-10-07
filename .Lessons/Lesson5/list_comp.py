# List comprehensions
# Что будет, если генераторное выражение записать не в круглых скобках, а в
# квадратных? Получим list comprehensions. Другие названия: list comp, генератор
# списков, списковое включение. И нет, это не генераторное выражение. Генератор
# списков полностью формирует список с элементами до его присваивания
# переменной слева от знака равно.
my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)
# Как и генераторные выражения списковые включения поддерживаю несколько
# циклов и логические проверки для каждого из циклов. Можно воспринимать их как
# синтаксический сахар, более короткую запись. Например выбираем все чётные
# числа из исходного списка и складываем их в результирующий.
# Длинный код:
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')
# Аналогичное решение, но с использованием синтаксического сахара listcomp:
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')
# 1. Не создаём пустой список в начале.
# 2. Не пишем двоеточия после цикла и логической проверки.
# 3. Исключаем метод append.
# Итого вместо 4 строк кода получаем одну.


# Генераторные выражения или генерация
# списка
# В примере из раздела “генераторные выражения” мы обернули генератор
# функцией list, чтобы сохранить значения в список. Можно воспринимать это как
# антипример кода. Какой же пример является верным? Если на выходе нужен
# готовый список, оптимальным будет следующий код:
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')
# А если нам не нужны все элементы разом. Например мы в дальнейшем хотим
# перебирать значения по одному в цикле. В этом случае подойдет генераторное
# выражение без преобразования в список.
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')
# 🔥 Важно! При написании кода заранее решите нужна вам сгенерированная
# коллекция целиком или нет. Не стоит тратить память на хранение всех
# элементов, если вы ими не пользуетесь одновременно.