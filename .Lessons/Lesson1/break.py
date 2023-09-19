# Ещё один способ управления циклом — команда break для его досрочного
# завершения. Она отлично подходит для создания циклов с постусловием,
# бесконечных циклов с возможностью выхода.
# Рассмотрим на примере программы, которая просит ввести число внутри заданного
# диапазона.

# min_limit = 0
# max_limit = 10
# while True:
#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число ' + str(num))

min_lim = 0
max_lim = 10

print("введите число между ", min_lim, "и ", max_lim)
#num = int(input()) --- сюда ставить эту строку нельзя так как при вводе
#числа вне диапазона залипнет НЕВЕРНО
while True:
    num = int(input())
    if num < min_lim or num > max_lim:
        print("неверно")
    else:
        break
print("было введено число: ", num)

# если число неверно то цикл бесконечный пока не будет верное число