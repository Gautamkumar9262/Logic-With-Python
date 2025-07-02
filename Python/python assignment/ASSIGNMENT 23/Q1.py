#write a python script to calculate factorial of a given number.
fac=1
for i in range(1,int(input("enter a number: "))+1):
    fac*=i
print(fac)