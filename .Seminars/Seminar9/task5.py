# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.


from task2 import game_decor # контроль значений
from task3 import func_dec # сохр параметров
from task4 import func_count # многократный запуск

@func_count(3)
@func_dec
@game_decor
def guess(rnd_num, count_try):
    for i in range(count_try):
        input_num = int(input("введите число: "))
        if input_num > rnd_num:
            print('число должно быть меньше')
        elif input_num < rnd_num:
            print('число должно быть больше')
        else:
            print(rnd_num)
            return True
    return False

if __name__ == '__main__':
    print(guess(101,1))




