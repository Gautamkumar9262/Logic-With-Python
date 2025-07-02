#write  a python function to print first N odd natural numbers.(tsrn)
def odd(n):
    for i in range(1, n+1):
        print(2*i-1)
    
odd(7)