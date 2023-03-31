# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

#A = 3; B = 5 -> 243 (3⁵)
#   A = 2; B = 3 -> 8

number = int(input('Введите число: '))
power = int(input('Введите степень числа: '))

def raiseToPower(number, power): 
    if (power == 0) or (number == 0):
        return 'Нет значения'

    if (power > 1):                  
        return (number * raiseToPower(number, power - 1)) 
    return number
    
result = raiseToPower(number, power) 
print(f"{number} в степени {power} = {result}")