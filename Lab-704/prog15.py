def numberOfDaysInAYear(year):
    if year%4 == 0 and year%100  != 0 or year%400 == 0:
        return 366
    else:
        return 365


start = int(input("Start year : "))
end = int(input("End year : "))

for i in range(start,end+1):
    print(i,"->",numberOfDaysInAYear(i))
