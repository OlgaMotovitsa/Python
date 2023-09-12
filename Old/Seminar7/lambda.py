def sum_(x,y):
    return x + y

print(sum_(4, 6))

print((lambda x,y: x + y)(3,6))

# 10
# 9

oper = {'+': sum}   #из текста вырываем плюсы и записываем функцию подсчета суммы

