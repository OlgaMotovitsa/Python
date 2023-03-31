# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))

def Sum(number_a, number_b): 
                 
    if (number_a > 0 and number_b > 0):                               
        return Sum(number_a-1, number_b+1)
    return (number_a+number_b)
    
    
result = Sum(number_a, number_b)
print(f'{number_a} + {number_b} = {result}')