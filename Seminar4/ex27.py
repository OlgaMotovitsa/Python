# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

import string

my_text = '''She sells sea shells on the sea shore 
           The shells that she sells are sea shells I am sure.
           So she sells sea shells on the sea shore I am sure 
           that the shells are sea shore shells'''

my_text = my_text.lower()
print(my_text)

punct = list(string.punctuation) + ['\n', '\t']
print(punct)

words = my_text.split()
my_text_set = set(words)
print(my_text_set)
print(f'Количество различных слов: {len(my_text_set)}')

