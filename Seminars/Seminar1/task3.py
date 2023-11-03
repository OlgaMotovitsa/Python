#Напишите программу, которая запрашивает год и проверяет
# его на високосность.
#Распишите все возможные проверки в цепочке elif
#Откажитесь от магических чисел
#Обязательно учтите год ввода Григорианского календаря
#В коде должны быть один input и один print

year = int(input('Введите год: '))
MAIN_DEVIDOR = 4
EXCEPTION_DIVIDER = 100
ADDITIONAL_DIVIDOR = 400

if (year % MAIN_DEVIDOR == 0
        and year % EXCEPTION_DIVIDER != 0
        or year % ADDITIONAL_DIVIDOR == 0):
    print('год високосный')

else:
    print('год обычный')
