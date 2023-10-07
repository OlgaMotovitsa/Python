# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку

# 3 способа:

res = [i for i in range(0, 101) if i % 2 == 0 and (i // 10 + i % 10 != 8)]
print(res)

res = [i for i in range(0, 101,2) if i // 10 + i % 10 != 8]
print(res)

res = [i for i in range(0, 101)
        if i % 2 == 0
            and sum(map(int,list(str(i)))) != 8]
print(res)

