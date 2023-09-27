# Перед вами список и три операции с ним. Напишите что выведет каждая из строк по
# вашему мнению, не запуская код. У вас 3 минуты.
data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'),
              globals().items()))
