#write a python script to count number of digit in a given number.
x=int(input("enter a numbers"))
count=0
for digit in str(x):
    if digit in "0123456789":
        count+=1
print(count)

