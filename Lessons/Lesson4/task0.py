# Перед вами функция и её вызов. Найдите три ошибки и напишите о них в чат. У вас
# три минуты.
def func(a=0.0, *, c=0.0):
    """func(a=0.0: int | float, /, b=0.0: int | float, *, c=0.0:
    int | float) -> : int | float"""
    if a > c:
        return a
    if a < c:
        return c
    return
print(func(c=1, a=3))