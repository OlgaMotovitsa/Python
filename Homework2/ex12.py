# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ = int(input('Введите сумму '))
power = int(input('Введите произведеение '))

for i in range(1000):
    for j in range(1000):
        if summ == i + j and power == j*i:
            print(i, j ) 





# summ = i + j
# power = i * j

# j = summ - i

# power = i *(summ - i)
# i**2 - summ * 1 - power = 0





