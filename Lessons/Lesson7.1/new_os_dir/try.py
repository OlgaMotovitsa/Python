
# создали файл 'text_data.txt'
f = open('text_data.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

# <_io.TextIOWrapper name='text_data.txt' mode='r' encoding='utf-8'>
# ['Привет мир\n', 'это я']
#--------------------------------------------------

# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write('Окончание файла\n')
# f.close() # Закрытие файла гарантирует сохранение информации на носителе.

# ['Привет мир\n', 'это я.\n', 'Окончание файла\n']
#--------------------------------------------------

# f = open('bin_data', 'wb', buffering=64)
# f.write(b'X' * 1200)
# f.close()
# # создался и записался файл 'bin_data'

# f = open('bin_data', 'r', encoding='utf-8')
# print(f)
# print(list(f))

# <_io.TextIOWrapper name='bin_data' mode='r' encoding='utf-8'>
# ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

#----------------------------------------------

# errors — используется только в текстовом режиме и определяет поведение в случае
# ошибок кодирования или декодирования. Рассмотрим несколько возможных
# вариантов параметра:
# ➢ 'strict' — вызывает исключение ValueError в случае ошибки. Работает как
# значение по умолчанию.
# ➢ 'ignore' — игнорирует ошибки кодирования. При этом игнорирование ошибок
# может привести к потере данных.
# ➢ 'replace' — вставляет маркер замены (например, '?') там, где есть
# некодируемые данные.
# ➢ 'namereplace' — при записи заменяет неподдерживаемые символы
# последовательностями \N{...}.

# ----------------------------------------------------------
# f = open('data.txt', 'wb') # открывают файл для чтения и записи и удаляют старое содержимое
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()
# создали файл 'data.txt' и перезаписали в него Привет, ���!

# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# f.close()
# не смогли открыть из-за отсутствия encode('cp1251') в open

# error но делаем как ниже и читаем файл

# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()

# ['Привет, ���!']

# newline — отвечает за преобразование окончания строки
# closefd — указывает оставлять ли файловый дескриптор открытым при закрытии файла
# opener — позволяет передать пользовательскую функцию для открытия файла.
# Подробнее об этих параметрах можно прочитать в официальной документации,
# если возникнет необходимость.