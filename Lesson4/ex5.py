

def where(f, col):
    return[x for x in col if f(x)]

data = [1,2,3,5,8,15,23,38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)