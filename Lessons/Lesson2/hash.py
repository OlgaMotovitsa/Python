x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list)) # получим ошибку, т.к. list изменяемый

# Как видите нижняя строка кода вызывает ошибку TypeError: unhashable type:
# 'list' Если вдруг забыли изменяемый объект или нет, просто попробуйте
# получить его хеш.
