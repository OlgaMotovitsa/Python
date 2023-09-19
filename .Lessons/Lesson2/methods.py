# Методы — это функции, которые описаны внутри объекта или класса. Они относятся
# к определенному объекту и позволяют взаимодействовать с ними или другими
# частями кода. По сути метод — это функция класса.
# В Python для обращения к методу используется точечная нотация, как и с
# атрибутами. Отличии в том, что после имени метода ставятся круглые скобки. А
# если метод ожидает получить данные на вход, они указываются как аргументы в
# скобках. Рассмотрим на примере:

print("Hello world!".upper())
print("Hello world!".count('l'))

# В первой строке мы вызвали метод строки, который пытается привести её к
# верхнему регистру. Метод count() принимает на вход аргумент — строку для поиска.
# В качестве ответа возвращается целое число, количество вхождений переданной
# строки внутри исходной.