#write a python script to print binary equivalent of a given decimal number.(do not use bin() method)
d=int(input("enter a number: "))
s=''
while d:
    r=d%2
    d=d//2
    s=str(r)+s
print(s)