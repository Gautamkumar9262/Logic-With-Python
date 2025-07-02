#write a python script to count digit in a given number.
x=int(input("enter number: "))
count=0
while x:
    x=x//10
    count+=1
print("count:",count)