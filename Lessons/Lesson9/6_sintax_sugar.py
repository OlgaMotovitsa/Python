# Функция может принимать другую функцию в качестве параметра

# def main(func):
#     def wrapper(*args, **kwargs):
#         # ...
#         result = func(*args, **kwargs)
#         # ...
#         return result
#     return wrapper
#
#
# def my_func(data):
#     # ...
#     return wrapper
#
#
# deco = main(my_func)



# Передача функции в качестве аргумента
# Синтаксический сахар Python, @
# Символ @ является более простым способом создать замыкание

def main(func):
    def wrapper(*args, **kwargs):
        # ...
        result = func(*args, **kwargs)
        # ...
        return result
    return wrapper
@main
def my_func(data):
    # ...
    return wrapper