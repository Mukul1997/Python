str = input("Enter string : ")

res = ""
for i in str:
    if i not in "’!()-[]{};:’’’,\<>/?@#$%^&*_~":
        res += i
print (res)
