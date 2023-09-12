#Работа в консоли в режиме интерпретатора Python.
#Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
#Используйте while и if. Попробуйте разные значения e и n.

n = 10
e = 5
count = 0

while count < n:
    break
summa = 0
while count < n:
    if count %e !=0:
        summa += count
    count += 2
print(summa)
