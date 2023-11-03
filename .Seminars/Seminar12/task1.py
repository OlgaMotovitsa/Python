# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class Factorial:
    def __init__(self, k):
        self.k = k
        self.dict_result = {}

    def __call__(self, num):
        count = 1
        for i in range(1, num + 1):
            count *= i
        self.rem(num, count)
        return count

    def rem(self, num, result):
        if len(self.dict_result.values()) > self.k - 1:
            self.dict_result = dict(list(self.dict_result.items())[1:])
        self.dict_result.update({num: result})

    def memory(self):
        return self.dict_result



f = Factorial(2)

print(f(3))
print(f(6))
print(f.memory())
print(f(5))
print(f.memory())