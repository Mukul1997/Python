str1 = input('String 1 :')
str2 = input('String 2 :')

def Capitalizer(str1,str2):
    res = ""
    for i in str1.split(" "):
        res += i[0].upper()
    for j in str2.split(" "):
        res += j[0].upper()
    return res

print(Capitalizer(str1,str2))
