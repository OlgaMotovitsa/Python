# сделать попытку на изменение свойства, получим ошибку.
# ● Getter
# Декоратор property позволяет создавать “геттеры”. Это методы, которые выдают
# себя за свойства, позволяют прочитать результат, но блокируют возможность
# записи. Рассмотрим другой пример “геттера”.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


user = User('Стивен', 'Спилберг')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
# user.full_name = 'Стивен Хокинг' # AttributeError: can't set attribute 'full_name'
user.last_name = 'Хокинг'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }\n')

# Теперь у пользователя есть два публичных свойства для имени и фамилии. Кроме
# того есть свойство (а не метод) для вывода полного имени, т.е. с фамилией. Все три
# свойства работают на чтение. А вот перезаписать полное имя мы не можем. Зато
# ничего не мешает изменить фамилию и получить обновлённое полное имя.
# ● Setter
# Python позволяет к “геттеру” добавить “сеттер” — метод контролирующий
# изменение свойства. Добавим пользователю возраст и будем контролировать
# чтобы новый возраст был больше старого. Например мы вручную обновляем
# данные раз в 5-10 лет.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')


user = User('Стивен', 'Спилберг')
user.age = 75
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошёл один год.')
user.age = 76
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.\n')
# user.age = 25 # ValueError: Новый возраст должен быть больше
# текущего: 76

# Что получилось:
# 1. защёщенное свойство _age получает значение ноль при рождении
# экземпляра, в дандер __init__
# 2. используя декоратор property создали свойство age для чтения текущего
# возраста
# 3. создаём “сеттер” для контроля записи новых значений в свойство _age
# ➢ применяем декоратор @age.setter. Имя между @ и точкой должно
# совпадать с именем “геттера”.
# ➢ методу присваиваем такое же имя как и у свойства и он должен
# принимать значения помимо self
# ➢ внутри метода делаем проверку на увеличения возраста
# ➢ если возраст увеличивается, обновляем свойство _age
# ➢ если возраст не увеличился вызываем ошибку ValueError и сообщаем
# её причину
# 4. В основном коде запросто увеличиваем возраст пользователя, но не можем
# его уменьшить.
# При создании “сеттера” не обязательно вызывать ошибки. В целом внутри может
# быть прописана любая логика. Например вы работает с финансовой программой и
# присваиваете новую сумму денег. “Сеттер” будет приводить сумму к типу Decimal
# перед присваиванием.


# ● Deleter
# Помимо “геттера” и “сеттера” можно создать “делейтер”. Он выполняется при
# вызове команды del для свойства. Один из возможных вариантов использования
# “делейтера” - заменять значение на какое-то по умолчанию или помечать элемент
# 14
# скрытым вместо удаления.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
    @age.deleter
    def age(self):
        self._age = 0


user = User('Стивен', 'Спилберг')
user.age = 75
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло много лет. Изобретена технология перерождения.')
del user.age
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')

# Создание “делейтера” аналогично “сеттеру”. Также используется декоратор с
# именем свойства, но после точки пишем deleter. Внутри метода прописываются
# действия для удаления.