# сумма всех чисел

n = 423
summ = 0

while n > 0:
    x = n % 10
    summ = summ + x
    n = n // 10
print(summ)