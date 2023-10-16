# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import pathlib


# def sort_files(path):
#     os.chdir(path)    # сменили тут директорию
#
#     ext = {} # создали после 16 строки словарь
#     for i in path.iterdir(): # проходимся по всем файлам в директории
#         if i.is_file():
#             ext[i.suffix] = ext.get(i.suffix,[]) + [i] # складываем списки
#     for key, value in ext.items(): # проходимся по всем элементам словаря
#         os.mkdir(key) # создаем директорию
#         for file in value:
#             try:
#                 file.replace(path/key/file.name)
#             except PermissionError:
#                 continue
#
#
# sort_files(pathlib.Path(r"C:\Users\Оля\OneDrive\Рабочий стол\Учеба\Python\.Seminars\Seminar7\test"))



# def sort_files(path):
#     os.chdir(path)    # сменили тут директорию
#     files = os.listdir() # вернул листом все файлы
#     ext = {} # создали после 16 строки словарь
#     for i in files: # проходимся по всем файлам в директории
#         *_, extention = i.split('.')   # *_ - сюда попадут все элементы кроме последнего, extention - расширение, все разделяется через точку
#         ext[extention] = ext.get(extention,[]) + [i] # складываем списки
#     for key, value in ext.items(): # проходимся по всем элементам словаря
#         os.mkdir(key)
#         for i in value:
#             os.replace(i, key)
#
#

def sort_files(path):
    os.chdir(path)    # сменили тут директорию
    files = os.listdir() # вернул листом все файлы
    ext = {} # создали после 16 строки словарь
    for i in files: # проходимся по всем файлам в директории
        *_, extention = i.split('.')   # *_ - сюда попадут все элементы кроме последнего, extention - расширение, все разделяется через точку
        ext[extention] = ext.get(extention,[]) + [i] # складываем списки
    for key, value in ext.items(): # проходимся по всем элементам словаря
        os.mkdir(key)
        for i in value:
            os.replace(i, f"{key}\\{i}")

sort_files(r"C:\Users\Оля\OneDrive\Рабочий стол\Учеба\Python\.Seminars\Seminar7\test")



