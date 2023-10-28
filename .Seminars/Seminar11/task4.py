# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """
    Задание №3
    Добавьте к задачам 1 и 2 строки документации для классов.
    """
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

    def __str__(self) -> str:
        return f"now {self.text}, now {self.number}, arhiv_text {self.text_history}, arhiv_num {self.number_history}"

    def __repr__(self) -> str:
        return f"Archive({self.text}, {self.number})"

a = Archive('one', 5)
print(a.text_history, a.number_history)
b = Archive('two', 10)
print(b.text_history, b.number_history)
print(a.text_history, a.number_history)
print(Archive.__doc__)
print(repr(b))





