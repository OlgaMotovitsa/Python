# Менеджер контекста with open
# Если после открытия файла в коде возникнет ошибка, строка f.close() не будет
# выполнена. В результате ресурсы не освободятся, возможно возникнут проблемы в
# работе с открываемым файлом. Чтобы избежать подобных ошибок используют
# менеджер контекста with.

# with open('text_data.txt', 'r+', encoding='utf-8') as f:
#     print(list(f))
#     print(f.write('Пока')) # ValueError: I/O operation on closed file.

# В отличии от прошлых примеров с open вместо присвоения “f =” в начале строки
# используем “as f:” в конце строки. Вложенный в with блок кода позволяет работать с
# файлом через файловый дескриптор f. При завершении вложенного блока
# происходит автоматическое закрытие файла. При этом даже в случае ошибки
# внутри блока сначала будет закрыт файл, а только потом произведено аварийное
# завершение программы.
# Обычно вариант написания кода с менеджером контекста with предпочтительнее,
# чем напрямую с open. Но если вам надо одновременно работать с несколькими
# файлами, вариант с open позволит избежать нескольких уровней вложенности. В
# этом случае не стоит забывать про закрытие всех файлов.
#
#
# Однако менеджер контекста позволяет одновременно открыть несколько файлов
# следующим образом:

with (
        open('text_data.txt', 'r+', encoding='utf-8') as f1,
        open('bin_data', 'rb') as f2,
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
):

    print(list(f1))
    print(list(f2))
    print(list(f3))

# ['Привет мир\n', 'это я.\n', 'Окончание файла\n', 'Пока']
# [b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
# ['Привет, \\xec\\xe8\\xf0!']


# Обратите внимание на запятые между open. И при переносе кода на новую строку
# обязательно указывать обратную косую черту (бэкслеш). Так Python поймёт, что это
# одна длинная строка с переносами, а не несколько отдельных.
# Начиная с Python 3.10 менеджер контекста поддерживает круглые скобки для
# группировки нескольких операторов по строкам:


