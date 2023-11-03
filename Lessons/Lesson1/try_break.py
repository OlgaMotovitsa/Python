# Зарезервированное слово else может применятся не только к ветвлениям, но и к
# циклам. Для этого else должно быть расположено на том же уровне, т.е. иметь
# столько же пробельных отступов, что и начало цикла — while.
# Доработаем прошлую программу и дадим 3 попытки на попадание в диапазон.
min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1

    num = float(input('Введи число между ' + str(min_limit) +
                      ' и ' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))
