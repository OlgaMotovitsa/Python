# , когда мы перебираем какие-то данные, вместо однобуквенных переменных
# можно использовать подходящие имена. Например так может выглядеть перебор
# животных, которые хранятся в массиве данных.

animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for animal in animals:
    print(animal)
# cat
# dog
# wolf
# rat
# dragon


animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
# 1 cat
# 2 dog
# 3 wolf
# 4 rat
# 5 dragon
