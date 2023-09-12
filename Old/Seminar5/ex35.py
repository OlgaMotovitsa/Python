# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


def findSimple(x):
    for i in range(2,x):
        if x % i == 0:
            return 'составное'
    return 'простое'

print(findSimple(12))