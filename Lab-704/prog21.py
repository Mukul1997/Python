total = 0
avg = 0.0
l = list()

fp = open("score.txt","r")

for f in fp:
    for g in f.split(' '):
        l.append(int(g.strip('\n')))
        total += int(g)
fp.close()
avg = total / len(l)

print('Marks : ',l)
print('Total : ',total)
print('Average : ',avg)
