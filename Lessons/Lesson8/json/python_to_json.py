# ● Преобразование Python в JSON
# Что делать, если мы хотим превратить Словарь Python в JSON объект? Для этого
# используем функции сериализации dump и dumps. Смысл окончания s у dumps
# такой же как и у loads.

# import json
# my_dict = {
#     "first_name": "Джон",
#     "last_name": "Смит",
#             "hobbies": ["кузнечное дело", "программирование", "путешествия"],
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Алиса",
#             "age": 5
#         },
#         {
#             "first_name": "Маруся",
#             "age": 3
#         }
#     ]
# }
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f:
#     json.dump(my_dict, f)

# Создаём словарь, открываем файл для записи и сохраняем содержимое функцией
# dump. В качестве первого аргумента функция получает словарь или список, вторым
# передаем файловый дескриптор либо другой объект, поддерживающий метод write.
# Сама функция dump ничего не возвращает.

# Если мы откроем файл new_user.json, увидим одну длинную строку:
# {"first_name": "\u0414\u0436\u043e\u043d", "last_name":
# "\u0421\u043c\u0438\u0442", "hobbies":
# ["\u043a\u0443\u0437\u043d\u0435\u0447\u043d\u043e\u0435
# \u0434\u0435\u043b\u043e",
# "\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u04
# 3e\u0432\u0430\u043d\u0438\u0435",
# "\u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u04
# 4f"], "age": 35, "children": [{"first_name":
# "\u0410\u043b\u0438\u0441\u0430", "age": 5}, {"first_name":
# "\u041c\u0430\u0440\u0443\u0441\u044f", "age": 3}]}

# Как вы видите символы отличные от ASCII были заменены на специальные коды.
# Это не означает, что файл повреждён или что-то пошло не так. Проведём
# десериализацию уже знакомым способом и проверим целостность данных.

# import json
#
# with open('new_user.json', 'r', encoding='utf-8') as f:
#     new_dict = json.load(f)
# print(f'{new_dict = }')
# ______________________________________________________________

# Если же мы хотим отказаться от символов экранирования в JSON файле, следует
# установить дополнительный параметр ensure_ascii в значение ложь.
# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False) - смотри пример ниже
# Воспользуемся словарём my_dict ещё раз для проверки функции dumps

import json
my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
            "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)

#  все в файле нью юзер стало на русском

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# type(dict_to_json_text) = <class 'str'>
# dict_to_json_text = '{"first_name": "\\u0414\\u0436\\u043e\\u043d", "last_name": "\\u0421\\u043c\\u04...
# type(dict_to_json_text) = <class 'str'>
# dict_to_json_text = '{"first_name": "Джон", "last_name": "Смит", "hobbies": ["кузнечное дело", "пр...

# На выходе получаем объект типа str хранящий структуру json. Подобные данные мы
# видели в сохранённом файле.
