import random as rnd

print(f'{rnd.random() = }')
rnd.seed(42) # передаем случайное число или время в секундах
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state)
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
