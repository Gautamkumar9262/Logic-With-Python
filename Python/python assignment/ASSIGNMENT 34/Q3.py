#write a python function to print all prime numbers between two given numbers (tsrn)





def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True





def printprimerange(a,b):
    x=a+1
    while x<b:
        if isprime(x):
            print(x,end=' ')
        x+=1
printprimerange(5,4)
