# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters

def remove_char(text):
    new_text = []
    for el in text.lower():
        if el in ascii_letters + ' ':
            new_text.append(el)
    return ''.join(new_text)

print(remove_char('hfh@@dj shsjsJJGG'))


