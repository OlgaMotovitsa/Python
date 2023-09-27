# Документирование кода функций
# Несколько слов о документировании функций. Начнём с того, что документация
# обычно пишется на английском языке, как универсальном для программистов из
# любой страны. Вполне допустим и родной язык, если проект локальный. Но лучше
# воспользоваться онлайн переводчиком и сразу привыкнуть к документированию на
# английском.

def max_before_hundred(*args):
    """Return the maximum number not exceeding 100."""
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m
print(max_before_hundred(-42, 73, 256, 0))

# Пояснения к однострочной строке документации
# ● Тройные кавычки используются, даже если строка помещается на одной
# строке. Это позволяет легко расширить его позже.
# ● Закрывающие кавычки находятся на той же строке, что и открывающие. Это
# выглядит лучше для однострочников.
# ● Нет пустой строки ни до, ни после строки документации.
# ● Строка документации — это фраза, заканчивающаяся точкой. Он описывает
# действие функции или метода как команду
# ● Однострочная строка документации не должна повторять параметры
# функции.
# 🔥 Внимание! В программе использована переменная, а точнее константа
# “минус бесконечность” float('-inf'). Это особая форма представления
# бесконечности в памяти интерпретатора, аналогичная бесконечности из
# модуля math.
# Если описание функции подразумевает больше подробностей, после первой строки
# документации оставляют одну пустую. Далее в несколько строк даётся всё
# необходимое описание. Закрывающие кавычки ставятся на отдельной строке, без
# текста.
def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
...
# Подобная запись автоматические помещает текст в переменную __doc__. Описание
# функции можно будет получить через вызов справки help с передачей функции в
# качестве аргумента.
help(max_before_hundred)
