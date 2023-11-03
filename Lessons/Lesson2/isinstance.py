# Для проверки типа объекта используется функция isinstance().

a = (input())
print(type(a), id(a), hash(a))

# <class 'str'> 1446128137968 4698279867718945346

data = 3.14
print(isinstance(data, (int, float, complex)))

# True