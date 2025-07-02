#write a python script to calculate sum of digit of a given number.
num=int(input("enter number: "))
s=0
while num:
    r=num%10
    s=s+r
    num=num//10
print("sum",s)

