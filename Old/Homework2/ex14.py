# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

digit = int(input('Введите число '))
power = 2

while power <= digit:
    print(power, end= ' ')
    power = power * 2





