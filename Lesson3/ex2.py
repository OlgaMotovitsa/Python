

def sum_str(*args):
    res = ''         # тип данных строка
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', '1' ))
print(sum_str('q', 'e', '1', 'd' ))
# print(sum_str(1, 8, 9))