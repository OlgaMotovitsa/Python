# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def func_count(count):
    def func_def(func):
        new_list = []
        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                new_list.append(result)
            return new_list
        return wrapper
    return func_def

@func_count(10)
def sum_func(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    print(sum_func(5, 3))
