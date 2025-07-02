#write a python script to create a list of first N terms of a fibonacci series.
# n=int(input("enter number: "))
# x=0
# y=1
# z=0
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y

#second
n=int(input("enter number: "))
fib=[]
a,b=-1,1
while n:
    c=a+b
    fib.append(c)
    a,b=b,c
    n-=1
print(fib)