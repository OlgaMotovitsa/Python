
# Запись CSV из словаря
# import csv
# ● Параметры класса DictWriter аналогичны параметрам DictReader
# ● csv_write.writeheader()
# сохранение первой строки с заголовками в порядке их
# перечисления в параметре fieldnames
# ● csv_write.writerow(line)
# сохранение списка в одной строке файла в формате CSV
# ● csv_write.writerows(all_data)
# сохранение матрицы в нескольких строках файла в формате CSV

# Для записи содержимого словаря в CSV используют класс DictWriter. Его параметры
# схожи с рассмотренными выше параметрами DictReader.
import csv

from typing import Iterator
with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('biostats_new1.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read: Iterator[dict] = csv.DictReader(f_read,
                        fieldnames=["name", "sex", "age", "height", "weight", "office"], restval="Main Office",
                        dialect='excel-tab',
                        quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
                        dialect='excel-tab',
                        quoting=csv.QUOTE_ALL)
    csv_write.writeheader()
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)
    csv_write.writerows(all_data)

# Класс DictWriter получил список полей для записи, где добавлено новое поле id. В
# качестве диалекта выбран excel с табуляцией. В параметре quoting указали, что все
# значения стоит заключать в кавычки.
# Новый для нас метод writeheader сохранил первую строку с заголовками в том
# порядке, в котором мы их перечислили в параметре fieldnames. Далее мы работаем
# с элементами словаря и формируем список словарей для одноразовой записи в
# файл.

# 🔥 Важно! Обратите внимание на импорт объекта Iterator из модуля typing.
# При написании кода IDE подсвечивала возможные ошибки, так как не
# понимала что за объект csv_read. Запись csv_read: Iterator[dict] = … сообщает,
# что мы используем объект итератор, который возвращает словари. После
# уточнения типа IDE исключила подсветку “ошибок”.
