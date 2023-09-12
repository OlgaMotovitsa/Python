dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)

dictionary[895] = 85756
print(dictionary)
print(dictionary['up'])

dictionary['left'] =  '⇐'
# print(dictionary['type']) # эррор такого элемента нет

del dictionary['left']
print(dictionary)

for i in dictionary:
    print('{}: {}' .format(i,dictionary[i]))   
    # выводятся ключи и значения: 
# up: ↑
# down: ↓
# right: →
# 895: 85756


    # print(i)  #выводятся ключи 
    # up 
    # down 
    # left 
    # right

# for (k,v) in dictionary.items():
#     print(k,v)

print(dictionary.items())










# up: ↑
# down: ↓
# right: →