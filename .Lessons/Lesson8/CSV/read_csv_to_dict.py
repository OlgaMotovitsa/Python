# ● Чтение в словарь
# import csv
#
# csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"], restkey="new", restval="Main office")

# fieldnames - список заголовков столбцов, ключей словаря
# restkey -  значение ключа для столбцов, которых нет в fieldnames
# restval -  значение поля для ключей fieldnames, которых нет в файле Csv



# Помимо сохранения таблицы в список можно использовать для хранения словарь.
# Ключи словаря — названия столбцов, значения — очередная строка файла CSV.
# Прочитаем файл biostats_tab.csv из примера выше, но не в список, а в словарь.
# Воспользуемся классом DictReader.

# import csv
#
# with open('biostats_tab.csv', 'r', newline="") as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"], restkey="new", restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')

# Если передать список строк в параметр fieldnames, они будут использоваться для
# ключей словаря, а не первая строка файла. В нашем примере передан “лишний”
# ключ count. Т.к. в таблице нет шестого столбца, ему было присвоено значение из
# параметра restval.
# import csv
# with open('biostats_tab.csv', 'r', newline='') as f:
# csv_file = csv.DictReader(f, fieldnames=["name", "sex",
# "age", ], restkey="new", restval="Main Office",
# dialect='excel-tab',
# quoting=csv.QUOTE_NONNUMERIC)
# for line in csv_file:
# print(f'{line = }')
# print(f'{line["name"] = }\t{line["age"] = }')
# 15
# Если количество ключей оказывается меньше, чем столбцов, недостающий ключ
# берётся из параметра restkey. При этом все столбцы без ключа сохраняются как
# элементы списка в restkey ключ.

# -----------------------------------
# Если передать список строк в параметр fieldnames, они будут использоваться для
# ключей словаря, а не первая строка файла. В нашем примере передан “лишний”
# ключ count. Т.к. в таблице нет шестого столбца, ему было присвоено значение из
# параметра restval.

import csv
with open('biostats.csv', 'r', newline='') as f: # в лекции надо открывать biostats_tab.csv  и ниже писать dialect='excel-tab'  но так не работает
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office", dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# Если количество ключей оказывается меньше, чем столбцов, недостающий ключ
# берётся из параметра restkey. При этом все столбцы без ключа сохраняются как
# элементы списка в restkey ключ.
