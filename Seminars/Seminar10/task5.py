# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Cat:
    def __init__(self, color: str, age: int, name: str):
        self.color = color
        self.age = age
        self.name = name

    def print_info(self):
        return f'{self.color} {self.age} {self.name}'


class Dog:
    def __init__(self, poroda: str, xvost: str, name: str):
        self.poroda = poroda
        self.xvost = xvost
        self.name = name

    def print_info(self):
        return f'{self.poroda} {self.xvost} {self.name}'


class Horse:
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


