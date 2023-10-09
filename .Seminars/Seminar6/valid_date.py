'''Задание №7
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
'''
#

__all__ = ['check_date']


def check_date(date: str) -> bool:
    day, month, year = map(int, date.split('.')) # DD.MM.YYYY разделяем дату на 3 куска и переводим в инт
    if _leap_year(year) and month == 2:
        return 1 <= day <= 29
    return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999

    # if day not in 1 <= day <= 31:
    #     return False
    # if month not in 1 <= month <= 12:
    #     return False
    # if year not in 1 <= year <= 9999:
    #     return False
    # return True


def _leap_year(year): # високосный год
    return year % 4 == 0 and year % 100 != 0


if __name__ == '__main__':
    print(check_date("29.02.2024"))




