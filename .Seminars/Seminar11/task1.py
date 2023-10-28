# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import datetime
class MyStr(str):

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = datetime.datetime.now()
        return instance


a = MyStr('Hello', 'Andrey')
print(a.time,a,a.name)
b = MyStr('ghg','hghg')
print(b.time)

