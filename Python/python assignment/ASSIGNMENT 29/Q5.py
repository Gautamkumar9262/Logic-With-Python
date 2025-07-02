#write a python script to find the sum of all odd numbers stored in a tuple.
t1=[30,45,31,13,11,16,15]
x=0
for e in t1:
    if e%2==1:
        x=x+e
print("Sum of all odd numbers is ",x)