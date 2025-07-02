#write a python script to create a list of first N prime numbers.
x=int(input("First a number: "))
prime=[]
n=2
while x:
    for i in range(2,n):
        if n%2==0:
            break
    else:
        prime.append(n)
        x-=1
    n+=1
print(prime)



        