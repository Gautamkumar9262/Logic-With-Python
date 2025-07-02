#write a python script to print N evenm natural numbers inn reverse order.
x=int(input("enter a number: "))
i=1
j=x
while i<=x:
    print(j*2)
    i+=1
    j-=1

#second
x=int(input("enter a number: "))
j=x
while j>=1:
    print(j*2,end=' ')
    j-=1
    