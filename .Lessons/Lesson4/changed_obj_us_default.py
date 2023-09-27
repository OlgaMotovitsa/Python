# Изменяемый объект как значение
# по умолчанию
# В качестве значения по умолчанию нельзя указывать изменяемы типы: списки,
# словари и т.п. Это приведёт к неожиданным результатам:

def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')

# new_list = [1, 2, 3, 4, 5]
# other_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]

# other_list содержит в себе и новую последовательность и ту, которая была в списке
# new_list. Связано это с тем, что значение по умолчанию задаётся один раз при
# создании функции. Каждый вызов — работа со списком data и его очередное
# изменение.
# Если в качестве значения по умолчанию нужен изменяемый тип данных,
# используют особый приём с None
def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')

# new_list = [1, 2, 3, 4, 5]
# other_list = [1, 2, 3, 4, 5, 6, 7]
# Если изменяемый объект не передан, он создаётся по новой для каждого вызова
# функции.
