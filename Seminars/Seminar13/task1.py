# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def ask_user():
    while True:
        try:
            num = int(input("введите число "))
            print("ok")
            return num
        except ValueError:
            print("это не то")


a = ask_user()
print(a)