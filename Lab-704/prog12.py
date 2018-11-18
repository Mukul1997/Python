lst = list(map(int,input('Enter elements : ').split(',')))
print(lst)
key = int(input("Key to search : "))

def binSearch(key,lst):
    low = 0;
    high = len(lst)-1

    while low <= high:
        mid = (low+high) // 2

        if key == lst[mid]:
            return "Found at index "+str(mid)
        elif key > lst[mid]:
            low = mid+1
        else:
            high = mid-1

    else:
        return "not found"

print(binSearch(key,lst))
