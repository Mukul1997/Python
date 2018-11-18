def indexOfSmallestElement(lst):
    l = len(lst)
    min = 0
    for i in range(1,l):
        if lst[i] < lst[min]:
            min = i
    return 'Smallest element at index '+str(min)

lst = list(map(int,input("Enter elements : ").split(',')))
print(lst)
print(indexOfSmallestElement(lst))
