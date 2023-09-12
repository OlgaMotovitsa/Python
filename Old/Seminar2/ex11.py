# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# num = int(input('Введите натураньное число: '))

# Fib_prev = 0
# Fib_curr = 1
# i = 1

# while Fib_curr < num:
#     fib_next = Fib_prev + Fib_curr
#     Fib_prev = Fib_curr
#     Fib_curr = fib_next
#     i += 1

# if Fib_curr == num:
#     print(i)
# else:
#     print(-1)




num = int(input('Введите натураньное число: '))

fibo_1, fibo_2, index = 0, 1, 1

while fibo_2 < num:
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    index += 1

if fibo_2 == num:
    print(index)
else:
    print(-1)