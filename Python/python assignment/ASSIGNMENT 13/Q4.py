#write a python script to check whether a given year is a leap year or not.
x=int(input("Enter a year: "))
if(x%4==0):print("%d is a leap year",x) 
elif(x%400==0):print(" is leap year",x)
elif(x%100==0):print("%d is a not leap year",x)
else:print("%d is not a leap year",x)

year=int(input("Enter a year: "))
print("leap year" if year%400)