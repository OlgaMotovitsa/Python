# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def ran_num(rnd_num, count_try):
    def guess():
        for i in range(count_try):
            input_num = int(input("введите число: "))
            if input_num > rnd_num:
                print('число должно быть меньше')
            elif input_num < rnd_num:
                print('число должно быть больше')
            else:
                print(rnd_num)
                return 'это загаданное число'
        return 'не угадано'
    return guess


rnd = ran_num(4,5)
# print(ran_num)
print(rnd())