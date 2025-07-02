#write a python script to calculate sum of square of first N natural numbers.
sum=0
for i in range(1,int(input("enter a number: "))+1):
    sum+=i**2
print(sum)
