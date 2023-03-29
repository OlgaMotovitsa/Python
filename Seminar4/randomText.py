import random
import string

my_random_text = []

for i in range(20):
    word = ''
    for j in range(random.randint(4,8)):
        word += random.choice(string.ascii_lowercase)
    my_random_text.append(word + str(random.choice(['.', ',', '?'])
    if random.choice([0,0,1]) else '')) # типо слитно с пред строчкой

print(' '.join(my_random_text))