# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей




# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json

class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level

    def __repr__(self) -> str:
        return f'User({self.name}, {self.id}, {self.level})'

def read(file_name):
    new_set = set()
    with open(file_name, "r") as f:
        data = json.load(f)
    for level, user in data.items():
        for id, name in user.items():
            new_set.add(User(name, id, level))
    return new_set

def data(name: str, id: str, level: str, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}}
    users[level][id] = name
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)


def request(file_name):
    while True:
        name = input("Введите имя: ")
        id = input("Введите ид: ")
        level = input("Введите уровень доступа: ")
        data(name, id, level, file_name)


# request("users1.json")
print(read("users1.json"))


# data('name1', '11', '2', 'users.json')
# data('name2', '12', '1', 'users.json')
# data('name3', '13', '6', 'users.json')