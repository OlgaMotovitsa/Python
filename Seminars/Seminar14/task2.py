# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters

def remove_char(text):
    """
    >>> remove_char("qwerty")
    'qwerty'
    >>> remove_char("qwerTTTy")
    'qwerttty'
    >>> remove_char("qwert,!y")
    'qwerty'
    >>> remove_char("qwertыв")
    'qwert'
    >>> remove_char("qwerTы,вy")
    'qwerty'
    """

    new_text = []
    for el in text.lower():
        if el in ascii_letters + ' ':
            new_text.append(el)
    return ''.join(new_text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()




