#write a python script to print first N odd natural numbers in reverse order.
x=int(input("enter a number: "))
i=1
j=x
while i<=x:
    print(j*2-1)
    i+=1
    j-=1
    
#second
x=int(input("enter a number: "))
i=x
while i>=1:
    print(i*2-1,end=' ')
    i-=1
    
