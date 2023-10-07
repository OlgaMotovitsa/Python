# ● Множественное присваивание
# Если несколько переменных должны получить одинаковые значение, можно
# объединить несколько строк в одну.
a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')
# Подобная запись допустима только с неизменяемыми типами данных. В противном
# случае изменение одной переменной приведёт к изменению и других.
a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')
# Другой вариант множественного присваивания похож на обмен переменных
# местами.

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')
# Число элементов в левой части должно совпадать с числом элементов справа от
# равно.
# А если в левой части указать лишь одну переменную, получим кортеж.
t = 1, 2, 3
print(f'{t=}, {type(t)}')
# 🔥 Важно! Тип объектов может отличаться. Не только целые числа, как в
# примерах. Строки, любые коллекции. Ошибки это не вызовет. Но для
# повышения читаемости рекомендуется не смешивать разные типы данных при
# присваивании одной строкой.
# ● Множественное сравнение
# Аналогично присваиванию можно сравнить несколько переменных внутри
# конструкции if.
a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')
# Запись становится короче, т.к. исключается команда and внутри сравнения.
# Работает подобная запись не только с проверкой на равенство, но и с другими
# операциями.
if a < b < c:
    print('b больше a и меньше c')
# Проверяем, что b больше a и b меньше c.
