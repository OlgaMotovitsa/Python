# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120 


while True:
    num = input('Ввудите число: ')
    if num.isdigit():
        num = abs(int(num))
        break
    else:
        print('Введите целое неотрицательное число: ')



# num =  abs(int(input('Введите число: '))) #abs - число по модулю
factorial = 1
# print(num)

while num > 1: #0
    factorial *= num
    num -=1

print(factorial)