#write a python function to print first N prime numbers (tsrn)
def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def nextprime(num):
    num+=1
    while(not isprime(num)):
        num+=1
    return num
def printprime(n):
    x=2
    for i in range(1,n+1):
        print(x,end=' ')
        x=nextprime(x)

printprime(10)