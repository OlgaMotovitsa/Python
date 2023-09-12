def calc1(a):
    return a+a

def calc2(a):
    return a*a

def math(op, x):
    print(op(x))

math(calc1, 5)
math(calc2, 5)

# 10
# 25


def calc1(a, b):
    return a + b

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calc1, 5, 7)
math(calc2, 5 , 7)

# 12
# 35