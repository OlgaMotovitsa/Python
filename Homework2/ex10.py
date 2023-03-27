# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2



from random import randint

mon = int(input('Введите кол-во монет: '))
print(f'{mon} - монет всего')
gerb = 0
reh = 1
count_gerb = 0
count_reh = 0
count = 0
sum = 0

for  _ in range(mon): #проходим по всем монетам
    array_mon = randint(gerb, reh)
    print(array_mon, end= ' ')

    if array_mon == 0:
        count_gerb +=1
    if array_mon == 1:
        count_reh += 1

print()
print(f'{count_gerb} - гербом вверх, {count_reh} - решкой вверх' )

if count_gerb < count_reh:
    print(f'{count_gerb} - минимальное количество монет, которое нужно перевернуть')
else:
    print(f'{count_reh} - минимальное количество монет, которое нужно перевернуть')



   
        

  
    









 

     

    






