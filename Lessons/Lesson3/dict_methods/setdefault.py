# Метод setdefault
# Метод setdefault похож не get, но отсутствующий ключ добавляется в словарь.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
# spam = None	my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None}

eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
# eggs = 6	my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None, 'six': 6}

new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
# new_spam=2	my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None, 'six': 6}

new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')
# new_eggs=1	my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None, 'six': 6}






# При вызове метода с одним аргументом отсутствующий ключ добавляется в
# словарь. В качестве значения передаётся None. Если указать два аргумента и ключ
# отсутствует, второй аргумент становится значением ключа и также добавляется в
# словарь. При обращении к существующему ключу, словарь не изменяется
# независимо от того указанные один или два аргумента.