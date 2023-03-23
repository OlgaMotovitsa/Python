
n = int(input('Введите 6-значное число '))

summ = 0
digit1 = n % 1000
while n > 0:
    x = n % 10
    summ = summ + x
    n = n // 10
print(summ)


num1 = int(input('Введите 6-значное число ' ))
# num2 = num1

summ1 = 0
digit1 = num1 % 1000

while num1 > 0:
    x = num1 % 10
    summ1 = summ1 + x
    num1 = num1 // 10

print(digit1)
print(summ1)

# summ2 = 0
# digit2 = num2 % 1000
# while num2 > 0:
#     x = num2 % 10
#     summ2 = summ2 + x
#     num2 = num2 // 10
# print(summ2)
# print(digit2)

# if summ1 == summ2:
#     print('True')
# else:
#     print('False')