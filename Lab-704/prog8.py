str = input("Enter string : ")

v = {'a':0,'e':0,'i':0,'o':0,'u':0}

cnt = 0
for i in str:
    if i.lower() in "aeiou":
        v[i.lower()] += 1
print (v)
