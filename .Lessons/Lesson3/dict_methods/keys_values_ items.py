# Метод keys
# Метод keys возвращает объект-итератор dict_keys.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())

for key in my_dict.keys(): # можно не писать .keys():
    print(key)

# dict_keys(['one', 'two', 'three', 'four', 'ten'])
# one
# two
# three
# four
# ten

# Обычно объект не используют напрямую. Метод keys применяется в связке с
# циклом for для перебора ключей словаря.
# 🔥 Важно! Запись цикла for key in my_dict: отработает аналогично. По
# умолчанию словарь возвращает ключи для итерации в цикле.
# 💡 Внимание! В отличии от списков, кортежей и строк доступ к
# элементу-значению осуществляется не по индексу, а по ключу. При этом
# начиная с версии Python 3.7 словарь сохраняет порядок добавления ключей. В
# 30
# каком порядке ключи были добавлены, в том порядке они будут возвращены в
# случае итерации по словарю.

# Метод values
# Метод values похож на keys, но возвращает значения в виде объекта итератора
# dict_values, а не ключи.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)

# dict_values([1, 2, 3, 4, 10])
# 1
# 2
# 3
# 4
# 10

# Метод items
# Если в цикле необходимо работать одновременно с ключами и значениями, как с
# парами, используют метод items.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())
# dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('ten', 10)])

for tuple_data in my_dict.items():
    print(tuple_data)
# ('one', 1)
# ('two', 2)
# ('three', 3)
# ('four', 4)
# ('ten', 10)

for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')
# key = 'one' value before 100 - 99
# key = 'two' value before 100 - 98
# key = 'three' value before 100 - 97
# key = 'four' value before 100 - 96
# key = 'ten' value before 100 - 90

# Метод возвращает объект итератор dict_items. Если создать цикл for с одной
#     переменной между for и in, получим кортеж из пар элементов — ключа и значения.
# Обычной используют две переменные в цикле: первая принимает ключ, а вторая
# значение. Такой подход облегчает чтение кода и позволяют использовать ключ и
# значение по-отдельности.