import calendar 
year = int(input("Enter year :"))

#PRINT calendar
print(calendar.calendar(year, 2, 1, 8, 3))

#CHECK LEAP YEAR
if calendar.isleap(year):
    print("YES")
else:
    print("NO")


#MONTHRANGE
print(calendar.monthrange(year, 2))
