# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from random import randint


class Person:
    def __init__(self, name, second_name, patronymic, age):
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic
        self.__age = age

    def birthday(self):
        self.__age += 1

    def fio(self):
        return f"{self.name} {self.second_name} {self.patronymic} {self.__age}"


class Employee(Person):
    def __init__(self, name, second_name, patronymic, age):
        super().__init__(name, second_name, patronymic, age)
        self.id = randint(100_000, 999_999)
        self.lvl = self.id % 7


person1 = Employee("ivan", "ivanov", "ivanovich", 444)
print(person1.fio(), person1.id, person1.lvl)
person1.birthday()
print(person1.fio(), person1.id, person1.lvl)


