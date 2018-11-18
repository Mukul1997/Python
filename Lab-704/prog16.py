import random as ran

n = int(input('Enter order : '))

for i in range(n):
    for j in range(n):
        print(ran.randint(0,1),end=" ")
    print()
