#write a python script to print the octal equivalent of given decimal number.(do not use oct() method)
d=int(input("enter a number: "))
s=''
while d:
    r=d%8
    d=d//8
    s=str(r)+s
print(s)