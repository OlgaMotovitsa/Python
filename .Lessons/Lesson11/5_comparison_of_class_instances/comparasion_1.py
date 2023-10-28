# 5. Сравнение экземпляров класса
# Числа сравниваются по значению, строки посимвольно. Но при желании можно
# сравнивать любые объекты Python реализовав перечисленные ниже дандер
# методы.
# ● __eq__ - равно, ==
# ● __ne__ - не равно, !=
# ● __gt__ - больше, >
# ● __ge__ - не больше, меньше или равно, <=
# ● __lt__ - меньше, <
# ● __le__ - не меньше, больше или равно, >=
# Перечисленные методы попарно противоположны. Обратите внимание на
# приставку не в списке. Реализовав один из пары, второй Python попытается
# получить инвертируя значение. Не истина — это ложь, а не ложь — это истина.
# При реализации метода обычно принято возвращать True или False. Если
# возвращается другое значение в конструкциях вида if x == y:, Python применит
# функцию bool() к результату для получения True или False.
