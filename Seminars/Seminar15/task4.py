# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import datetime
from log_decor import log_dec

MOUTH = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
        "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}

WEEKDAY = {"понедельник": 1, "вторник": 2, "среда": 3,
        "четверг": 4, "пятница": 5, "суббота": 6, "воскресенье": 7}

@log_dec
def print_date(str_day):
    num, weekday, mouth = str_day.split()
    num = int(num[0])
    weekday = WEEKDAY[weekday] - 1
    mouth = MOUTH[mouth]
    count = 0
    for i in range(1, 32):
        temp_date = datetime.datetime(datetime.datetime.now().year, mouth, i)
        if temp_date.weekday() == weekday:
            count += 1
            if count == num:
                return temp_date
    raise ValueError
