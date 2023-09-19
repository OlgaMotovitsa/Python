# num = float(input('Введите число: '))
# count = 0
# while count < num:
#     count += 2
#     if count % 12 == 0:
#         continue
#     print(count)



# При необходимости работу цикла можно прервать и досрочно вернуться к проверке
# условия. Для этого используем зарезервированное слово continue.
# Выведем все чётные числа (как в прошлом примере), кроме тех, которые кратны 12.

# num = float(input('Введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)



num = float(input("Введите число: "))

step = 2
count = 0
while count < num - step:
    count += step
    if count % 12 == 0:
        continue
    print(count)













