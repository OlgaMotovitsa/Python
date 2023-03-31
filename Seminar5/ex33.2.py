mass = [1,2,3,4,5,5,4,3,2]
mn = min(mass)
mx = max(mass)


for i in range(len(mass)):
    if mass[0] == mx:
        mass[0] = mn
print(mass)


