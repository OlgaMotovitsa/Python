# Задача №1
# За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.
n = 700
m = 750

import math

n = int(input('Сколько машина проедет за день: '))
m = int(input('Сколько машина проедет всего: '))

print (math.ceil(m / n))

print(f'Мвшине потребуется {(m + n - 1) // n} дней')