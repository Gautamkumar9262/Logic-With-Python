#write a python function to print all factors of a given number (tsrn)
def print_factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')

print_factors(36)
print()