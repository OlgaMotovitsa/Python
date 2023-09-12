
import random
import string

all_chars = string.ascii_lowercase + string.digits 
print(all_chars)

my_string = [random.choice(all_chars) for _ in range(20)]
print(my_string)

dict_count = {}  

for item in my_string:
    dict_count[item] = dict_count.get(item, -1) + 1
    if dict_count.get(item) > 0:
        print(f'{item}_{dict_count.get(item)}', end= ' ')
    else:
        print(item, end=' ')