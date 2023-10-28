

# Атрибуты класса и экземпляров
# Переменная max_up в классе считается атрибутом класса. В некоторой литературе
# такие переменные называют свойствами класса. Также иногда используют термин
# поля класса. Свойства позволяют хранить значения и переходят ко всем
# экземплярам класса.
# Рассмотрим несколько особенностей работы с атрибутами.

class Person:
    max_up = 3 # атрибут класса


p1 = Person() # создаем 2 экземпляра класса персон
p2 = Person()

print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
p1.max_up = 12
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 42
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

# Изначально у класса и двух его экземпляров значения max_up совпадают.
# Экземпляры “не видят” max_up у себя и берут значение у класса.
# После изменения свойства у экземпляра p1 мы видим новое значение у него, но
# старые у класса и экземпляра p2. Изменения экземпляра всегда затрагивают этот
# экземпляр.
# Далее мы меняем значение свойства у класса. Экземпляр p2 “не видит” max_up у
# себя, поэтому снова обращается к классу и возвращает новое значение. Экземпляр
# p1 имеет собственную локальную переменную max_up, поэтому его свойство не
# изменилось. Изменения свойств класса затрагивают те экземпляры, которые не
# имеют собственных свойств