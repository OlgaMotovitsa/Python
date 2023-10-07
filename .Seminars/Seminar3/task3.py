# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа

a = [1,2,3,'one','two','three',1.0,2.1,2.2, [1,2,1,1]]
answer = {}
for i in a:
    answer[type(i)] = answer.get(type(i), []) + [i]
    #answer[type(i)].append(i) - это и есть + [i]

print(answer)