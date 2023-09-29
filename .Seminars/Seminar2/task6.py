# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

s = 10000
count = 0

while True:
    action = input("Введите операцию: ")

    if s >= 5_000_000: # При превышении суммы в 5 млн, вычитать налог
        s *= 0.9       # на богатство 10% перед каждой операцией, даже ошибочной

    if count % 3 == 0 and count != 0: # После каждой третей операции пополнения
        s *= 1.03               # или снятия начисляются проценты - 3%
        count = 0

    if action == "1":
        withdraw = int(input(" введите сумму: "))
        if withdraw % 50 == 0:
            s += withdraw
            count += 1

    elif action == "2":
        withdraw = int(input(" введите сумму: "))
        if withdraw % 50 == 0:
            comission = withdraw * 0.015
            if comission < 30:
                comission = 30
            elif comission > 600:
                comission = 600
            if (withdraw + comission) < s:
                s -= withdraw + comission
                count += 1

    else:
        break



# s = 10000
# count = 0
# RICHLIMIT = 5_000_000
# RICHTAX = 0.9
# THREEOPERATIONS = 3
# BONUSTHREE = 1.03
# FREENDERING = 50
# COMMISSIONOUTDROW = 0.015
# MINLIMIT = 30
# MAXLIMIT = 600
# while True:
#     action = input('Введите операцию 1,2,3: ')
#     if s >= RICHLIMIT:
#         s *= RICHTAX
#     if count % THREEOPERATIONS == 0 and count != 0:
#         s *= BONUSTHREE
#         count = 0
#     if action == '1':
#         withdrow = int(input('введиет сумму: '))
#         if withdrow % FREENDERING == 0:
#             count += 1
#         s += withdrow
#     elif action == '2':
#         withdrow = int(input('введиет сумму: '))
#         if withdrow % FREENDERING == 0:
#             comission = withdrow * COMMISSIONOUTDROW
#             if comission < MINLIMIT:
#                 comission = MINLIMIT
#             elif comission > MAXLIMIT:
#                 comission = MAXLIMIT
#             if (comission + withdrow) < s:
#                 s -= (withdrow + comission)
#                 count += 1
#     else:
#         break
#     print(s)


# summ = 10000
# in_money = 'Пополнить'
# out_money = 'Снять'
# exit_bank = 'Выйти'
# SUMM_SN = 50
# MOD_SUMM = 0.015
# MIN_MONEY = 30
# MAX_MONEY = 600
# IN_MOD = 1.03
# GOLD_HUMAN = 0.9
# MUILTIPLICITY = 3
# count = 10
# SUMM_GOLD_HUMAN = 5_000_000





print(s)










    # print(s - 1.5%(s))










