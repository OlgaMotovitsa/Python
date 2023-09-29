# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def nums (numbers: list[int], start: int, stop: int) -> int:
    if start > stop:
        start, stop = stop, start
    if start < 0 or start > len(numbers):
        start = 0
    if stop > len(numbers) or stop < 0:
        stop = len(numbers)
    return sum(numbers[start:stop])

numbers = [3,5,4,5,0,2]
print(nums(numbers, 0,10))

