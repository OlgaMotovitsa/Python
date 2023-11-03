import json
from task3 import ErrorAccess, ErrorLevel


class Project:
    def __init__(self, file_name) -> None:
        self.users = read(file_name)
        self.admin = User(None, None,None)


    def enter(self, name, id):
        temp_user = User(name,id, None)
        if temp_user not in self.users:
            raise ErrorAccess(id, name)
        for user in self.users:
            if user == temp_user:
                self.admin = user

    def add_user(self, new_name, new_id, new_level ):
        if int(new_level) < int(self.admin.level):
            raise ErrorLevel(self.admin.level, new_level)
        self.users.add(User(new_name, new_id, new_level))


class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level

    def __repr__(self) -> str:
        return f'User({self.name}, {self.id}, {self.level})'

    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id and self.name == __value.name

    def __hash__(self) -> int:
        return hash(self.id)



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



print(read("users1.json"))
new_p = Project("users1.json")
new_p.enter("fddffd", "5")
new_p.add_user("new_user", "19", "1")

print(new_p.users)