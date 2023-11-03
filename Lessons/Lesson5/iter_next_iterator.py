# # Функции iter и next для генераторов
# # Уже знакомые по сегодняшнему уроку функции iter и next могут работать с
# # созданными генераторами. Например так:
#
#
# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
#
# my_iter = iter(factorial(4))
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter)) # StopIteration



# Задание
# Перед вами несколько строк кода. Напишите что по вашему мнению выведет print,
# не запуская код. У вас 3 минуты.
def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }')