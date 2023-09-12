import math

number = int(input('Введите число: '))

def is_simple(number:int) -> bool:
    if number % 2 == 0:
        return False
    elif number in [1,2,3]:
        return True
    else: 
        for div in range(3, int(math.sqrt(number)) + 1,2):
            if number% div == 0:
                return False
    return True
print(is_simple(number))