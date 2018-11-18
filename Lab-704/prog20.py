l = 0
w = 0
c = 0

fp = open("input.txt","r")

for f in fp:
    l += 1
    for g in f.split(' '):
        w += 1
        for h in g:
            c += 1
fp.close()

print('Lines : ',l)
print('Words : ',w)
print('Characters : ',c)
