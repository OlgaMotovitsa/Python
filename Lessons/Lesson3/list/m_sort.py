# Метод sort()
# Метод sort осуществляет сортировку элементов списка
# без создания копии, inplace.

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# [1, 2, 2, 4, 7, 8, 9]
# [9, 8, 7, 4, 2, 2, 1]

# Как и функция sorted метод sort упорядочивает элементы по возрастанию. Если
# передать дополнительный параметр reverse=True, будет произведена сортировка по
# убыванию. Внутри метода работает тот же самый алгоритм сортировки Timsort. Но
# память на создание копии списка мы не тратим.

# Разворот списков
# Python поддерживает операции по развороту списка. Первый элемент становится
# последним, второй — предпоследним и так далее.