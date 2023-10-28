# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков, архивов
# list-архивы также являются свойствами экземпляра.


class Archive:

    instance = None

    def __new__(cls, *args, **kwargs):
        # применение свойств для класса
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.text_history = []
            cls.instance.number_history = []
        else:
            cls.instance.text_history.append(cls.instance.text)
            cls.instance.number_history.append(cls.instance.number)
        return cls.instance

    def __init__(self, text, number):
        self.text = text
        self.number = number


a = Archive('dfg', 5)
print(a.text_history, a.number_history)
b = Archive('vbn', 10)
print(b.text_history, b.number_history)
print(a.text_history, a.number_history)