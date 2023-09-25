# Работа со строками как с массивами
# Начнём с квадратных скобок.

text = 'Hello world!'
print(text[6])
print(text[3:7])
# w
# lo w

# Индексы и срезы работают аналогично спискам.
# Если необходимо заменить элемент новым, индексы не подойдут. Для этих целей
# нужен метод replace

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')
# Hello world!
# HeLLo world!

# Первый аргумент — подстрока, которую нужно заменить.
# Второй аргумент — подстрока, на которую нужно заменить.
# Третий аргумент — максимальное количество замен. Если его не указывать, будут
# заменены все совпадения.