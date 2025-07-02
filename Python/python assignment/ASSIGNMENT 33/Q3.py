#write a python function to check weather a number is prime. (tsrs)
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    
x=prime(5)
print(x)