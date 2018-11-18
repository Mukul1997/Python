def isConsecutiveFour(values):
    n = len(values)
    for i in range(n-3):
        if l[i:i+4] == [l[i],l[i],l[i],l[i]]:
            return True
    return False

l = list(map(int,input('Enter elements : ').split(',')))
print(l)
print(isConsecutiveFour(l))
