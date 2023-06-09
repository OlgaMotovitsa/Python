# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая 
# длинная оттепель. Оттепелью они называют период, в 
# который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

days = int(input('Введите кол-во дней: '))
today = 0
warm_count = 0
max_warm = 0

for  _ in range(days): #проходим по всем дням
    today += random.randint(-3,3)
    print(today, end= ' ')
    if today > 0:
        warm_count +=1
    else:
        if max_warm < warm_count:
            max_warm = warm_count
        warm_count = 0

if max_warm < warm_count:
    max_warm = warm_count
warm_count = 0

print(f'\n Самая долгая оттепель была {max_warm} дней')