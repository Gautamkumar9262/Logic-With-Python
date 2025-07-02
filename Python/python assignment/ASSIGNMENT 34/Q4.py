#write a python function to print first N terms of Fibonacci series (tsrn)
def printfib(n):
    a,b=-1,1
    while(n):
        c=a+b
        print(c,end=' ')
        a,b=b,c
        n-=1
printfib(5)