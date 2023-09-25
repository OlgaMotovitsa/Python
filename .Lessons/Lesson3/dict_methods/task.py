# Задание
# Перед вами словарь и несколько строк кода. Напишите что вернёт каждая из строк.
# Попробуйте справится с заданием без запуска кода. У вас 3 минуты.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['four']
print(my_dict)

# 10
# dict_values([1, 2, 3, 4, 10])
# 1
# {'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'one': 4}