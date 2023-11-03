# Слово else относится к тому if, с которым находится на одном уровне. В примере
# ниже верхний if связан с нижним else, а средний if со средним else.

pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны')
else:
    print('Доступ запрещён')
    print('Работа завершена')