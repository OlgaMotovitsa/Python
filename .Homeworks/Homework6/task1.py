# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.
import datetime


def date_to_prove(date: str):
    valid = True

    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        valid = False
    return valid


assert date_to_prove('15.4.2023')
assert not date_to_prove('31.6.2022')
assert not date_to_prove('0.5.2022')
assert not date_to_prove('12.0.2022')
assert not date_to_prove('12.5.-2022')
assert date_to_prove('29.2.2020')
assert date_to_prove('12.5.2022')
assert date_to_prove('28.2.2021')
assert date_to_prove('31.12.9999')
assert not date_to_prove('32.5.2022')
assert not date_to_prove('12.13.2022')
assert not date_to_prove('29.2.2021')
assert not date_to_prove('30.2.2020')


