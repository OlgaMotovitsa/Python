# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animals:
    def __int__(self, name):
        self.name = name

    def print_info(self):
        return f"{self.name}"

class Cat(Animals):
    def __init__(self, color: str, age: int, name: str):
        self.color = color
        self.age = age
        self.name = name

    def print_info(self):
        return f'{self.color} {self.age} {self.name}'


class Dog(Animals):
    def __init__(self, poroda: str, xvost: str, name: str):
        self.poroda = poroda
        self.xvost = xvost
        self.name = name

    def print_info(self):
        return f'{self.poroda} {self.xvost} {self.name}'


class Horse(Animals):
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def print_info(self):
        return f'{self.color} {self.name}'


p1 = Cat('Черный', 6, 'Вася')
p2 = Dog('Чау-чау', 'купированный', 'Собака')
p3 = Horse('Пегая', 'Белла')

print(f'{p1.print_info() = }')
print(f'{p2.print_info() = }')
print(f'{p3.print_info() = }')